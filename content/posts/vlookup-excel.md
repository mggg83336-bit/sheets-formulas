---
title: How to Use VLOOKUP in Excel
slug: vlookup-excel
date: '2026-10-22'
summary: VLOOKUP finds a value in the first column of a table and returns a value
  from another column in the same row. This guide shows the exact syntax, a worked
  price-list example, why you should almost always use FALSE for an exact match, and
  how to fix the errors people hit most often.
tags:
- Lookup & reference
- Excel
keyword: vlookup-excel
niche: sheets-formulas
provider: structured
entry_id: vlookup
platform: Excel
category: lookup
faq:
- q: Can VLOOKUP look to the left?
  a: No. VLOOKUP only searches the first column of the range and returns values to
    its right. Use XLOOKUP or INDEX with MATCH to return a column on the left.
- q: Is VLOOKUP case-sensitive?
  a: No. "p-104" and "P-104" are treated as the same value. For a case-sensitive lookup,
    use INDEX and MATCH with EXACT inside an array formula.
- q: What is the difference between TRUE and FALSE in VLOOKUP?
  a: FALSE returns only exact matches. TRUE (or leaving the argument out) does an
    approximate match and requires the first column to be sorted in ascending order;
    it returns the largest value less than or equal to the lookup value.
related:
- - xlookup-excel
  - xlookup-google-sheets
- - index-match-excel
  - index-match-google-sheets
- - vlookup-multiple-criteria-excel
  - vlookup-multiple-criteria-google-sheets
- - vlookup-another-sheet-excel
  - vlookup-another-sheet-google-sheets
- - na-error-excel
  - na-error-google-sheets
- - iferror-excel
  - iferror-google-sheets
sibling: vlookup-google-sheets
---
VLOOKUP finds a value in the first column of a table and returns a value from another column in the same row. This guide shows the exact syntax, a worked price-list example, why you should almost always use FALSE for an exact match, and how to fix the errors people hit most often.

## Quick answer

Use this formula in Excel:

```excel
=VLOOKUP(F2, $A$2:$D$6, 3, FALSE)
```

Syntax: `VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])`. Look up F2 in the first column of A2:D6 and return the value from the 3rd column of that range (column C). FALSE means exact match only.

## The problem

You have a product table with IDs in the first column and prices and stock levels in the columns to the right. Somewhere else (an order form, a report) you type a product ID and want the price to appear automatically instead of scrolling and copying it by hand.

## Worked example

Product IDs are in column A. The ID to find is typed in F2, and G2 and H2 return its price and stock.

| | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| 1 | **Product ID** | **Product** | **Price** | **Stock** |  | **Lookup ID** | **Price** | **Stock** |
| 2 | P-101 | Wireless Mouse | 24.99 | 120 |  | P-104 | **54.9** | **18** |
| 3 | P-102 | USB-C Hub | 39.5 | 45 |  |  |  |  |
| 4 | P-103 | Laptop Stand | 32 | 0 |  |  |  |  |
| 5 | P-104 | Webcam HD | 54.9 | 18 |  |  |  |  |
| 6 | P-105 | Desk Lamp | 27.75 | 60 |  |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**G2** — price of the ID in F2

```excel
=VLOOKUP(F2, $A$2:$D$6, 3, FALSE)
```

Result: **54.9**

**H2** — stock of the same ID

```excel
=VLOOKUP(F2, $A$2:$D$6, 4, FALSE)
```

Result: **18**

The column number counts from the first column of the table range, not from column A of the sheet. If your table started in column C, the price would still be column 3 of the range.

<!--AD_IN_ARTICLE-->

## How the formula works

1. `F2` is the value to find (P-104).
2. `$A$2:$D$6` is the table. VLOOKUP always searches the **leftmost** column of this range, so the IDs must be in column A here. The dollar signs keep the range fixed when you copy the formula down.
3. `3` tells VLOOKUP to return the value from the third column of the range (Price). Use 4 for Stock.
4. `FALSE` forces an exact match. If you leave it out, VLOOKUP assumes the first column is sorted and does an approximate match, which can quietly return the wrong row.
5. VLOOKUP stops at the first match it finds. If an ID appears twice, only the first row is used.

## Excel-specific notes

In Microsoft 365 and Excel 2021 you can look up a whole list at once: `=VLOOKUP(F2:F10, $A$2:$D$6, 3, FALSE)` spills one result per ID. If you are on Microsoft 365, XLOOKUP is usually the better choice because it can look left, defaults to an exact match and does not break when you insert a column inside the table. VLOOKUP is still worth knowing because it works in every Excel version back to the 1990s and in files you share with people on older versions.

**Same lookup with XLOOKUP (Microsoft 365 / Excel 2021+)**

```excel
=XLOOKUP(F2, $A$2:$A$6, $C$2:$C$6, "Not found")
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=VLOOKUP(F2, $A$2:$D$6, 3, FALSE)
```

Google Sheets uses the same syntax (the last argument is called is_sorted). To return a whole column of results, wrap the formula in ARRAYFORMULA.

<!--SIBLING-->


## Common errors and how to fix them

- **#N/A** — The lookup value is not in the first column, often because of an extra space or because one side is a number and the other is text that looks like a number. **Fix:** Check the value with `=LEN(F2)`, clean it with TRIM, or convert it with VALUE / TEXT so both sides match. Wrap the formula in IFNA to show a friendly message: `=IFNA(VLOOKUP(...), "Not found")`.
- **#REF!** — The column number is larger than the number of columns in the table range (for example 5 for A2:D6). **Fix:** Use a column number that exists inside the range, or widen the range.
- **Wrong value returned, no error** — The fourth argument was omitted or set to TRUE, so an approximate match was used on unsorted data. **Fix:** Always end the formula with FALSE unless you deliberately want a range lookup on sorted data (for example tax brackets).
- **Results break after inserting a column** — The column number is a hard-coded 3, so inserting a column inside the table shifts the data but not the number. **Fix:** Use `MATCH("Price", $A$1:$D$1, 0)` as the column number, or switch to XLOOKUP / INDEX MATCH.

## FAQ

### Can VLOOKUP look to the left?

No. VLOOKUP only searches the first column of the range and returns values to its right. Use XLOOKUP or INDEX with MATCH to return a column on the left.

### Is VLOOKUP case-sensitive?

No. "p-104" and "P-104" are treated as the same value. For a case-sensitive lookup, use INDEX and MATCH with EXACT inside an array formula.

### What is the difference between TRUE and FALSE in VLOOKUP?

FALSE returns only exact matches. TRUE (or leaving the argument out) does an approximate match and requires the first column to be sorted in ascending order; it returns the largest value less than or equal to the lookup value.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
