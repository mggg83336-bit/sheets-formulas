#!/usr/bin/env python3
"""内容流水线：按 niche 配置生成新文章（幂等，已生成的关键词会跳过）。

用法: python scripts/generate.py [--limit N] [--niche NAME] [--provider NAME]
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


def main():
    site = load_site()
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=site.get("generate_per_run", 3))
    ap.add_argument("--niche", default=site["niche"])
    ap.add_argument("--provider", default=site.get("provider", "template"))
    a = ap.parse_args()

    niche = load_niche(a.niche)
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
