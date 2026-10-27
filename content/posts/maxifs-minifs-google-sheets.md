---
title: MAX and MIN with Criteria (MAXIFS / MINIFS) in Google Sheets
slug: maxifs-minifs-google-sheets
date: '2026-10-27'
summary: MAXIFS and MINIFS return the largest or smallest number that meets one or
  more conditions, such as the best month for one store. This page shows both functions
  and the array formula to use in Excel versions that do not have them.
tags:
- Conditional sums & counts
- Google Sheets
keyword: maxifs-minifs-google-sheets
niche: sheets-formulas
provider: structured
entry_id: maxifs-minifs
platform: Google Sheets
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
- - sumifs-google-sheets
  - sumifs-excel
- - countifs-google-sheets
  - countifs-excel
- - xlookup-google-sheets
  - xlookup-excel
- - weighted-average-google-sheets
  - weighted-average-excel
sibling: maxifs-minifs-excel
---
MAXIFS and MINIFS return the largest or smallest number that meets one or more conditions, such as the best month for one store. This page shows both functions and the array formula to use in Excel versions that do not have them.

## Quick answer

Use this formula in Google Sheets:

```excel
=MAXIFS(C2:C7, A2:A7, E2)
```

Same syntax in Google Sheets.

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

## Google Sheets-specific notes

Google Sheets supports MAXIFS and MINIFS with the same arguments. An equally common Sheets pattern is to take the MAX of a FILTER, which reads naturally and can be reused for other statistics such as MEDIAN or AVERAGE on the same subset: `=MAX(FILTER(C2:C7, A2:A7=E2))`. Unlike MAXIFS, the FILTER version returns #N/A when nothing matches instead of 0.

**MAX of a FILTER**

```excel
=MAX(FILTER(C2:C7, A2:A7=E2))
```


## Excel version

The same formula works unchanged in Excel:

```excel
=MAXIFS(C2:C7, A2:A7, E2)
```

MAXIFS/MINIFS have the same syntax in Excel 2019 and later; Excel 2016 needs MAX(IF(...)).

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
