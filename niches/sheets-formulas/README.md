# niches/sheets-formulas: data schema and queue

```
niche.yaml          # pages_dir, queue_file, quality_gate
pages/*.yaml        # hand-written formula entries (one YAML list per category file)
pages/auto-*.yaml   # (optional) LLM drafts that passed the gate + LibreOffice recalc
keywords_300.csv    # original keyword list (keyword, platform, slug)
launch_extra.csv    # extra slugs for launch entries not in the 300 list
queue.csv           # the keyword queue (append-only): keyword, platform, slug, category, source, added
rejected.csv        # (auto) keywords whose LLM draft failed; retried after 30 days
```

## Entry schema (pages/*.yaml)

Each entry is one formula topic, and it can be rendered for **two platforms**: Excel and Google Sheets.
Each platform version gets its own URL, taken from `slugs`.

| field | required | meaning |
|---|---|---|
| `id` | yes | stable key, used in `related` |
| `category` | yes | lookup / conditional / logic / errors / text / date / financial / other |
| `launch` | – | `true` = the primary slug is published on the first run |
| `primary` | – | `excel` (default) or `sheets`: the platform published at launch |
| `slugs` | yes | `{excel: …, sheets: …}`. These are the URLs and must match `queue.csv` |
| `title` / `titles` | yes | base title (the platform is appended), or `{excel: …, sheets: …}` overrides |
| `summary`, `problem` | yes | intro paragraphs |
| `excel`, `sheets` | yes | platform block: `formula`, `explain`, `notes`, `alternatives` [{label, formula}], `diff` (how the *other* platform differs). `same_as: excel` copies a block |
| `example.grid` | yes | rows of cells (first row = headers; `null` = empty). Rendered like a spreadsheet with row/column labels |
| `example.checks` | yes | `{cell, label, excel, sheets?, result | results, fill?, array?, spill_cells?, spill_results?, expect?, verify?, sheets_verify?, why_unverified?}` (`sheets_verify: false` skips only the Sheets variant, e.g. Sheets-only argument syntax). These are the formulas typed into the grid and their exact results |
| `example.other_sheets` | – | extra sheets the formulas reference (e.g. `Prices!A:B`) |
| `steps` | ≥3 | step-by-step explanation |
| `errors` | ≥2 | `{error, cause, fix}` |
| `faq` | ≥2 | `{q, a}`. Rendered as FAQ and as FAQPage JSON-LD. In-body links may use `../{entry-id}/`, resolved to the same platform at publish time |
| `related` | – | entry ids. Links are resolved at build time (only to published pages, same platform first) |
| `sections` | – | extra H2s: `{after: quick\|errors, title, body}` or platform text under `excel` / `sheets` instead of `body` |
| `cta` | – | `hub` places the two-button buy block under Quick answer and again after Common errors |

## Quality gate (niche.yaml → quality_gate)

A page is published only if:
- its rendered prose has at least 450 words (code is not counted);
- it has at least 3 steps, 2 errors, 2 FAQs and 3 example rows;
- every formula passes the lint (balanced parentheses and quotes).

The **second-platform variant** (e.g. `…-google-sheets` when Excel is primary) must also have at least 45 words of its own platform notes. It also needs a different formula or platform-specific alternatives. Otherwise it would duplicate the primary page, so it is reported as *blocked* and never published.

## Verifying examples

```bash
.venv/bin/python scripts/verify_formulas.py      # needs LibreOffice (soffice) on PATH
```

The script:
- writes every example grid to an .xlsx;
- puts in the `excel` formulas, filling them down, spilling them, or entering them as arrays;
- recalculates the workbook with LibreOffice;
- compares the results with `result`/`results`. Use `expect` when the printed value is rounded.

Functions that LibreOffice lacks (CHOOSEROWS, TEXTSPLIT, TEXTBEFORE/AFTER, HSTACK, TAKE…) are listed as "not machine-verified". So are Sheets-only functions and checks with `verify: false`.

## The keyword queue

```bash
.venv/bin/python scripts/kwqueue.py ingest my_keywords.txt   # one keyword per line, '#' = comment
.venv/bin/python scripts/kwqueue.py ingest more.csv          # CSV with a 'keyword' column (+ optional platform, slug, category)
.venv/bin/python scripts/kwqueue.py status [-v]              # published / ready / blocked / needs-content per category
```

- Ingest infers the platform from the keyword text (sheets/google means Sheets, otherwise Excel). It builds a slug if none is given and assigns a category by regex rules. Duplicates are skipped by slug and by normalised keyword.
- `generate.py` walks the queue in order. It publishes up to `generate_per_run` keywords per run (site.yaml, currently 6) whose slug matches an entry that passes the gate. Every keyword without content is **skipped, not stubbed**.
- With `--provider llm` (or the `LLM_API_URL` secret in CI), a keyword that needs content gets an LLM draft. The draft is published only if it passes the gate **and** LibreOffice recalculation. Failures are logged in `rejected.csv` and retried after 30 days.
- To publish a needs-content keyword by hand, write an entry whose `slugs` contain that keyword's slug. The next daily run picks it up.
