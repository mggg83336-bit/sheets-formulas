---
title: How to Use SUMIF in Google Sheets
slug: sumif-google-sheets
date: '2026-10-24'
summary: 'SUMIF adds the numbers that meet one condition: all expenses in a category,
  all amounts over a threshold, or all items whose name starts with certain letters.
  Below are the syntax, three worked examples, and the mistakes that make SUMIF return
  0.'
tags:
- Conditional sums & counts
- Google Sheets
keyword: sumif-google-sheets
niche: sheets-formulas
provider: structured
entry_id: sumif
platform: Google Sheets
category: conditional
faq:
- q: What is the difference between SUMIF and SUMIFS?
  a: SUMIF supports one condition; SUMIFS supports one or more. SUMIFS puts the sum
    range first, SUMIF puts it last.
- q: Can SUMIF use a date as the criteria?
  a: Yes, e.g. =SUMIF(A2:A100, ">="&DATE(2026,1,1), B2:B100). For a date range use
    SUMIFS with two conditions.
- q: How do I sum cells that are not equal to something?
  a: Use "<>" in front of the value, e.g. =SUMIF(A2:A7, "<>Travel", C2:C7).
related:
- - sumifs-google-sheets
  - sumifs-excel
- - countif-google-sheets
  - countif-excel
- - sumifs-between-dates-google-sheets
  - sumifs-between-dates-excel
- - sum-by-month-google-sheets
  - sum-by-month-excel
- - maxifs-minifs-google-sheets
  - maxifs-minifs-excel
sibling: sumif-excel
---
SUMIF adds the numbers that meet one condition: all expenses in a category, all amounts over a threshold, or all items whose name starts with certain letters. Below are the syntax, three worked examples, and the mistakes that make SUMIF return 0.

## Quick answer

Use this formula in Google Sheets:

```excel
=SUMIF(A2:A7, E2, C2:C7)
```

Same syntax in Google Sheets: `SUMIF(range, criterion, [sum_range])`.

## The problem

You keep an expense list with a category for every line and want a total per category without filtering or adding cells by hand.

## Worked example

An expense list with three totals.

| | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 1 | **Category** | **Item** | **Amount** |  | **Criteria** | **Total** |
| 2 | Office | Paper | 45 |  | Office | **146** |
| 3 | Travel | Taxi | 32.5 |  | >40 | **198** |
| 4 | Office | Toner | 89 |  | T* | **185.5** |
| 5 | Meals | Lunch | 18.75 |  |  |  |
| 6 | Travel | Train | 64 |  |  |  |
| 7 | Office | Pens | 12 |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**F2** — total for the category in E2

```excel
=SUMIF(A2:A7, E2, C2:C7)
```

Result: **146**

**F3** — amounts greater than 40 (no sum_range needed)

```excel
=SUMIF(C2:C7, ">40")
```

Result: **198**

**F4** — items starting with T

```excel
=SUMIF(B2:B7, "T*", C2:C7)
```

Result: **185.5**

<!--AD_IN_ARTICLE-->

## How the formula works

1. The first argument is the range to test (Category).
2. The second is the condition: a value, a cell, or text such as ">40" or "T*".
3. The third is the range to add. It must line up row by row with the test range.
4. If the test range and the numbers are the same column, leave the third argument out, as in `=SUMIF(C2:C7, ">40")`.

## Google Sheets-specific notes

SUMIF behaves the same in Google Sheets, including wildcards. A Sheets-specific option is to build a full summary table with one formula: `=QUERY(A2:C7, "select A, sum(C) group by A label sum(C) 'Total'", 0)` returns each category with its total and updates when new categories appear, which is handy when you do not know the categories in advance.

**Totals for every category at once**

```excel
=QUERY(A2:C7, "select A, sum(C) group by A label sum(C) 'Total'", 0)
```


## Excel version

The same formula works unchanged in Excel:

```excel
=SUMIF(A2:A7, E2, C2:C7)
```

Excel uses the identical syntax and wildcards.

<!--SIBLING-->


## Common errors and how to fix them

- **Returns 0** — The amounts are stored as text (often after an import), or the criterion has an extra space. **Fix:** Convert the column to numbers (Data > Text to Columns > Finish in Excel, Format > Number in Sheets) and check the criterion with LEN.
- **Wrong total** — The sum range has a different size or starts on a different row than the test range. **Fix:** Make both ranges the same size, e.g. A2:A7 and C2:C7.
- **Operator criterion ignored** — The operator was not quoted, e.g. =SUMIF(C2:C7, >40). **Fix:** Put operators in quotes and join cell references with &, e.g. ">"&G1.

## FAQ

### What is the difference between SUMIF and SUMIFS?

SUMIF supports one condition; SUMIFS supports one or more. SUMIFS puts the sum range first, SUMIF puts it last.

### Can SUMIF use a date as the criteria?

Yes, e.g. =SUMIF(A2:A100, ">="&DATE(2026,1,1), B2:B100). For a date range use SUMIFS with two conditions.

### How do I sum cells that are not equal to something?

Use "<>" in front of the value, e.g. =SUMIF(A2:A7, "<>Travel", C2:C7).

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
