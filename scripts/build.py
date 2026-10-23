#!/usr/bin/env python3
"""静态站构建：content/posts/*.md -> dist/
生成：首页、文章页、标签页、404、sitemap.xml、robots.txt、feed.xml(RSS)。

用法: python scripts/build.py [--base-url URL]   (也可用环境变量 SITE_BASE_URL 覆盖)
"""
import argparse
import datetime as dt
import os
import re
import shutil
import sys
import xml.etree.ElementTree as ET
from email.utils import format_datetime
from urllib.parse import parse_qsl, quote, urlencode, urlparse, urlsplit, urlunsplit
from xml.sax.saxutils import escape

import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

from common import (AD_PLACEHOLDER, CONTENT, DIST, PRODUCT_PLACEHOLDER, ROOT,
                    load_site, read_post, slugify)
from structured import CATEGORY_LABELS, RELATED_PLACEHOLDER, SIBLING_PLACEHOLDER

SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
INDEXNOW_KEY = re.compile(r"[A-Za-z0-9-]{8,128}")


def indexnow_key(cfg):
    key = str((cfg.get("indexnow") or {}).get("key") or "").strip()
    if not INDEXNOW_KEY.fullmatch(key):
        raise SystemExit("site.yaml indexnow.key must be 8-128 characters from [A-Za-z0-9-]")
    return key


def product_view(p):
    """Copy a product and attach the public CTA href. offer_code is config-only."""
    url = str(p.get("url") or "").strip()
    code = str(p.get("offer_code") or "").strip()
    note = str(p.get("offer_note") or "").strip()
    href = url
    if code and url and "REPLACE_ME" not in url:
        parts = urlsplit(url)
        query = [(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True) if k != "code"]
        query.append(("code", code))
        href = urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(query), parts.fragment))
    return dict(p, url=url, offer_code=code, offer_note=note, href=href,
                live="REPLACE_ME" not in url)


def sitemap_locs(xml_text):
    root = ET.fromstring(xml_text)
    if root.tag != f"{SITEMAP_NS}urlset":
        raise ValueError("sitemap root is not urlset")
    locs = []
    for node in root.findall(f"{SITEMAP_NS}url"):
        loc = node.find(f"{SITEMAP_NS}loc")
        text = (loc.text or "").strip() if loc is not None else ""
        if not text:
            raise ValueError("sitemap url missing loc")
        locs.append(text)
    return locs


def check_published_files(root, base_url, key):
    sitemap_url = f"{base_url}/sitemap.xml"
    robots = (root / "robots.txt").read_text(encoding="utf-8")
    if f"Sitemap: {sitemap_url}" not in robots:
        raise SystemExit(f"robots.txt does not reference {sitemap_url}")
    locs = sitemap_locs((root / "sitemap.xml").read_text(encoding="utf-8"))
    if not locs:
        raise SystemExit("sitemap.xml has no URLs")
    prefix = base_url + "/"
    outside = [u for u in locs if not u.startswith(prefix)]
    if outside:
        raise SystemExit(f"sitemap URL is outside the site: {outside[0]}")
    key_file = root / f"{key}.txt"
    if not key_file.is_file() or key_file.read_text(encoding="utf-8").strip() != key:
        raise SystemExit("IndexNow key file is missing at the site root")
    print(f"[build] sitemap OK: {len(locs)} urls; robots references {sitemap_url}")


UI = {  # interface strings by site.language
    "en": {"no_posts": "No pages yet.", "tag_desc": "{t}: all formula guides", "not_found": "Page not found",
           "related_fallback": "More {c}", "sibling": "Using {p}? Read the {p} version of this guide",
           "home": "Home"},
    "zh-CN": {"no_posts": "暂无文章。", "tag_desc": "{t} 相关文章", "not_found": "页面不存在",
              "related_fallback": "更多{c}", "sibling": "{p} 版本", "home": "首页"},
}


