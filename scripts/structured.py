"""Structured page pipeline (data -> Markdown) for niches that set `pages_dir`.

Content source: niches/<niche>/<pages_dir>/*.yaml, a list of entries. One entry = one
formula topic, written once, rendered per platform (Excel / Google Sheets). Each entry
maps to one or two URL slugs (`slugs: {excel: ..., sheets: ...}`).

No LLM, no network: pages are rendered from hand-checked data with Jinja-free string
building so the output is deterministic. A quality gate refuses to render thin entries.
"""
import re
from pathlib import Path

import yaml

PLATFORMS = {"excel": "Excel", "sheets": "Google Sheets"}
CATEGORY_LABELS = {
    "lookup": "Lookup & reference",
    "conditional": "Conditional sums & counts",
    "logic": "Logic & error handling",
    "errors": "Fixing formula errors",
    "text": "Text formulas",
    "date": "Dates & times",
    "financial": "Financial & percentages",
    "other": "Formula basics & tips",
}
RELATED_PLACEHOLDER = "<!--RELATED-->"
SIBLING_PLACEHOLDER = "<!--SIBLING-->"

DEFAULT_GATE = {
    "min_words": 450,          # rendered page body, excluding code
    "min_steps": 3,
    "min_errors": 2,
    "min_faq": 2,
    "min_example_rows": 3,     # data rows (excluding header)
    "variant_min_notes_words": 45,  # secondary-platform page needs its own notes
}


# ---------------------------------------------------------------- loading
def load_entries(niche):
    d = niche["_dir"] / niche["pages_dir"]
    entries = []
    for f in sorted(d.glob("*.yaml")):
        data = yaml.safe_load(f.read_text(encoding="utf-8")) or []
        for e in data:
            e["_file"] = f.name
            entries.append(e)
    ids = [e["id"] for e in entries]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        raise ValueError(f"duplicate entry ids: {sorted(dup)}")
    return entries


def slug_map(entries):
    """slug -> (entry, platform_key)"""
    m = {}
    for e in entries:
        for p, s in (e.get("slugs") or {}).items():
            if s in m:
                raise ValueError(f"slug {s} used twice ({m[s][0]['id']}, {e['id']})")
            m[s] = (e, p)
    return m


def primary_platform(e):
    return e.get("primary") or ("excel" if "excel" in e.get("slugs", {}) else "sheets")


# ---------------------------------------------------------------- helpers
def col_letter(i):
    s = ""
    i += 1
    while i:
        i, r = divmod(i - 1, 26)
        s = chr(65 + r) + s
    return s


def cell_rc(ref):
    m = re.fullmatch(r"([A-Z]+)(\d+)", ref)
    col = 0
    for ch in m.group(1):
        col = col * 26 + ord(ch) - 64
    return int(m.group(2)) - 1, col - 1


def fmt_cell(v):
    if v is None:
        return ""
    if hasattr(v, "isoformat"):
        return v.isoformat()
    if isinstance(v, bool):
        return "TRUE" if v else "FALSE"
    v = str(v)
    if v != v.strip() or "  " in v:   # make significant spaces visible
        return "`\"" + v.replace("|", "\\|") + "\"`"
    return v.replace("|", "\\|")


def fmt_result(v):
    s = fmt_cell(v)
    return "*(blank)*" if s == "" else f"**{s}**"


