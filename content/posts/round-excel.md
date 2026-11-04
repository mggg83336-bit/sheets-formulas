---
title: How to Use ROUND, ROUNDUP, and ROUNDDOWN in Excel
slug: round-excel
date: '2026-11-04'
summary: ROUND sends a number to a chosen digit with half-away-from-zero rules, ROUNDUP
  always moves away from zero, and ROUNDDOWN always moves toward zero. Negative digit
  values round to tens, hundreds, and beyond — useful for currency, estimates, and
  clean reports.
tags:
- Financial & percentages
- Excel
keyword: round-excel
niche: sheets-formulas
provider: structured
entry_id: round
platform: Excel
category: financial
faq:
- q: What is the difference between ROUND, ROUNDUP, and ROUNDDOWN?
  a: ROUND uses half away from zero. ROUNDUP always moves away from zero. ROUNDDOWN
    always moves toward zero. Pick based on whether understating or overstating is
    worse for the report.
- q: What do negative num_digits mean?
  a: They round to the left of the decimal point. -1 rounds to tens, -2 to hundreds,
    -3 to thousands.
- q: How do I round to the nearest nickel or 5 minutes?
  a: Use MROUND with the step size, for example =MROUND(A2, 0.05) for nickels or =MROUND(A2,
    5) for multiples of 5.
related:
- - percentage-change-excel
  - percentage-change-google-sheets
- - weighted-average-excel
  - weighted-average-google-sheets
- - pmt-excel
  - pmt-google-sheets
- - cagr-excel
  - cagr-google-sheets
sibling: round-google-sheets
---
ROUND sends a number to a chosen digit with half-away-from-zero rules, ROUNDUP always moves away from zero, and ROUNDDOWN always moves toward zero. Negative digit values round to tens, hundreds, and beyond — useful for currency, estimates, and clean reports.

## Quick answer

Use this formula in Excel:

```excel
=ROUND(A2, 2)
```

Syntax: `ROUND(number, num_digits)`. With 2, values round to hundredths (currency style). Positive num_digits keep that many digits after the decimal; 0 rounds to an integer; negative values round to the left of the decimal (tens, hundreds).

## The problem

A pricing sheet shows long decimals from tax and FX formulas. Stakeholders want two decimal places for money, whole numbers for headcount, and rounded hundreds for rough forecasts, but plain cell formatting only changes the display while downstream formulas still see the full precision.

## Worked example

Five numbers covering two-decimal currency rounding, integer rounding of 2.5, negative values, and rounding to hundreds. Extra columns compare ROUNDUP, ROUNDDOWN, and MROUND.

| | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 1 | **Value** | **Digits** | **ROUND** | **ROUNDUP** | **ROUNDDOWN** | **MROUND to 5** |
| 2 | 2.345 | 2 | **2.35** | **2.35** | **2.34** |  |
| 3 | 3.14159 | 2 | **3.14** | **3.15** | **3.14** |  |
| 4 | -1.567 | 2 | **-1.57** | **-1.57** | **-1.56** |  |
| 5 | 2.5 | 0 | **3** | **3** | **2** |  |
| 6 | 1234.567 | -2 | **1200** | **1300** | **1200** |  |
| 7 | 17 | 0 |  |  |  | **15** |

Formulas used in the example (results shown in **bold** in the table above):

**C2 (filled to C6)** — ROUND with per-row digits

```excel
=ROUND(A2, B2)
```

Results: **2.35**, **3.14**, **-1.57**, **3**, **1200**

**D2 (filled to D6)** — ROUNDUP with per-row digits

```excel
=ROUNDUP(A2, B2)
```

Results: **2.35**, **3.15**, **-1.57**, **3**, **1300**

**E2 (filled to E6)** — ROUNDDOWN with per-row digits

```excel
=ROUNDDOWN(A2, B2)
```

Results: **2.34**, **3.14**, **-1.56**, **2**, **1200**

**F7** — MROUND to nearest 5

```excel
=MROUND(A7, 5)
```

Result: **15**

<!--AD_IN_ARTICLE-->

## How the formula works

1. List the raw values in column A and the num_digits argument in column B (2, 0, or -2).
2. Type `=ROUND(A2, B2)` and fill down for standard half-away-from-zero rounding.
3. Add ROUNDUP and ROUNDDOWN columns when you need always-up or always-down behaviour.
4. Use a negative digit such as -2 to round to hundreds for rough forecasts.
5. Reach for MROUND when the target is a multiple (5, 0.05, 100) rather than a decimal place.

## Excel-specific notes

Excel's ROUND uses half away from zero: 2.5 → 3 and -2.5 → -3 when num_digits is 0. That differs from banker's rounding in some programming languages. ROUNDUP always moves away from zero (3.141 with 2 → 3.15; -1.567 with 2 → -1.57). ROUNDDOWN always moves toward zero (3.141 → 3.14; -1.567 → -1.56). Use ROUND for typical reporting, ROUNDUP when you must not understate a charge or a safety stock, and ROUNDDOWN when you must not overstate. Negative digits are handy for forecasts: `=ROUND(A2, -2)` turns 1234.567 into 1200. MROUND rounds to a chosen multiple (`=MROUND(17, 5)` → 15). Remember that number formats alone do not change the stored value — wrap the formula in ROUND when later cells should inherit the rounded figure. Pair with currency formats after rounding to two places.

**Always round away from zero**

```excel
=ROUNDUP(A2, 2)
```

**Always round toward zero**

```excel
=ROUNDDOWN(A2, 2)
```

**Round to nearest hundred**

```excel
=ROUND(A2, -2)
```

**Round to a multiple of 5**

```excel
=MROUND(A2, 5)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=ROUND(A2, 2)
```

Excel uses the same functions; fill down or spill instead of ARRAYFORMULA.

<!--SIBLING-->


## Common errors and how to fix them

- **Display shows 2.35 but another formula still uses 2.345** — Only the cell format was changed; the stored value stayed full precision. **Fix:** Wrap the source formula in ROUND (or ROUNDUP/ROUNDDOWN) so dependents see the rounded value.
- **Negative number rounded the "wrong" way** — ROUNDUP moves away from zero and ROUNDDOWN toward zero, which feels opposite to "up on the number line" for negatives. **Fix:** Check the sign rule, or use ABS tricks only when you truly want number-line direction.
- **#NUM! or unexpected MROUND result with uneven multiples** — MROUND expects the multiple and the value to allow a valid nearest multiple (and non-zero multiple). **Fix:** Use a non-zero multiple; for banker's or custom rules, build an explicit formula instead.
- **Totals off by a cent after rounding each line** — Summing pre-rounded lines differs from rounding the unrounded sum once. **Fix:** Decide a policy (round lines then sum, or sum then round) and apply it consistently.

## FAQ

### What is the difference between ROUND, ROUNDUP, and ROUNDDOWN?

ROUND uses half away from zero. ROUNDUP always moves away from zero. ROUNDDOWN always moves toward zero. Pick based on whether understating or overstating is worse for the report.

### What do negative num_digits mean?

They round to the left of the decimal point. -1 rounds to tens, -2 to hundreds, -3 to thousands.

### How do I round to the nearest nickel or 5 minutes?

Use MROUND with the step size, for example =MROUND(A2, 0.05) for nickels or =MROUND(A2, 5) for multiples of 5.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
