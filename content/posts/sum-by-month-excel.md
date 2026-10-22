---
title: How to Sum by Month in Excel
slug: sum-by-month-excel
date: '2026-10-22'
summary: To total daily transactions by month, use SUMIFS with a start date and EOMONTH
  as the end date. This guide builds a monthly summary that you can fill down, plus
  a SUMPRODUCT version and a one-formula QUERY report for Google Sheets.
tags:
- Conditional sums & counts
- Excel
keyword: sum-by-month-excel
niche: sheets-formulas
provider: structured
entry_id: sum-by-month
platform: Excel
category: conditional
faq:
- q: How do I sum by week instead?
  a: Put the start date of each week in the summary column and use "<"&D2+7 as the
    upper limit.
- q: Can I sum by month without a summary table?
  a: Use a PivotTable grouped by months (Excel), or the QUERY formula above (Google
    Sheets).
related:
- - sumifs-between-dates-excel
  - sumifs-between-dates-google-sheets
- - sumifs-excel
  - sumifs-google-sheets
- - eomonth-excel
  - eomonth-google-sheets
- - sumif-excel
  - sumif-google-sheets
sibling: sum-by-month-google-sheets
---
To total daily transactions by month, use SUMIFS with a start date and EOMONTH as the end date. This guide builds a monthly summary that you can fill down, plus a SUMPRODUCT version and a one-formula QUERY report for Google Sheets.

## Quick answer

Use this formula in Excel:

```excel
=SUMIFS($B$2:$B$7, $A$2:$A$7, ">="&D2, $A$2:$A$7, "<="&EOMONTH(D2, 0))
```

D2 holds the first day of the month. EOMONTH(D2, 0) returns the last day of the same month, so SUMIFS adds every transaction between the two.

## The problem

Transactions are listed with their dates. You want a summary with one row per month and the total for that month.

## Worked example

D2:D4 contain the first day of each month (formatted as month and year).

| | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 1 | **Date** | **Amount** |  | **Month** | **Total** |  |
| 2 | 2026-01-05 | 120 |  | 2026-01-01 | **200** | **200** |
| 3 | 2026-01-19 | 80 |  | 2026-02-01 | **250** | **250** |
| 4 | 2026-02-02 | 200 |  | 2026-03-01 | **100** | **100** |
| 5 | 2026-02-20 | 50 |  |  |  |  |
| 6 | 2026-03-11 | 75 |  |  |  |  |
| 7 | 2026-03-30 | 25 |  |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**E2 (filled to E4)** — filled down to E4

```excel
=SUMIFS($B$2:$B$7, $A$2:$A$7, ">="&D2, $A$2:$A$7, "<="&EOMONTH(D2, 0))
```

Results: **200**, **250**, **100**

**F2 (filled to F4)** — SUMPRODUCT version, filled down to F4

```excel
=SUMPRODUCT((MONTH($A$2:$A$7)=MONTH(D2))*(YEAR($A$2:$A$7)=YEAR(D2))*$B$2:$B$7)
```

Results: **200**, **250**, **100**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `">="&D2` keeps dates on or after the 1st of the month.
2. `EOMONTH(D2, 0)` returns the last day of that month (Jan 31, Feb 28, Mar 31), and `"<="&` turns it into an upper limit.
3. The absolute references ($) keep the data ranges fixed while D2 changes to D3 and D4 as you fill down.
4. The SUMPRODUCT version compares the month and year of every date with the month and year in column D and multiplies by the amounts.

## Excel-specific notes

Put real dates (the 1st of each month) in the month column and format them as "mmm yyyy"; typing text like "Jan" will not work with the comparison. In Microsoft 365 you can build the month list automatically with `=UNIQUE(EOMONTH(A2:A7, -1)+1)`. A PivotTable grouped by month is the no-formula alternative when you only need a one-off report.

**SUMPRODUCT by month number and year**

```excel
=SUMPRODUCT((MONTH($A$2:$A$7)=MONTH(D2))*(YEAR($A$2:$A$7)=YEAR(D2))*$B$2:$B$7)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=SUMIFS($B$2:$B$7, $A$2:$A$7, ">="&D2, $A$2:$A$7, "<="&EOMONTH(D2, 0))
```

The same formula works in Google Sheets, which can also build the full monthly summary with one QUERY.

<!--SIBLING-->


## Common errors and how to fix them

- **All totals are 0** — The month column contains text ("Jan") or the transaction dates are text. **Fix:** Use real dates such as 2026-01-01 formatted as "mmm yyyy", and check the data with ISNUMBER.
- **Last day of the month missing** — Dates include times, so the 31st at 14:00 is after EOMONTH's midnight. **Fix:** Use "<"&EOMONTH(D2,0)+1 as the upper limit.
- **January of two years added together** — The SUMPRODUCT version only checks MONTH. **Fix:** Also compare YEAR, as in the formula above.

## FAQ

### How do I sum by week instead?

Put the start date of each week in the summary column and use "<"&D2+7 as the upper limit.

### Can I sum by month without a summary table?

Use a PivotTable grouped by months (Excel), or the QUERY formula above (Google Sheets).

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
