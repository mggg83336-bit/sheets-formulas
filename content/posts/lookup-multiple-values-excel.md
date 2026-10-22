---
title: How to Lookup and Return Multiple Values in Excel
slug: lookup-multiple-values-excel
date: '2026-10-22'
summary: VLOOKUP and XLOOKUP stop at the first match. When a customer has several
  orders and you need all of them, use FILTER to list every match, or TEXTJOIN to
  put them in one cell. An INDEX/SMALL version for older Excel is included.
tags:
- Lookup & reference
- Excel
keyword: lookup-multiple-values-excel
niche: sheets-formulas
provider: structured
entry_id: lookup-multiple-values
platform: Excel
category: lookup
faq:
- q: Can VLOOKUP return multiple matches?
  a: No, VLOOKUP returns only the first match. Use FILTER (Excel 365, Google Sheets)
    or the INDEX/SMALL array formula in older Excel.
- q: How do I return the matches across columns instead of down?
  a: Wrap the result in TRANSPOSE, e.g. =TRANSPOSE(FILTER(A2:A7, B2:B7=E2)).
related:
- - vlookup-multiple-criteria-excel
  - vlookup-multiple-criteria-google-sheets
- - textjoin-excel
  - textjoin-google-sheets
- - xlookup-excel
  - xlookup-google-sheets
- - count-unique-excel
  - count-unique-google-sheets
sibling: lookup-multiple-values-google-sheets
---
VLOOKUP and XLOOKUP stop at the first match. When a customer has several orders and you need all of them, use FILTER to list every match, or TEXTJOIN to put them in one cell. An INDEX/SMALL version for older Excel is included.

## Quick answer

Use this formula in Excel:

```excel
=FILTER(A2:A7, B2:B7=E2, "No orders")
```

FILTER returns every value in A2:A7 where the customer in B2:B7 equals E2, spilling one result per row. The third argument is shown when nothing matches.

## The problem

Your order log lists each order with its customer. For a given customer you want every order ID, not just the first one VLOOKUP would return.

## Worked example

All orders for the customer in E2.

| | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| 1 | **Order ID** | **Customer** | **Amount** |  | **Customer** | **Orders** | **All in one cell** |
| 2 | 5001 | Acme | 250 |  | Acme | **5001** | **5001, 5003, 5005** |
| 3 | 5002 | Globex | 120 |  |  | **5003** |  |
| 4 | 5003 | Acme | 75 |  |  | **5005** |  |
| 5 | 5004 | Initech | 300 |  |  |  |  |
| 6 | 5005 | Acme | 180 |  |  |  |  |
| 7 | 5006 | Globex | 90 |  |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**F2** — spills down to F4

```excel
=FILTER(A2:A7, B2:B7=E2, "No orders")
```

Results: **5001**, **5003**, **5005**

**G2** — joined into one cell

```excel
=TEXTJOIN(", ", TRUE, FILTER(A2:A7, B2:B7=E2))
```

Result: **5001, 5003, 5005**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `B2:B7=E2` is evaluated for every row and returns TRUE for the three Acme rows.
2. FILTER keeps only the rows of A2:A7 where that test is TRUE and spills them downward.
3. TEXTJOIN joins the filtered list with ", " and TRUE skips empty values.
4. The results update automatically when orders are added inside the range; use a bigger range or an Excel Table to include future rows.

## Excel-specific notes

FILTER needs Microsoft 365 or Excel 2021+. For Excel 2019 and older, use the INDEX/SMALL formula below in F2, confirm with Ctrl+Shift+Enter in versions before 365, and copy it down as many rows as the largest possible number of matches; extra rows show blank. Add SORT around FILTER to order the results, e.g. `=SORT(FILTER(A2:C7, B2:B7=E2), 3, -1)` to sort by amount, largest first.

**All matches in one cell**

```excel
=TEXTJOIN(", ", TRUE, FILTER(A2:A7, B2:B7=E2))
```

**Older Excel (copy down; array formula)**

```excel
=IFERROR(INDEX($A$2:$A$7, SMALL(IF($B$2:$B$7=$E$2, ROW($B$2:$B$7)-ROW($B$2)+1), ROWS($F$2:F2))), "")
```


## Google Sheets version

In Google Sheets, use:

```excel
=FILTER(A2:A7, B2:B7=E2)
```

Google Sheets' FILTER has no if_empty argument, so use IFNA(FILTER(...), "No orders").

<!--SIBLING-->


## Common errors and how to fix them

- **#CALC! (Excel) / #N/A (Google Sheets)** — No row matched and no if_empty value was given. **Fix:** Use FILTER's third argument in Excel, or IFNA in Google Sheets.
- **#SPILL! / #REF!** — Cells below the formula are not empty, so the list cannot expand. **Fix:** Clear the cells below the formula.
- **#VALUE!** — The condition range has a different size than the range being filtered. **Fix:** Make both ranges cover the same rows.

## FAQ

### Can VLOOKUP return multiple matches?

No, VLOOKUP returns only the first match. Use FILTER (Excel 365, Google Sheets) or the INDEX/SMALL array formula in older Excel.

### How do I return the matches across columns instead of down?

Wrap the result in TRANSPOSE, e.g. =TRANSPOSE(FILTER(A2:A7, B2:B7=E2)).

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
