---
title: 'How to Fix the #DIV/0! Error in Excel'
slug: div0-error-excel
date: '2026-10-22'
summary: '#DIV/0! appears when a formula divides by zero or by an empty cell. This
  page shows how to show a blank or a message instead, how AVERAGE-type functions
  trigger it, and when the error is actually useful.'
tags:
- Fixing formula errors
- Excel
keyword: div0-error-excel
niche: sheets-formulas
provider: structured
entry_id: div0-error
platform: Excel
category: errors
faq:
- q: Should I return 0 or blank?
  a: Return blank ("") when there is no meaningful value, so averages and charts are
    not pulled down by fake zeros. Return 0 only when zero is the true answer.
- q: Why is
  a: It signals missing input. In a template, leaving it visible until the user fills
    in the divisor can prevent wrong decisions based on an incomplete sheet.
related:
- - iferror-excel
  - iferror-google-sheets
- - value-error-excel
  - value-error-google-sheets
- - percentage-change-excel
  - percentage-change-google-sheets
- - weighted-average-excel
  - weighted-average-google-sheets
sibling: div0-error-google-sheets
---
#DIV/0! appears when a formula divides by zero or by an empty cell. This page shows how to show a blank or a message instead, how AVERAGE-type functions trigger it, and when the error is actually useful.

## Quick answer

Use this formula in Excel:

```excel
=IF(C2=0, "", B2/C2)
```

An empty cell counts as 0, so C2=0 catches both zeros and blanks. Only when C2 has a non-zero value is the division performed.

## The problem

An average-order-value column divides revenue by orders. Months with no orders, or where the orders cell is still empty, show #DIV/0!.

## Worked example

February had no orders and April's orders are not entered yet.

| | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| 1 | **Month** | **Revenue** | **Orders** | **Plain division** | **Fixed** |  | **Avg revenue in May** |
| 2 | Jan | 4200 | 60 | **70** | **70** |  | **0** |
| 3 | Feb | 0 | 0 | **#DIV/0!** | **** |  |  |
| 4 | Mar | 3150 | 45 | **70** | **70** |  |  |
| 5 | Apr | 2800 |  | **#DIV/0!** | **** |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**D2 (filled to D5)** — plain division, filled down

```excel
=B2/C2
```

Results: **70**, **#DIV/0!**, **70**, **#DIV/0!**

**E2 (filled to E5)** — fixed, filled down

```excel
=IF(C2=0, "", B2/C2)
```

Results: **70**, *(blank)*, **70**, *(blank)*

**G2** — AVERAGEIF with no matching month

```excel
=IFERROR(AVERAGEIF(A2:A5, "May", B2:B5), 0)
```

Result: **0**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Division by 0 is undefined, so the spreadsheet returns
2. `C2=0` is TRUE for 0 and for an empty cell.
3. When it is TRUE, IF returns "" (an empty-looking cell); otherwise it performs the division.
4. AVERAGEIF divides the matching total by the number of matches. With no "May" rows that count is 0, so IFERROR supplies 0.

## Excel-specific notes

Checking the divisor with IF is clearer than IFERROR because it only handles the division problem; IFERROR would also hide a typo or a #REF!. AVERAGE, AVERAGEIF and AVERAGEIFS return #DIV/0! when there is nothing to average, for example when no row meets the condition. Returning "" makes the cell look empty, but remember that charts and some formulas treat "" differently from a truly blank cell.

**AVERAGEIF with no matches**

```excel
=IFERROR(AVERAGEIF(A2:A5, "May", B2:B5), 0)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=IF(C2=0, "", B2/C2)
```

The same formula works in Google Sheets.

<!--SIBLING-->


## Common errors and how to fix them

- **Division by an empty cell** — The divisor has not been filled in yet. **Fix:** Test the divisor with IF(C2=0, ...) or IF(C2="", ...).
- **AVERAGE of nothing** — The range contains no numbers, or AVERAGEIF(S) found no match. **Fix:** Wrap in IFERROR, or test with COUNTIF first.
- **Divisor is text** — Text in the divisor causes **Fix:** Check the cell the divisor refers to, including hidden rows.

## FAQ

### Should I return 0 or blank?

Return blank ("") when there is no meaningful value, so averages and charts are not pulled down by fake zeros. Return 0 only when zero is the true answer.

### Why is

It signals missing input. In a template, leaving it visible until the user fills in the divisor can prevent wrong decisions based on an incomplete sheet.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
