---
title: Loan Payment Formula with PMT in Excel
slug: pmt-excel
date: '2026-10-22'
summary: PMT calculates the fixed periodic payment for a loan or mortgage from the
  interest rate, number of payments and loan amount. Worked example for a 30-year
  mortgage, plus total interest and the sign convention.
tags:
- Financial & percentages
- Excel
keyword: pmt-excel
niche: sheets-formulas
provider: structured
entry_id: pmt
platform: Excel
category: financial
faq:
- q: Does PMT include property tax and insurance?
  a: No. PMT covers principal and interest only. Add escrow items separately.
- q: How do I calculate how much I can borrow for a given payment?
  a: Use PV, e.g. =PV(B3/12, B4*12, -1500) returns the loan amount a 1,500 monthly
    payment supports.
- q: How do I build an amortization schedule?
  a: List payment numbers 1 to 360 in a column, then use =IPMT($B$3/12, A10, $B$4*12,
    -$B$2) for the interest part and =PPMT($B$3/12, A10, $B$4*12, -$B$2) for the principal
    part of each payment. The two always add up to the PMT result.
related:
- - compound-interest-excel
  - compound-interest-google-sheets
- - cagr-excel
  - cagr-google-sheets
- - percentage-change-excel
  - percentage-change-google-sheets
sibling: pmt-google-sheets
---
PMT calculates the fixed periodic payment for a loan or mortgage from the interest rate, number of payments and loan amount. Worked example for a 30-year mortgage, plus total interest and the sign convention.

## Quick answer

Use this formula in Excel:

```excel
=PMT(B3/12, B4*12, -B2)
```

Syntax: `PMT(rate, nper, pv, [fv], [type])`. Monthly rate = annual rate / 12, number of payments = years x 12, pv = loan amount (negative so the payment shows as positive).

## The problem

You want the monthly payment for a 250,000 loan at 6.5% annual interest over 30 years, and the total interest paid over the life of the loan.

## Worked example

A 30-year fixed-rate loan.

| | A | B |
|---|---|---|
| 1 | **Input** | **Value** |
| 2 | Loan amount | 250000 |
| 3 | Annual rate | 6.5% |
| 4 | Years | 30 |
| 5 | Monthly payment | **1,580.17** |
| 6 | Total interest | **318,861.22** |
| 7 | Interest in month 1 | **1,354.17** |

Formulas used in the example (results shown in **bold** in the table above):

**B5**

```excel
=PMT(B3/12, B4*12, -B2)
```

Result: **1,580.17**

**B6**

```excel
=B5*B4*12-B2
```

Result: **318,861.22**

**B7**

```excel
=IPMT(B3/12, 1, B4*12, -B2)
```

Result: **1,354.17**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `B3/12` is the monthly interest rate (0.5417%).
2. `B4*12` is the number of monthly payments, 360.
3. `-B2` is the loan amount, negative because it is money you receive; the payment then comes out positive.
4. Total interest = payment x number of payments - loan amount: 1,580.17 x 360 - 250,000 = 318,861.22.
5. In month 1 almost all of the payment is interest: 250,000 x 0.5417% = 1,354.17.

## Excel-specific notes

PMT returns a negative number when the loan amount is positive, because the payment is money going out; entering the amount as -B2 (or writing =-PMT(...)) gives a positive payment. The result covers principal and interest only, not taxes, insurance or fees. Use IPMT and PPMT to split a specific payment into interest and principal, and type = 1 if payments are made at the start of each period.

**Interest part of the first payment**

```excel
=IPMT(B3/12, 1, B4*12, -B2)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=PMT(B3/12, B4*12, -B2)
```

The same PMT, IPMT and PPMT functions work in Google Sheets.

<!--SIBLING-->


## Common errors and how to fix them

- **Payment is negative** — The loan amount was entered as a positive pv. **Fix:** Use -B2 or put a minus sign in front of PMT.
- **Payment is far too high** — The annual rate was used without dividing by 12, or years were used instead of months. **Fix:** Use rate/12 and years*12 for monthly payments.
- **#NUM!** — The number of periods is 0 or the inputs are inconsistent. **Fix:** Check that nper is positive and the rate is a reasonable decimal.

## FAQ

### Does PMT include property tax and insurance?

No. PMT covers principal and interest only. Add escrow items separately.

### How do I calculate how much I can borrow for a given payment?

Use PV, e.g. =PV(B3/12, B4*12, -1500) returns the loan amount a 1,500 monthly payment supports.

### How do I build an amortization schedule?

List payment numbers 1 to 360 in a column, then use =IPMT($B$3/12, A10, $B$4*12, -$B$2) for the interest part and =PPMT($B$3/12, A10, $B$4*12, -$B$2) for the principal part of each payment. The two always add up to the PMT result.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
