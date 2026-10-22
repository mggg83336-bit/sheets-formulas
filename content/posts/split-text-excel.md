---
title: How to Split Text into Columns with a Formula in Excel
slug: split-text-excel
date: '2026-10-22'
summary: Split "Name, Department, City" into separate cells with TEXTSPLIT in Excel
  365 or SPLIT in Google Sheets. A classic formula for older Excel is included, along
  with the SPLIT quirk that splits on every character of the delimiter.
tags:
- Text formulas
- Excel
keyword: split-text-excel
niche: sheets-formulas
provider: structured
entry_id: split-text
platform: Excel
category: text
faq:
- q: How do I split into rows instead of columns?
  a: In Excel 365 use the row delimiter, =TEXTSPLIT(A2, , ","). In Google Sheets use
    =TRANSPOSE(SPLIT(A2, ",")).
- q: How do I get only the second part?
  a: Excel 365, =INDEX(TEXTSPLIT(A2, ","), 2); Google Sheets, =INDEX(SPLIT(A2, ","),
    2).
related:
- - text-before-character-excel
  - text-before-character-google-sheets
- - text-after-character-excel
  - text-after-character-google-sheets
- - textjoin-excel
  - textjoin-google-sheets
- - trim-excel
  - trim-google-sheets
sibling: split-text-google-sheets
---
Split "Name, Department, City" into separate cells with TEXTSPLIT in Excel 365 or SPLIT in Google Sheets. A classic formula for older Excel is included, along with the SPLIT quirk that splits on every character of the delimiter.

## Quick answer

Use this formula in Excel:

```excel
=TEXTSPLIT(A2, ",")
```

Syntax: `TEXTSPLIT(text, col_delimiter, [row_delimiter], [ignore_empty], [match_mode], [pad_with])`. Split A2 at each comma; the parts spill to the right.

## The problem

Each row has one cell containing several values separated by commas, for example from a form export. You want each value in its own column, and you want it to update when the source changes, which Text to Columns does not do.

## Worked example

Each cell in column A holds name, department and city.

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **Record** | **Name** | **Department** | **City** |
| 2 | Ana Lopez,Sales,Madrid | **Ana Lopez** | **Sales** | **Madrid** |
| 3 | Ben Carter,IT,Boston | **Ben Carter** | **IT** | **Boston** |
| 4 | Chloe Wong,Finance,Singapore | **Chloe Wong** | **Finance** | **Singapore** |

Formulas used in the example (results shown in **bold** in the table above):

**B2** — spills into B2:D2

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

1. TEXTSPLIT / SPLIT find every comma and return the pieces between them as separate cells.
2. The results spill into the cells to the right, so leave enough empty columns.
3. The classic formula replaces each comma with 100 spaces, which pushes every part into its own 100-character block.
4. `MID(..., (n-1)*100+1, 100)` cuts out block n, where n comes from COLUMN(A1)=1, COLUMN(B1)=2, and so on as you copy right.
5. TRIM removes the padding spaces, leaving just the value. It works as long as each part is shorter than 100 characters.

## Excel-specific notes

TEXTSPLIT is available in Microsoft 365, Excel 2024 and Excel for the web. If your data has a space after each comma, split on ", " (comma and space) or wrap the result in TRIM. For several possible delimiters pass an array: `TEXTSPLIT(A2, {",",";"})`. In Excel 2021 and older use the SUBSTITUTE/REPT formula below; copy it across as many columns as you need parts. For a one-off split, Data > Text to Columns is faster but does not update.

**Any Excel version (copy across; n-th part from the column number)**

```excel
=TRIM(MID(SUBSTITUTE($A2, ",", REPT(" ", 100)), (COLUMN(A1)-1)*100+1, 100))
```


## Google Sheets version

In Google Sheets, use:

```excel
=SPLIT(A2, ",")
```

By default SPLIT splits on each character of the delimiter, so pass FALSE as the third argument to split on a multi-character string.

<!--SIBLING-->


## Common errors and how to fix them

- **Names split in two (Google Sheets)** — SPLIT with a delimiter like ", " splits on each character, including the space. **Fix:** Add FALSE as the third argument.
- **#SPILL! / #REF!** — The cells to the right are not empty. **Fix:** Clear them before entering the formula.
- **Leading spaces in the parts** — The data uses ", " but you split on ",". **Fix:** Split on ", " (with FALSE in Sheets) or wrap the result in TRIM.

## FAQ

### How do I split into rows instead of columns?

In Excel 365 use the row delimiter, =TEXTSPLIT(A2, , ","). In Google Sheets use =TRANSPOSE(SPLIT(A2, ",")).

### How do I get only the second part?

Excel 365, =INDEX(TEXTSPLIT(A2, ","), 2); Google Sheets, =INDEX(SPLIT(A2, ","), 2).

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
