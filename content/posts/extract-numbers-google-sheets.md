---
title: How to Extract Numbers from Text in Google Sheets
slug: extract-numbers-google-sheets
date: '2026-10-28'
summary: Pull digits out of mixed cells — order IDs, invoice codes, totals buried
  in phrases — with MID / FIND when the layout is fixed, nested SUBSTITUTE when you
  can strip known labels, or a general digits-only formula in Excel 365 and REGEXREPLACE
  / REGEXEXTRACT in Google Sheets.
tags:
- Text formulas
- Google Sheets
keyword: extract-numbers-google-sheets
niche: sheets-formulas
provider: structured
entry_id: extract_numbers
platform: Google Sheets
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
- - substitute-google-sheets
  - substitute-excel
- - left-right-mid-google-sheets
  - left-right-mid-excel
- - text-before-character-google-sheets
  - text-before-character-excel
- - replace-google-sheets
  - replace-excel
sibling: extract-numbers-excel
---
Pull digits out of mixed cells — order IDs, invoice codes, totals buried in phrases — with MID / FIND when the layout is fixed, nested SUBSTITUTE when you can strip known labels, or a general digits-only formula in Excel 365 and REGEXREPLACE / REGEXEXTRACT in Google Sheets.

## Quick answer

Use this formula in Google Sheets:

```excel
=REGEXREPLACE(A2, "[^0-9]", "")
```

REGEXREPLACE removes every character that is not a digit, leaving the number as text — e.g. `SKU-1042-RED` becomes `1042`.

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
=REGEXREPLACE(A2, "[^0-9]", "")
```

Result: **1042**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Look at the source text and decide whether the number sits in a fixed place, between delimiters, or anywhere in the string.
2. For between-delimiter codes use MID + FIND, e.g. `=MID(A2, FIND("-",A2)+1, FIND("-",A2,FIND("-",A2)+1)-FIND("-",A2)-1)`.
3. For a known label, strip it with SUBSTITUTE, then VALUE if you need a numeric result.
4. In Excel 365, use the TEXTJOIN + SEQUENCE formula on this page to keep every digit regardless of layout.
5. In Google Sheets, prefer `=REGEXREPLACE(A2, "[^0-9]", "")` or `=REGEXEXTRACT(A2, "\d+")`, and wrap with ARRAYFORMULA for a whole column.

## Google Sheets-specific notes

Google Sheets has no SEQUENCE-based digit walk like Excel 365; REGEXREPLACE and REGEXEXTRACT are the native tools. `=REGEXREPLACE(A2, "[^0-9]", "")` keeps every digit (and concatenates them if several groups exist). `=REGEXEXTRACT(A2, "\d+")` returns only the first run of digits. To keep a decimal point use `[^0-9.]` carefully, or extract with `=REGEXEXTRACT(A2, "\d+\.\d+")`. VALUE(...) turns the digit string into a number. MID, FIND and SUBSTITUTE work exactly as in Excel when the layout is fixed, and ARRAYFORMULA applies any of these across a column: `=ARRAYFORMULA(IF(A2:A="", "", REGEXREPLACE(A2:A, "[^0-9]", "")))`.

**First digit group only**

```excel
=REGEXEXTRACT(A2, "\d+")
```

**Whole column of digits-only values**

```excel
=ARRAYFORMULA(IF(A2:A="", "", REGEXREPLACE(A2:A, "[^0-9]", "")))
```

**Number between dashes (same as Excel)**

```excel
=MID(A2, FIND("-", A2)+1, FIND("-", A2, FIND("-", A2)+1)-FIND("-", A2)-1)
```


## Excel version

In Excel, use:

```excel
=MID(A2, FIND("-", A2)+1, FIND("-", A2, FIND("-", A2)+1)-FIND("-", A2)-1)
```

Excel leans on MID/FIND/SUBSTITUTE or Excel 365 dynamic arrays. Google Sheets usually solves the same job with one REGEXEXTRACT or REGEXREPLACE call.

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
