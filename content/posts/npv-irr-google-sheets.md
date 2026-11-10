---
title: How to Calculate NPV and IRR in Google Sheets
slug: npv-irr-google-sheets
date: '2026-11-10'
summary: 'NPV discounts a series of cash flows to today''s value; IRR is the rate
  that makes NPV equal zero. Excel and Google Sheets both have the same NPV quirk:
  `NPV(rate, values)` treats the first value as the end of period 1, so an immediate
  (t=0) investment is added separately. IRR takes the full series, '
tags:
- Financial & percentages
- Google Sheets
keyword: npv-irr-google-sheets
niche: sheets-formulas
provider: structured
entry_id: npv-irr
platform: Google Sheets
category: financial
faq:
- q: Why isn't the initial investment inside the NPV function?
  a: Excel and Google Sheets NPV treat the first argument value as the end of period
    1, not today. If you put the t=0 outlay in that first slot, it is discounted one
    full period and the project NPV is wrong by a year of interest. Add it outside
    the function instead.
- q: What is the difference between NPV and IRR?
  a: 'NPV is an amount — the discounted value of the project in today''s currency
    at a rate you choose. IRR is a rate — the discount rate at which NPV would be
    zero. Use both: a high IRR can still be a small project, and NPV tells you how
    much value is added at your required return.'
- q: What if the cash flows are not evenly spaced?
  a: Do not force irregular invoices or mid-year draws into NPV or IRR. Put a date
    next to each flow and use XNPV and XIRR, which discount by actual day count. Both
    functions exist in Excel and Google Sheets.
- q: Can I use GOOGLEFINANCE or a live market rate as the discount rate?
  a: You can, but it is usually the wrong input for a project appraisal. The discount
    rate is a required return you choose (cost of capital, hurdle rate), not a ticker.
    Keep it as a typed assumption so the NPV is reproducible.
related:
- - compound-interest-google-sheets
  - compound-interest-excel
- - cagr-google-sheets
  - cagr-excel
- - pmt-google-sheets
  - pmt-excel
- - percentage-change-google-sheets
  - percentage-change-excel
sibling: npv-irr-excel
---
NPV discounts a series of cash flows to today's value; IRR is the rate that makes NPV equal zero. Excel and Google Sheets both have the same NPV quirk: `NPV(rate, values)` treats the first value as the end of period 1, so an immediate (t=0) investment is added separately. IRR takes the full series, including that initial outflow. Worked example included.

## Quick answer

Use this formula in Google Sheets:

```excel
=NPV(E2, B3:B7)+B2
```

Same timing rule in Google Sheets: `NPV` discounts from the end of period 1, so add the immediate investment outside the function. `IRR` includes the t=0 flow in the range.

## The problem

You are reviewing a five-year project that costs 10,000 today and returns 3,000, 3,500, 4,000, 4,000 and 2,500 at the end of each of the next five years. You want the net present value at a 10% discount rate and the internal rate of return, and you need the spreadsheet functions to treat the timing correctly.

## Worked example

A 10,000 investment at t=0, then five year-end inflows. The discount rate in E2 is an input (10%). NPV adds the initial outflow outside the function; IRR uses the whole column. The third result shows what NPV returns before that t=0 adjustment.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Year** | **Cash flow** |  | **Item** | **Value** |
| 2 | 0 | -10000 |  | Discount rate | 10% |
| 3 | 1 | 3000 |  | NPV | **2,909.45** |
| 4 | 2 | 3500 |  | IRR | **20.81%** |
| 5 | 3 | 4000 |  | PV of future flows | **12,909.45** |
| 6 | 4 | 4000 |  |  |  |
| 7 | 5 | 2500 |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**E3** — NPV including the t=0 investment

```excel
=NPV(E2, B3:B7)+B2
```

Result: **2,909.45**

**E4** — IRR of the full series

```excel
=IRR(B2:B7)
```

Result: **20.81%**

**E5** — NPV of year-1-to-5 flows only

```excel
=NPV(E2, B3:B7)
```

Result: **12,909.45**

<!--AD_IN_ARTICLE-->

## How the formula works

