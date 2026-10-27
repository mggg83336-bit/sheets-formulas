---
title: How to CONCATENATE Text in Excel
slug: concatenate-excel
date: '2026-10-27'
summary: CONCATENATE (and its modern cousins CONCAT, the & operator, and TEXTJOIN)
  sticks pieces of text into one cell. This page shows the classic CONCATENATE syntax,
  when to prefer & or TEXTJOIN, and how Excel and Google Sheets differ on ranges and
  empty cells.
tags:
- Text formulas
- Excel
keyword: concatenate-excel
niche: sheets-formulas
provider: structured
entry_id: concatenate
platform: Excel
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
- - textjoin-excel
  - textjoin-google-sheets
- - split-text-excel
  - split-text-google-sheets
- - trim-excel
  - trim-google-sheets
- - leading-zeros-excel
  - leading-zeros-google-sheets
sibling: concatenate-google-sheets
---
CONCATENATE (and its modern cousins CONCAT, the & operator, and TEXTJOIN) sticks pieces of text into one cell. This page shows the classic CONCATENATE syntax, when to prefer & or TEXTJOIN, and how Excel and Google Sheets differ on ranges and empty cells.

## Quick answer

Use this formula in Excel:

```excel
=CONCATENATE(A2, " ", B2)
```

Syntax: `CONCATENATE(text1, [text2], ...)`. Join A2, a space, and B2 into one string. Each argument is a single value; CONCATENATE does not accept a multi-cell range.

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

## Excel-specific notes

CONCATENATE works in every Excel version still in use, but Microsoft marks it as compatibility-only. Prefer `A2 & " " & B2` for two or three pieces, `CONCAT(A2:B2)` when you want to join a range without a delimiter (Excel 2019+ / Microsoft 365), and `TEXTJOIN(", ", TRUE, A2:A7)` when you need a delimiter and want to skip blanks. CONCATENATE turns numbers into their raw values, so format with TEXT first if you need currency or dates in the result. A cell can hold at most 32,767 characters.

**Ampersand (any Excel version)**

```excel
=A2 & " " & B2
```

**CONCAT over a range (Excel 2019+ / Microsoft 365)**

```excel
=CONCAT(A2:B2)
```

**TEXTJOIN with a delimiter, skipping blanks**

```excel
=TEXTJOIN(" ", TRUE, A2:B2)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=CONCATENATE(A2, " ", B2)
```

Sheets adds JOIN and ARRAYFORMULA for whole-column joins. CONCATENATE still cannot take a range as a single argument — use CONCAT, &, JOIN, or TEXTJOIN instead.

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
