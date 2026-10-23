---
title: VLOOKUP with Multiple Criteria in Google Sheets
slug: vlookup-multiple-criteria-google-sheets
date: '2026-10-23'
summary: 'VLOOKUP only matches one value, but there are three reliable ways to look
  up a row that must match two or more conditions: XLOOKUP with multiplied conditions,
  INDEX MATCH as an array, and VLOOKUP with a helper key. Each is shown below with
  a worked example.'
tags:
- Lookup & reference
- Google Sheets
keyword: vlookup-multiple-criteria-google-sheets
niche: sheets-formulas
provider: structured
entry_id: vlookup-multiple-criteria
platform: Google Sheets
category: lookup
faq:
- q: Can VLOOKUP itself take two lookup values?
  a: Not directly. Join the criteria into one key (with a helper column or CHOOSE)
    so VLOOKUP has a single value to search for.
- q: How do I sum instead of returning the first match?
  a: Use SUMIFS, e.g. =SUMIFS(C2:C7, A2:A7, E2, B2:B7, F2). It adds all matching rows
    instead of returning one.
- q: How do I use OR instead of AND between the criteria?
  a: Add the conditions instead of multiplying them, e.g. ((A2:A7="East")+(A2:A7="West"))>0.
related:
- - xlookup-google-sheets
  - xlookup-excel
- - index-match-google-sheets
  - index-match-excel
- - vlookup-google-sheets
  - vlookup-excel
- - lookup-multiple-values-google-sheets
  - lookup-multiple-values-excel
- - sumifs-google-sheets
  - sumifs-excel
- - countifs-google-sheets
  - countifs-excel
sibling: vlookup-multiple-criteria-excel
---
VLOOKUP only matches one value, but there are three reliable ways to look up a row that must match two or more conditions: XLOOKUP with multiplied conditions, INDEX MATCH as an array, and VLOOKUP with a helper key. Each is shown below with a worked example.

## Quick answer

Use this formula in Google Sheets:

```excel
=FILTER(C2:C7, A2:A7=E2, B2:B7=F2)
```

FILTER takes one condition per argument and returns every row that meets all of them.

## The problem

Your sales table has a Region column and a Product column. You need the units for one specific region and product, for example West + Apples, but each region appears several times and so does each product.

## Worked example

Find the units for the region in E2 and the product in F2.

| | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| 1 | **Region** | **Product** | **Units** |  | **Region** | **Product** | **Units** |
| 2 | East | Apples | 120 |  | West | Apples | **95** |
| 3 | East | Pears | 80 |  |  |  | **95** |
| 4 | West | Apples | 95 |  |  |  |  |
| 5 | West | Pears | 60 |  |  |  |  |
| 6 | North | Apples | 150 |  |  |  |  |
| 7 | North | Pears | 70 |  |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**G2** — XLOOKUP (Excel) / FILTER (Google Sheets)

```excel
=FILTER(C2:C7, A2:A7=E2, B2:B7=F2)
```

Result: **95**

**G3** — INDEX MATCH version

```excel
=INDEX(C2:C7, MATCH(1, (A2:A7=E2)*(B2:B7=F2), 0))
```

Result: **95**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `(A2:A7=E2)` returns {FALSE;FALSE;TRUE;TRUE;FALSE;FALSE}: which rows are West.
2. `(B2:B7=F2)` returns {TRUE;FALSE;TRUE;FALSE;TRUE;FALSE}: which rows are Apples.
3. Multiplying the two arrays gives {0;0;1;0;0;0}. Only row 3 of the range meets both conditions.
4. XLOOKUP (or MATCH) searches that array for 1 and returns the Units from the same position, 95.
5. Add more conditions by multiplying more comparisons, e.g. `*(D2:D7=G2)`.

## Google Sheets-specific notes

In Google Sheets, FILTER is the most natural way to match several criteria because each condition is simply another argument, and it works without ARRAYFORMULA. It returns all matches, so if duplicates are possible and you only want the first, wrap it in `INDEX(..., 1)`. The VLOOKUP helper-key trick also works in Sheets, but the expression inside the curly braces must be wrapped in ARRAYFORMULA, otherwise only the first row is evaluated.

**First match only**

```excel
=INDEX(FILTER(C2:C7, A2:A7=E2, B2:B7=F2), 1)
```

**VLOOKUP with a virtual helper column**

```excel
=ARRAYFORMULA(VLOOKUP(E2&"|"&F2, {A2:A7&"|"&B2:B7, C2:C7}, 2, FALSE))
```


## Excel version

In Excel, use:

```excel
=XLOOKUP(1, (A2:A7=E2)*(B2:B7=F2), C2:C7)
```

In Excel 365 the usual answer is XLOOKUP with multiplied conditions, which returns only the first match. FILTER also exists in Excel 365.

<!--SIBLING-->


## Common errors and how to fix them

- **#N/A** — No row meets all conditions, or a criterion has a trailing space. **Fix:** Check each condition separately (e.g. `=COUNTIFS(A2:A7,E2,B2:B7,F2)` should be at least 1) and use an if_not_found argument.
- **#VALUE!** — The ranges in the conditions have different sizes. **Fix:** Make every range cover the same rows (A2:A7, B2:B7, C2:C7).
- **Returns the wrong row in older Excel** — The INDEX MATCH array formula was entered with plain Enter in Excel 2019 or older. **Fix:** Re-enter it with Ctrl+Shift+Enter, or use the helper-column method.

## FAQ

### Can VLOOKUP itself take two lookup values?

Not directly. Join the criteria into one key (with a helper column or CHOOSE) so VLOOKUP has a single value to search for.

### How do I sum instead of returning the first match?

Use SUMIFS, e.g. =SUMIFS(C2:C7, A2:A7, E2, B2:B7, F2). It adds all matching rows instead of returning one.

### How do I use OR instead of AND between the criteria?

Add the conditions instead of multiplying them, e.g. ((A2:A7="East")+(A2:A7="West"))>0.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
