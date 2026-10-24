---
title: How to Use AVERAGEIF in Google Sheets
slug: averageif-google-sheets
date: '2026-10-24'
summary: 'AVERAGEIF returns the average of the numbers that meet one condition, such
  as the average sale in one region or the average of all values above a threshold.
  This page walks through four worked examples, explains how blanks and zeros are
  treated, and shows how to stop the #DIV/0! error when nothing m'
tags:
- Conditional sums & counts
- Google Sheets
keyword: averageif-google-sheets
niche: sheets-formulas
provider: structured
entry_id: averageif
platform: Google Sheets
category: conditional
faq:
- q: What is the difference between AVERAGEIF and AVERAGEIFS?
  a: AVERAGEIF takes one condition and puts the average range last; AVERAGEIFS takes
    one or more conditions and puts the average range first.
- q: Does AVERAGEIF ignore blank cells?
  a: Yes, blank cells in the average range are skipped, but cells containing 0 are
    counted.
- q: How do I average values between two numbers?
  a: Use AVERAGEIFS with the same column twice, e.g. =AVERAGEIFS(C2:C7, C2:C7, ">=400",
    C2:C7, "<=1000").
related:
- - sumif-google-sheets
  - sumif-excel
- - countif-google-sheets
  - countif-excel
- - sumifs-google-sheets
  - sumifs-excel
- - weighted-average-google-sheets
  - weighted-average-excel
- - div0-error-google-sheets
  - div0-error-excel
sibling: averageif-excel
---
AVERAGEIF returns the average of the numbers that meet one condition, such as the average sale in one region or the average of all values above a threshold. This page walks through four worked examples, explains how blanks and zeros are treated, and shows how to stop the #DIV/0! error when nothing matches.

## Quick answer

Use this formula in Google Sheets:

```excel
=AVERAGEIF(A2:A7, E2, C2:C7)
```

Same syntax in Google Sheets: `AVERAGEIF(criteria_range, criterion, [average_range])`.

## The problem

Your sales list has a Region and an amount for every deal. You want the average deal size per region, the average of large deals only, and a safe result for regions that have no deals yet, without filtering the list or building a helper column.

## Worked example

Six deals in three regions; there are no deals in South yet.

| | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 1 | **Region** | **Rep** | **Sales** |  | **Criteria** | **Average** |
| 2 | East | Kim | 1200 |  | East | **700** |
| 3 | West | Ruiz | 950 |  | >500 | **905** |
| 4 | East | Patel | 300 |  | <>East | **743.33** |
| 5 | North | Lee | 870 |  | South | **0** |
| 6 | West | Diaz | 410 |  |  |  |
| 7 | East | Cho | 600 |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**F2** — average for the region in E2

```excel
=AVERAGEIF(A2:A7, E2, C2:C7)
```

Result: **700**

**F3** — average of deals over 500 (no average_range needed)

```excel
=AVERAGEIF(C2:C7, ">500")
```

Result: **905**

**F4** — every region except East, rounded to 2 decimals

```excel
=ROUND(AVERAGEIF(A2:A7, "<>East", C2:C7), 2)
```

Result: **743.33**

**F5** — no matching rows, so IFERROR returns 0

```excel
=IFERROR(AVERAGEIF(A2:A7, E5, C2:C7), 0)
```

Result: **0**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `A2:A7` is the range tested against the condition; here, the Region column.
2. `E2` holds the condition, East. It could also be typed directly as `"East"`, or be an operator such as `">500"`.
3. `C2:C7` is the range to average. Only rows where the region is East are used: (1200 + 300 + 600) / 3 = 700.
4. When the tested range and the numbers are the same column, leave the third argument out: `=AVERAGEIF(C2:C7, ">500")` averages 1200, 950, 870 and 600 to get 905.
5. `"<>East"` averages every other region: (950 + 870 + 410) / 3 = 743.333…, which ROUND turns into 743.33.
6. South has no deals, so AVERAGEIF would return #DIV/0!. IFERROR replaces it with 0.

## Google Sheets-specific notes

AVERAGEIF works the same way in Google Sheets, including wildcards and the #DIV/0! result when nothing matches. If you need the average for every region at once, a single QUERY builds the whole summary table and adds new regions automatically: `=QUERY(A2:C7, "select A, avg(C) group by A label avg(C) 'Average'", 0)`. For conditions that criteria strings cannot express, average a FILTER result instead, for example `=AVERAGE(FILTER(C2:C7, REGEXMATCH(A2:A7, "^(East|West)$")))`.

**Average for every region in one formula**

```excel
=QUERY(A2:C7, "select A, avg(C) group by A label avg(C) 'Average'", 0)
```

**Average with a regular-expression condition**

```excel
=AVERAGE(FILTER(C2:C7, REGEXMATCH(A2:A7, "^(East|West)$")))
```


## Excel version

The same formula works unchanged in Excel:

```excel
=AVERAGEIF(A2:A7, E2, C2:C7)
```

Excel uses the identical syntax and the same handling of blanks, zeros and #DIV/0!.

<!--SIBLING-->


## Common errors and how to fix them

- **#DIV/0!** — No cell meets the condition, or every matching cell in the average range is blank or text. **Fix:** Check the criterion for typos and extra spaces, then wrap the formula in IFERROR, e.g. =IFERROR(AVERAGEIF(...), 0).
- **Average is too low** — Zeros were entered for missing values, and zeros are included in the average while blanks are not. **Fix:** Leave missing values blank, or exclude zeros with AVERAGEIFS, e.g. =AVERAGEIFS(C2:C7, A2:A7, "East", C2:C7, "<>0").
- **Wrong average** — The average range has a different size or starts on a different row than the criteria range. **Fix:** Make both ranges cover the same rows, such as A2:A7 and C2:C7.

## FAQ

### What is the difference between AVERAGEIF and AVERAGEIFS?

AVERAGEIF takes one condition and puts the average range last; AVERAGEIFS takes one or more conditions and puts the average range first.

### Does AVERAGEIF ignore blank cells?

Yes, blank cells in the average range are skipped, but cells containing 0 are counted.

### How do I average values between two numbers?

Use AVERAGEIFS with the same column twice, e.g. =AVERAGEIFS(C2:C7, C2:C7, ">=400", C2:C7, "<=1000").

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
