---
title: SUMIFS Between Two Dates in Excel
slug: sumifs-between-dates-excel
date: '2026-10-22'
summary: 'To add values that fall within a date range, use SUMIFS with the date column
  twice: once with ">=" the start date and once with "<=" the end date. This page
  shows the cell-based version, the hard-coded version and how to avoid losing rows
  that contain a time.'
tags:
- Conditional sums & counts
- Excel
keyword: sumifs-between-dates-excel
niche: sheets-formulas
provider: structured
entry_id: sumifs-between-dates
platform: Excel
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
- - sumifs-excel
  - sumifs-google-sheets
- - countifs-excel
  - countifs-google-sheets
- - sum-by-month-excel
  - sum-by-month-google-sheets
- - days-between-dates-excel
  - days-between-dates-google-sheets
- - eomonth-excel
  - eomonth-google-sheets
sibling: sumifs-between-dates-google-sheets
---
To add values that fall within a date range, use SUMIFS with the date column twice: once with ">=" the start date and once with "<=" the end date. This page shows the cell-based version, the hard-coded version and how to avoid losing rows that contain a time.

## Quick answer

Use this formula in Excel:

```excel
=SUMIFS(B2:B7, A2:A7, ">="&D2, A2:A7, "<="&E2)
```

The date column A2:A7 is tested twice: on or after the start date in D2 and on or before the end date in E2. Only rows meeting both are added.

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

## Excel-specific notes

Write fixed dates with the DATE function (`">="&DATE(2026,2,1)`) rather than as text such as ">=2/1/2026", because text dates are interpreted using the computer's regional settings and can silently flip day and month. If the dates include a time (exports from forms or systems often do), use `"<"&E2+1` as the upper bound so the whole end day is included.

**Fixed dates without input cells**

```excel
=SUMIFS(B2:B7, A2:A7, ">="&DATE(2026,2,1), A2:A7, "<"&DATE(2026,3,1))
```

**Dates that include times**

```excel
=SUMIFS(B2:B7, A2:A7, ">="&D2, A2:A7, "<"&E2+1)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=SUMIFS(B2:B7, A2:A7, ">="&D2, A2:A7, "<="&E2)
```

The same formula works in Google Sheets; QUERY with ISO date literals is an alternative there.

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

`">=L1"` is the characters >=L1. SUMIFS looks for that text and does not read the date in L1, so the total is 0. `">="&L1` joins the operator to the date serial in L1, which is what SUMIFS compares. The same join is how you write any threshold on [SUMIFS](../sumifs-excel/), and how you count the rows with [COUNTIFS](../countifs-excel/).

### How do I count rows between two dates instead?

Use [COUNTIFS](../countifs-excel/) with the same two conditions: `=COUNTIFS(A2:A7, ">="&D2, A2:A7, "<="&E2)`.

## Related formulas

<!--RELATED-->
