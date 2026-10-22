---
title: How to Calculate CAGR in Excel
slug: cagr-excel
date: '2026-10-22'
summary: The compound annual growth rate (CAGR) is the constant yearly rate that takes
  a starting value to an ending value over a number of years. Use (end/start)^(1/years)-1
  or the RRI function. Worked example included.
tags:
- Financial & percentages
- Excel
keyword: cagr-excel
niche: sheets-formulas
provider: structured
entry_id: cagr
platform: Excel
category: financial
faq:
- q: How is CAGR different from the average growth rate?
  a: The simple average of yearly growth rates ignores compounding and overstates
    growth when rates vary. CAGR gives the single rate that reproduces the actual
    start and end values.
- q: Can I calculate CAGR for months?
  a: Yes. Use the number of months as the period, then annualize with =(1+monthly_rate)^12-1.
- q: How do I project a future value from a CAGR?
  a: 'Multiply the latest value by (1 + CAGR) raised to the number of years ahead,
    e.g. =B3*(1+B5)^3 for three years after 2025. Treat it as a trend line, not a
    forecast: CAGR smooths out every up and down year between the start and end.'
- q: Should I use CAGR or XIRR for investments with deposits?
  a: CAGR only looks at the first and last value, so it ignores money added or withdrawn
    in between. For a portfolio with contributions, use XIRR with the dated cash flows
    instead; it works in both Excel and Google Sheets.
related:
- - compound-interest-excel
  - compound-interest-google-sheets
- - percentage-change-excel
  - percentage-change-google-sheets
- - pmt-excel
  - pmt-google-sheets
sibling: cagr-google-sheets
---
The compound annual growth rate (CAGR) is the constant yearly rate that takes a starting value to an ending value over a number of years. Use (end/start)^(1/years)-1 or the RRI function. Worked example included.

## Quick answer

Use this formula in Excel:

```excel
=(B3/B2)^(1/B4)-1
```

Ending value divided by starting value, raised to the power of 1/years, minus 1. Format the result as a percentage.

## The problem

Revenue grew from 50,000 in 2020 to 84,000 in 2025. You want a single annual growth rate to compare with other businesses.

## Worked example

Growth between 2020 and 2025.

| | A | B |
|---|---|---|
| 1 | **Input** | **Value** |
| 2 | Start value (2020) | 50000 |
| 3 | End value (2025) | 84000 |
| 4 | Years | 5 |
| 5 | CAGR (formula) | **10.93%** |
| 6 | CAGR (RRI) | **10.93%** |

Formulas used in the example (results shown in **bold** in the table above):

**B5**

```excel
=(B3/B2)^(1/B4)-1
```

Result: **10.93%**

**B6**

```excel
=RRI(B4, B2, B3)
```

Result: **10.93%**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `B3/B2` is the total growth factor: 84,000 / 50,000 = 1.68.
2. `^(1/B4)` takes the 5th root, the factor that applied five times gives 1.68: about 1.1093.
3. `-1` turns the factor into a rate: 10.93% per year.
4. Check: 50,000 x 1.1093^5 is approximately 84,000.

## Excel-specific notes

RRI(nper, pv, fv) returns the same rate and is available from Excel 2013. The number of years is the number of periods between the two values, not the number of data points: from 2020 to 2025 is 5 years even though there are six yearly figures. CAGR cannot be calculated when the starting value is zero or when the two values have different signs.

**RRI function**

```excel
=RRI(B4, B2, B3)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=(B3/B2)^(1/B4)-1
```

The same formula and RRI function work in Google Sheets.

<!--SIBLING-->


## Common errors and how to fix them

- **#NUM!** — The start value is negative and the end value positive (or vice versa). **Fix:** CAGR is not defined in that case; report the absolute change instead.
- **#DIV/0!** — The start value is 0. **Fix:** Use the first non-zero year as the start.
- **Rate too low** — The number of data points (6) was used instead of the number of years between them (5). **Fix:** Use end year - start year.

## FAQ

### How is CAGR different from the average growth rate?

The simple average of yearly growth rates ignores compounding and overstates growth when rates vary. CAGR gives the single rate that reproduces the actual start and end values.

### Can I calculate CAGR for months?

Yes. Use the number of months as the period, then annualize with =(1+monthly_rate)^12-1.

### How do I project a future value from a CAGR?

Multiply the latest value by (1 + CAGR) raised to the number of years ahead, e.g. =B3*(1+B5)^3 for three years after 2025. Treat it as a trend line, not a forecast: CAGR smooths out every up and down year between the start and end.

### Should I use CAGR or XIRR for investments with deposits?

CAGR only looks at the first and last value, so it ignores money added or withdrawn in between. For a portfolio with contributions, use XIRR with the dated cash flows instead; it works in both Excel and Google Sheets.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
