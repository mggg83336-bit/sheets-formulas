---
title: VLOOKUP with Multiple Criteria in Excel
slug: vlookup-multiple-criteria-excel
date: '2026-10-22'
summary: 'VLOOKUP only matches one value, but there are three reliable ways to look
  up a row that must match two or more conditions: XLOOKUP with multiplied conditions,
  INDEX MATCH as an array, and VLOOKUP with a helper key. Each is shown below with
  a worked example.'
tags:
- Lookup & reference
- Excel
keyword: vlookup-multiple-criteria-excel
niche: sheets-formulas
provider: structured
entry_id: vlookup-multiple-criteria
platform: Excel
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
- - xlookup-excel
  - xlookup-google-sheets
- - index-match-excel
  - index-match-google-sheets
- - vlookup-excel
  - vlookup-google-sheets
- - na-error-excel
  - na-error-google-sheets
- - lookup-multiple-values-excel
  - lookup-multiple-values-google-sheets
- - sumifs-excel
  - sumifs-google-sheets
- - countifs-excel
  - countifs-google-sheets
sibling: vlookup-multiple-criteria-google-sheets
---
VLOOKUP only matches one value, but there are three reliable ways to look up a row that must match two or more conditions: XLOOKUP with multiplied conditions, INDEX MATCH as an array, and VLOOKUP with a helper key. Each is shown below with a worked example.

## Quick answer

Use this formula in Excel:

```excel
=XLOOKUP(1, (A2:A7=E2)*(B2:B7=F2), C2:C7)
```

Each comparison returns TRUE/FALSE for every row. Multiplying them turns TRUE*TRUE into 1, so XLOOKUP finds the first row where both conditions are met.

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
=XLOOKUP(1, (A2:A7=E2)*(B2:B7=F2), C2:C7)
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

## Excel-specific notes

The XLOOKUP version needs Microsoft 365 or Excel 2021+. In Excel 2019 and older use the INDEX MATCH version and confirm it with Ctrl+Shift+Enter, because those versions have no dynamic arrays. If you prefer plain VLOOKUP, add a helper column that joins the criteria (for example `=A2&"|"&B2`), put it as the first column of the lookup range and search for `E2&"|"&F2`. The separator prevents false matches such as "AB"&"C" vs "A"&"BC".

**INDEX MATCH array version (all Excel versions)**

```excel
=INDEX(C2:C7, MATCH(1, (A2:A7=E2)*(B2:B7=F2), 0))
```

**VLOOKUP with a virtual helper column**

```excel
=VLOOKUP(E2&"|"&F2, CHOOSE({1,2}, A2:A7&"|"&B2:B7, C2:C7), 2, FALSE)
```


## Google Sheets version

In Google Sheets, use:

```excel
=FILTER(C2:C7, A2:A7=E2, B2:B7=F2)
```

FILTER is simpler in Google Sheets: one argument per condition, and it returns every match.

<!--SIBLING-->


## Common errors and how to fix them

- **#N/A** — No row meets all conditions, or a criterion has a trailing space. **Fix:** Check each condition separately (e.g. `=COUNTIFS(A2:A7,E2,B2:B7,F2)` should be at least 1) and use an if_not_found argument. When each value exists on its own but the pair still fails, see [how to fix #N/A](../na-error-excel/).
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
