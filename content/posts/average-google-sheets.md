---
title: How to Calculate an Average in Google Sheets
slug: average-google-sheets
date: '2026-11-05'
summary: AVERAGE returns the arithmetic mean of numbers and skips blank cells and
  text. Pair it with AVERAGEIF or AVERAGEIFS when you need a mean for one region,
  status, or threshold, and use IF to ignore zeros when a blank should stay blank
  instead of counting as zero.
tags:
- Financial & percentages
- Google Sheets
keyword: average-google-sheets
niche: sheets-formulas
provider: structured
entry_id: average
platform: Google Sheets
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
- - weighted-average-google-sheets
  - weighted-average-excel
- - averageif-google-sheets
  - averageif-excel
- - median-mode-google-sheets
  - median-mode-excel
- - round-google-sheets
  - round-excel
- - percentage-google-sheets
  - percentage-excel
sibling: average-excel
---
AVERAGE returns the arithmetic mean of numbers and skips blank cells and text. Pair it with AVERAGEIF or AVERAGEIFS when you need a mean for one region, status, or threshold, and use IF to ignore zeros when a blank should stay blank instead of counting as zero.

## Quick answer

Use this formula in Google Sheets:

```excel
=AVERAGE(B2:B8)
```

Same AVERAGE syntax in Google Sheets. Blank cells and text inside the range are skipped.

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

## Google Sheets-specific notes

Whole-column mean that expands as rows are added: `=AVERAGE(B2:B)` — trailing blanks stay ignored. Conditional means use the same AVERAGEIF / AVERAGEIFS signatures as Excel. Wrap a growing column with `=ARRAYFORMULA(IF(B2:B="", "", AVERAGEIF(...)))` only when you need a per-row helper, not for a single class mean. Sheets treats typed TRUE/FALSE inside ranges like Excel (ignored in AVERAGE). Locale settings change decimal commas on screen, not the mean itself. Prefer AVERAGEIF `"<>0"` over deleting zeros when a zero means “not yet scored”. When the file must open in Excel, avoid Sheets-only helpers and stick to AVERAGE / AVERAGEIF / AVERAGEIFS. For weights that differ by assessment, switch to AVERAGE.WEIGHTED or SUMPRODUCT/SUM on the weighted-average page instead of forcing a plain AVERAGE.

**Growing column average**

```excel
=AVERAGE(B2:B)
```

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


## Excel version

The same formula works unchanged in Excel:

```excel
=AVERAGE(B2:B8)
```

Google Sheets supports the same AVERAGE, AVERAGEIF, and AVERAGEIFS functions. Use ARRAYFORMULA when you want a column of per-row rolling means.

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
