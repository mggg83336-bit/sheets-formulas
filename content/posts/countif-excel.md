---
title: How to Use COUNTIF in Excel
slug: countif-excel
date: '2026-10-22'
summary: 'COUNTIF counts the cells in a range that meet one condition: a specific
  word, numbers above a threshold, blanks, or anything except a value. Four worked
  examples show exactly which criteria to type, including the surprising way blank
  cells are treated.'
tags:
- Conditional sums & counts
- Excel
keyword: countif-excel
niche: sheets-formulas
provider: structured
entry_id: countif
platform: Excel
category: conditional
faq:
- q: How do I count cells that contain a word?
  a: Use wildcards, e.g. =COUNTIF(A2:A100, "*mouse*").
- q: How do I count with two conditions?
  a: Use COUNTIFS, which takes several range/criteria pairs.
- q: How do I count non-blank cells?
  a: Use =COUNTIF(A2:A100, "<>") or =COUNTA(A2:A100).
related:
- - countifs-excel
  - countifs-google-sheets
- - sumif-excel
  - sumif-google-sheets
- - count-unique-excel
  - count-unique-google-sheets
- - contains-text-excel
  - contains-text-google-sheets
sibling: countif-google-sheets
---
COUNTIF counts the cells in a range that meet one condition: a specific word, numbers above a threshold, blanks, or anything except a value. Four worked examples show exactly which criteria to type, including the surprising way blank cells are treated.

## Quick answer

Use this formula in Excel:

```excel
=COUNTIF(C2:C8, "Pass")
```

Syntax: `COUNTIF(range, criteria)`. Count the cells in C2:C8 equal to "Pass" (not case-sensitive).

## The problem

In a class results sheet you want to know how many students passed, how many scored 70 or more, and how many results are still missing.

## Worked example

Ivy's result has not been entered yet.

| | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 1 | **Student** | **Score** | **Result** |  | **Question** | **Count** |
| 2 | Ava | 88 | Pass |  | Passed | **4** |
| 3 | Liam | 54 | Fail |  | Scored 70+ | **3** |
| 4 | Mia | 92 | Pass |  | Missing result | **1** |
| 5 | Noah | 67 | Pass |  | Not "Pass" | **3** |
| 6 | Zoe | 45 | Fail |  |  |  |
| 7 | Eli | 73 | Pass |  |  |  |
| 8 | Ivy |  |  |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**F2**

```excel
=COUNTIF(C2:C8, "Pass")
```

Result: **4**

**F3**

```excel
=COUNTIF(B2:B8, ">=70")
```

Result: **3**

**F4**

```excel
=COUNTIF(C2:C8, "")
```

Result: **1**

**F5** — includes the blank cell

```excel
=COUNTIF(C2:C8, "<>Pass")
```

Result: **3**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `C2:C8` is the range to check; it can be a column or a block of cells.
2. `"Pass"` counts exact matches, ignoring case.
3. `">=70"` applies a comparison to numbers. Text and empty cells are ignored, so Ivy is not counted.
4. `""` counts empty cells (and cells containing an empty string from a formula).
5. `"<>Pass"` counts everything that is not Pass, including the empty cell: Liam, Zoe and Ivy.

## Excel-specific notes

Criteria follow the same rules as SUMIF: operators go in quotes (`">=70"`), cell references are joined with & (`">="&E1`), and wildcards are supported (`"*pass*"` counts cells that contain "pass"). Note that "<>Pass" also counts empty cells, which surprises many people. COUNTIF only accepts ranges, not arrays, so you cannot pass it the result of another calculation such as `LEFT(A2:A8,1)`; use SUMPRODUCT for that.


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=COUNTIF(C2:C8, "Pass")
```

Google Sheets uses the same syntax. For complex patterns, combine REGEXMATCH and SUMPRODUCT.

<!--SIBLING-->


## Common errors and how to fix them

- **Count is 0** — Leading or trailing spaces in the data, or numbers stored as text when counting with ">". **Fix:** Clean the data with TRIM and convert text numbers to real numbers.
- **Count includes blanks** — "<>value" counts empty cells too. **Fix:** Use COUNTIFS to exclude blanks: =COUNTIFS(C2:C8, "<>Pass", C2:C8, "<>").
- **Wrong count for long numbers** — COUNTIF converts text that looks like a number, so IDs longer than 15 digits are compared as rounded numbers. **Fix:** Use =SUMPRODUCT(--(A2:A8=E2)) for long numeric IDs.

## FAQ

### How do I count cells that contain a word?

Use wildcards, e.g. =COUNTIF(A2:A100, "*mouse*").

### How do I count with two conditions?

Use COUNTIFS, which takes several range/criteria pairs.

### How do I count non-blank cells?

Use =COUNTIF(A2:A100, "<>") or =COUNTA(A2:A100).

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
