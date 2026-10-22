---
title: How to Calculate a Weighted Average in Excel
slug: weighted-average-excel
date: '2026-10-22'
summary: A weighted average gives some values more influence than others, like exams
  that count more than homework or prices weighted by quantity. Use SUMPRODUCT divided
  by SUM; Google Sheets also has AVERAGE.WEIGHTED.
tags:
- Financial & percentages
- Excel
keyword: weighted-average-excel
niche: sheets-formulas
provider: structured
entry_id: weighted-average
platform: Excel
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
- - percentage-change-excel
  - percentage-change-google-sheets
- - sumifs-excel
  - sumifs-google-sheets
- - maxifs-minifs-excel
  - maxifs-minifs-google-sheets
- - cagr-excel
  - cagr-google-sheets
sibling: weighted-average-google-sheets
---
A weighted average gives some values more influence than others, like exams that count more than homework or prices weighted by quantity. Use SUMPRODUCT divided by SUM; Google Sheets also has AVERAGE.WEIGHTED.

## Quick answer

Use this formula in Excel:

```excel
=SUMPRODUCT(B2:B5, C2:C5)/SUM(C2:C5)
```

SUMPRODUCT multiplies each score by its weight and adds the products; dividing by the sum of weights gives the weighted average.

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
=SUMPRODUCT(B2:B5, C2:C5)/SUM(C2:C5)
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

## Excel-specific notes

Dividing by SUM(C2:C5) means the weights do not have to add up to 100%: you can use 2, 3, 2, 3 or quantities instead of percentages. Excel has no dedicated weighted-average function, so SUMPRODUCT/SUM is the standard. For a weighted average with a condition, multiply in the condition: `=SUMPRODUCT((A2:A5="Final")*B2:B5*C2:C5)/SUMIFS(C2:C5, A2:A5, "Final")`.

**Plain average for comparison**

```excel
=AVERAGE(B2:B5)
```


## Google Sheets version

In Google Sheets, use:

```excel
=AVERAGE.WEIGHTED(B2:B5, C2:C5)
```

Google Sheets also has a built-in AVERAGE.WEIGHTED function that gives the same result.

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
