---
title: How to Use the TEXTSPLIT Function in Excel
slug: textsplit-excel
date: '2026-10-27'
summary: TEXTSPLIT is Excel 365 / 2024's formula for splitting one cell into many
  columns or rows. This page covers the full argument list (column and row delimiters,
  ignore_empty, pad_with), a classic formula for older Excel, and the Google Sheets
  SPLIT equivalent with its split-by-each quirk.
tags:
- Text formulas
- Excel
keyword: textsplit-excel
niche: sheets-formulas
provider: structured
entry_id: textsplit
platform: Excel
category: text
faq:
- q: How is TEXTSPLIT different from Text to Columns?
  a: 'TEXTSPLIT is a live formula: when the source cell changes, the split updates.
    Text to Columns pastes static values once.'
- q: How do I get only the second part?
  a: 'Excel 365: =INDEX(TEXTSPLIT(A2, ","), 2). Google Sheets: =INDEX(SPLIT(A2, ","),
    2). Older Excel: put the classic formula in column C (the second copy-across cell).'
- q: Can TEXTSPLIT split on more than one delimiter?
  a: Yes — pass an array constant as the column delimiter, e.g. =TEXTSPLIT(A2, {",",";","|"}).
related:
- - split-text-excel
  - split-text-google-sheets
- - text-before-character-excel
  - text-before-character-google-sheets
- - text-after-character-excel
  - text-after-character-google-sheets
- - textjoin-excel
  - textjoin-google-sheets
sibling: null
---
TEXTSPLIT is Excel 365 / 2024's formula for splitting one cell into many columns or rows. This page covers the full argument list (column and row delimiters, ignore_empty, pad_with), a classic formula for older Excel, and the Google Sheets SPLIT equivalent with its split-by-each quirk.

## Quick answer

Use this formula in Excel:

```excel
=TEXTSPLIT(A2, ",")
```

Syntax: `TEXTSPLIT(text, col_delimiter, [row_delimiter], [ignore_empty], [match_mode], [pad_with])`. Split A2 at each comma; the parts spill across the row.

## The problem

A column holds values like "Ana Lopez,Sales,Madrid" or multi-line blocks, and you want each piece in its own cell — updating automatically when the source changes, which Data > Text to Columns does not do.

## Worked example

Split comma-separated records; also show the classic formula that works in every Excel.

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **Record** | **Name** | **Department** | **City** |
| 2 | Ana Lopez,Sales,Madrid | **Ana Lopez** | **Sales** | **Madrid** |
| 3 | Ben Carter,IT,Boston | **Ben Carter** | **IT** | **Boston** |
| 4 | Chloe Wong,Finance,Singapore | **Chloe Wong** | **Finance** | **Singapore** |

Formulas used in the example (results shown in **bold** in the table above):

**B2** — TEXTSPLIT spills into B2:D2

```excel
=TEXTSPLIT(A2, ",")
```

Results: **Ana Lopez**, **Sales**, **Madrid**

**B3 (filled to D3)** — classic formula, filled across to D3

```excel
=TRIM(MID(SUBSTITUTE($A3, ",", REPT(" ", 100)), (COLUMN(A1)-1)*100+1, 100))
```

Results: **Ben Carter**, **IT**, **Boston**

**B4 (filled to D4)** — classic formula, filled across to D4

```excel
=TRIM(MID(SUBSTITUTE($A4, ",", REPT(" ", 100)), (COLUMN(A2)-1)*100+1, 100))
```

Results: **Chloe Wong**, **Finance**, **Singapore**

<!--AD_IN_ARTICLE-->

## How the formula works

1. In Excel 365 type `=TEXTSPLIT(A2, ",")` and press Enter; the parts spill into the cells to the right.
2. Leave enough empty columns (or rows, if you use a row delimiter) so the spill is not blocked.
3. Optional arguments: set ignore_empty to TRUE to drop blank pieces, or pass CHAR(10) as the row delimiter for line breaks.
4. In older Excel, enter the SUBSTITUTE/REPT formula in B3 and copy it across as many columns as you have parts.
5. In Google Sheets use `=SPLIT(A2, ",")`, and add FALSE as the third argument when the delimiter is more than one character.

## Excel-specific notes

TEXTSPLIT needs Microsoft 365, Excel 2024 or Excel for the web. Pass a row delimiter as the third argument to spill down instead of (or as well as) across — e.g. `TEXTSPLIT(A2, , CHAR(10))` for line breaks. `ignore_empty` TRUE drops blank pieces from double commas. `match_mode` 1 makes the delimiter case-insensitive. `pad_with` fills missing pieces when you split into a 2D grid so every row has the same width. For several delimiters at once use an array: `TEXTSPLIT(A2, {",",";","|"})`. In Excel 2021 and older, use the SUBSTITUTE/REPT formula below, or Data > Text to Columns for a one-off split.

**Any Excel version (copy across; n-th part from the column number)**

```excel
=TRIM(MID(SUBSTITUTE($A2, ",", REPT(" ", 100)), (COLUMN(A1)-1)*100+1, 100))
```

**Split into rows on commas**

```excel
=TEXTSPLIT(A2, , ",")
```


## Google Sheets version

In Google Sheets, use:

```excel
=SPLIT(A2, ",")
```

Sheets uses SPLIT, not TEXTSPLIT. Pass FALSE as the third argument for multi-character delimiters, and use TRANSPOSE when you want rows instead of columns.

<!--SIBLING-->


## Common errors and how to fix them

- **#NAME?** — TEXTSPLIT is not available in Excel 2021 or older. **Fix:** Use the SUBSTITUTE/REPT formula on this page, upgrade to Microsoft 365 / Excel 2024, or use Data > Text to Columns for a static split.
- **#SPILL!** — A non-empty cell sits inside the spill range. **Fix:** Clear the cells to the right (or below) of the formula, then press Enter again.
- **Names split on spaces (Google Sheets)** — SPLIT with a delimiter like ", " treats every character as a delimiter by default. **Fix:** Pass FALSE as the third argument: `=SPLIT(A2, ", ", FALSE)`.

## FAQ

### How is TEXTSPLIT different from Text to Columns?

TEXTSPLIT is a live formula: when the source cell changes, the split updates. Text to Columns pastes static values once.

### How do I get only the second part?

Excel 365: `=INDEX(TEXTSPLIT(A2, ","), 2)`. Google Sheets: `=INDEX(SPLIT(A2, ","), 2)`. Older Excel: put the classic formula in column C (the second copy-across cell).

### Can TEXTSPLIT split on more than one delimiter?

Yes — pass an array constant as the column delimiter, e.g. `=TEXTSPLIT(A2, {",",";","|"})`.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
