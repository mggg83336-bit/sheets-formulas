---
title: How to Split Text into Columns with a Formula in Google Sheets
slug: split-text-google-sheets
date: '2026-10-26'
summary: Split "Name, Department, City" into separate cells with TEXTSPLIT in Excel
  365 or SPLIT in Google Sheets. A classic formula for older Excel is included, along
  with the SPLIT quirk that splits on every character of the delimiter.
tags:
- Text formulas
- Google Sheets
keyword: split-text-google-sheets
niche: sheets-formulas
provider: structured
entry_id: split-text
platform: Google Sheets
category: text
faq:
- q: How do I split into rows instead of columns?
  a: In Excel 365 use the row delimiter, =TEXTSPLIT(A2, , ","). In Google Sheets use
    =TRANSPOSE(SPLIT(A2, ",")).
- q: How do I get only the second part?
  a: Excel 365, =INDEX(TEXTSPLIT(A2, ","), 2); Google Sheets, =INDEX(SPLIT(A2, ","),
    2).
related:
- - text-before-character-google-sheets
  - text-before-character-excel
- - text-after-character-google-sheets
  - text-after-character-excel
- - textjoin-google-sheets
  - textjoin-excel
- - trim-google-sheets
  - trim-excel
sibling: split-text-excel
---
Split "Name, Department, City" into separate cells with TEXTSPLIT in Excel 365 or SPLIT in Google Sheets. A classic formula for older Excel is included, along with the SPLIT quirk that splits on every character of the delimiter.

## Quick answer

Use this formula in Google Sheets:

```excel
=SPLIT(A2, ",")
```

Syntax: `SPLIT(text, delimiter, [split_by_each], [remove_empty_text])`. The parts spill to the right.

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
=SPLIT(A2, ",")
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

## Google Sheets-specific notes

Watch the third argument: by default SPLIT treats every character in the delimiter as a separate delimiter. `=SPLIT(A2, ", ")` therefore splits on commas AND spaces, breaking "Ana Lopez" into two cells. Use `=SPLIT(A2, ", ", FALSE)` to split on the exact text ", ". SPLIT also removes empty parts by default (the fourth argument). It turns numeric-looking parts into numbers, so a ZIP code like 02134 loses its leading zero; format the output column as plain text first if that matters.

**Split on the exact text ", " (not on each character)**

```excel
=SPLIT(A2, ", ", FALSE)
```

**Split a whole column at once**

```excel
=ARRAYFORMULA(IF(A2:A="", "", SPLIT(A2:A, ",")))
```


## Excel version

In Excel, use:

```excel
=TEXTSPLIT(A2, ",")
```

TEXTSPLIT (Excel 365 / 2024) treats the delimiter as a whole string; older Excel needs the SUBSTITUTE/REPT formula.

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
