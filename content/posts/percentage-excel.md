---
title: How to Calculate a Percentage in Excel
slug: percentage-excel
date: '2026-11-04'
summary: A percentage is part divided by total. Format the result as Percent, lock
  the total with $, and use (1+rate) or (1-rate) when you need to increase or decrease
  a number by a percent. This page covers share-of-total, "what percent is X of Y",
  and percent markups — not period over period change (see pe
tags:
- Financial & percentages
- Excel
keyword: percentage-excel
niche: sheets-formulas
provider: structured
entry_id: percentage
platform: Excel
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
- - percentage-change-excel
  - percentage-change-google-sheets
- - div0-error-excel
  - div0-error-google-sheets
- - weighted-average-excel
  - weighted-average-google-sheets
- - cagr-excel
  - cagr-google-sheets
sibling: percentage-google-sheets
---
A percentage is part divided by total. Format the result as Percent, lock the total with $, and use (1+rate) or (1-rate) when you need to increase or decrease a number by a percent. This page covers share-of-total, "what percent is X of Y", and percent markups — not period over period change (see percentage-change).

## Quick answer

Use this formula in Excel:

```excel
=B2/SUM($B$2:$B$5)
```

Divide the part (B2) by the locked total. Format the cell as a percentage (Ctrl+Shift+%). The $ anchors keep every row dividing by the same grand total when you fill down.

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

## Excel-specific notes

Do not multiply by 100 when the cell uses Percentage format — Excel already shows 0.25 as 25%. For "what percent is X of Y" use `=A2/B2` with Y nonzero. To increase a value by a percent, multiply by one plus the rate: `=A2*(1+10%)` or `=A2*(1+C2)` when C2 holds 10%. To decrease, use `=A2*(1-10%)`. Percentage formatting is display only; the stored value remains a fraction. When the total can be blank or zero, wrap with IF to avoid #DIV/0! (see the div0-error guide). For growth or decline between two periods, use the percentage-change page instead — that is (new-old)/old, not part/total.

**What percent is X of Y**

```excel
=A2/B2
```

**Increase by a percent**

```excel
=A2*(1+C2)
```

**Decrease by a percent**

```excel
=A2*(1-C2)
```

**Safe share of total**

```excel
=IF(SUM($B$2:$B$5)=0, 0, B2/SUM($B$2:$B$5))
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=B2/SUM($B$2:$B$5)
```

Excel uses the same formulas; fill down instead of ARRAYFORMULA, and use Ctrl+Shift+% or a Percent format instead of TO_PERCENT.

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
