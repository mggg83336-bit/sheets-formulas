#!/usr/bin/env python3
"""静态站构建：content/posts/*.md -> dist/
生成：首页、文章页、标签页、404、sitemap.xml、robots.txt、feed.xml(RSS)。

用法: python scripts/build.py [--base-url URL]   (也可用环境变量 SITE_BASE_URL 覆盖)
"""
import argparse
import datetime as dt
import os
import shutil
import sys
from email.utils import format_datetime
from urllib.parse import quote, urlparse
from xml.sax.saxutils import escape

import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

from common import (AD_PLACEHOLDER, CONTENT, DIST, PRODUCT_PLACEHOLDER, ROOT,
                    load_site, read_post, slugify)


def main():
    cfg = load_site()
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", default=os.environ.get("SITE_BASE_URL") or cfg["site"]["base_url"])
    a = ap.parse_args()
    base_url = a.base_url.rstrip("/")
    base_path = urlparse(base_url).path.rstrip("/")  # 例如 /autosite

    env = Environment(loader=FileSystemLoader(ROOT / "templates"),
                      autoescape=select_autoescape(["html"]))
    md = markdown.Markdown(extensions=["extra", "toc"])

    posts = []
    for p in sorted(CONTENT.glob("*.md")):
        meta, body = read_post(p)
        md.reset()
        html = md.convert(body)
        meta["html"] = html
        meta["date"] = str(meta["date"])
        meta["url"] = f"{base_path}/posts/{quote(meta['slug'])}/"
        meta["abs_url"] = f"{base_url}/posts/{quote(meta['slug'])}/"
        meta["tag_links"] = [(t, f"{base_path}/tags/{quote(slugify(t))}/") for t in meta.get("tags", [])]
        posts.append(meta)
    posts.sort(key=lambda m: (m["date"], m["slug"]), reverse=True)
    if len({m["slug"] for m in posts}) != len(posts):
        raise SystemExit("duplicate slugs in content/posts")

    tmp = DIST.with_name("dist.tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    tmp.mkdir(parents=True)
    shutil.copytree(ROOT / "static", tmp / "static")

    g = dict(site=cfg["site"], ads=cfg.get("ads", {}), products=cfg.get("products", []),
             affiliate_links=cfg.get("affiliate_links", []), analytics=cfg.get("analytics", {}),
             base_path=base_path, base_url=base_url, year=dt.date.today().year)
    product_html = env.get_template("_products.html").render(**g)
    ad_html = env.get_template("_ad.html").render(**g)

    def write(rel, tpl, **kw):
        out = tmp / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(env.get_template(tpl).render(**g, **kw), encoding="utf-8")

    write("index.html", "index.html", posts=posts, page_title=cfg["site"]["title"],
          description=cfg["site"]["description"], canonical=f"{base_url}/")
    for m in posts:
        body = m["html"].replace(AD_PLACEHOLDER, ad_html).replace(PRODUCT_PLACEHOLDER, product_html)
        write(f"posts/{m['slug']}/index.html", "post.html", post=m, body=body,
              page_title=f"{m['title']} | {cfg['site']['title']}",
              description=m.get("summary") or cfg["site"]["description"], canonical=m["abs_url"])
    tags = {}
    for m in posts:
        for t in m.get("tags", []):
            tags.setdefault(t, []).append(m)
    for t, ps in tags.items():
        write(f"tags/{slugify(t)}/index.html", "index.html", posts=ps,
              page_title=f"{t} | {cfg['site']['title']}", description=f"{t} 相关文章",
              canonical=f"{base_url}/tags/{quote(slugify(t))}/")
    write("404.html", "404.html", page_title="页面不存在", description="404", canonical=f"{base_url}/404.html")

    # sitemap.xml
    urls = [(f"{base_url}/", posts[0]["date"] if posts else dt.date.today().isoformat())]
    urls += [(m["abs_url"], m["date"]) for m in posts]
    urls += [(f"{base_url}/tags/{quote(slugify(t))}/", ps[0]["date"]) for t, ps in tags.items()]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f"  <url><loc>{escape(u)}</loc><lastmod>{d}</lastmod></url>" for u, d in urls]
    sm.append("</urlset>")
    (tmp / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")

    (tmp / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {base_url}/sitemap.xml\n", encoding="utf-8")

    # RSS 2.0
    def rfc822(d):
        return format_datetime(dt.datetime.fromisoformat(d).replace(tzinfo=dt.timezone.utc))
    items = "".join(
        f"<item><title>{escape(m['title'])}</title><link>{escape(m['abs_url'])}</link>"
        f"<guid>{escape(m['abs_url'])}</guid><pubDate>{rfc822(m['date'])}</pubDate>"
        f"<description>{escape(m.get('summary', ''))}</description></item>" for m in posts[:50])
    s = cfg["site"]
    (tmp / "feed.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel>'
        f"<title>{escape(s['title'])}</title><link>{escape(base_url)}/</link>"
        f"<description>{escape(s['description'])}</description><language>{s['language']}</language>"
        f"{items}</channel></rss>\n", encoding="utf-8")
    (tmp / ".nojekyll").write_text("")

    # 原子替换：只有完整构建成功才覆盖 dist/
    shutil.rmtree(DIST, ignore_errors=True)
    tmp.rename(DIST)
    print(f"[build] OK: {len(posts)} posts, {len(tags)} tags -> {DIST} (base_url={base_url})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
