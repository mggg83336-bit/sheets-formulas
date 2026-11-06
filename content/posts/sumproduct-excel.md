---
title: How to Use SUMPRODUCT in Excel
slug: sumproduct-excel
date: '2026-11-06'
summary: SUMPRODUCT multiplies aligned arrays and adds the products. Use it for weighted
  totals (quantity × price) and for conditional sums with boolean tests — a portable
  pattern that works when SUMIFS is awkward or you need several conditions expressed
  as array logic.
tags:
- Conditional sums & counts
- Excel
keyword: sumproduct-excel
niche: sheets-formulas
provider: structured
entry_id: sumproduct
platform: Excel
category: conditional
faq:
- q: When should I use SUMPRODUCT instead of SUMIFS?
  a: Use SUMIFS for ordinary conditional sums on large data. Use SUMPRODUCT when you
    need to multiply columns (weighted totals) or express OR / array logic that SUMIFS
    cannot.
- q: Why multiply by (Region="East")?
  a: The comparison returns TRUE/FALSE. Multiplying coerces TRUE to 1 and FALSE to
    0 so only matching rows contribute to the total.
- q: Does SUMPRODUCT need Ctrl+Shift+Enter?
  a: No. SUMPRODUCT is designed to accept array calculations in normal Enter mode
    in classic Excel.
- q: Can SUMPRODUCT do a weighted average?
  a: Yes. Divide SUMPRODUCT(values, weights) by SUM(weights). See the weighted-average
    page for a full walkthrough.
related:
- - sumif-excel
  - sumif-google-sheets
- - sumifs-excel
  - sumifs-google-sheets
- - weighted-average-excel
  - weighted-average-google-sheets
- - averageif-excel
  - averageif-google-sheets
- - countif-excel
  - countif-google-sheets
sibling: sumproduct-google-sheets
---
SUMPRODUCT multiplies aligned arrays and adds the products. Use it for weighted totals (quantity × price) and for conditional sums with boolean tests — a portable pattern that works when SUMIFS is awkward or you need several conditions expressed as array logic.

## Quick answer

Use this formula in Excel:

```excel
=SUMPRODUCT(B2:B6, C2:C6)
```

Syntax: `SUMPRODUCT(array1, [array2], …)`. Matching positions are multiplied, then those products are added. With one array it behaves like SUM of that array.

## The problem

A line-item list has quantity and unit price, or region flags beside amounts. People multiply in a helper column then SUM, forget that TRUE/FALSE must coerce to 1/0, or paste an array formula that needs Ctrl+Shift+Enter in older Excel when SUMPRODUCT would have done it alone.

## Worked example

Five line items with region, quantity, and unit price. SUMPRODUCT builds the weighted total and the East-only revenue without a helper column.

| | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 1 | **Region** | **Qty** | **Price** |  | **Metric** | **Value** |
| 2 | East | 3 | 10 |  |  | **176** |
| 3 | West | 5 | 8 |  |  | **82** |
| 4 | East | 2 | 12 |  |  | **94** |
| 5 | East | 4 | 7 |  |  | **9** |
| 6 | West | 6 | 9 |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**F2** — weighted total qty × price

```excel
=SUMPRODUCT(B2:B6, C2:C6)
```

Result: **176**

**F3** — East revenue via boolean SUMPRODUCT

```excel
=SUMPRODUCT((A2:A6="East")*(B2:B6)*(C2:C6))
```

Result: **82**

**F4** — West revenue via boolean SUMPRODUCT

```excel
=SUMPRODUCT((A2:A6="West")*(B2:B6)*(C2:C6))
```

Result: **94**

**F5** — East quantity only (compare with SUMIF)

```excel
=SUMIF(A2:A6, "East", B2:B6)
```

Result: **9**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Lay out matching columns for factors you will multiply (Qty beside Price, or Region beside Amount).
2. For a weighted total type `=SUMPRODUCT(B2:B6, C2:C6)` — no helper column required.
3. For a conditional total multiply by a test: `=SUMPRODUCT((A2:A6="East")*(B2:B6)*(C2:C6))`.
4. Confirm array heights match; include only data rows, not headers.
5. Prefer SUMIFS for simple single-column conditions on very large sheets.

## Excel-specific notes

Classic weighted total: `=SUMPRODUCT(Qty, Price)` avoids a helper column. Conditional sum multiplies a boolean test by the values: `=SUMPRODUCT((Region="East")*(Qty)*(Price))`. In Excel, the `*` operator coerces TRUE/FALSE to 1/0; writing `=SUMPRODUCT((Region="East"), Amount)` with a comma does **not** treat the boolean the same way — prefer `*` for conditions. Arrays must be the same height; a mismatched range returns #VALUE!. SUMPRODUCT is slower than SUMIFS on huge sheets, so prefer SUMIFS for simple criteria and keep SUMPRODUCT for weighted products, OR-style logic, or criteria that SUMIFS cannot express cleanly. Double unary `--` also coerces booleans: `=SUMPRODUCT(--(Region="East"), Amount)`. Do not include header rows inside the arrays. Empty numeric cells count as 0 in multiplication.

**East revenue (qty × price)**

```excel
=SUMPRODUCT((A2:A6="East")*(B2:B6)*(C2:C6))
```

**Conditional sum with double unary**

```excel
=SUMPRODUCT(--(A2:A6="East"), B2:B6*C2:C6)
```

**Plain SUMIF for amount-only condition**

```excel
=SUMIF(A2:A6, "East", D2:D6)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=SUMPRODUCT(B2:B6, C2:C6)
```

Excel relies on SUMPRODUCT or SUMIFS; Sheets can also use FILTER/QUERY for the same totals.

<!--SIBLING-->


## Common errors and how to fix them

- **#VALUE!** — The arrays have different dimensions, or text that cannot coerce sat inside a product. **Fix:** Use equal-sized ranges and keep factors numeric (or coerce with VALUE / N).
- **Conditional SUMPRODUCT returns 0 unexpectedly** — Used a comma between the boolean and the amounts instead of `*`, or region text does not match exactly. **Fix:** Write (condition)*(values) or --(condition), and trim criteria text.
- **Result doubles after adding a helper column** — Both the helper products and SUMPRODUCT are included in a downstream SUM. **Fix:** Use either helper×SUM or SUMPRODUCT, not both on the same numbers.
- **Slow workbook** — SUMPRODUCT over entire columns (B:B) on tens of thousands of rows. **Fix:** Limit ranges to the used block, or switch simple cases to SUMIFS.

## FAQ

### When should I use SUMPRODUCT instead of SUMIFS?

Use SUMIFS for ordinary conditional sums on large data. Use SUMPRODUCT when you need to multiply columns (weighted totals) or express OR / array logic that SUMIFS cannot.

### Why multiply by (Region="East")?

The comparison returns TRUE/FALSE. Multiplying coerces TRUE to 1 and FALSE to 0 so only matching rows contribute to the total.

### Does SUMPRODUCT need Ctrl+Shift+Enter?

No. SUMPRODUCT is designed to accept array calculations in normal Enter mode in classic Excel.

### Can SUMPRODUCT do a weighted average?

Yes. Divide SUMPRODUCT(values, weights) by SUM(weights). See the weighted-average page for a full walkthrough.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