1. List every cash flow in time order, with the immediate investment as a negative number in B2 and the year-end inflows in B3:B7.
2. Enter the discount rate in E2 as 10% (or 0.1), not 10.
3. `=NPV(E2, B3:B7)` discounts only the future flows, as if the first of them arrives at the end of year 1: 12,909.45.
4. Add the t=0 investment outside NPV: `=NPV(E2, B3:B7)+B2` equals 12,909.45 − 10,000 = 2,909.45. That is the project NPV.
5. `=IRR(B2:B7)` uses the entire series, including the initial outflow, and returns about 20.81%. At that rate the NPV of the same flows is zero.

## Google Sheets-specific notes

Sheets NPV and IRR follow the same semantics as Excel, including the t=0 pitfall, so a file exchanged between the two platforms will usually recalculate the same project NPV. Be careful with open-ended ranges such as `B3:B` or `B2:B`: a trailing zero, a stray total row, or a blank that later becomes 0 will be treated as an extra cash flow and can quietly distort IRR. Prefer a closed range, or wrap the series with FILTER to drop blanks, before you grow the column. XNPV and XIRR exist in Sheets too and are the right tools when the dates are irregular; do not press GOOGLEFINANCE into service as a substitute for the discount rate in this kind of project example — the rate is an input you choose, not a live ticker. Locale settings change the argument separator (comma vs semicolon) and how percentages display, not the math. If collaborators still open the workbook in desktop Excel, stay with NPV, IRR, XNPV and XIRR; leave ARRAYFORMULA and GOOGLEFINANCE out of the shared file.

**Open-ended future flows (watch trailing zeros)**

```excel
=NPV(E2, B3:B)+B2
```

**IRR that ignores blank cells in a growing column**

```excel
=IRR(FILTER(B2:B, B2:B<>""))
```

**XNPV when each flow has a real date**

```excel
=XNPV(E2, B2:B7, C2:C7)
```

**XIRR for irregular dates**

```excel
=XIRR(B2:B7, C2:C7)
```


## Excel version

The same formula works unchanged in Excel:

```excel
=NPV(E2, B3:B7)+B2
```

Google Sheets uses the same NPV and IRR functions with the same t=0 timing rule. XNPV and XIRR are available in Sheets as well when the flows have actual dates.

<!--SIBLING-->


## Common errors and how to fix them

- **NPV is 10,000 too high (about 12,909 instead of 2,909)** — The initial investment was included inside NPV, or it was left out of the addition, so t=0 was treated as the end of period 1 (or omitted). **Fix:** Call NPV on the period-1-to-n flows only, then add the t=0 cash flow: `=NPV(rate, B3:B7)+B2`.
- **#NUM! from IRR** — The cash flows never change sign, or they change sign more than once and IRR cannot settle on one root. **Fix:** Confirm there is at least one outflow and one inflow. For multiple sign changes, supply a guess (`=IRR(B2:B7, 0.1)`) or switch to MIRR / a plotted NPV profile.
- **Discounting looks wildly off** — The rate was entered as 10 rather than 10% (or 0.1), so the function discounted at 1000%. **Fix:** Type 10% or 0.1. Format the rate cell as a percentage so the next edit is obviously a rate.
- **IRR changes after you extend the column** — An open-ended range, a trailing zero, or a total row was pulled into the series as an extra period. **Fix:** Use a closed range (B2:B7) or FILTER out blanks and totals before IRR and NPV see the list.

## FAQ

### Why isn't the initial investment inside the NPV function?

Excel and Google Sheets NPV treat the first argument value as the end of period 1, not today. If you put the t=0 outlay in that first slot, it is discounted one full period and the project NPV is wrong by a year of interest. Add it outside the function instead.

### What is the difference between NPV and IRR?

NPV is an amount — the discounted value of the project in today's currency at a rate you choose. IRR is a rate — the discount rate at which NPV would be zero. Use both: a high IRR can still be a small project, and NPV tells you how much value is added at your required return.

### What if the cash flows are not evenly spaced?

Do not force irregular invoices or mid-year draws into NPV or IRR. Put a date next to each flow and use XNPV and XIRR, which discount by actual day count. Both functions exist in Excel and Google Sheets.

### Can I use GOOGLEFINANCE or a live market rate as the discount rate?

You can, but it is usually the wrong input for a project appraisal. The discount rate is a required return you choose (cost of capital, hurdle rate), not a ticker. Keep it as a typed assumption so the NPV is reproducible.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
