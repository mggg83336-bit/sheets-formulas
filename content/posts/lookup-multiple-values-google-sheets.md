---
title: How to Lookup and Return Multiple Values in Google Sheets
slug: lookup-multiple-values-google-sheets
date: '2026-10-23'
summary: VLOOKUP and XLOOKUP stop at the first match. When a customer has several
  orders and you need all of them, use FILTER to list every match, or TEXTJOIN to
  put them in one cell. An INDEX/SMALL version for older Excel is included.
tags:
- Lookup & reference
- Google Sheets
keyword: lookup-multiple-values-google-sheets
niche: sheets-formulas
provider: structured
entry_id: lookup-multiple-values
platform: Google Sheets
category: lookup
faq:
- q: Can VLOOKUP return multiple matches?
  a: No, VLOOKUP returns only the first match. Use FILTER (Excel 365, Google Sheets)
    or the INDEX/SMALL array formula in older Excel.
- q: How do I return the matches across columns instead of down?
  a: Wrap the result in TRANSPOSE, e.g. =TRANSPOSE(FILTER(A2:A7, B2:B7=E2)).
related:
- - vlookup-multiple-criteria-google-sheets
  - vlookup-multiple-criteria-excel
- - textjoin-google-sheets
  - textjoin-excel
- - xlookup-google-sheets
  - xlookup-excel
- - count-unique-google-sheets
  - count-unique-excel
sibling: lookup-multiple-values-excel
---
VLOOKUP and XLOOKUP stop at the first match. When a customer has several orders and you need all of them, use FILTER to list every match, or TEXTJOIN to put them in one cell. An INDEX/SMALL version for older Excel is included.

## Quick answer

Use this formula in Google Sheets:

```excel
=FILTER(A2:A7, B2:B7=E2)
```

Google Sheets FILTER takes the range and one or more conditions. It has no "if empty" argument, so wrap it in IFERROR or IFNA for a custom message.

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
=FILTER(A2:A7, B2:B7=E2)
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

## Google Sheets-specific notes

Google Sheets' FILTER does not have Excel's third if_empty argument; when nothing matches it returns #N/A with the message "No matches are found in FILTER evaluation". Use `=IFNA(FILTER(A2:A7, B2:B7=E2), "No orders")`. QUERY is a powerful alternative in Sheets: it can filter, sort and pick columns in one formula using a SQL-like language, which is handy when you need several columns of each matching row.

**Custom message when nothing matches**

```excel
=IFNA(FILTER(A2:A7, B2:B7=E2), "No orders")
```

**QUERY version (orders and amounts, largest first)**

```excel
=QUERY(A2:C7, "select A, C where B = '"&E2&"' order by C desc", 0)
```


## Excel version

In Excel, use:

```excel
=FILTER(A2:A7, B2:B7=E2, "No orders")
```

FILTER works the same in Excel 365 and Excel 2021. Older Excel needs the INDEX/SMALL array formula instead.

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
