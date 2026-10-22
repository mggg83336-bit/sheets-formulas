---
title: SUMIFS with Multiple Criteria in Excel
slug: sumifs-excel
date: '2026-10-22'
summary: SUMIFS adds numbers that meet several conditions at the same time, for example
  sales for one region AND one product. This page covers AND logic, number thresholds,
  and the trick for OR logic across several values.
tags:
- Conditional sums & counts
- Excel
keyword: sumifs-excel
niche: sheets-formulas
provider: structured
entry_id: sumifs
platform: Excel
category: conditional
faq:
- q: Can SUMIFS use OR logic?
  a: Not directly; all conditions are AND. Use SUM(SUMIFS(...)) with an array constant,
    or add two SUMIFS together.
- q: How do I sum between two dates with SUMIFS?
  a: Use the date column twice, e.g. =SUMIFS(B:B, A:A, ">="&D2, A:A, "<="&E2).
- q: Is SUMIFS case-sensitive?
  a: No. Use SUMPRODUCT with EXACT if you need a case-sensitive sum.
related:
- - sumif-excel
  - sumif-google-sheets
- - sumifs-between-dates-excel
  - sumifs-between-dates-google-sheets
- - countifs-excel
  - countifs-google-sheets
- - sum-by-month-excel
  - sum-by-month-google-sheets
- - vlookup-multiple-criteria-excel
  - vlookup-multiple-criteria-google-sheets
sibling: sumifs-google-sheets
---
SUMIFS adds numbers that meet several conditions at the same time, for example sales for one region AND one product. This page covers AND logic, number thresholds, and the trick for OR logic across several values.

## Quick answer

Use this formula in Excel:

```excel
=SUMIFS(D2:D8, A2:A8, F2, C2:C8, G2)
```

Syntax: `SUMIFS(sum_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)`. Add D2:D8 where A2:A8 equals F2 AND C2:C8 equals G2.

## The problem

Your sales log has Region, Rep, Product and Sales columns. You need totals such as "East region laptops" or "Monitors sold in East or West" for a report.

## Worked example

Three totals from the same sales log.

| | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| 1 | **Region** | **Rep** | **Product** | **Sales** |  | **Region** | **Product** | **Total** |
| 2 | East | Kim | Laptop | 1200 |  | East | Laptop | **2300** |
| 3 | West | Ruiz | Laptop | 950 |  |  |  | **2600** |
| 4 | East | Patel | Monitor | 300 |  |  |  | **990** |
| 5 | East | Kim | Monitor | 280 |  |  |  |  |
| 6 | West | Ruiz | Monitor | 410 |  |  |  |  |
| 7 | East | Patel | Laptop | 1100 |  |  |  |  |
| 8 | North | Lee | Laptop | 870 |  |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**H2** — East AND Laptop

```excel
=SUMIFS(D2:D8, A2:A8, F2, C2:C8, G2)
```

Result: **2300**

**H3** — East AND sales of at least 300

```excel
=SUMIFS(D2:D8, A2:A8, "East", D2:D8, ">=300")
```

Result: **2600**

**H4** — Monitors in East OR West

```excel
=SUM(SUMIFS(D2:D8, A2:A8, {"East","West"}, C2:C8, "Monitor"))
```

Result: **990**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `D2:D8` is the column to add. In SUMIFS it always comes first.
2. Then come pairs: a range to test and the condition for it. `A2:A8, F2` keeps rows where Region is East.
3. `C2:C8, G2` additionally keeps rows where Product is Laptop. Only rows meeting every pair are added: 1200 + 1100 = 2300.
4. The sum range can also be a criteria range, as in `D2:D8, ">=300"`.
5. For OR, the array constant makes SUMIFS return one total per region, {580, 410} (East monitors and West monitors), and SUM adds them: 990.

## Excel-specific notes

All conditions in SUMIFS are combined with AND. For OR logic on one column, pass an array constant and wrap the result in SUM: `=SUM(SUMIFS(D2:D8, A2:A8, {"East","West"}, C2:C8, "Monitor"))`; Excel evaluates it once per value and adds the results. You can use up to 127 range/criteria pairs, and every criteria range must be the same size as the sum range, otherwise Excel returns #VALUE!.


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=SUMIFS(D2:D8, A2:A8, F2, C2:C8, G2)
```

Google Sheets uses the same syntax, but OR logic with an array constant must be wrapped in ARRAYFORMULA.

<!--SIBLING-->


## Common errors and how to fix them

- **#VALUE!** — A criteria range is a different size than the sum range (e.g. A2:A8 vs D2:D9). **Fix:** Make every range cover the same rows.
- **Returns 0** — Numbers stored as text, a trailing space in a criterion, or the arguments are in SUMIF order (sum range last). **Fix:** Put the sum range first and clean the data.
- **OR total is too low in Google Sheets** — The {"East","West"} array was used without ARRAYFORMULA, so only East was counted. **Fix:** Wrap the formula in ARRAYFORMULA.

## FAQ

### Can SUMIFS use OR logic?

Not directly; all conditions are AND. Use SUM(SUMIFS(...)) with an array constant, or add two SUMIFS together.

### How do I sum between two dates with SUMIFS?

Use the date column twice, e.g. =SUMIFS(B:B, A:A, ">="&D2, A:A, "<="&E2).

### Is SUMIFS case-sensitive?

No. Use SUMPRODUCT with EXACT if you need a case-sensitive sum.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