def resolve_links(m, by_slug, html, ui):
    """Fill RELATED / SIBLING placeholders with links to pages that are actually published."""
    if RELATED_PLACEHOLDER in html:
        picks, seen = [], {m["slug"]}
        for cands in m.get("related") or []:
            cands = cands if isinstance(cands, list) else [cands]
            for c in cands:
                if c in by_slug and c not in seen:
                    picks.append(by_slug[c])
                    seen.add(c)
                    break
        if len(picks) < 3:  # top up with same-category pages so every page links onward
            for o in by_slug.values():
                if len(picks) >= 5:
                    break
                if o["slug"] not in seen and o.get("category") == m.get("category"):
                    picks.append(o)
                    seen.add(o["slug"])
        items = "".join(f'<li><a href="{o["url"]}">{escape(o["title"])}</a></li>' for o in picks)
        html = html.replace(RELATED_PLACEHOLDER, f'<ul class="related">{items}</ul>' if items else "")
    if SIBLING_PLACEHOLDER in html:
        sib = by_slug.get(m.get("sibling") or "")
        link = (f'<p class="sibling"><a href="{sib["url"]}">{escape(ui["sibling"].format(p=sib.get("platform", "")))} &rarr;</a></p>'
                if sib else "")
        html = html.replace(f"<p>{SIBLING_PLACEHOLDER}</p>", link).replace(SIBLING_PLACEHOLDER, link)
    return html


def main():
    cfg = load_site()
    key = indexnow_key(cfg)
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", default=os.environ.get("SITE_BASE_URL") or cfg["site"]["base_url"])
    a = ap.parse_args()
    base_url = a.base_url.rstrip("/")
    base_path = urlparse(base_url).path.rstrip("/")  # 例如 /autosite

    env = Environment(loader=FileSystemLoader(ROOT / "templates"),
                      autoescape=select_autoescape(["html"]))
    md = markdown.Markdown(extensions=["extra", "toc"])
    env.filters["faq_entity"] = lambda f: {"@type": "Question", "name": f["q"],
                                           "acceptedAnswer": {"@type": "Answer", "text": f["a"]}}

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
    ui = UI.get(cfg["site"].get("language", "en"), UI["en"])
    by_slug = {m["slug"]: m for m in sorted(posts, key=lambda m: m["title"])}
    for m in posts:
        m["html"] = resolve_links(m, by_slug, m["html"], ui)
        if m.get("category"):
            m["category_label"] = CATEGORY_LABELS.get(m["category"], m["category"])
            m["category_url"] = f"{base_path}/tags/{quote(slugify(m['category_label']))}/"
            m["category_abs_url"] = f"{base_url}/tags/{quote(slugify(m['category_label']))}/"
    groups = {}
    for m in sorted(posts, key=lambda m: m["title"]):
        groups.setdefault(m.get("category_label") or "", []).append(m)
    order = list(CATEGORY_LABELS.values())
    groups = sorted(groups.items(), key=lambda kv: order.index(kv[0]) if kv[0] in order else 99)
    if len({m["slug"] for m in posts}) != len(posts):
        raise SystemExit("duplicate slugs in content/posts")

    tmp = DIST.with_name("dist.tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    tmp.mkdir(parents=True)
    shutil.copytree(ROOT / "static", tmp / "static")

    products = [product_view(p) for p in cfg.get("products", [])]
    g = dict(site=cfg["site"], ads=cfg.get("ads", {}), products=products, ui=ui,
             affiliate_links=cfg.get("affiliate_links", []), analytics=cfg.get("analytics", {}),
             base_path=base_path, base_url=base_url, year=dt.date.today().year)
    product_html = env.get_template("_products.html").render(**g)
    g["product_top_html"] = env.get_template("_products.html").render(**g, compact=True)
    ad_html = env.get_template("_ad.html").render(**g)

    def write(rel, tpl, **kw):
        out = tmp / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(env.get_template(tpl).render(**g, **kw), encoding="utf-8")

    write("index.html", "index.html", posts=posts, groups=groups, is_home=True,
          page_title=cfg["site"]["title"] + (f" | {cfg['site']['tagline']}" if cfg["site"].get("tagline") else ""),
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
              page_title=f"{t} | {cfg['site']['title']}", description=ui["tag_desc"].format(t=t),
              canonical=f"{base_url}/tags/{quote(slugify(t))}/")
    write("404.html", "404.html", page_title=ui["not_found"], description="404", canonical=f"{base_url}/404.html")

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
    (tmp / f"{key}.txt").write_text(key, encoding="utf-8")
    check_published_files(tmp, base_url, key)

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
