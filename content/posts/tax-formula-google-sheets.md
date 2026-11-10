---
title: How to Calculate Tax in a Spreadsheet in Google Sheets
slug: tax-formula-google-sheets
date: '2026-11-10'
summary: A flat `income * rate` formula only works when every dollar is taxed the
  same. Progressive (marginal) tax applies a different rate to each band of income.
  This guide builds a clear three-bracket example with a nested IF and a SUMPRODUCT
  form that reads the brackets from a table, then shows the effec
tags:
- Financial & percentages
- Google Sheets
keyword: tax-formula-google-sheets
niche: sheets-formulas
provider: structured
entry_id: tax-formula
platform: Google Sheets
category: financial
faq:
- q: What is the difference between the marginal rate and the effective rate?
  a: The marginal rate is the rate on the next dollar of income (22% once you are
    above 40,000 in this schedule). The effective rate is total tax divided by total
    income (about 14.36% here). Pay slips and planning conversations often mix the
    two up.
- q: When should I use IFS instead of a nested IF?
  a: IFS is easier to read once you have more than two or three tests, and it is the
    usual choice in Google Sheets. Nested IF and SUMPRODUCT remain the most portable
    options when the file also has to open in older Excel. Do not rely on IFS alone
    if you need the example to recalculate in LibreOffice.
- q: Can I use QUERY or a lookup to compute marginal tax?
  a: A lookup can return the *top* rate, which is useful for a marginal-rate label
    but not for the tax amount. QUERY is the wrong tool for walking brackets. Use
    IF/IFS for a short schedule, or SUMPRODUCT (or LAMBDA) against a threshold table
    when the bands may change.
- q: Does this formula work for payroll withholding or VAT?
  a: Not by itself. Withholding tables, allowances, credits, and VAT-inclusive prices
    follow different rules. Use this pattern only for a progressive tax on a single
    taxable-income figure, and keep a published rate table next to the formula so
    the brackets stay auditable.
related:
- - ifs-google-sheets
  - ifs-excel
- - nested-if-google-sheets
  - nested-if-excel
- - if-google-sheets
  - if-excel
- - percentage-google-sheets
  - percentage-excel
- - pmt-google-sheets
  - pmt-excel
sibling: tax-formula-excel
---
A flat `income * rate` formula only works when every dollar is taxed the same. Progressive (marginal) tax applies a different rate to each band of income. This guide builds a clear three-bracket example with a nested IF and a SUMPRODUCT form that reads the brackets from a table, then shows the effective rate as tax divided by income.

## Quick answer

Use this formula in Google Sheets:

```excel
=IF(B2<=10000, B2*0.1, IF(B2<=40000, 1000+(B2-10000)*0.12, 1000+3600+(B2-40000)*0.22))
```

The same nested IF works in Google Sheets. IFS is often easier to read for this kind of bracket walk, and a SUMPRODUCT of a threshold table stays compatible with Excel.

## The problem

Taxable income is 55,000. The first 10,000 is taxed at 10%, the next 30,000 (up to 40,000) at 12%, and anything above 40,000 at 22%. You want the tax due and the effective rate, with formulas that still work if the income changes.

## Worked example

Income of 55,000 against three brackets: 0–10,000 at 10%, 10,000–40,000 at 12%, and above 40,000 at 22%. B3 uses a nested IF; B4 reads the threshold table with SUMPRODUCT and should match. The effective rate is tax divided by income.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Item** | **Value** |  | **Threshold** | **Rate** |
| 2 | Income | 55000 |  | 0 | 10% |
| 3 | Tax (nested IF) | **7,900** |  | 10000 | 12% |
| 4 | Tax (SUMPRODUCT) | **7,900** |  | 40000 | 22% |
| 5 | Effective rate | **14.36%** |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**B3** — tax with a nested IF

```excel
=IF(B2<=10000, B2*0.1, IF(B2<=40000, 1000+(B2-10000)*0.12, 1000+3600+(B2-40000)*0.22))
```

Result: **7,900**

**B4** — tax from the bracket table

```excel
=SUMPRODUCT((B2>$D$2:$D$4)*(B2-$D$2:$D$4)*($E$2:$E$4-N($E$1:$E$3)))
```

Result: **7,900**

**B5** — effective rate

```excel
=B3/B2
```

Result: **14.36%**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Tax in the first band is 10,000 × 10% = 1,000. The next 30,000 (from 10,000 to 40,000) is taxed at 12% = 3,600. The remaining 15,000 is taxed at 22% = 3,300. Total tax is 1,000 + 3,600 + 3,300 = 7,900.
2. The nested IF encodes the same arithmetic: at 55,000 it takes the third branch, `1000+3600+(B2-40000)*0.22`.
3. The SUMPRODUCT form looks up the thresholds in D2:D4 and the rates in E2:E4 and should return the same 7,900. Change the table, not the formula, when a band is revised.
4. Effective rate is tax ÷ income: 7,900 / 55,000 ≈ 14.36%, which is well below the 22% top rate because only the last slice is taxed at 22%.
5. To reuse the schedule, put other incomes in column B and fill the tax formula down, with the bracket table locked by absolute references.