def words(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    return len(re.findall(r"[A-Za-z][A-Za-z'’-]*", text))


def platform_block(e, p):
    b = e.get(p) or {}
    if not b.get("formula"):
        other = "sheets" if p == "excel" else "excel"
        if b.get("same_as") == other or (not b and e.get(other)):
            b = {**(e.get(other) or {}), **{k: v for k, v in b.items() if k != "same_as"}}
    return b


def check_formula(c, p):
    return c.get(p) or (c.get("excel") if p == "sheets" else c.get("sheets")) or c.get("formula")


# ---------------------------------------------------------------- quality gate
def gate(e, p, cfg=None, body=None):
    """Return list of problems; empty list = OK to publish."""
    g = {**DEFAULT_GATE, **(cfg or {})}
    probs = []
    if p not in (e.get("slugs") or {}):
        return [f"no slug for platform {p}"]
    b = e.get(p) or {}
    if not platform_block(e, p).get("formula"):
        probs.append(f"no {p} formula")
    for k in ("title", "summary", "problem"):
        if not e.get(k):
            probs.append(f"missing {k}")
    ex = e.get("example") or {}
    if len(ex.get("grid") or []) - 1 < g["min_example_rows"]:
        probs.append("example table too small")
    if not ex.get("checks"):
        probs.append("example has no formula results")
    if len(e.get("steps") or []) < g["min_steps"]:
        probs.append("too few explanation steps")
    if len(e.get("errors") or []) < g["min_errors"]:
        probs.append("too few common errors")
    if len(e.get("faq") or []) < g["min_faq"]:
        probs.append("too few FAQ items")
    if p != primary_platform(e):
        pb = platform_block(e, primary_platform(e))
        differs = (b.get("formula") or "").strip() != (pb.get("formula") or "").strip() or b.get("alternatives")
        if words(b.get("notes", "")) < g["variant_min_notes_words"] or not differs:
            probs.append(f"{p} page would duplicate the {primary_platform(e)} page "
                         "(needs its own notes plus a different formula or platform-specific alternatives)")
    if body is not None and words(body) < g["min_words"]:
        probs.append(f"too thin: {words(body)} words < {g['min_words']}")
    return probs


# ---------------------------------------------------------------- rendering
def render_grid(e, p):
    ex = e["example"]
    grid = [list(r) for r in ex["grid"]]
    width = max(len(r) for r in grid)
    results = {}
    for c in ex.get("checks", []):
        cells = c.get("spill_cells") or c.get("fill") or [c["cell"]]
        vals = c.get("spill_results") or c.get("results") or [c.get("result")]
        for ref, v in zip(cells, vals):
            results[ref] = v
    for ref in results:
        r, cidx = cell_rc(ref)
        while len(grid) <= r:
            grid.append([])
        width = max(width, cidx + 1)
    lines = ["| | " + " | ".join(col_letter(i) for i in range(width)) + " |",
             "|---|" + "---|" * width]
    for ri, row in enumerate(grid):
        cells = []
        for ci in range(width):
            ref = f"{col_letter(ci)}{ri + 1}"
            if ref in results:
                cells.append(f"**{fmt_cell(results[ref])}**")
            else:
                v = row[ci] if ci < len(row) else None
                cells.append(f"**{fmt_cell(v)}**" if ri == 0 and v not in (None, "") else fmt_cell(v))
        lines.append(f"| {ri + 1} | " + " | ".join(cells) + " |")
    out = "\n".join(lines)
    for name, og in (ex.get("other_sheets") or {}).items():
        w = max(len(r) for r in og)
        out += f"\n\nSheet **{name}**:\n\n| | " + " | ".join(col_letter(i) for i in range(w)) + " |\n|---|" + "---|" * w
        for ri, row in enumerate(og):
            out += f"\n| {ri + 1} | " + " | ".join(fmt_cell(row[i] if i < len(row) else None) for i in range(w)) + " |"
    return out


def code(f):
    return f"```excel\n{f.strip()}\n```"


def page_title(e, p):
    t = e.get("titles", {}).get(p) or e["title"]
    return t if PLATFORMS[p].lower() in t.lower() else f"{t} in {PLATFORMS[p]}"


def render(e, p):
    """Render one entry for platform p. Returns dict(title, summary, tags, body_md, faq, related)."""
    P, other = PLATFORMS[p], ("sheets" if p == "excel" else "excel")
    O = PLATFORMS[other]
    b = platform_block(e, p)
    ob = platform_block(e, other) if other in (e.get("slugs") or {}) or e.get(other) else {}
    ex = e["example"]
    parts = [e["summary"].strip(), "", "## Quick answer", "",
             f"Use this formula in {P}:", "", code(b["formula"])]
    if b.get("explain"):
        parts += ["", b["explain"].strip()]
    parts += ["", "## The problem", "", e["problem"].strip(), "", "## Worked example", ""]
    if ex.get("intro"):
        parts += [ex["intro"].strip(), ""]
    parts += [render_grid(e, p), "", "Formulas used in the example (results shown in **bold** in the table above):", ""]
    for c in ex["checks"]:
        where = f"{c['cell']}" + (f" (filled to {c['fill'][-1]})" if c.get("fill") else "")
        label = f"**{where}**" + (f" — {c['label']}" if c.get("label") else "")
        vals = c.get("spill_results") or c.get("results") or [c.get("result")]
        res = ", ".join(fmt_result(v) for v in vals)
        word = "Results" if len(vals) > 1 else "Result"
        parts += [label, "", code(check_formula(c, p)), "", f"{word}: {res}", ""]
    if ex.get("note"):
        parts += [ex["note"].strip(), ""]
    parts += ["<!--AD_IN_ARTICLE-->", "", "## How the formula works", ""]
    parts += [f"{i}. {s.strip()}" for i, s in enumerate(e["steps"], 1)]
    if b.get("notes") or b.get("alternatives"):
        parts += ["", f"## {P}-specific notes", ""]
        if b.get("notes"):
            parts += [b["notes"].strip(), ""]
        for a in b.get("alternatives") or []:
            parts += [f"**{a['label']}**", "", code(a["formula"]), ""]
            if a.get("note"):
                parts += [a["note"].strip(), ""]
    if ob.get("formula"):
        parts += ["", f"## {O} version", ""]
        same = ob["formula"].strip() == b["formula"].strip()
        parts += [f"The same formula works unchanged in {O}:" if same else f"In {O}, use:", "", code(ob["formula"]), ""]
        if ob.get("diff"):
            parts += [ob["diff"].strip(), ""]
        parts += [SIBLING_PLACEHOLDER, ""]
    parts += ["", "## Common errors and how to fix them", ""]
    for er in e["errors"]:
        parts += [f"- **{er['error']}** — {er['cause'].strip()} **Fix:** {er['fix'].strip()}"]
    parts += ["", "## FAQ", ""]
    for q in e["faq"]:
        parts += [f"### {q['q'].strip()}", "", q["a"].strip(), ""]
    parts += ["## Related formulas", "", RELATED_PLACEHOLDER, "", "<!--PRODUCT_BOX-->"]
    body = "\n".join(parts)
    return {
        "title": page_title(e, p),
        "summary": (e.get("meta_description") or e["summary"]).strip().split("\n")[0][:300],
        "tags": [CATEGORY_LABELS.get(e.get("category", "other"), CATEGORY_LABELS["other"]), P],
        "body_md": body,
        "faq": [{"q": q["q"].strip(), "a": re.sub(r"`([^`]*)`", r"\1", q["a"].strip())} for q in e["faq"]],
    }


def related_slugs(e, p, entries_by_id):
    """Candidate related slugs (same platform first); build.py links only the published ones."""
    out = []
    for rid in e.get("related") or []:
        r = entries_by_id.get(rid)
        if not r:
            continue
        s = r.get("slugs", {})
        cands = [s[k] for k in (p, "excel" if p == "sheets" else "sheets") if k in s]
        if cands:
            out.append(cands)
    return out


def sibling_slug(e, p):
    other = "sheets" if p == "excel" else "excel"
    return (e.get("slugs") or {}).get(other)
