---
title: How to Calculate an Average in Excel
slug: average-excel
date: '2026-11-05'
summary: AVERAGE returns the arithmetic mean of numbers and skips blank cells and
  text. Pair it with AVERAGEIF or AVERAGEIFS when you need a mean for one region,
  status, or threshold, and use IF to ignore zeros when a blank should stay blank
  instead of counting as zero.
tags:
- Financial & percentages
- Excel
keyword: average-excel
niche: sheets-formulas
provider: structured
entry_id: average
platform: Excel
category: financial
faq:
- q: Does AVERAGE ignore blank cells?
  a: Yes. Blanks and text in the range are skipped. A typed 0 is a number and is included.
- q: How do I average only values above a threshold?
  a: Use =AVERAGEIF(range, ">80") or AVERAGEIFS with extra conditions on other columns.
- q: When should I use a weighted average instead?
  a: When inputs have different importance (exam weights, quantity-weighted price).
    See the weighted-average guide.
- q: Can I average a filtered list only?
  a: Yes. Use =SUBTOTAL(1, B2:B8) (or 101 to ignore hidden rows) so filtered-out rows
    drop out of the mean.
related:
- - weighted-average-excel
  - weighted-average-google-sheets
- - averageif-excel
  - averageif-google-sheets
- - median-mode-excel
  - median-mode-google-sheets
- - round-excel
  - round-google-sheets
- - percentage-excel
  - percentage-google-sheets
sibling: average-google-sheets
---
AVERAGE returns the arithmetic mean of numbers and skips blank cells and text. Pair it with AVERAGEIF or AVERAGEIFS when you need a mean for one region, status, or threshold, and use IF to ignore zeros when a blank should stay blank instead of counting as zero.

## Quick answer

Use this formula in Excel:

```excel
=AVERAGE(B2:B8)
```

Syntax: `AVERAGE(number1, [number2], …)`. Pass a range or individual numbers. Blank cells and text are ignored; logical values typed directly are counted, but logicals inside a cell range are ignored.

## The problem

A score sheet needs the class mean, the mean of scores above 80, and the East-region mean. People use SUM/COUNT by hand, forget that zeros pull the average down, or mix AVERAGE with a weighted average when some assessments count more than others.

## Worked example

Seven student scores with a region column. Checks cover the class mean, the mean above 80, the East-only mean, and how a typed zero changes the result versus a blank.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Region** | **Score** |  | **Metric** | **Value** |
| 2 | East | 72 |  |  | **83.7142857142857** |
| 3 | West | 88 |  |  | **90** |
| 4 | East | 95 |  |  | **85.75** |
| 5 | East | 88 |  |  | **73.25** |
| 6 | West | 64 |  |  |  |
| 7 | West | 91 |  |  |  |
| 8 | East | 88 |  |  |  |
| 9 |  | 0 |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**E2** — class average (B2:B8)

```excel
=AVERAGE(B2:B8)
```

Result: **83.7142857142857**

**E3** — average of scores above 80

```excel
=AVERAGEIF(B2:B8, ">80")
```

Result: **90**

**E4** — East region average

```excel
=AVERAGEIF(A2:A8, "East", B2:B8)
```

Result: **85.75**

**E5** — average including the typed zero in B9

```excel
=AVERAGE(B2:B9)
```

Result: **73.25**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Enter the numbers to average in a single column (and optional criteria columns beside them).
2. Type `=AVERAGE(B2:B8)` for the plain mean; blanks and text are skipped automatically.
3. Add `=AVERAGEIF(B2:B8, ">80")` or `=AVERAGEIF(A2:A8, "East", B2:B8)` for conditional means.
4. Clear cells instead of typing 0 when a value is missing, or use AVERAGEIF `"<>0"` to skip zeros.
5. Use the weighted-average page when some inputs must count more than others.

## Excel-specific notes

AVERAGE is the plain arithmetic mean. Empty cells do not shrink the denominator, but a typed 0 does — clear the cell if the student was absent rather than scoring zero. For a conditional mean use `=AVERAGEIF(A2:A8, "East", B2:B8)` or `=AVERAGEIF(B2:B8, ">80")` when the criteria sit on the same range as the values. AVERAGEIFS handles multiple conditions (`=AVERAGEIFS(B2:B8, A2:A8, "East", B2:B8, ">80")`). To ignore zeros without deleting them, use `=AVERAGEIF(B2:B8, "<>0")` or an array-style `=AVERAGE(IF(B2:B8<>0, B2:B8))` entered normally in Excel 365. Do not confuse this with a weighted average — when homework and exams have different weights, use SUMPRODUCT/SUM (see weighted-average). ROUND the result only when reporting requires a fixed number of decimals.

**Mean of values above 80**

```excel
=AVERAGEIF(B2:B8, ">80")
```

**Mean for one region**

```excel
=AVERAGEIF(A2:A8, "East", B2:B8)
```

**Ignore zeros**

```excel
=AVERAGEIF(B2:B8, "<>0")
```

**Mean of numbers only via SUBTOTAL on a filtered list**

```excel
=SUBTOTAL(1, B2:B8)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=AVERAGE(B2:B8)
```

Excel uses the same AVERAGE family; fill down or use Excel 365 dynamic arrays instead of open-ended B2:B ranges when you need per-row helpers.

<!--SIBLING-->


## Common errors and how to fix them

- **Average looks too low** — Zeros for missing scores were typed into the range, so they count in the denominator. **Fix:** Clear the cells, or use =AVERAGEIF(range, "<>0").
- **#DIV/0!** — The range has no numeric values (all blank/text), or AVERAGEIF matched nothing. **Fix:** Confirm the criteria and that at least one number is present.
- **Conditional average includes the wrong rows** — Criteria range and average range are misaligned or different heights. **Fix:** Use matching row spans in AVERAGEIF / AVERAGEIFS.
- **Result differs from a hand SUM/COUNT** — COUNT counted text or blanks differently than AVERAGE's skip rules. **Fix:** Prefer AVERAGE itself; or use COUNT on the same numeric range only.

## FAQ

### Does AVERAGE ignore blank cells?

Yes. Blanks and text in the range are skipped. A typed 0 is a number and is included.

### How do I average only values above a threshold?

Use =AVERAGEIF(range, ">80") or AVERAGEIFS with extra conditions on other columns.

### When should I use a weighted average instead?

When inputs have different importance (exam weights, quantity-weighted price). See the weighted-average guide.

### Can I average a filtered list only?

Yes. Use =SUBTOTAL(1, B2:B8) (or 101 to ignore hidden rows) so filtered-out rows drop out of the mean.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
