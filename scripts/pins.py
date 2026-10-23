#!/usr/bin/env python3
"""Build-time Pinterest pins (1000x1500 PNG) and the RSS item image tags.

New formula pages pick up a pin on the next build. No network calls.
"""
import re
from email.utils import format_datetime
from urllib.parse import urlparse
from xml.sax.saxutils import escape

from common import ROOT

PIN_W, PIN_H = 1000, 1500
MEDIA_NS = "http://search.yahoo.com/mrss/"
ATOM_NS = "http://www.w3.org/2005/Atom"
FONT_DIR = ROOT / "assets" / "fonts"
REGULAR = FONT_DIR / "DejaVuSans.ttf"
BOLD = FONT_DIR / "DejaVuSans-Bold.ttf"

GREEN = "#107c41"
GREEN_DEEP = "#0c5c32"
INK = "#1f2328"
MUTED = "#656d76"
WHITE = "#ffffff"
MINT = "#e7f6ee"

# One honest fallback when a page has no summary. Every formula page is that.
FALLBACK_BENEFIT = "Copy-ready formula with a worked example and fixes for common errors."


def benefit_line(summary):
    """First sentence of the page summary, collapsed to a single line of meaning."""
    text = re.sub(r"\s+", " ", str(summary or "")).strip()
    if not text:
        return FALLBACK_BENEFIT
    return re.split(r"(?<=[.!?])\s+", text, maxsplit=1)[0]


def _font(path, size):
    from PIL import ImageFont
    if not path.is_file():
        raise SystemExit(f"pin font missing: {path}")
    return ImageFont.truetype(str(path), size=size)


def _wrap(draw, text, font, max_width):
    words = str(text).split()
    if not words:
        return [""]
    lines, cur = [], ""
    for word in words:
        trial = word if not cur else f"{cur} {word}"
        if draw.textlength(trial, font=font) <= max_width:
            cur = trial
            continue
        if cur:
            lines.append(cur)
        if draw.textlength(word, font=font) <= max_width:
            cur = word
            continue
        chunk = ""
        for ch in word:
            if draw.textlength(chunk + ch, font=font) <= max_width:
                chunk += ch
            else:
                if chunk:
                    lines.append(chunk)
                chunk = ch
        cur = chunk
    if cur:
        lines.append(cur)
    return lines


def _ellipsize(draw, lines, font, max_width, max_lines):
    if len(lines) <= max_lines:
        return lines
    kept = lines[:max_lines]
    last = kept[-1]
    ell = "…"
    while last and draw.textlength(last + ell, font=font) > max_width:
        last = last[:-1].rstrip()
    kept[-1] = (last + ell) if last else ell
    return kept


def _line_step(font, spacing=1.18):
    ascent, descent = font.getmetrics()
    return int((ascent + descent) * spacing)


def _draw_centered(draw, lines, font, cx, top, fill):
    step = _line_step(font, 1.12)
    for i, line in enumerate(lines):
        draw.text((cx, top + i * step), line, font=font, fill=fill, anchor="mt")
    return max(len(lines), 1) * step


def _draw_left(draw, lines, font, x, top, fill):
    step = _line_step(font, 1.16)
    for i, line in enumerate(lines):
        draw.text((x, top + i * step), line, font=font, fill=fill, anchor="lt")
    return max(len(lines), 1) * step


