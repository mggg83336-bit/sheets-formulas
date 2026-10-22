#!/usr/bin/env python3
"""内容流水线：按 niche 配置生成新文章（幂等，已生成的关键词会跳过）。

用法: python scripts/generate.py [--limit N] [--niche NAME] [--provider NAME] [--refresh]

Structured niches (niche.yaml has `pages_dir`, e.g. sheets-formulas):
  1. Launch set: every entry with `launch: true` is published (not limited by --limit).
  2. Queue: walk niche `queue_file` in order and publish up to --limit keywords whose
     content exists and passes the quality gate. Keywords without real content are
     skipped (left in the queue), never published as stubs.
  --refresh re-renders already-published structured pages from the data (keeps dates).
"""
import argparse
import csv
import datetime as dt
import sys

from common import (AD_PLACEHOLDER, CONTENT, PRODUCT_PLACEHOLDER, load_niche,
                    load_site, read_post, slugify, write_post)
from providers import get_provider


def collect_topics(niche):
    topics = list(niche.get("topics", []))
    df = niche.get("data_file")
    if df and (niche["_dir"] / df).exists():
        with open(niche["_dir"] / df, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                kw = row.pop("keyword")
                topics.append({"keyword": kw, "data": row})
    return topics


def publish_structured(e, plat, niche_name, gate_cfg, entries_by_id, date, reason):
    import structured
    out = structured.render(e, plat)
    probs = structured.gate(e, plat, gate_cfg, body=out["body_md"])
    slug = e["slugs"][plat]
    if probs:
        print(f"[generate] skip {slug}: " + "; ".join(probs))
        return False
    meta = {"title": out["title"], "slug": slug, "date": date, "summary": out["summary"],
            "tags": out["tags"], "keyword": slug, "niche": niche_name, "provider": "structured",
            "entry_id": e["id"], "platform": structured.PLATFORMS[plat],
            "category": e.get("category", "other"), "faq": out["faq"],
            "related": structured.related_slugs(e, plat, entries_by_id),
            "sibling": structured.sibling_slug(e, plat)}
    write_post(CONTENT / f"{slug}.md", meta, out["body_md"])
    print(f"[generate] + {slug} ({reason})")
    return True


REJECT_DAYS = 30


def load_rejected(niche):
    p = niche["_dir"] / "rejected.csv"
    if not p.exists():
        return {}
    with open(p, encoding="utf-8") as f:
        return {r["slug"]: r for r in csv.DictReader(f)}


def reject(niche, slug, reason):
    p = niche["_dir"] / "rejected.csv"
    new = not p.exists()
    with open(p, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["slug", "date", "reason"])
        if new:
            w.writeheader()
        w.writerow({"slug": slug, "date": dt.date.today().isoformat(), "reason": reason[:300]})
    print(f"[generate] rejected {slug}: {reason[:200]}")


def try_llm_entry(a, niche, row, entries, st):
    """Optional: draft content for a queued keyword with an LLM, then accept it only if it passes
    the quality gate AND every worked-example result recalculates correctly in LibreOffice."""
    import os
    import shutil
    import structured
    if a.provider != "llm" or not os.environ.get("LLM_API_URL") or st["attempts"] >= st["max"]:
        return None
    old = st["rejected"].get(row["slug"])
    if old and (dt.date.today() - dt.date.fromisoformat(old["date"])).days < REJECT_DAYS:
        return None
    if not (shutil.which("soffice") or shutil.which("libreoffice")):
        print("[generate] LLM drafts need LibreOffice for verification; skipping")
        st["attempts"] = st["max"]
        return None
    from providers.llm import generate_entry
    from verify_formulas import verify_entries
    st["attempts"] += 1
    plat = "sheets" if "sheets" in row.get("platform", "").lower() else "excel"
    e = generate_entry(row["keyword"], plat, row["slug"], row.get("category"), entries[0])
    if not e:
        return None
    try:
        probs = structured.gate(e, plat, niche.get("quality_gate", {}), body=structured.render(e, plat)["body_md"])
    except Exception as ex:  # malformed draft
        probs = [f"render failed: {ex}"]
    if not probs:
        vp, n_ok, _ = verify_entries([e])
        probs = vp or ([] if n_ok >= 2 else [f"only {n_ok} machine-verified result(s); need 2"])
    if probs:
        reject(niche, row["slug"], "; ".join(probs))
        return None
    import yaml
    out = niche["_dir"] / niche["pages_dir"] / f"auto-{row['slug']}.yaml"
    out.write_text("# Drafted by LLM, passed quality gate + LibreOffice recalculation\n"
                   + yaml.safe_dump([e], allow_unicode=True, sort_keys=False), encoding="utf-8")
    return e


def run_structured(a, niche):
    import structured
    from kwqueue import load_queue
    entries = structured.load_entries(niche)
    by_id = {e["id"]: e for e in entries}
    smap = structured.slug_map(entries)
    gate_cfg = niche.get("quality_gate", {})
    CONTENT.mkdir(parents=True, exist_ok=True)
    published = {p.stem: p for p in CONTENT.glob("*.md")}
    today = dt.date.today().isoformat()

    if a.refresh:
        n = 0
        for slug, path in published.items():
            meta, _ = read_post(path)
            if meta.get("provider") == "structured" and slug in smap:
                e, plat = smap[slug]
                n += publish_structured(e, plat, a.niche, gate_cfg, by_id, str(meta["date"]), "refresh")
        print(f"[generate] refreshed {n} page(s)")
        return 0

    launched = 0
    for e in entries:
        if e.get("launch"):
            plat = structured.primary_platform(e)
            slug = e["slugs"][plat]
            if slug not in published and publish_structured(e, plat, a.niche, gate_cfg, by_id, today, "launch"):
                launched += 1
                published[slug] = None

    made, waiting = 0, 0
    llm_state = {"attempts": 0, "max": a.limit * 2, "rejected": load_rejected(niche)}
    for r in load_queue(niche):
        if made >= a.limit:
            break
        slug = r["slug"]
        if slug in published:
            continue
        if slug not in smap:
            entry = try_llm_entry(a, niche, r, entries, llm_state)
            if not entry:
                waiting += 1   # no content yet -> stays queued; never publish a stub
                continue
            entries.append(entry)
            by_id[entry["id"]] = entry
            smap[slug] = (entry, entry["primary"])
        e, plat = smap[slug]
        if publish_structured(e, plat, a.niche, gate_cfg, by_id, today, f"queue: {r['keyword']}"):
            made += 1
            published[slug] = None
    print(f"[generate] launch +{launched}, queue +{made} (limit {a.limit}); "
          f"{waiting} queued keyword(s) passed over for lack of content; total pages {len(published)}")
    return 0


def main():
    site = load_site()
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=site.get("generate_per_run", 3))
    ap.add_argument("--niche", default=site["niche"])
    ap.add_argument("--provider", default=site.get("provider", "template"))
    ap.add_argument("--refresh", action="store_true", help="re-render published structured pages")
    a = ap.parse_args()

    niche = load_niche(a.niche)
    if niche.get("pages_dir"):
        return run_structured(a, niche)
    gen = get_provider(a.provider)
    CONTENT.mkdir(parents=True, exist_ok=True)
    done = {read_post(p)[0].get("keyword") for p in CONTENT.glob("*.md")}
    today = dt.date.today()
    ctx = {"today": today, "ad_in_article": AD_PLACEHOLDER, "product_box": PRODUCT_PLACEHOLDER}

    made = 0
    for t in collect_topics(niche):
        if made >= a.limit:
            break
        if t["keyword"] in done:
            continue
        out = gen(t, niche, ctx)
        slug = slugify(t.get("slug") or f"{niche.get('category_slug', 'post')}-{t['keyword']}")
        meta = {"title": out["title"], "slug": slug, "date": today.isoformat(),
                "summary": out.get("summary", ""), "tags": out.get("tags", []),
                "keyword": t["keyword"], "niche": a.niche, "provider": a.provider}
        write_post(CONTENT / f"{slug}.md", meta, out["body_md"])
        print(f"[generate] + {slug}")
        made += 1
    print(f"[generate] {made} new post(s); total {len(done) + made}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
