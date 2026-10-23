#!/usr/bin/env python3
"""Confirm the live RSS feed is well-formed and every pin image is a 1000x1500 PNG.

Usage: LIVE_URL=https://example.github.io/repo python scripts/check_feed.py
Exit 0 when the feed and every enclosure return HTTP 200.
"""
import os
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

from common import load_site
from pins import PIN_H, PIN_W, assert_item_fields, parse_feed, png_size


def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers={
        "User-Agent": "autosite-feedcheck/1.0",
        "Cache-Control": "no-cache",
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.status, response.read()
    except urllib.error.HTTPError as err:
        return err.code, err.read()
    except urllib.error.URLError as err:
        return 0, str(err.reason).encode()


def wait_for(label, check, attempts=5):
    for attempt in range(attempts):
        ok, detail = check()
        if ok:
            print(f"[feed] {label}: {detail}")
            return detail
        print(f"[feed] {label} attempt {attempt + 1} not ready: {detail}", file=sys.stderr)
        if attempt < attempts - 1:
            time.sleep(min(8 * 2 ** attempt, 40))
    raise SystemExit(f"[feed] gave up waiting for {label}")


def main():
    base = (os.environ.get("LIVE_URL") or os.environ.get("SITE_BASE_URL") or load_site()["site"]["base_url"]).rstrip("/")
    feed_url = f"{base}/feed.xml"

    def check_feed():
        status, body = fetch(feed_url)
        if status != 200:
            return False, f"{feed_url} -> {status}"
        try:
            items = parse_feed(body.decode("utf-8"))
            for item in items:
                assert_item_fields(item)
        except (SystemExit, ValueError, ET.ParseError) as err:
            return False, str(err)
        if not items:
            return False, "feed has no items"
        return True, f"{feed_url} 200, {len(items)} items"

    wait_for("feed.xml", check_feed)

    def check_image(url):
        def check():
            status, body = fetch(url)
            if status != 200:
                return False, f"{url} -> {status}"
            try:
                width, height = png_size(body)
            except ValueError as err:
                return False, f"{url} -> {err}"
            if (width, height) != (PIN_W, PIN_H):
                return False, f"{url} -> {width}x{height}"
            return True, f"{url} 200 {width}x{height}"
        return check

    # Re-parse after the successful fetch so image checks use the live items.
    status, body = fetch(feed_url)
    if status != 200:
        raise SystemExit(f"{feed_url} returned {status}")
    items = parse_feed(body.decode("utf-8"))
    for item in items:
        assert_item_fields(item)
        wait_for("pin", check_image(item["enclosure_url"]))
    sample = items[0]["enclosure_url"]
    print(f"[feed] OK: {feed_url}")
    print(f"[feed] sample pin {sample}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
