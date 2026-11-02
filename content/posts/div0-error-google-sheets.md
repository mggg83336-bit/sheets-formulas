---
title: 'How to Fix the #DIV/0! Error in Google Sheets'
slug: div0-error-google-sheets
date: '2026-11-02'
summary: '#DIV/0! appears when a formula divides by zero or by an empty cell. This
  page shows how to show a blank or a message instead, how AVERAGE-type functions
  trigger it, and when the error is actually useful.'
tags:
- Fixing formula errors
- Google Sheets
keyword: div0-error-google-sheets
niche: sheets-formulas
provider: structured
entry_id: div0-error
platform: Google Sheets
category: errors
faq:
- q: Should I return 0 or blank?
  a: Return blank ("") when there is no meaningful value, so averages and charts are
    not pulled down by fake zeros. Return 0 only when zero is the true answer.
- q: Why is
  a: It signals missing input. In a template, leaving it visible until the user fills
    in the divisor can prevent wrong decisions based on an incomplete sheet.
related:
- - iferror-google-sheets
  - iferror-excel
- - value-error-google-sheets
  - value-error-excel
- - percentage-change-google-sheets
  - percentage-change-excel
- - weighted-average-google-sheets
  - weighted-average-excel
sibling: div0-error-excel
---
#DIV/0! appears when a formula divides by zero or by an empty cell. This page shows how to show a blank or a message instead, how AVERAGE-type functions trigger it, and when the error is actually useful.

## Quick answer

Use this formula in Google Sheets:

```excel
=IF(C2=0, "", B2/C2)
```

Identical guard pattern in Google Sheets: test the divisor first, return a blank when it is zero or empty, and only then divide revenue by orders so #DIV/0! never appears in the report.

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

## Google Sheets-specific notes

Google Sheets also has a DIVIDE function, and its hover message reads "Function DIVIDE parameter 2 cannot be zero", which makes the cause easy to confirm. To fill a whole column without errors, use ARRAYFORMULA with the same test: `=ARRAYFORMULA(IF(C2:C=0, "", B2:B/C2:C))`. Because empty rows also have C=0, the formula leaves them blank automatically. Prefer the explicit IF test over IFERROR so typos and #REF! issues stay visible; IFERROR is still useful around AVERAGEIF when a month has no matching rows. Format the result column as a number, and return "" rather than 0 when the month simply has no activity so charts are not pulled down by fake zeros.

**Whole column with ARRAYFORMULA**

```excel
=ARRAYFORMULA(IF(C2:C=0, "", B2:B/C2:C))
```

**Show a message instead of blank**

```excel
=IF(C2=0, "No orders", B2/C2)
```

**AVERAGEIF with no matches**

```excel
=IFERROR(AVERAGEIF(A2:A5, "May", B2:B5), 0)
```


## Excel version

The same formula works unchanged in Excel:

```excel
=IF(C2=0, "", B2/C2)
```

Excel uses the identical formula.

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
