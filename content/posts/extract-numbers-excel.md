---
title: How to Extract Numbers from Text in Excel
slug: extract-numbers-excel
date: '2026-10-28'
summary: Pull digits out of mixed cells — order IDs, invoice codes, totals buried
  in phrases — with MID / FIND when the layout is fixed, nested SUBSTITUTE when you
  can strip known labels, or a general digits-only formula in Excel 365 and REGEXREPLACE
  / REGEXEXTRACT in Google Sheets.
tags:
- Text formulas
- Excel
keyword: extract-numbers-excel
niche: sheets-formulas
provider: structured
entry_id: extract_numbers
platform: Excel
category: text
faq:
- q: How do I extract only the first number when a cell has several?
  a: 'Google Sheets: =REGEXEXTRACT(A2, "\d+"). Excel 365: take the first element of
    a digit-group split, or use TEXTBEFORE/TEXTAFTER around the first non-digit run.
    Structure-aware MID/FIND is safest when the layout is fixed.'
- q: How do I keep a decimal point?
  a: 'Sheets: =REGEXEXTRACT(A2, "\d+\.\d+") or =REGEXREPLACE(A2, "[^0-9.]", "") then
    VALUE. Excel: strip currency symbols and thousands separators with SUBSTITUTE,
    then VALUE.'
- q: Can I convert the extracted digits to a real number?
  a: Yes — wrap with VALUE, e.g. =VALUE(B2). Format the cell as Number. Leave it as
    text when leading zeros must be preserved.
related:
- - substitute-excel
  - substitute-google-sheets
- - left-right-mid-excel
  - left-right-mid-google-sheets
- - text-before-character-excel
  - text-before-character-google-sheets
- - replace-excel
  - replace-google-sheets
sibling: extract-numbers-google-sheets
---
Pull digits out of mixed cells — order IDs, invoice codes, totals buried in phrases — with MID / FIND when the layout is fixed, nested SUBSTITUTE when you can strip known labels, or a general digits-only formula in Excel 365 and REGEXREPLACE / REGEXEXTRACT in Google Sheets.

## Quick answer

Use this formula in Excel:

```excel
=MID(A2, FIND("-", A2)+1, FIND("-", A2, FIND("-", A2)+1)-FIND("-", A2)-1)
```

When the number sits between two dashes, FIND locates each dash and MID returns the characters between them — here the `1042` inside `SKU-1042-RED`.

## The problem

Values like "SKU-1042-RED", "Order #1042" or "Total: 35 units" sit in one column, and you need only the numeric part in its own cell for sorting, matching or calculations.

## Worked example

Pull the middle code segment, strip a label, then read a total after a colon.

| | A | B | C |
|---|---|---|---|
| 1 | **Text** | **Extracted** |  |
| 2 | SKU-1042-RED | **1042** | **1042** |
| 3 | Order #1042 | **1042** |  |
| 4 | Inv-12-34 | **1234** |  |
| 5 | Total: 35 units | **35** |  |

Formulas used in the example (results shown in **bold** in the table above):

**B2** — digits between the two dashes

```excel
=MID(A2, FIND("-", A2)+1, FIND("-", A2, FIND("-", A2)+1)-FIND("-", A2)-1)
```

Result: **1042**

**B3** — strip the Order label and hash

```excel
=SUBSTITUTE(SUBSTITUTE(A3, "Order ", ""), "#", "")
```

Result: **1042**

**B4** — strip Inv- and remaining dashes

```excel
=SUBSTITUTE(SUBSTITUTE(A4, "Inv-", ""), "-", "")
```

Result: **1234**

**B5** — number after the colon

```excel
=VALUE(TRIM(MID(A5, FIND(":", A5)+1, 3)))
```

Result: **35**

**C2** — Sheets digits-only via REGEXREPLACE

```excel
=MID(A2, 5, 4)
```

