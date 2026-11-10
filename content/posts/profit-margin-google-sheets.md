---
title: How to Calculate Profit Margin in Google Sheets
slug: profit-margin-google-sheets
date: '2026-11-10'
summary: Profit margin is profit divided by revenue, shown as a percentage. Gross
  margin uses revenue minus cost of goods sold; net margin also subtracts operating
  expenses. Markup is a different ratio — profit divided by cost, not by revenue —
  and will look larger than the matching margin on the same number
tags:
- Financial & percentages
- Google Sheets
keyword: profit-margin-google-sheets
niche: sheets-formulas
provider: structured
entry_id: profit-margin
platform: Google Sheets
category: financial
faq:
- q: What is the difference between gross margin and net margin?
  a: Gross margin only subtracts the cost of goods sold from revenue. Net margin also
    subtracts operating expenses (and, in a fuller income statement, other costs).
    Net margin is always equal to or lower than gross margin on the same numbers.
- q: Is markup the same as profit margin?
  a: No. Markup divides profit by cost; margin divides profit by revenue. On this
    example the gross margin is 35% and the markup is about 53.85%. Convert with markup
    = margin / (1 − margin), or margin = markup / (1 + markup).
- q: Should I average product margins to get a company margin?
  a: Not if the products have different revenue. Compute total profit ÷ total revenue
    (a weighted result). A simple average of row margins overstates small lines and
    understates large ones.
- q: How should I format the results?
  a: Format profit cells as currency and margin or markup cells as percentages. Keep
    full precision in the cells that feed other formulas; rounding belongs in a display
    column or in a figure you have agreed to freeze.
related:
- - percentage-google-sheets
  - percentage-excel
- - percentage-change-google-sheets
  - percentage-change-excel
- - average-google-sheets
  - average-excel
- - cagr-google-sheets
  - cagr-excel
sibling: profit-margin-excel
---
Profit margin is profit divided by revenue, shown as a percentage. Gross margin uses revenue minus cost of goods sold; net margin also subtracts operating expenses. Markup is a different ratio — profit divided by cost, not by revenue — and will look larger than the matching margin on the same numbers. Worked example included.

## Quick answer

Use this formula in Google Sheets:

```excel
=(B2-B3)/B2
```

Same gross-margin formula in Google Sheets. Format the result with Format > Number > Percent. Net margin and markup use the same ratios as in Excel.

## The problem

A product line brought in 80,000 of revenue, with 52,000 of cost of goods sold and 14,000 of operating expenses. You want gross profit, gross margin, net profit, net margin, and the markup on cost, all from the same inputs, formatted as currency or percentages.

## Worked example

One product line: 80,000 revenue, 52,000 COGS, 14,000 operating expenses. Helper cells compute gross and net profit; the margin and markup rows are formatted as percentages.

| | A | B |
|---|---|---|
| 1 | **Item** | **Amount** |
| 2 | Revenue | 80000 |
| 3 | COGS | 52000 |
| 4 | Operating expenses | 14000 |
| 5 | Gross profit | **28,000** |
| 6 | Gross margin | **35%** |
| 7 | Net profit | **14,000** |
| 8 | Net margin | **17.5%** |
| 9 | Markup | **53.85%** |

Formulas used in the example (results shown in **bold** in the table above):

**B5** — gross profit

```excel
=B2-B3
```

Result: **28,000**

**B6** — gross margin

```excel
=B5/B2
```

Result: **35%**

**B7** — net profit

```excel
=B5-B4
```

Result: **14,000**

**B8** — net margin

```excel
=B7/B2
```

Result: **17.5%**

**B9** — markup on cost

```excel
=B5/B3
```