def render_pin(title, benefit, site_name, tagline=""):
    """Vertical pin: site name, page title, and a one-sentence benefit."""
    from PIL import Image, ImageDraw

    img = Image.new("RGB", (PIN_W, PIN_H), GREEN)
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((36, 36, PIN_W - 36, PIN_H - 36), radius=36, fill=WHITE)
    draw.rectangle((36, 250, PIN_W - 36, 268), fill=GREEN)

    site_font = _font(BOLD, 58)
    tag_font = _font(REGULAR, 28)
    tagline = re.sub(r"\s+", " ", str(tagline or "")).strip()
    tag_lines = _ellipsize(draw, _wrap(draw, tagline, tag_font, 760), tag_font, 760, 2) if tagline else []

    _draw_centered(draw, [site_name or "FormulaFix"], site_font, PIN_W // 2, 88, GREEN_DEEP)
    if tag_lines:
        _draw_centered(draw, tag_lines, tag_font, PIN_W // 2, 168, MUTED)

    content_w = 760
    x = (PIN_W - content_w) // 2
    title_font = benefit_font = None
    title_lines = benefit_lines = None
    for title_size, benefit_size, max_title, max_benefit in (
        (64, 34, 4, 6),
        (56, 32, 5, 7),
        (48, 28, 6, 8),
    ):
        title_font = _font(BOLD, title_size)
        benefit_font = _font(REGULAR, benefit_size)
        title_lines = _ellipsize(draw, _wrap(draw, title, title_font, content_w), title_font, content_w, max_title)
        benefit_lines = _ellipsize(
            draw, _wrap(draw, benefit, benefit_font, content_w), benefit_font, content_w, max_benefit)
        block_h = (
            _line_step(title_font) * len(title_lines)
            + 48
            + _line_step(benefit_font) * len(benefit_lines)
        )
        if block_h <= 980 and title_lines[-1][-1:] != "…" and benefit_lines[-1][-1:] != "…":
            break

    block_h = (
        _line_step(title_font) * len(title_lines)
        + 48
        + _line_step(benefit_font) * len(benefit_lines)
    )
    top = 300
    bottom = 1380
    y = top + max(0, (bottom - top - block_h) // 2)
    y += _draw_left(draw, title_lines, title_font, x, y, INK)
    y += 28
    draw.rectangle((x, y, x + 112, y + 8), fill=GREEN)
    y += 28
    _draw_left(draw, benefit_lines, benefit_font, x, y, MUTED)

    foot_font = _font(BOLD, 28)
    _draw_centered(draw, [site_name or "FormulaFix"], foot_font, PIN_W // 2, 1424, GREEN)
    if img.size != (PIN_W, PIN_H):
        raise SystemExit(f"pin rendered at {img.size}, expected {(PIN_W, PIN_H)}")
    return img


def save_pin(image, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, "PNG", optimize=True)
    data = path.read_bytes()
    width, height = png_size(data)
    if (width, height) != (PIN_W, PIN_H):
        raise SystemExit(f"{path.name} is {width}x{height}, expected {PIN_W}x{PIN_H}")
    return len(data)


def png_size(data):
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        raise ValueError("not a PNG")
    return int.from_bytes(data[16:20], "big"), int.from_bytes(data[20:24], "big")


def _attr(value):
    return escape(str(value), {'"': "&quot;", "'": "&apos;"})


def render_feed(site, base_url, posts, now):
    """RSS 2.0 with one item per formula page. Image is enclosure and media:content."""
    base = base_url.rstrip("/")
    items = []
    for m in posts:
        pin = m["pin_url"]
        desc = re.sub(r"\s+", " ", str(m.get("summary") or m.get("benefit") or "")).strip() or m["title"]
        items.append(
            "<item>"
            f"<title>{escape(m['title'])}</title>"
            f"<link>{_attr(m['abs_url'])}</link>"
            f'<guid isPermaLink="true">{_attr(m["abs_url"])}</guid>'
            f"<pubDate>{escape(m['pub_date'])}</pubDate>"
            f"<description>{escape(desc)}</description>"
            f'<enclosure url="{_attr(pin)}" length="{int(m["pin_bytes"])}" type="image/png"/>'
            f'<media:content url="{_attr(pin)}" medium="image" type="image/png" '
            f'width="{PIN_W}" height="{PIN_H}" fileSize="{int(m["pin_bytes"])}"/>'
            "</item>"
        )
    title = site["title"]
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<rss version="2.0" xmlns:media="{MEDIA_NS}" xmlns:atom="{ATOM_NS}">'
        "<channel>"
        f"<title>{escape(title)}</title>"
        f"<link>{_attr(base)}/</link>"
        f'<atom:link href="{_attr(base)}/feed.xml" rel="self" type="application/rss+xml"/>'
        f"<description>{escape(site.get('description') or title)}</description>"
        f"<language>{escape(site.get('language') or 'en')}</language>"
        f"<lastBuildDate>{escape(format_datetime(now))}</lastBuildDate>"
        + "".join(items)
        + "</channel></rss>\n"
    )


def _abs_http(url):
    parts = urlparse(url)
    return parts.scheme in ("http", "https") and bool(parts.netloc)


def parse_feed(xml_text):
    import xml.etree.ElementTree as ET
    root = ET.fromstring(xml_text)
    if root.tag != "rss":
        raise ValueError("feed root is not rss")
    if root.get("version") != "2.0":
        raise ValueError("feed is not RSS 2.0")
    channel = root.find("channel")
    if channel is None:
        raise ValueError("feed has no channel")
    items = []
    for item in channel.findall("item"):
        def text(tag):
            node = item.find(tag)
            return (node.text or "").strip() if node is not None else ""
        enc = item.find("enclosure")
        media = item.find(f"{{{MEDIA_NS}}}content")
        items.append({
            "title": text("title"),
            "link": text("link"),
            "description": text("description"),
            "pubDate": text("pubDate"),
            "enclosure_url": enc.get("url") if enc is not None else "",
            "enclosure_type": enc.get("type") if enc is not None else "",
            "enclosure_length": enc.get("length") if enc is not None else "",
            "media_url": media.get("url") if media is not None else "",
            "media_type": media.get("type") if media is not None else "",
        })
    return items


def assert_item_fields(item):
    """Title, link, description, pubDate, and a PNG image on absolute URLs."""
    missing = [k for k in ("title", "link", "description", "pubDate") if not item[k]]
    if missing:
        raise SystemExit(f"feed item missing {', '.join(missing)}: {item['link'] or item['title']}")
    for label, url in (("link", item["link"]), ("enclosure", item["enclosure_url"]), ("media:content", item["media_url"])):
        if not _abs_http(url):
            raise SystemExit(f"feed {label} is not an absolute URL: {url}")
    if item["enclosure_type"] != "image/png" or item["media_type"] != "image/png":
        raise SystemExit(f"feed image type is not image/png: {item['link']}")
    if item["enclosure_url"] != item["media_url"]:
        raise SystemExit(f"enclosure and media:content differ: {item['link']}")


def assert_feed(xml_text, posts):
    """Well-formed RSS, one item per formula page, absolute URLs, matching pin files."""
    items = parse_feed(xml_text)
    if len(items) != len(posts):
        raise SystemExit(f"feed has {len(items)} items, expected {len(posts)} formula pages")
    by_link = {m["abs_url"]: m for m in posts}
    for item in items:
        assert_item_fields(item)
        post = by_link.get(item["link"])
        if post is None or post["pin_url"] != item["enclosure_url"]:
            raise SystemExit(f"feed item does not match a formula page: {item['link']}")
        length = int(item["enclosure_length"] or "0")
        if length != int(post["pin_bytes"]) or length < 1000:
            raise SystemExit(f"feed enclosure length does not match {post['slug']}.png")
    return items
