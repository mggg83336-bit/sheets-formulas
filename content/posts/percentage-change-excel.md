---
title: How to Calculate Percentage Change in Excel
slug: percentage-change-excel
date: '2026-10-22'
summary: Percentage change is (new - old) / old. This guide shows the formula, how
  to format the result as a percentage, how to handle a starting value of zero, and
  the common mix-up between percentage change and percentage points.
tags:
- Financial & percentages
- Excel
keyword: percentage-change-excel
niche: sheets-formulas
provider: structured
entry_id: percentage-change
platform: Excel
category: financial
faq:
- q: What is the difference between percentage change and percentage points?
  a: If a rate goes from 10% to 12%, it rose 2 percentage points, but the percentage
    change is (12-10)/10 = 20%.
- q: How do I calculate a percentage of a total instead?
  a: Divide the part by the total, e.g. =B2/SUM($B$2:$B$10), and lock the total with
    $.
- q: How do I apply a percentage increase to a number?
  a: 'Multiply by 1 plus the percentage: =B2*(1+10%) increases B2 by 10%, and =B2*(1-10%)
    decreases it by 10%. Note that a 10% increase followed by a 10% decrease does
    not return to the original value.'
- q: How do I calculate the change between two percentages?
  a: Subtract them for the change in percentage points (=C2-B2 shows 12% - 10% = 2%),
    or use the same (new-old)/old formula for the relative change (20%). Say which
    one you mean in reports, because both are often called "percent change".
related:
- - cagr-excel
  - cagr-google-sheets
- - compound-interest-excel
  - compound-interest-google-sheets
- - div0-error-excel
  - div0-error-google-sheets
- - weighted-average-excel
  - weighted-average-google-sheets
sibling: percentage-change-google-sheets
---
Percentage change is (new - old) / old. This guide shows the formula, how to format the result as a percentage, how to handle a starting value of zero, and the common mix-up between percentage change and percentage points.

## Quick answer

Use this formula in Excel:

```excel
=(C2-B2)/B2
```

Subtract the old value from the new one and divide by the old value. Format the cell as a percentage (Ctrl+Shift+%).

## The problem

You have last year's and this year's sales per product and want the growth or decline in percent.

## Worked example

Sales per product in two years. Results are formatted as percentages.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Product** | **2025** | **2026** | **Change** | **Safe change** |
| 2 | Mice | 1200 | 1500 | **25%** | **25%** |
| 3 | Hubs | 800 | 680 | **-15%** | **-15%** |
| 4 | Stands | 0 | 150 | **#DIV/0!** | **n/a** |

Formulas used in the example (results shown in **bold** in the table above):

**D2 (filled to D4)** — filled down

```excel
=(C2-B2)/B2
```

Results: **25%**, **-15%**, **#DIV/0!**

**E2 (filled to E4)** — filled down

```excel
=IF(B2=0, "n/a", (C2-B2)/B2)
```

Results: **25%**, **-15%**, **n/a**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `C2-B2` is the absolute change: 1500 - 1200 = 300.
2. Dividing by the old value gives the relative change: 300 / 1200 = 0.25.
3. Formatting 0.25 as a percentage shows 25%. Negative results are declines (Hubs fell 15%).
4. When the old value is 0 (Stands), there is no meaningful percentage, so the safe version shows "n/a".

## Excel-specific notes

The parentheses matter: =C2-B2/B2 divides first and gives a wrong answer. The equivalent form `=C2/B2-1` is shorter. When the old value is 0 the change is mathematically undefined, so handle it explicitly instead of letting #DIV/0! appear in a report. For a percentage that should always be shown with a sign, use a custom format such as +0.0%;-0.0%;0.0%.

**Shorter equivalent**

```excel
=C2/B2-1
```

**Handle a zero starting value**

```excel
=IF(B2=0, "n/a", (C2-B2)/B2)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=(C2-B2)/B2
```

The same formula works in Google Sheets (format with Format > Number > Percent).

<!--SIBLING-->


## Common errors and how to fix them

- **#DIV/0!** — The old value is 0 or empty. **Fix:** Test it with IF(B2=0, ..., ...).
- **Result like 2500%** — The result was multiplied by 100 and then formatted as a percentage. **Fix:** Do not multiply by 100 when using percentage formatting.
- **Wrong result** — Missing parentheses, e.g. =C2-B2/B2. **Fix:** Write =(C2-B2)/B2.

## FAQ

### What is the difference between percentage change and percentage points?

If a rate goes from 10% to 12%, it rose 2 percentage points, but the percentage change is (12-10)/10 = 20%.

### How do I calculate a percentage of a total instead?

Divide the part by the total, e.g. =B2/SUM($B$2:$B$10), and lock the total with $.

### How do I apply a percentage increase to a number?

Multiply by 1 plus the percentage: =B2*(1+10%) increases B2 by 10%, and =B2*(1-10%) decreases it by 10%. Note that a 10% increase followed by a 10% decrease does not return to the original value.

### How do I calculate the change between two percentages?

Subtract them for the change in percentage points (=C2-B2 shows 12% - 10% = 2%), or use the same (new-old)/old formula for the relative change (20%). Say which one you mean in reports, because both are often called "percent change".

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
