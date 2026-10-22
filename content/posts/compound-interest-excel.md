---
title: Compound Interest Formula in Excel
slug: compound-interest-excel
date: '2026-10-22'
summary: Calculate how an investment grows with compound interest, using the math
  formula P*(1+r/n)^(n*t) or the built-in FV function. Includes monthly compounding,
  the sign convention that confuses FV users, and regular monthly contributions.
tags:
- Financial & percentages
- Excel
keyword: compound-interest-excel
niche: sheets-formulas
provider: structured
entry_id: compound-interest
platform: Excel
category: financial
faq:
- q: What is the formula for continuous compounding?
  a: =B2*EXP(B3*B5), i.e. principal times e raised to rate times years.
- q: How do I show the balance for every year?
  a: Put years 1 to 10 in a column and use =$B$2*(1+$B$3/$B$4)^($B$4*A12), where A12
    is the year.
related:
- - pmt-excel
  - pmt-google-sheets
- - cagr-excel
  - cagr-google-sheets
- - percentage-change-excel
  - percentage-change-google-sheets
sibling: compound-interest-google-sheets
---
Calculate how an investment grows with compound interest, using the math formula P*(1+r/n)^(n*t) or the built-in FV function. Includes monthly compounding, the sign convention that confuses FV users, and regular monthly contributions.

## Quick answer

Use this formula in Excel:

```excel
=B2*(1+B3/B4)^(B4*B5)
```

Principal times (1 + rate per period) raised to the number of periods. B3/B4 is the monthly rate and B4*B5 the number of months.

## The problem

You invest 10,000 at 5% per year, compounded monthly, for 10 years, and want the final balance and the interest earned.

## Worked example

Inputs in B2:B5, results in B6:B8.

| | A | B |
|---|---|---|
| 1 | **Input** | **Value** |
| 2 | Principal | 10000 |
| 3 | Annual rate | 5% |
| 4 | Compounds per year | 12 |
| 5 | Years | 10 |
| 6 | Future value (formula) | **16,470.09** |
| 7 | Future value (FV) | **16,470.09** |
| 8 | Interest earned | **6,470.09** |

Formulas used in the example (results shown in **bold** in the table above):

**B6**

```excel
=B2*(1+B3/B4)^(B4*B5)
```

Result: **16,470.09**

**B7**

```excel
=FV(B3/B4, B4*B5, 0, -B2)
```

Result: **16,470.09**

**B8**

```excel
=B6-B2
```

Result: **6,470.09**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `B3/B4` converts the annual rate into a rate per period: 5% / 12 = 0.4167% per month.
2. `B4*B5` is the number of compounding periods: 12 x 10 = 120 months.
3. `(1+B3/B4)^(B4*B5)` is the growth factor, about 1.647.
4. Multiplying by the principal gives the balance, 16,470.09. Subtracting the principal gives the interest earned.
5. Increase the compounding frequency (e.g. 365) to see that it matters far less than the rate and the number of years.

## Excel-specific notes

FV gives the same result and also handles regular deposits. Its sign convention follows cash flow: money you pay out (the initial deposit) is negative and money you receive is positive, which is why the formula uses -B2. To add a monthly contribution of 200, put -200 in the third argument: `=FV(B3/B4, B4*B5, -200, -B2)`. Use the rate and the number of periods in the same unit: monthly rate with months, annual rate with years.

**FV function**

```excel
=FV(B3/B4, B4*B5, 0, -B2)
```

**With a monthly contribution of 200**

```excel
=FV(B3/B4, B4*B5, -200, -B2)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=B2*(1+B3/B4)^(B4*B5)
```

The same formula and FV function work in Google Sheets.

<!--SIBLING-->


## Common errors and how to fix them

- **Negative result from FV** — The present value was entered as a positive number. **Fix:** Enter the deposit as negative (-B2), or put a minus in front of FV.
- **Result far too large** — The rate was entered as 5 instead of 5% (0.05). **Fix:** Enter the rate as a percentage or decimal.
- **Mixed units** — Annual rate used with months (or monthly rate with years). **Fix:** Divide the rate and multiply the periods by the same number of periods per year.

## FAQ

### What is the formula for continuous compounding?

=B2*EXP(B3*B5), i.e. principal times e raised to rate times years.

### How do I show the balance for every year?

Put years 1 to 10 in a column and use =$B$2*(1+$B$3/$B$4)^($B$4*A12), where A12 is the year.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
