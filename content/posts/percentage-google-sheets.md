---
title: How to Calculate a Percentage in Google Sheets
slug: percentage-google-sheets
date: '2026-11-04'
summary: A percentage is part divided by total. Format the result as Percent, lock
  the total with $, and use (1+rate) or (1-rate) when you need to increase or decrease
  a number by a percent. This page covers share-of-total, "what percent is X of Y",
  and percent markups — not period over period change (see pe
tags:
- Financial & percentages
- Google Sheets
keyword: percentage-google-sheets
niche: sheets-formulas
provider: structured
entry_id: percentage
platform: Google Sheets
category: financial
faq:
- q: How is this different from percentage change?
  a: Percentage (this page) is part divided by total, or a markup on a single value.
    Percentage change compares two periods with (new-old)/old.
- q: Do I multiply by 100?
  a: Not when the cell uses Percentage format. Store 0.25 and let the format show
    25%.
- q: How do I show one decimal place in the percent?
  a: After applying Percent format, increase or decrease decimal places on the Home
    ribbon (Excel) or the toolbar (Sheets), for example 26.7%.
related:
- - percentage-change-google-sheets
  - percentage-change-excel
- - div0-error-google-sheets
  - div0-error-excel
- - weighted-average-google-sheets
  - weighted-average-excel
- - cagr-google-sheets
  - cagr-excel
sibling: percentage-excel
---
A percentage is part divided by total. Format the result as Percent, lock the total with $, and use (1+rate) or (1-rate) when you need to increase or decrease a number by a percent. This page covers share-of-total, "what percent is X of Y", and percent markups — not period over period change (see percentage-change).

## Quick answer

Use this formula in Google Sheets:

```excel
=B2/SUM($B$2:$B$5)
```

Same share-of-total formula in Google Sheets. Format with Format > Number > Percent, and keep $ on the total range when filling down.

## The problem

A budget sheet needs each category as a percent of the grand total, a score of 45 out of 180 as a percent, and a price increased by 10%. People multiply by 100 by hand, forget absolute references on the total, or confuse this with percentage change between two periods.

## Worked example

Four budget lines as a share of total, a score as a percent of max points, and a price increased then decreased by a stored rate.

| | A | B | C | D | E | F | G | H | I | J | K | L |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Category** | **Amount** | **Share of total** |  | **Score** | **Max** | **Score %** |  | **Price** | **Rate** | **After increase** | **After decrease** |
| 2 | Rent | 1200 | **26.6667%** |  |  |  |  |  |  |  |  |  |
| 3 | Payroll | 2500 | **55.5556%** |  |  |  |  |  |  |  |  |  |
| 4 | Software | 400 | **8.8889%** |  |  |  |  |  |  |  |  |  |
| 5 | Travel | 400 | **8.8889%** |  |  |  |  |  |  |  |  |  |
| 6 |  |  |  |  | 45 | 180 | **25%** |  |  |  |  |  |
| 7 |  |  |  |  |  |  |  |  | 200 | 10% | **220** | **180** |

Formulas used in the example (results shown in **bold** in the table above):

**C2 (filled to C5)** — share of total filled down

```excel
=B2/SUM($B$2:$B$5)
```

Results: **26.6667%**, **55.5556%**, **8.8889%**, **8.8889%**

**G6** — score as percent of max

```excel
=E6/F6
```

Result: **25%**

**K7** — price increased by rate

```excel
=I7*(1+J7)
```

Result: **220**

**L7** — price decreased by rate

```excel
=I7*(1-J7)
```

Result: **180**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Enter category amounts in column B and total them with SUM.
2. Type `=B2/SUM($B$2:$B$5)`, lock the total with $, format as Percent, and fill down.
3. For a score or quota, divide part by max with `=E6/F6` and format as Percent.
4. To apply a markup or discount, multiply by `(1+rate)` or `(1-rate)`.
5. Use IF around divisions when the total can be zero, and use percentage-change for period growth.

## Google Sheets-specific notes

Whole-column shares: `=ARRAYFORMULA(IF(B2:B5="", "", B2:B5/SUM($B$2:$B$5)))`. Sheets also offers `=TO_PERCENT(B2/SUM($B$2:$B$5))` to force percent formatting in the formula output, which helps when values are copied into documents. Increase and decrease patterns are identical: `=A2*(1+C2)` and `=A2*(1-C2)`. Locale changes the decimal and percent symbols on screen, not the underlying fraction. Prefer IF or IFERROR around divisions when totals can be empty. Keep this page for part/total and markups; use the percentage-change guide for period-over-period growth so reports do not mix the two meanings of "percent".

**Whole column share of total**

```excel
=ARRAYFORMULA(IF(B2:B5="", "", B2:B5/SUM($B$2:$B$5)))
```

**TO_PERCENT wrapper**

```excel
=TO_PERCENT(B2/SUM($B$2:$B$5))
```

**What percent is X of Y**

```excel
=A2/B2
```

**Increase by a percent**

```excel
=A2*(1+C2)
```


## Excel version

The same formula works unchanged in Excel:

```excel
=B2/SUM($B$2:$B$5)
```

Google Sheets uses the same part/total arithmetic. Format > Number > Percent, and TO_PERCENT can apply percent formatting inside the formula.

<!--SIBLING-->


## Common errors and how to fix them

- **Shares show 2667% or similar** — The formula multiplied by 100 and the cell was also formatted as Percent. **Fix:** Divide only; let Percentage format scale the display.
- **Every row divides by a different total after fill-down** — The SUM range was relative (B2:B5) without $ anchors. **Fix:** Write SUM($B$2:$B$5) so each row uses the same grand total.
- **#DIV/0!** — The total or denominator is 0 or blank. **Fix:** Guard with IF(total=0, 0, part/total) or see the div0-error guide.
- **Mixed up with percentage change** — Used (new-old)/old when the question was share of total, or the reverse. **Fix:** Part/total for this page; (new-old)/old on the percentage-change page.

## FAQ

### How is this different from percentage change?

Percentage (this page) is part divided by total, or a markup on a single value. Percentage change compares two periods with (new-old)/old.

### Do I multiply by 100?

Not when the cell uses Percentage format. Store 0.25 and let the format show 25%.

### How do I show one decimal place in the percent?

After applying Percent format, increase or decrease decimal places on the Home ribbon (Excel) or the toolbar (Sheets), for example 26.7%.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
