---
title: How to Calculate a Weighted Average in Google Sheets
slug: weighted-average-google-sheets
date: '2026-10-26'
summary: A weighted average gives some values more influence than others, like exams
  that count more than homework or prices weighted by quantity. Use SUMPRODUCT divided
  by SUM; Google Sheets also has AVERAGE.WEIGHTED.
tags:
- Financial & percentages
- Google Sheets
keyword: weighted-average-google-sheets
niche: sheets-formulas
provider: structured
entry_id: weighted-average
platform: Google Sheets
category: financial
faq:
- q: Do the weights have to add up to 100%?
  a: No, as long as you divide by their sum. The result is the same.
- q: How do I calculate a weighted average price?
  a: Use quantities as weights, e.g. =SUMPRODUCT(price, qty)/SUM(qty).
- q: How do I handle a missing score?
  a: 'Leave the score cell empty and exclude its weight from the denominator: =SUMPRODUCT(B2:B5,
    C2:C5)/SUMIFS(C2:C5, B2:B5, "<>"). Otherwise the empty score counts as 0 and drags
    the average down.'
- q: Can SUMPRODUCT weight by a condition?
  a: Yes. Multiply in a test, e.g. =SUMPRODUCT((A2:A5<>"Homework")*B2:B5*C2:C5)/SUMIFS(C2:C5,
    A2:A5, "<>Homework") averages everything except homework with the remaining weights.
related:
- - percentage-change-google-sheets
  - percentage-change-excel
- - sumifs-google-sheets
  - sumifs-excel
- - maxifs-minifs-google-sheets
  - maxifs-minifs-excel
- - cagr-google-sheets
  - cagr-excel
sibling: weighted-average-excel
---
A weighted average gives some values more influence than others, like exams that count more than homework or prices weighted by quantity. Use SUMPRODUCT divided by SUM; Google Sheets also has AVERAGE.WEIGHTED.

## Quick answer

Use this formula in Google Sheets:

```excel
=AVERAGE.WEIGHTED(B2:B5, C2:C5)
```

Syntax: `AVERAGE.WEIGHTED(values, weights, [additional values, additional weights])`.

## The problem

A course grade is made of homework (20%), midterm (30%), project (20%) and final (30%). A plain average of the four scores would treat them all as equally important.

## Worked example

Scores and their weights.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Assessment** | **Score** | **Weight** |  | **Result** |
| 2 | Homework | 92 | 20% |  | **84.6** |
| 3 | Midterm | 78 | 30% |  | **85.5** |
| 4 | Project | 88 | 20% |  |  |
| 5 | Final | 84 | 30% |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**E2** — weighted average

```excel
=AVERAGE.WEIGHTED(B2:B5, C2:C5)
```

Result: **84.6**

**E3** — plain average (ignores weights)

```excel
=AVERAGE(B2:B5)
```

Result: **85.5**

<!--AD_IN_ARTICLE-->

## How the formula works

1. SUMPRODUCT multiplies row by row: 92 x 20% + 78 x 30% + 88 x 20% + 84 x 30% = 18.4 + 23.4 + 17.6 + 25.2 = 84.6.
2. SUM(C2:C5) is 100%, so the division leaves 84.6.
3. The plain average is 85.5 because it lets the weak midterm count as much as the homework.
4. If the weights were 2, 3, 2, 3 instead of percentages, the division by their sum (10) would give the same 84.6.

## Google Sheets-specific notes

Google Sheets has a built-in AVERAGE.WEIGHTED function, which is easier to read than SUMPRODUCT and divides by the sum of weights automatically. It requires the values and weights ranges to be the same size and the weights to be non-negative. The SUMPRODUCT/SUM formula also works in Sheets and is the better choice if the file will be opened in Excel, where AVERAGE.WEIGHTED does not exist.

**Excel-compatible version**

```excel
=SUMPRODUCT(B2:B5, C2:C5)/SUM(C2:C5)
```


## Excel version

In Excel, use:

```excel
=SUMPRODUCT(B2:B5, C2:C5)/SUM(C2:C5)
```

Excel has no AVERAGE.WEIGHTED function, so SUMPRODUCT divided by SUM is the standard there.

<!--SIBLING-->


## Common errors and how to fix them

- **Result far too large** — The formula was not divided by the sum of weights, and the weights do not add up to 1. **Fix:** Always divide by SUM(weights).
- **#VALUE!** — The two ranges have different sizes. **Fix:** Use ranges covering the same rows.
- **#NAME? in Excel** — AVERAGE.WEIGHTED is Google Sheets only. **Fix:** Use SUMPRODUCT/SUM.

## FAQ

### Do the weights have to add up to 100%?

No, as long as you divide by their sum. The result is the same.

### How do I calculate a weighted average price?

Use quantities as weights, e.g. =SUMPRODUCT(price, qty)/SUM(qty).

### How do I handle a missing score?

Leave the score cell empty and exclude its weight from the denominator: =SUMPRODUCT(B2:B5, C2:C5)/SUMIFS(C2:C5, B2:B5, "<>"). Otherwise the empty score counts as 0 and drags the average down.

### Can SUMPRODUCT weight by a condition?

Yes. Multiply in a test, e.g. =SUMPRODUCT((A2:A5<>"Homework")*B2:B5*C2:C5)/SUMIFS(C2:C5, A2:A5, "<>Homework") averages everything except homework with the remaining weights.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
