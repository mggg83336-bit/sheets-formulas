---
title: How to Calculate a Running Total in Excel
slug: running-total-excel
date: '2026-11-06'
summary: A running total (cumulative sum) adds each new row to everything above it.
  The portable pattern is an expanding SUM with a locked start cell — `=SUM($B$2:B2)`
  filled down — so each row shows year-to-date sales, spend, or inventory movement
  without a pivot table.
tags:
- Conditional sums & counts
- Excel
keyword: running-total-excel
niche: sheets-formulas
provider: structured
entry_id: running-total
platform: Excel
category: conditional
faq:
- q: How is a running total different from a regular SUM?
  a: SUM of the whole block repeats the same grand total on every row. A running total
    grows row by row so you can see progress through the period.
- q: Does this work inside an Excel Table?
  a: Yes. Use a structured expanding reference such as =SUM(INDEX([Sales],1):[@Sales])
    so new table rows keep the pattern.
- q: Can I reset the total each month?
  a: Add a month helper column and restart when the month changes, or use SUMIFS with
    “date ≤ this row” and “same month” criteria.
- q: What about Google Sheets SCAN?
  a: SCAN spills the whole cumulative column from one cell. Use it when everyone stays
    in Sheets or Excel 365; keep expanding SUM for maximum portability.
related:
- - sumif-excel
  - sumif-google-sheets
- - sumifs-excel
  - sumifs-google-sheets
- - sum-by-month-excel
  - sum-by-month-google-sheets
- - averageif-excel
  - averageif-google-sheets
- - countif-excel
  - countif-google-sheets
sibling: running-total-google-sheets
---
A running total (cumulative sum) adds each new row to everything above it. The portable pattern is an expanding SUM with a locked start cell — `=SUM($B$2:B2)` filled down — so each row shows year-to-date sales, spend, or inventory movement without a pivot table.

## Quick answer

Use this formula in Excel:

```excel
=SUM($B$2:B2)
```

Lock the first amount with `$B$2` and leave the end reference relative (`B2`). Fill down so row 3 becomes `=SUM($B$2:B3)`, row 4 becomes `=SUM($B$2:B4)`, and so on.

## The problem

A daily sales log needs a cumulative column that updates when amounts change. People retype totals by hand, use a plain SUM of the whole column on every row (so every row shows the grand total), or forget to lock the starting cell and break the fill-down.

## Worked example

Five weekdays of sales. The running-total column starts at 100 and grows to the week total of 650. Each check uses the expanding SUM filled down.

| | A | B | C |
|---|---|---|---|
| 1 | **Day** | **Sales** | **Running total** |
| 2 | Mon | 100 | **100** |
| 3 | Tue | 150 | **250** |
| 4 | Wed | 80 | **330** |
| 5 | Thu | 200 | **530** |
| 6 | Fri | 120 | **650** |
| 7 |  |  |  |
| 8 |  |  | **650** |
| 9 |  |  | **100** |

Formulas used in the example (results shown in **bold** in the table above):

**C2 (filled to C6)** — running total filled down

```excel
=SUM($B$2:B2)
```

Results: **100**, **250**, **330**, **530**, **650**

**C8** — week grand total for contrast

```excel
=SUM(B2:B6)
```

Result: **650**

**C9** — prior-plus-this-row style on first data row

```excel
=N(C1)+B2
```

Result: **100**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Enter dates or labels in column A and the amounts to accumulate in column B.
2. In C2 type `=SUM($B$2:B2)` — note the $ on the starting cell only.
3. Fill the formula down beside every amount row; each end reference expands automatically.
4. Confirm the last running total equals `=SUM(B2:B6)` for the same block.
5. Optional: switch power users to SCAN for a single spilled cumulative column.

## Excel-specific notes

The expanding-range pattern works in every Excel version and in LibreOffice. Put the formula beside the first data row, then double-click the fill handle. Absolute-relative mix is the whole trick: `$B$2` never moves; `B2` grows. An equivalent row-math form is `=N(C1)+B2` when C is the running-total column and C1 is a header (N turns text into 0) — useful when you want each row to add only the prior total plus this row’s amount. Tables (`=SUM(INDEX([Sales],1):[@Sales])`) keep the range correct as the table grows in modern Excel. Do not put `=SUM($B$2:$B$6)` on every row — that repeats the grand total. For a running total that resets each month, add a helper that checks the month and restarts the sum, or use SUMIFS with a “date ≤ this row and same month” pattern. SCAN in Excel 365 can spill a cumulative column in one formula, but the expanding SUM remains the most portable teaching pattern for mixed Excel / Sheets files.

**Prior total plus this row**

```excel
=N(C1)+B2
```

**Excel 365 SCAN spill**

```excel
=SCAN(0, B2:B6, LAMBDA(a,b, a+b))
```

**Grand total (not running — contrast)**

```excel
=SUM($B$2:$B$6)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=SUM($B$2:B2)
```

Excel fill-down with expanding SUM is the shared baseline; Excel 365 also has SCAN like Sheets.

<!--SIBLING-->


## Common errors and how to fix them

- **Every row shows the same grand total** — Both ends of the SUM were absolute (`$B$2:$B$6`) or the formula summed the whole column. **Fix:** Use `=SUM($B$2:B2)` so only the start stays locked.
- **Totals break after inserting a row at the top** — The locked start no longer points at the first amount. **Fix:** Point $ at the real first data cell again, or use a Table structured reference.
- **First running-total cell shows an error or wrong number** — The formula referenced a header without N(), or pointed one row too high. **Fix:** Start on the first amount row; use =N(C1)+B2 only when C1 is a text header.
- **Cumulative includes future rows** — The end reference was the full column (B:B) instead of the current row. **Fix:** Keep a relative end cell that matches the formula’s row.

## FAQ

### How is a running total different from a regular SUM?

SUM of the whole block repeats the same grand total on every row. A running total grows row by row so you can see progress through the period.

### Does this work inside an Excel Table?

Yes. Use a structured expanding reference such as =SUM(INDEX([Sales],1):[@Sales]) so new table rows keep the pattern.

### Can I reset the total each month?

Add a month helper column and restart when the month changes, or use SUMIFS with “date ≤ this row” and “same month” criteria.

### What about Google Sheets SCAN?

SCAN spills the whole cumulative column from one cell. Use it when everyone stays in Sheets or Excel 365; keep expanding SUM for maximum portability.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
