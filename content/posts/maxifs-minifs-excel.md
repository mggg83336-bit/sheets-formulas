---
title: MAX and MIN with Criteria (MAXIFS / MINIFS) in Excel
slug: maxifs-minifs-excel
date: '2026-10-22'
summary: MAXIFS and MINIFS return the largest or smallest number that meets one or
  more conditions, such as the best month for one store. This page shows both functions
  and the array formula to use in Excel versions that do not have them.
tags:
- Conditional sums & counts
- Excel
keyword: maxifs-minifs-excel
niche: sheets-formulas
provider: structured
entry_id: maxifs-minifs
platform: Excel
category: conditional
faq:
- q: How do I get the name that goes with the maximum?
  a: Combine with a lookup, e.g. =XLOOKUP(MAXIFS(C2:C7,A2:A7,E2), C2:C7, B2:B7) returns
    the month of the best result (first match if there is a tie).
- q: Is there an AVERAGEIFS too?
  a: Yes, AVERAGEIFS uses the same argument order and works in Excel 2007+ and Google
    Sheets.
- q: How do I find the second-highest value with a condition?
  a: MAXIFS only returns the top value. Use LARGE with FILTER in Excel 365 or Google
    Sheets, e.g. =LARGE(FILTER(C2:C7, A2:A7=E2), 2), or the array formula =LARGE(IF(A2:A7=E2,
    C2:C7), 2) in older Excel.
related:
- - sumifs-excel
  - sumifs-google-sheets
- - countifs-excel
  - countifs-google-sheets
- - xlookup-excel
  - xlookup-google-sheets
- - weighted-average-excel
  - weighted-average-google-sheets
sibling: maxifs-minifs-google-sheets
---
MAXIFS and MINIFS return the largest or smallest number that meets one or more conditions, such as the best month for one store. This page shows both functions and the array formula to use in Excel versions that do not have them.

## Quick answer

Use this formula in Excel:

```excel
=MAXIFS(C2:C7, A2:A7, E2)
```

Syntax: `MAXIFS(max_range, criteria_range1, criteria1, ...)`. MINIFS uses the same arguments. The value range comes first, like SUMIFS.

## The problem

You track monthly revenue for several stores and want the highest and lowest month for a chosen store, and the best result of any store in February.

## Worked example

Revenue by store and month.

| | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 1 | **Store** | **Month** | **Revenue** |  | **Store** | **Result** |
| 2 | Downtown | Jan | 18200 |  | Downtown | **18200** |
| 3 | Airport | Jan | 9400 |  |  | **16900** |
| 4 | Downtown | Feb | 16900 |  |  | **16900** |
| 5 | Airport | Feb | 11250 |  |  |  |
| 6 | Mall | Jan | 13700 |  |  |  |
| 7 | Mall | Feb | 12100 |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**F2** — best month for Downtown

```excel
=MAXIFS(C2:C7, A2:A7, E2)
```

Result: **18200**

**F3** — weakest month for Downtown

```excel
=MINIFS(C2:C7, A2:A7, E2)
```

Result: **16900**

**F4** — best store result in February

```excel
=MAXIFS(C2:C7, B2:B7, "Feb")
```

Result: **16900**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `C2:C7` holds the numbers to compare.
2. `A2:A7, E2` keeps only rows for the store in E2 (Downtown): 18,200 and 16,900.
3. MAXIFS returns the larger of those, MINIFS the smaller.
4. Add more pairs for more conditions, e.g. `B2:B7, "Feb"`.

## Excel-specific notes

MAXIFS and MINIFS exist in Excel 2019, 2021, 2024 and Microsoft 365. In Excel 2016 and older they return #NAME?; use `=MAX(IF(A2:A7=E2, C2:C7))` confirmed with Ctrl+Shift+Enter instead. When no row meets the conditions, MAXIFS returns 0 rather than an error, which can be misleading for negative numbers; check with COUNTIFS first if that matters.

**Excel 2016 and older (array formula)**

```excel
=MAX(IF(A2:A7=E2, C2:C7))
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=MAXIFS(C2:C7, A2:A7, E2)
```

Google Sheets uses the same MAXIFS / MINIFS syntax.

<!--SIBLING-->


## Common errors and how to fix them

- **#NAME?** — Excel 2016 or older does not have MAXIFS / MINIFS. **Fix:** Use =MAX(IF(...)) entered with Ctrl+Shift+Enter, or AGGREGATE.
- **Returns 0** — No row meets the conditions (or the numbers are text). **Fix:** Check with COUNTIFS; wrap in IF(COUNTIFS(...)=0, "None", MAXIFS(...)).
- **#VALUE!** — The criteria range and max range are different sizes. **Fix:** Use ranges covering the same rows.

## FAQ

### How do I get the name that goes with the maximum?

Combine with a lookup, e.g. =XLOOKUP(MAXIFS(C2:C7,A2:A7,E2), C2:C7, B2:B7) returns the month of the best result (first match if there is a tie).

### Is there an AVERAGEIFS too?

Yes, AVERAGEIFS uses the same argument order and works in Excel 2007+ and Google Sheets.

### How do I find the second-highest value with a condition?

MAXIFS only returns the top value. Use LARGE with FILTER in Excel 365 or Google Sheets, e.g. =LARGE(FILTER(C2:C7, A2:A7=E2), 2), or the array formula =LARGE(IF(A2:A7=E2, C2:C7), 2) in older Excel.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
