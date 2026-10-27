---
title: SUMIFS Between Two Dates in Google Sheets
slug: sumifs-between-dates-google-sheets
date: '2026-10-27'
summary: 'To add values that fall within a date range, use SUMIFS with the date column
  twice: once with ">=" the start date and once with "<=" the end date. This page
  shows the cell-based version, the hard-coded version and how to avoid losing rows
  that contain a time.'
tags:
- Conditional sums & counts
- Google Sheets
keyword: sumifs-between-dates-google-sheets
niche: sheets-formulas
provider: structured
entry_id: sumifs-between-dates
platform: Google Sheets
category: conditional
faq:
- q: Why does the operator go in quotes?
  a: SUMIFS criteria are text. The & joins the operator with the date's serial number
    to form a condition such as ">=46054".
- q: Why does ">=L1" return 0 when the dates are right?
  a: '">=L1" is the characters >=L1. SUMIFS looks for that text and does not read
    the date in L1, so the total is 0. ">="&L1 joins the operator to the date serial
    in L1, which is what SUMIFS compares. The same join is how you write any threshold
    on SUMIFS, and how you count the rows with COUNTIFS.'
- q: How do I count rows between two dates instead?
  a: 'Use COUNTIFS with the same two conditions: =COUNTIFS(A2:A7, ">="&D2, A2:A7,
    "<="&E2).'
related:
- - sumifs-google-sheets
  - sumifs-excel
- - countifs-google-sheets
  - countifs-excel
- - sum-by-month-google-sheets
  - sum-by-month-excel
- - days-between-dates-google-sheets
  - days-between-dates-excel
- - eomonth-google-sheets
  - eomonth-excel
sibling: sumifs-between-dates-excel
---
To add values that fall within a date range, use SUMIFS with the date column twice: once with ">=" the start date and once with "<=" the end date. This page shows the cell-based version, the hard-coded version and how to avoid losing rows that contain a time.

## Quick answer

Use this formula in Google Sheets:

```excel
=SUMIFS(B2:B7, A2:A7, ">="&D2, A2:A7, "<="&E2)
```

Identical in Google Sheets. The comparison works on the underlying date serial numbers.

<!--CTA_PROMINENT-->

## The problem

You have dated transactions and need the total for February, or for any start and end date typed into two input cells.

## Worked example

Total of transactions between the start date in D2 and the end date in E2.

| | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 1 | **Date** | **Amount** |  | **Start** | **End** | **Total** |
| 2 | 2026-01-28 | 400 |  | 2026-02-01 | 2026-02-28 | **1000** |
| 3 | 2026-02-03 | 250 |  |  |  | **1000** |
| 4 | 2026-02-14 | 600 |  |  |  |  |
| 5 | 2026-02-28 | 150 |  |  |  |  |
| 6 | 2026-03-01 | 300 |  |  |  |  |
| 7 | 2026-03-15 | 200 |  |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**F2** — from input cells

```excel
=SUMIFS(B2:B7, A2:A7, ">="&D2, A2:A7, "<="&E2)
```

Result: **1000**

**F3** — fixed dates for February

```excel
=SUMIFS(B2:B7, A2:A7, ">="&DATE(2026,2,1), A2:A7, "<"&DATE(2026,3,1))
```

Result: **1000**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `">="&D2` builds the text ">=46054" (the serial number of Feb 1, 2026). SUMIFS compares it with the dates in A2:A7.
2. `"<="&E2` adds the upper limit. Both conditions must be true, so only Feb 3, Feb 14 and Feb 28 are included.
3. The amounts on those rows are added: 250 + 600 + 150 = 1000.
4. Using `<` with the first day of the next month is a safe way to include the entire last day.

## Google Sheets-specific notes

Google Sheets also lets you do this with QUERY, which uses ISO date literals and is not affected by the spreadsheet's locale: `=QUERY(A2:B7, "select sum(B) where A >= date '2026-02-01' and A <= date '2026-02-28' label sum(B) ''", 0)`. Check File > Settings > Locale if typed dates are interpreted with day and month swapped; the formula is right, but the dates in the cells may not be real dates.

**QUERY with ISO date literals**

```excel
=QUERY(A2:B7, "select sum(B) where A >= date '2026-02-01' and A <= date '2026-02-28' label sum(B) ''", 0)
```


## Excel version

The same formula works unchanged in Excel:

```excel
=SUMIFS(B2:B7, A2:A7, ">="&D2, A2:A7, "<="&E2)
```

Excel uses the identical SUMIFS formula; write fixed dates with DATE() to avoid regional format problems.

<!--SIBLING-->


## Common errors and how to fix them

- **Returns 0** — The dates in column A are text, not real dates (they are often left-aligned). **Fix:** Convert them with DATEVALUE or Text to Columns; =ISNUMBER(A2) should return TRUE.
- **Last day missing** — The dates contain times, so 2026-02-28 15:30 is greater than 2026-02-28. **Fix:** Use "<"&E2+1 as the upper bound.
- **#VALUE!** — The sum range and the date ranges have different sizes. **Fix:** Use ranges covering the same rows.

<!--CTA_AFTER_ERRORS-->

## FAQ

### Why does the operator go in quotes?

SUMIFS criteria are text. The & joins the operator with the date's serial number to form a condition such as ">=46054".

### Why does ">=L1" return 0 when the dates are right?

`">=L1"` is the characters >=L1. SUMIFS looks for that text and does not read the date in L1, so the total is 0. `">="&L1` joins the operator to the date serial in L1, which is what SUMIFS compares. The same join is how you write any threshold on [SUMIFS](../sumifs-google-sheets/), and how you count the rows with [COUNTIFS](../countifs-google-sheets/).

### How do I count rows between two dates instead?

Use [COUNTIFS](../countifs-google-sheets/) with the same two conditions: `=COUNTIFS(A2:A7, ">="&D2, A2:A7, "<="&E2)`.

## Related formulas

<!--RELATED-->
