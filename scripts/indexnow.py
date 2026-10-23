#!/usr/bin/env python3
"""Submit every sitemap URL to IndexNow after GitHub Pages is live.

The key is public (site.yaml indexnow.key). build.py publishes it at the
site root as <key>.txt. No API secret. Exit 0 only when IndexNow returns
200 or 202.

Usage:
  LIVE_URL=https://example.github.io/repo python scripts/indexnow.py
  python scripts/indexnow.py --dry-run
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

from common import DIST, load_site

ENDPOINT = "https://api.indexnow.org/indexnow"
SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
KEY_RE = re.compile(r"[A-Za-z0-9-]{8,128}")
OK = {200, 202}
CHUNK = 10000


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


def fetch(url, timeout=30, data=None, headers=None):
    req = urllib.request.Request(
        url,
        data=data,
        method="POST" if data is not None else "GET",
        headers=headers or {"User-Agent": "autosite-indexnow/1.0", "Cache-Control": "no-cache"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.status, response.read()
    except urllib.error.HTTPError as err:
        return err.code, err.read()
    except urllib.error.URLError as err:
        return 0, str(err.reason).encode()


def wait_for(label, check, attempts=6):
    for attempt in range(attempts):
        ok, detail = check()
        if ok:
            print(f"[indexnow] {label}: {detail}")
            return
        print(f"[indexnow] {label} attempt {attempt + 1} not ready: {detail}", file=sys.stderr)
        if attempt < attempts - 1:
            time.sleep(min(10 * 2 ** attempt, 60))
    raise SystemExit(f"[indexnow] gave up waiting for {label}")


def load_key():
    key = str((load_site().get("indexnow") or {}).get("key") or "").strip()
    if not KEY_RE.fullmatch(key):
        raise SystemExit("site.yaml indexnow.key must be 8-128 characters from [A-Za-z0-9-]")
    return key


def urls_from_sitemap(xml_text, prefix):
    locs = list(dict.fromkeys(sitemap_locs(xml_text)))
    if not locs:
        raise SystemExit("sitemap.xml has no URLs")
    outside = [u for u in locs if not u.startswith(prefix)]
    if outside:
        raise SystemExit(f"sitemap URL is outside the key location: {outside[0]}")
    return locs


def submit(payload):
    data = json.dumps(payload).encode("utf-8")
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "User-Agent": "autosite-indexnow/1.0",
    }
    status, body = 0, b""
    for attempt in range(4):
        status, body = fetch(ENDPOINT, data=data, headers=headers)
        if status in OK:
            print(f"IndexNow response: {status}")
            return status
        snippet = body.decode("utf-8", "replace")[:300]
        print(f"[indexnow] HTTP {status} attempt {attempt + 1}: {snippet}", file=sys.stderr)
        if status == 400 or attempt == 3:
            break
        time.sleep(min(10 * 2 ** attempt, 60))
    print(f"IndexNow response: {status}")
    raise SystemExit(f"IndexNow failed with HTTP {status}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="validate local dist/ and do not POST")
    ap.add_argument("--base-url", default=os.environ.get("LIVE_URL") or os.environ.get("SITE_BASE_URL") or "")
    args = ap.parse_args()

    key = load_key()
    base = (args.base_url or load_site()["site"]["base_url"]).rstrip("/")
    host = urlparse(base).netloc
    if not host:
        raise SystemExit(f"could not parse host from {base}")
    prefix = base + "/"
    key_url = f"{prefix}{key}.txt"
    sitemap_url = f"{prefix}sitemap.xml"
    robots_url = f"{prefix}robots.txt"

    if args.dry_run:
        robots = (DIST / "robots.txt").read_text(encoding="utf-8")
        xml_text = (DIST / "sitemap.xml").read_text(encoding="utf-8")
        published = (DIST / f"{key}.txt").read_text(encoding="utf-8").strip()
        if published != key:
            raise SystemExit("local IndexNow key file does not match site.yaml")
        if f"Sitemap: {sitemap_url}" not in robots:
            raise SystemExit(f"robots.txt does not reference {sitemap_url}")
    else:
        def check_key():
            status, body = fetch(key_url)
            text = body.decode("utf-8", "replace").strip()
            if status == 200 and text == key:
                return True, key_url
            return False, f"{key_url} -> {status} {text[:80]!r}"

        def check_robots():
            status, body = fetch(robots_url)
            text = body.decode("utf-8", "replace")
            if status == 200 and f"Sitemap: {sitemap_url}" in text:
                return True, sitemap_url
            return False, f"{robots_url} -> {status}"

        def check_sitemap():
            status, body = fetch(sitemap_url)
            if status != 200:
                return False, f"{sitemap_url} -> {status}"
            try:
                urls_from_sitemap(body.decode("utf-8"), prefix)
            except (ET.ParseError, ValueError, SystemExit) as err:
                return False, str(err)
            return True, sitemap_url

        wait_for("key file", check_key)
        wait_for("robots.txt", check_robots)
        wait_for("sitemap.xml", check_sitemap)
        status, body = fetch(sitemap_url)
        robots_status, robots_body = fetch(robots_url)
        if robots_status != 200 or f"Sitemap: {sitemap_url}" not in robots_body.decode("utf-8", "replace"):
            raise SystemExit("live robots.txt does not reference sitemap.xml")
        if status != 200:
            raise SystemExit(f"live sitemap.xml returned {status}")
        xml_text = body.decode("utf-8")

    locs = urls_from_sitemap(xml_text, prefix)
    print(f"[indexnow] {len(locs)} sitemap urls; host={host}; keyLocation={key_url}")
    if args.dry_run:
        print("IndexNow response: dry-run")
        return 0

    codes = []
    for start in range(0, len(locs), CHUNK):
        chunk = locs[start:start + CHUNK]
        codes.append(submit({
            "host": host,
            "key": key,
            "keyLocation": key_url,
            "urlList": chunk,
        }))
    if any(code not in OK for code in codes):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