Result: **53.85%**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Gross profit is revenue minus COGS: 80,000 − 52,000 = 28,000 (`=B2-B3`).
2. Gross margin divides that profit by revenue: 28,000 / 80,000 = 35% (`=B5/B2`). Format as a percentage.
3. Net profit subtracts operating expenses from gross profit: 28,000 − 14,000 = 14,000 (`=B5-B4`).
4. Net margin is net profit ÷ revenue: 14,000 / 80,000 = 17.5% (`=B7/B2`).
5. Markup uses cost in the denominator, not revenue: 28,000 / 52,000 ≈ 53.85% (`=B5/B3`). That is not the same figure as gross margin.

## Google Sheets-specific notes

To compute a margin column down a product list, use `=ARRAYFORMULA(IF(B2:B="",, (B2:B-C2:C)/B2:B))` so each new revenue/COGS row fills in without a manual fill-down. `=TO_PERCENT(B5/B2)` applies percent formatting as part of the formula, which is handy when the value is copied into a dashboard; Format > Number > Percent does the same thing at the cell level and stays more Excel-compatible. Prefer closed ranges, or be deliberate with open-ended ones (`B2:B`): a total row or a stray zero at the bottom will flow into an ARRAYFORMULA and can show a nonsense margin. QUERY is a good way to roll up revenue and cost by product or category first (`=QUERY(A1:C, "select A, sum(B), sum(C) where A is not null group by A", 1)`), then compute margin on the totals — do not average already-computed row margins if the products are different sizes. Locale settings change decimal and argument separators, not the ratio. If the workbook must open in Excel, avoid TO_PERCENT, ARRAYFORMULA and QUERY; the plain `(revenue-COGS)/revenue` formula travels cleanly.

**Margin column for a growing product list**

```excel
=ARRAYFORMULA(IF(B2:B="",, (B2:B-C2:C)/B2:B))
```

**TO_PERCENT wrapper**

```excel
=TO_PERCENT(B5/B2)
```

**Net margin**

```excel
=(B2-B3-B4)/B2
```

**Markup on cost**

```excel
=(B2-B3)/B3
```


## Excel version

The same formula works unchanged in Excel:

```excel
=(B2-B3)/B2
```

Google Sheets uses the same arithmetic. Format with Format > Number > Percent, or wrap the result in TO_PERCENT if you want the formula itself to apply the percent format.

<!--SIBLING-->


## Common errors and how to fix them

- **Result like 3500%** — The ratio was multiplied by 100 and then formatted as a percentage. **Fix:** Use `=(B2-B3)/B2` and format as Percent. Do not multiply by 100.
- **#DIV/0!** — Revenue (for margin) or COGS (for markup) is 0 or blank. **Fix:** Guard with IF, e.g. `=IF(B2=0, "n/a", (B2-B3)/B2)`.
- **Margin and markup are used interchangeably** — Profit was divided by cost when a margin was requested, or by revenue when a markup was requested. **Fix:** Margin = profit / revenue; markup = profit / cost. Label the cell so the denominator is obvious.
- **Net margin looks too high** — Operating expenses were left out, so the figure is actually gross margin, or a cost was subtracted twice. **Fix:** Net margin uses revenue − COGS − operating expenses, all over revenue. Check the helper cells first.

## FAQ

### What is the difference between gross margin and net margin?

Gross margin only subtracts the cost of goods sold from revenue. Net margin also subtracts operating expenses (and, in a fuller income statement, other costs). Net margin is always equal to or lower than gross margin on the same numbers.

### Is markup the same as profit margin?

No. Markup divides profit by cost; margin divides profit by revenue. On this example the gross margin is 35% and the markup is about 53.85%. Convert with markup = margin / (1 − margin), or margin = markup / (1 + markup).

### Should I average product margins to get a company margin?

Not if the products have different revenue. Compute total profit ÷ total revenue (a weighted result). A simple average of row margins overstates small lines and understates large ones.

### How should I format the results?

Format profit cells as currency and margin or markup cells as percentages. Keep full precision in the cells that feed other formulas; rounding belongs in a display column or in a figure you have agreed to freeze.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
