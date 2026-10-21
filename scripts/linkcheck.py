#!/usr/bin/env python3
"""链接检查器：扫描 dist/ 下所有 HTML，检查站内链接/资源是否存在；可选检查站外链接。

用法: python scripts/linkcheck.py [--external] [--base-url URL]
退出码 0 = 全部正常，1 = 有坏链。
"""
import argparse
import os
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from urllib.parse import unquote, urljoin, urlparse

from common import DIST, load_site


class _P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for k, v in attrs:
            if v and ((k == "href" and tag in ("a", "link")) or (k == "src" and tag in ("img", "script", "iframe"))):
                self.links.append(v)


def internal_target(path: str):
    """把站内 URL 路径映射到 dist/ 中的文件。"""
    p = DIST / unquote(path).lstrip("/")
    if path.endswith("/") or p.is_dir():
        p = p / "index.html"
    return p


def check_external(url, timeout=15):
    err = "unknown error"
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers={"User-Agent": "autosite-linkcheck/1.0"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                if r.status < 400:
                    return None
        except Exception as e:  # noqa: BLE001
            err = str(e)
            continue
    return err


def run(external=False, base_url=None):
    cfg = load_site()
    base_url = (base_url or os.environ.get("SITE_BASE_URL") or cfg["site"]["base_url"]).rstrip("/")
    bu = urlparse(base_url)
    base_path = bu.path.rstrip("/")
    if not DIST.exists():
        print("[linkcheck] dist/ not found; run build first")
        return 1
    broken, externals, n = [], {}, 0
    for html in DIST.rglob("*.html"):
        rel = "/" + html.relative_to(DIST).as_posix()
        page_url = base_path + (rel[: -len("index.html")] if rel.endswith("index.html") else rel)
        p = _P()
        p.feed(html.read_text(encoding="utf-8"))
        for link in p.links:
            n += 1
            if link.startswith(("mailto:", "tel:", "javascript:", "#", "data:")):
                continue
            u = urlparse(urljoin(page_url, link))
            if u.scheme in ("http", "https") and u.netloc != bu.netloc:
                externals.setdefault(link.split("#")[0], []).append(rel)
                continue
            path = u.path
            if base_path and not path.startswith(base_path + "/") and path != base_path:
                broken.append((rel, link, "outside base path"))
                continue
            path = path[len(base_path):] or "/"
            if not internal_target(path).exists():
                broken.append((rel, link, "missing file"))
    for x in ("sitemap.xml", "robots.txt", "feed.xml", "index.html", "404.html"):
        if not (DIST / x).exists():
            broken.append(("-", x, "required file missing"))
    if external and externals:
        with ThreadPoolExecutor(8) as ex:
            for url, err in zip(externals, ex.map(check_external, externals)):
                if err:
                    broken.append((externals[url][0], url, f"external: {err}"))
    for b in broken:
        print(f"[linkcheck] BROKEN {b[0]} -> {b[1]} ({b[2]})")
    print(f"[linkcheck] checked {n} links ({len(externals)} external{'' if external else ', skipped'}); broken={len(broken)}")
    return 1 if broken else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--external", action="store_true")
    ap.add_argument("--base-url")
    a = ap.parse_args()
    sys.exit(run(a.external or load_site().get("health", {}).get("check_external_links", False), a.base_url))
