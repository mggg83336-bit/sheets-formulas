#!/usr/bin/env python3
"""Keyword queue for structured niches.

The queue is a CSV (niche.yaml -> queue_file) with columns:
    keyword,platform,slug,category,source,added
Order = publishing order. Nothing is ever deleted; "published" is derived from
content/posts/<slug>.md, so the file never needs rewriting by the daily job.

Commands:
  python scripts/kwqueue.py ingest FILE [FILE...] [--source NAME] [--platform Excel|"Google Sheets"]
      FILE is either a plain list (one keyword per line, '#' comments ok) or a CSV whose
      header contains `keyword` (optional columns: platform, slug, category).
      Duplicates (same slug or same normalized keyword) are skipped.
  python scripts/kwqueue.py status [--verbose]
      Counts: published / ready (has content that passes the quality gate) / waiting for content.
"""
import argparse
import csv
import datetime as dt
import re
import sys

from common import CONTENT, load_niche, load_site

FIELDS = ["keyword", "platform", "slug", "category", "source", "added"]

CATEGORY_RULES = [  # first match wins
    ("errors", r"#n/a|#value|#ref|#div|#name|#num|#spill|circular|not calculating|\berror\b|show formulas"),
    ("conditional", r"with criteria"),
    ("lookup", r"sequence|row and column|flip a column|lookup|index|match|xmatch|indirect|offset|choose\b|two way|last value|exists in list|missing values|"
               r"compare two|filter|unique|sort|query|importrange|transpose|dropdown|sheet name|hyperlink"),
    ("conditional", r"sumif|countif|averageif|maxifs|minifs|sumproduct|count unique|sum by|count by|non blank|"
                    r"blank cells|sum every|sum ignoring|frequency|median by group|pivot|running total|duplicates"),
    ("date", r"date|day|days|month|week|year|time|hour|minute|today|now\b|eomonth|networkdays|workday|age\b|"
             r"birthday|countdown|quarter|overtime|attendance|gantt"),
    ("financial", r"interest|pmt|loan|mortgage|cagr|npv|irr|profit|margin|tax|commission|percentage|percent|"
                  r"currency|budget|invoice|googlefinance|average|median|rank|round|correlation|forecast|"
                  r"standard deviation|large|small|grade|inventory|rand"),
    ("text", r"text|concat|join|split|trim|substitute|replace|left|right|mid|len\b|upper|lower|proper|"
             r"character|characters|word|leading zeros|regex|domain|name|line break|reverse"),
    ("logic", r"\bif\b|ifs|iferror|switch|and or|isblank|isnumber|istext|let\b|lambda|array"),
]


def slugify_en(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def categorize(keyword):
    k = keyword.lower()
    for cat, rx in CATEGORY_RULES:
        if re.search(rx, k):
            return cat
    return "other"


def infer_platform(keyword, default=""):
    k = keyword.lower()
    if "google sheets" in k or "gsheets" in k:
        return "Google Sheets"
    if "excel" in k:
        return "Excel"
    return default


def norm(keyword):
    return re.sub(r"\s+", " ", keyword.strip().lower())


def queue_path(niche):
    return niche["_dir"] / niche.get("queue_file", "queue.csv")


def load_queue(niche):
    p = queue_path(niche)
    if not p.exists():
        return []
    with open(p, encoding="utf-8-sig", newline="") as f:
        return [r for r in csv.DictReader(f) if (r.get("slug") or "").strip()]


def read_input(path, default_platform):
    text = open(path, encoding="utf-8-sig").read()
    first = text.splitlines()[0] if text.strip() else ""
    rows = []
    if "keyword" in [h.strip().lower() for h in first.split(",")]:
        for r in csv.DictReader(text.splitlines()):
            r = {k.strip().lower(): (v or "").strip() for k, v in r.items() if k}
            if r.get("keyword"):
                rows.append(r)
    else:
        for line in text.splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                rows.append({"keyword": line})
    out = []
    for r in rows:
        kw = re.sub(r"\s+", " ", r["keyword"])
        plat = r.get("platform") or infer_platform(kw, default_platform)
        slug = slugify_en(r.get("slug") or kw)
        out.append({"keyword": kw, "platform": plat, "slug": slug,
                    "category": r.get("category") or categorize(kw)})
    return out


def cmd_ingest(a, niche):
    q = load_queue(niche)
    seen_slug = {r["slug"] for r in q}
    seen_kw = {norm(r["keyword"]) for r in q}
    today = dt.date.today().isoformat()
    added, dups = [], 0
    for path in a.files:
        src = a.source or path.split("/")[-1]
        for r in read_input(path, a.platform):
            if r["slug"] in seen_slug or norm(r["keyword"]) in seen_kw:
                dups += 1
                continue
            seen_slug.add(r["slug"])
            seen_kw.add(norm(r["keyword"]))
            added.append({**r, "source": src, "added": today})
    p = queue_path(niche)
    new_file = not p.exists()
    with open(p, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if new_file:
            w.writeheader()
        w.writerows(added)
    print(f"[queue] +{len(added)} keyword(s), {dups} duplicate(s) skipped -> {p} (total {len(q) + len(added)})")
    return 0


def queue_report(niche, site=None):
    """Return rows annotated with state: published | ready | needs-content | blocked(reason)."""
    import structured
    entries = structured.load_entries(niche)
    smap = structured.slug_map(entries)
    published = {p.stem for p in CONTENT.glob("*.md")}
    gate_cfg = niche.get("quality_gate", {})
    out = []
    for r in load_queue(niche):
        s = r["slug"]
        if s in published:
            st = "published"
        elif s in smap:
            e, plat = smap[s]
            probs = structured.gate(e, plat, gate_cfg)
            st = "ready" if not probs else "blocked: " + "; ".join(probs)
        else:
            st = "needs-content"
        out.append({**r, "state": st})
    return out


def cmd_status(a, niche):
    rows = queue_report(niche)
    from collections import Counter
    c = Counter(r["state"].split(":")[0] for r in rows)
    print(f"[queue] {len(rows)} keywords: " + ", ".join(f"{k}={v}" for k, v in sorted(c.items())))
    cats = Counter((r["category"], r["state"].split(":")[0]) for r in rows)
    for cat in sorted({r["category"] for r in rows}):
        print(f"  {cat:12s} " + ", ".join(f"{s}={cats[(cat, s)]}" for s in ("published", "ready", "blocked", "needs-content") if cats[(cat, s)]))
    if a.verbose:
        for r in rows:
            if r["state"] != "published":
                print(f"  {r['state'][:60]:60s} {r['slug']}")
    return 0


def main():
    site = load_site()
    ap = argparse.ArgumentParser()
    ap.add_argument("--niche", default=site["niche"])
    sub = ap.add_subparsers(dest="cmd", required=True)
    i = sub.add_parser("ingest")
    i.add_argument("files", nargs="+")
    i.add_argument("--source")
    i.add_argument("--platform", default="", help="platform for lines that do not mention one")
    s = sub.add_parser("status")
    s.add_argument("--verbose", "-v", action="store_true")
    a = ap.parse_args()
    niche = load_niche(a.niche)
    return cmd_ingest(a, niche) if a.cmd == "ingest" else cmd_status(a, niche)


if __name__ == "__main__":
    sys.exit(main())
