---
title: How to CONCATENATE Text in Google Sheets
slug: concatenate-google-sheets
date: '2026-10-27'
summary: CONCATENATE (and its modern cousins CONCAT, the & operator, and TEXTJOIN)
  sticks pieces of text into one cell. This page shows the classic CONCATENATE syntax,
  when to prefer & or TEXTJOIN, and how Excel and Google Sheets differ on ranges and
  empty cells.
tags:
- Text formulas
- Google Sheets
keyword: concatenate-google-sheets
niche: sheets-formulas
provider: structured
entry_id: concatenate
platform: Google Sheets
category: text
faq:
- q: Should I use CONCATENATE, CONCAT, & or TEXTJOIN?
  a: Use & for two or three pieces, CONCAT to join a range with no delimiter, and
    TEXTJOIN when you need a delimiter and want to skip blanks. Keep CONCATENATE only
    for older-file compatibility.
- q: Can CONCATENATE join a whole range like A2:A10?
  a: No. Pass each cell separately, or switch to CONCAT (no delimiter) or TEXTJOIN
    (with a delimiter). In Google Sheets you can also use JOIN or an ARRAYFORMULA
    with &.
- q: How do I add a line break between joined pieces?
  a: Use CHAR(10) as the separator, e.g. =A2 & CHAR(10) & B2, and turn on Wrap Text
    for the cell.
related:
- - textjoin-google-sheets
  - textjoin-excel
- - split-text-google-sheets
  - split-text-excel
- - trim-google-sheets
  - trim-excel
- - leading-zeros-google-sheets
  - leading-zeros-excel
sibling: concatenate-excel
---
CONCATENATE (and its modern cousins CONCAT, the & operator, and TEXTJOIN) sticks pieces of text into one cell. This page shows the classic CONCATENATE syntax, when to prefer & or TEXTJOIN, and how Excel and Google Sheets differ on ranges and empty cells.

## Quick answer

Use this formula in Google Sheets:

```excel
=CONCATENATE(A2, " ", B2)
```

Same CONCATENATE syntax in Google Sheets: pass each piece as its own argument.

## The problem

You have first names in one column and last names in another, and you need a full-name column that updates when either part changes — or a label that mixes text with a number and a separator.

## Worked example

Build full names, then a mixed label with a product code.

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **First** | **Last** | **Full name** | **Label** |
| 2 | Ana | Lopez | **Ana Lopez** | **Hello, Ana Lopez!** |
| 3 | Ben | Carter | **Ben Carter** |  |
| 4 | Chloe | Wong | **Chloe Wong** |  |
| 5 | 1042 | RED | **1042-RED** | **1042RED** |

Formulas used in the example (results shown in **bold** in the table above):

**C2 (filled to C4)** — full name, filled down

```excel
=CONCATENATE(A2, " ", B2)
```

Results: **Ana Lopez**, **Ben Carter**, **Chloe Wong**

**C5** — ampersand alternative on the same row

```excel
=A5 & "-" & B5
```

Result: **1042-RED**

**D2** — label with fixed text and a name

```excel
=CONCATENATE("Hello, ", A2, " ", B2, "!")
```

Result: **Hello, Ana Lopez!**

**D5** — CONCAT joins a range with no delimiter

```excel
=CONCAT(A5:B5)
```

Result: **1042RED**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Type `=CONCATENATE(` and click the first cell (A2), then type a comma.
2. Add any literal text in quotes — here `" "` for a space — then another comma and the next cell (B2).
3. Close the parenthesis and press Enter. Fill the formula down the column for the other rows.
4. For two or three pieces, `A2 & " " & B2` is shorter and works in every Excel and Sheets version.
5. When you need a delimiter between many cells and want to skip blanks, switch to TEXTJOIN instead of CONCATENATE.

## Google Sheets-specific notes

Google Sheets also keeps CONCATENATE for compatibility and prefers CONCAT or & for new work. `=CONCAT(A2, B2)` joins two values with no delimiter; for a whole column use `=ARRAYFORMULA(A2:A & " " & B2:B)` so every row fills at once. Sheets also has JOIN (`=JOIN(", ", A2:A7)`), which inserts a delimiter but does not skip blanks — use TEXTJOIN when empty cells would create double commas. Like Excel, CONCATENATE will not accept a multi-cell range as one argument; pass cells one by one or switch to CONCAT / &.

**Ampersand, filled down a column with ARRAYFORMULA**

```excel
=ARRAYFORMULA(IF(A2:A="", "", A2:A & " " & B2:B))
```

**JOIN with a delimiter (keeps blanks)**

```excel
=JOIN(", ", A2:A4)
```

**TEXTJOIN skipping blanks**

```excel
=TEXTJOIN(", ", TRUE, A2:A4)
```


## Excel version

The same formula works unchanged in Excel:

```excel
=CONCATENATE(A2, " ", B2)
```

Excel's CONCATENATE and CONCAT match Google Sheets. Excel has no JOIN function; use TEXTJOIN when you need a delimiter.

<!--SIBLING-->


## Common errors and how to fix them

- **Numbers or dates look wrong in the result** — CONCATENATE uses the raw value (0.5, a serial date), not the cell's display format. **Fix:** Wrap with TEXT, e.g. `CONCATENATE(TEXT(C2,"0%"), " complete")` or `TEXT(D2,"yyyy-mm-dd")`.
- **#VALUE! or a truncated string** — The joined result is longer than 32,767 characters (Excel cell limit). **Fix:** Join fewer pieces, or split the output across several cells.
- **Unexpected commas or double spaces** — An argument was blank, or you added a delimiter by hand next to an empty cell. **Fix:** Use TEXTJOIN with ignore_empty TRUE, or wrap optional pieces in IF so blanks contribute nothing.

## FAQ

### Should I use CONCATENATE, CONCAT, & or TEXTJOIN?

Use & for two or three pieces, CONCAT to join a range with no delimiter, and TEXTJOIN when you need a delimiter and want to skip blanks. Keep CONCATENATE only for older-file compatibility.

### Can CONCATENATE join a whole range like A2:A10?

No. Pass each cell separately, or switch to CONCAT (no delimiter) or TEXTJOIN (with a delimiter). In Google Sheets you can also use JOIN or an ARRAYFORMULA with &.

### How do I add a line break between joined pieces?

Use CHAR(10) as the separator, e.g. `=A2 & CHAR(10) & B2`, and turn on Wrap Text for the cell.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
