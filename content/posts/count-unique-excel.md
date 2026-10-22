---
title: How to Count Unique Values in Excel
slug: count-unique-excel
date: '2026-10-22'
summary: Count how many different values appear in a list, for example how many distinct
  customers placed orders. This page covers the modern UNIQUE approach, the classic
  SUMPRODUCT/COUNTIF formula for older Excel, and counting values that appear only
  once.
tags:
- Conditional sums & counts
- Excel
keyword: count-unique-excel
niche: sheets-formulas
provider: structured
entry_id: count-unique
platform: Excel
category: conditional
faq:
- q: Is UNIQUE case-sensitive?
  a: No. "acme" and "Acme" are treated as the same value in both Excel and Google
    Sheets.
- q: How do I count unique values with a condition?
  a: In Excel 365 use =COUNTA(UNIQUE(FILTER(A2:A8, B2:B8="East"))); in Google Sheets
    use COUNTUNIQUEIFS.
- q: How do I list the unique values instead of counting them?
  a: Use =UNIQUE(A2:A8) in Excel 365 or Google Sheets; it spills the distinct values
    down the column. Wrap it in SORT for an alphabetical list, e.g. =SORT(UNIQUE(A2:A8)).
related:
- - countif-excel
  - countif-google-sheets
- - countifs-excel
  - countifs-google-sheets
- - lookup-multiple-values-excel
  - lookup-multiple-values-google-sheets
- - textjoin-excel
  - textjoin-google-sheets
sibling: count-unique-google-sheets
---
Count how many different values appear in a list, for example how many distinct customers placed orders. This page covers the modern UNIQUE approach, the classic SUMPRODUCT/COUNTIF formula for older Excel, and counting values that appear only once.

## Quick answer

Use this formula in Excel:

```excel
=COUNTA(UNIQUE(A2:A8))
```

UNIQUE returns each distinct customer once; COUNTA counts them.

## The problem

Your order log repeats customer names. You want the number of distinct customers, not the number of orders.

## Worked example

Seven orders from four different customers.

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **Customer** |  | **Question** | **Count** |
| 2 | Acme |  | Distinct customers | **4** |
| 3 | Globex |  | Classic formula | **4** |
| 4 | Acme |  | Ordered exactly once | **2** |
| 5 | Initech |  |  |  |
| 6 | Globex |  |  |  |
| 7 | Acme |  |  |  |
| 8 | Umbrella |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**D2**

```excel
=COUNTA(UNIQUE(A2:A8))
```

Result: **4**

**D3**

```excel
=SUMPRODUCT(1/COUNTIF(A2:A8, A2:A8))
```

Result: **4**

**D4** — Initech and Umbrella

```excel
=COUNTA(UNIQUE(A2:A8, FALSE, TRUE))
```

Result: **2**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `UNIQUE(A2:A8)` returns {Acme; Globex; Initech; Umbrella}.
2. `COUNTA` counts the four items.
3. In the classic formula, `COUNTIF(A2:A8, A2:A8)` returns how often each value occurs: {3;2;3;1;2;3;1}.
4. `1/` turns those into fractions (each Acme contributes 1/3), so each customer adds up to exactly 1. SUMPRODUCT adds them: 4.
5. UNIQUE's third argument (exactly_once = TRUE) returns only values that occur once.

## Excel-specific notes

UNIQUE needs Microsoft 365 or Excel 2021+. If the range may contain blank cells, filter them out first, otherwise the blank counts as one value: `=COUNTA(UNIQUE(FILTER(A2:A100, A2:A100<>"")))`. For older Excel use the SUMPRODUCT/COUNTIF formula below; it gets slow above a few thousand rows because it counts every value against every other value.

**Older Excel versions**

```excel
=SUMPRODUCT(1/COUNTIF(A2:A8, A2:A8))
```

**Older Excel, range with blanks**

```excel
=SUMPRODUCT((A2:A8<>"")/COUNTIF(A2:A8, A2:A8&""))
```


## Google Sheets version

In Google Sheets, use:

```excel
=COUNTUNIQUE(A2:A8)
```

Google Sheets has a dedicated COUNTUNIQUE function, which ignores blank cells, and COUNTUNIQUEIFS for counting with conditions.

<!--SIBLING-->


## Common errors and how to fix them

- **#DIV/0! in the classic formula** — The range contains blank cells, and COUNTIF of a blank returns 0. **Fix:** Use the blank-safe version: =SUMPRODUCT((A2:A8<>"")/COUNTIF(A2:A8, A2:A8&"")).
- **Count is one too high** — A blank cell inside the range was counted as a unique value by UNIQUE. **Fix:** Wrap the range in FILTER(..., range<>"") before UNIQUE.
- **"Acme" and "Acme " counted separately** — Trailing spaces make the values different. **Fix:** Clean the column with TRIM first.

## FAQ

### Is UNIQUE case-sensitive?

No. "acme" and "Acme" are treated as the same value in both Excel and Google Sheets.

### How do I count unique values with a condition?

In Excel 365 use =COUNTA(UNIQUE(FILTER(A2:A8, B2:B8="East"))); in Google Sheets use COUNTUNIQUEIFS.

### How do I list the unique values instead of counting them?

Use =UNIQUE(A2:A8) in Excel 365 or Google Sheets; it spills the distinct values down the column. Wrap it in SORT for an alphabetical list, e.g. =SORT(UNIQUE(A2:A8)).

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