## Google Sheets-specific notes

IFS is a natural fit in Sheets and avoids the hard-to-scan nesting of a long IF chain (`=IFS(B2<=10000, B2*0.1, B2<=40000, 1000+(B2-10000)*0.12, TRUE, 1000+3600+(B2-40000)*0.22)`). To apply the same schedule down a column of incomes, wrap a closed-form expression in ARRAYFORMULA rather than filling cell by cell; do not ask QUERY to compute marginal brackets — QUERY can group and filter, but it will not walk a rate table the way SUMPRODUCT or IFS does. LAMBDA (and a Named Function) is a clean way to package the tax logic once and call `=TAX(B2)` from many sheets. Locale settings change separators and how percentages appear, not which band an income falls into. Open-ended ranges in an ARRAYFORMULA will tax stray zeros or totals at the bottom of the column, so keep a bounded income list. If Excel collaborators will open the file, stick to IF or SUMPRODUCT; IFS exists in current Excel but ARRAYFORMULA and Sheets Named Functions will not travel.

**IFS brackets**

```excel
=IFS(B2<=10000, B2*0.1, B2<=40000, 1000+(B2-10000)*0.12, TRUE, 1000+3600+(B2-40000)*0.22)
```

**SUMPRODUCT from a bracket table**

```excel
=SUMPRODUCT((B2>$D$2:$D$4)*(B2-$D$2:$D$4)*($E$2:$E$4-N($E$1:$E$3)))
```

**Tax for a whole column of incomes**

```excel
=ARRAYFORMULA(IF(B2:B="",, IF(B2:B<=10000, B2:B*0.1, IF(B2:B<=40000, 1000+(B2:B-10000)*0.12, 1000+3600+(B2:B-40000)*0.22))))
```

**Effective rate**

```excel
=B3/B2
```


## Excel version

The same formula works unchanged in Excel:

```excel
=IF(B2<=10000, B2*0.1, IF(B2<=40000, 1000+(B2-10000)*0.12, 1000+3600+(B2-40000)*0.22))
```

Google Sheets accepts the same nested IF and SUMPRODUCT formulas. IFS is often the cleaner Sheets rewrite, and ARRAYFORMULA can apply the tax formula down a column of incomes.

<!--SIBLING-->


## Common errors and how to fix them

- **Tax equals income times the top rate (12,100 here)** — A flat `=B2*0.22` was used, so every dollar was taxed at the marginal rate. **Fix:** Tax each band separately with a nested IF, IFS, or a SUMPRODUCT of the bracket table.
- **Off-by-one band, or a jump at the threshold** — The test used `<` when the band is `<=` (or the other way around), so income of exactly 10,000 or 40,000 landed in the wrong slice. **Fix:** Pick one convention and apply it at every threshold. In this example a threshold is the top of the lower band (`B2<=10000`, `B2<=40000`).
- **SUMPRODUCT does not match the nested IF** — The rate column is not contiguous, the cell above the first rate is numeric, or the thresholds are in the wrong order. **Fix:** Keep thresholds ascending, rates directly beside them, and a header (or a blank) immediately above the first rate so N(...) of that cell is 0.
- **#DIV/0! on the effective rate** — Income is 0 or blank. **Fix:** Use `=IF(B2=0, "n/a", B3/B2)` and format the result as a percentage, not as currency.

## FAQ

### What is the difference between the marginal rate and the effective rate?

The marginal rate is the rate on the next dollar of income (22% once you are above 40,000 in this schedule). The effective rate is total tax divided by total income (about 14.36% here). Pay slips and planning conversations often mix the two up.

### When should I use IFS instead of a nested IF?

IFS is easier to read once you have more than two or three tests, and it is the usual choice in Google Sheets. Nested IF and SUMPRODUCT remain the most portable options when the file also has to open in older Excel. Do not rely on IFS alone if you need the example to recalculate in LibreOffice.

### Can I use QUERY or a lookup to compute marginal tax?

A lookup can return the *top* rate, which is useful for a marginal-rate label but not for the tax amount. QUERY is the wrong tool for walking brackets. Use IF/IFS for a short schedule, or SUMPRODUCT (or LAMBDA) against a threshold table when the bands may change.

### Does this formula work for payroll withholding or VAT?

Not by itself. Withholding tables, allowances, credits, and VAT-inclusive prices follow different rules. Use this pattern only for a progressive tax on a single taxable-income figure, and keep a published rate table next to the formula so the brackets stay auditable.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
