---
title: How to Use MEDIAN and MODE in Google Sheets
slug: median-mode-google-sheets
date: '2026-11-05'
summary: MEDIAN returns the middle value after sorting, so outliers hurt it less than
  AVERAGE. MODE (MODE.SNGL in modern Excel) returns the value that appears most often.
  Use both beside the mean when you describe a skewed score or price distribution.
tags:
- Financial & percentages
- Google Sheets
keyword: median-mode-google-sheets
niche: sheets-formulas
provider: structured
entry_id: median-mode
platform: Google Sheets
category: financial
faq:
- q: When should I use MEDIAN instead of AVERAGE?
  a: When outliers would pull the mean (income, house prices, a single failed exam).
    The median stays on the middle of the sorted list.
- q: What is the difference between MODE and MODE.SNGL?
  a: In current Excel they both return one most-frequent value. MODE.MULT returns
    every mode as a spill. Google Sheets only has MODE.
- q: What does MEDIAN do with an even number of values?
  a: 'It averages the two middle numbers after sorting. Example: MEDIAN of 1, 2, 3,
    4 is 2.5.'
- q: Can MEDIAN or MODE ignore zeros?
  a: Not automatically. Filter zeros with AVERAGEIF-style helpers, or use IF inside
    an array-capable median formula in Excel 365 / Sheets.
related:
- - average-google-sheets
  - average-excel
- - weighted-average-google-sheets
  - weighted-average-excel
- - rank-google-sheets
  - rank-excel
- - round-google-sheets
  - round-excel
sibling: median-mode-excel
---
MEDIAN returns the middle value after sorting, so outliers hurt it less than AVERAGE. MODE (MODE.SNGL in modern Excel) returns the value that appears most often. Use both beside the mean when you describe a skewed score or price distribution.

## Quick answer

Use this formula in Google Sheets:

```excel
=MEDIAN(B2:B8)
```

Same MEDIAN behaviour in Google Sheets. Use MODE for the most common numeric value.

## The problem

A class has many mid-80s scores and one very low outlier. The mean drops, stakeholders ask for the “typical” score, and nobody remembers whether to reach for MEDIAN or MODE — or how ties work when several values share the highest frequency.

## Worked example

Seven scores with a repeated 88. MEDIAN and MODE both land on 88 while AVERAGE is pulled by the low 64. A second even-sized list shows MEDIAN averaging the two central values.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Student** | **Score** |  | **Stat** | **Result** |
| 2 | Ava | 72 |  |  | **88** |
| 3 | Ben | 88 |  |  | **88** |
| 4 | Cara | 95 |  |  | **83.7142857142857** |
| 5 | Drew | 88 |  |  | **85** |
| 6 | Eve | 64 |  |  |  |
| 7 | Finn | 91 |  |  |  |
| 8 | Gia | 88 |  |  |  |
| 9 |  |  |  |  |  |
| 10 | Hana | 70 |  |  |  |
| 11 | Ian | 80 |  |  |  |
| 12 | Jade | 90 |  |  |  |
| 13 | Kai | 100 |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**E2** — median of class scores

```excel
=MEDIAN(B2:B8)
```

Result: **88**

**E3** — mode of class scores

```excel
=MODE(B2:B8)
```

Result: **88**

**E4** — average for comparison

```excel
=AVERAGE(B2:B8)
```

Result: **83.7142857142857**

**E5** — median of even-sized list (four scores)

```excel
=MEDIAN(B10:B13)
```

Result: **85**

<!--AD_IN_ARTICLE-->

## How the formula works

1. List the numeric sample in one column (scores, prices, ratings).
2. Type `=MEDIAN(B2:B8)` for the middle value after sorting.
3. Type `=MODE(B2:B8)` (or MODE.SNGL in modern Excel) for the most frequent value.
4. Place AVERAGE beside them so skew from outliers is visible.
5. If MODE returns

## Google Sheets-specific notes

Open-ended ranges work: `=MEDIAN(B2:B)` and `=MODE(B2:B)` grow with new rows while blanks stay ignored. Sheets has no MODE.SNGL or MODE.MULT; stick to MODE for the primary modal value, or build a FREQUENCY / QUERY helper if you need every tied mode listed. ARRAYFORMULA is unnecessary for a single median or mode summary cell. When sharing with Excel users, MEDIAN and MODE are portable; avoid Sheets-only QUERY wrappers if the file must round-trip. Put AVERAGE, MEDIAN, and MODE in neighbouring cells so a skewed class distribution is obvious at a glance. Locale decimal separators affect display only. If MODE returns #N/A, every value appears once — there is no repeated number to report as a mode.

**Most frequent value**

```excel
=MODE(B2:B8)
```

**Growing column median**

```excel
=MEDIAN(B2:B)
```

**Mean for comparison**

```excel
=AVERAGE(B2:B8)
```

**Trim extremes then average**

```excel
=TRIMMEAN(B2:B8, 0.2)
```


## Excel version

The same formula works unchanged in Excel:

```excel
=MEDIAN(B2:B8)
```

Google Sheets supports MEDIAN and MODE. It does not use MODE.SNGL / MODE.MULT names — MODE covers the single most-frequent value.

<!--SIBLING-->


## Common errors and how to fix them

- **#N/A from MODE** — No value repeats in the range. **Fix:** Expected when all values are unique; widen the sample or report “no mode”.
- **Median looks like an average of two scores** — The list has an even count, so MEDIAN averages the two central values. **Fix:** That is correct behaviour; add or remove a point if you need a single observed value.
- **Mode picks the “wrong” tied value** — Several numbers share the top frequency; MODE returns one of them (typically the first). **Fix:** Use MODE.MULT in Excel 365 to list every modal value, or inspect with COUNTIF.
- **Text or errors in the range** — Non-numeric cells mixed into the sample. **Fix:** Keep the range numeric-only, or clean with VALUE / IFERROR first.

## FAQ

### When should I use MEDIAN instead of AVERAGE?

When outliers would pull the mean (income, house prices, a single failed exam). The median stays on the middle of the sorted list.

### What is the difference between MODE and MODE.SNGL?

In current Excel they both return one most-frequent value. MODE.MULT returns every mode as a spill. Google Sheets only has MODE.

### What does MEDIAN do with an even number of values?

It averages the two middle numbers after sorting. Example: MEDIAN of 1, 2, 3, 4 is 2.5.

### Can MEDIAN or MODE ignore zeros?

Not automatically. Filter zeros with AVERAGEIF-style helpers, or use IF inside an array-capable median formula in Excel 365 / Sheets.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