Result: **1042**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Look at the source text and decide whether the number sits in a fixed place, between delimiters, or anywhere in the string.
2. For between-delimiter codes use MID + FIND, e.g. `=MID(A2, FIND("-",A2)+1, FIND("-",A2,FIND("-",A2)+1)-FIND("-",A2)-1)`.
3. For a known label, strip it with SUBSTITUTE, then VALUE if you need a numeric result.
4. In Excel 365, use the TEXTJOIN + SEQUENCE formula on this page to keep every digit regardless of layout.
5. In Google Sheets, prefer `=REGEXREPLACE(A2, "[^0-9]", "")` or `=REGEXEXTRACT(A2, "\d+")`, and wrap with ARRAYFORMULA for a whole column.

## Excel-specific notes

Prefer a structure-aware formula when codes follow a pattern: MID + FIND for between delimiters, RIGHT/LEFT for a fixed-width suffix or prefix, or SUBSTITUTE to strip a known label (`Order #`, `Inv-`). Wrap with VALUE when you need a real number rather than text digits. In Microsoft 365 a general "keep every digit" approach is `=TEXTJOIN("", TRUE, IF(ISNUMBER(--MID(A2, SEQUENCE(LEN(A2)), 1)), MID(A2, SEQUENCE(LEN(A2)), 1), ""))` — it walks each character and joins the ones that are digits. Older Excel can use helper columns or Power Query's "Split / Extract" instead. Flash Fill (Data > Flash Fill) also works for one-off extractions when the pattern is consistent.

**Strip a known label with SUBSTITUTE**

```excel
=SUBSTITUTE(SUBSTITUTE(A2, "Order ", ""), "#", "")
```

**Excel 365 — keep every digit**

```excel
=TEXTJOIN("", TRUE, IF(ISNUMBER(--MID(A2, SEQUENCE(LEN(A2)), 1)), MID(A2, SEQUENCE(LEN(A2)), 1), ""))
```

**Number after a colon**

```excel
=VALUE(TRIM(MID(A2, FIND(":", A2)+1, 3)))
```


## Google Sheets version

In Google Sheets, use:

```excel
=REGEXREPLACE(A2, "[^0-9]", "")
```

Sheets prefers REGEXREPLACE / REGEXEXTRACT for general digit extraction; Excel uses MID/FIND/SUBSTITUTE or an Excel 365 TEXTJOIN+SEQUENCE formula for the same result.

<!--SIBLING-->


## Common errors and how to fix them

- **#VALUE!** — FIND did not find the delimiter, or VALUE received a non-numeric string (letters still present). **Fix:** Wrap FIND with IFERROR, or clean remaining letters with SUBSTITUTE / REGEXREPLACE before VALUE.
- **Wrong digits or missing leading zeros** — VALUE dropped leading zeros, or several digit groups were concatenated when you only wanted the first. **Fix:** Keep the result as text (`="" & …`) when zeros matter. In Sheets use REGEXEXTRACT for the first group only.
- **#NAME? in older Excel** — TEXTJOIN / SEQUENCE need Microsoft 365 or Excel 2021+. **Fix:** Use the MID/FIND or SUBSTITUTE patterns on this page, or extract with Power Query / Flash Fill.

## FAQ

### How do I extract only the first number when a cell has several?

Google Sheets: `=REGEXEXTRACT(A2, "\d+")`. Excel 365: take the first element of a digit-group split, or use TEXTBEFORE/TEXTAFTER around the first non-digit run. Structure-aware MID/FIND is safest when the layout is fixed.

### How do I keep a decimal point?

Sheets: `=REGEXEXTRACT(A2, "\d+\.\d+")` or `=REGEXREPLACE(A2, "[^0-9.]", "")` then VALUE. Excel: strip currency symbols and thousands separators with SUBSTITUTE, then VALUE.

### Can I convert the extracted digits to a real number?

Yes — wrap with VALUE, e.g. `=VALUE(B2)`. Format the cell as Number. Leave it as text when leading zeros must be preserved.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
