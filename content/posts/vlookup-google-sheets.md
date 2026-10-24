---
title: How to Use VLOOKUP in Google Sheets
slug: vlookup-google-sheets
date: '2026-10-23'
summary: VLOOKUP finds a value in the first column of a table and returns a value
  from another column in the same row. This guide shows the exact syntax, a worked
  price-list example, why you should almost always use FALSE for an exact match, and
  how to fix the errors people hit most often.
tags:
- Lookup & reference
- Google Sheets
keyword: vlookup-google-sheets
niche: sheets-formulas
provider: structured
entry_id: vlookup
platform: Google Sheets
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
- q: Why does VLOOKUP return 0?
  a: 'The lookup found a row, and the cell it returned was empty. Excel and Google
    Sheets turn that empty cell into 0. A missing key is a different result, #N/A.
    IFERROR and IFNA only replace errors, so they leave the 0 in place. Use the INDEX
    test or XLOOKUP with a blanked return range, in the section above, when you need
    a blank cell instead.'
related:
- - xlookup-google-sheets
  - xlookup-excel
- - iferror-google-sheets
  - iferror-excel
- - na-error-google-sheets
  - na-error-excel
- - index-match-google-sheets
  - index-match-excel
- - vlookup-multiple-criteria-google-sheets
  - vlookup-multiple-criteria-excel
- - vlookup-another-sheet-google-sheets
  - vlookup-another-sheet-excel
- - lookup-multiple-values-google-sheets
  - lookup-multiple-values-excel
- - xlookup-return-multiple-columns-google-sheets
  - xlookup-return-multiple-columns-excel
- - last-value-google-sheets
  - last-value-excel
sibling: vlookup-excel
---
VLOOKUP finds a value in the first column of a table and returns a value from another column in the same row. This guide shows the exact syntax, a worked price-list example, why you should almost always use FALSE for an exact match, and how to fix the errors people hit most often.

## Quick answer

Use this formula in Google Sheets:

```excel
=VLOOKUP(F2, $A$2:$D$6, 3, FALSE)
```

Syntax: `VLOOKUP(search_key, range, index, [is_sorted])`. Google Sheets names the last argument is_sorted, but it behaves the same way: FALSE (or 0) means exact match.

<!--CTA_PROMINENT-->

## VLOOKUP returns 0 or blank cell

A match and a missing key are different problems. If the ID is not in the first column, VLOOKUP returns [#N/A](../na-error-excel/). If the ID is found but the cell you return is empty, VLOOKUP returns 0. [IFERROR](../iferror-google-sheets/) and IFNA only replace errors, so they leave that 0 on the sheet.

An empty cell and a stored 0 are not the same. In the worked example further down, the Laptop Stand has stock 0, and that 0 should stay. Test the source cell with INDEX, which can tell an empty cell from a real zero. LET calculates it once (Microsoft 365, Excel 2021, and Google Sheets):

```excel
=LET(
  src, INDEX($C$2:$C$6, MATCH(F2, $A$2:$A$6, 0)),
  IF(src="", "", src)
)
```

Without LET, write the test twice:

```excel
=IF(INDEX($C$2:$C$6, MATCH(F2, $A$2:$A$6, 0))="", "", INDEX($C$2:$C$6, MATCH(F2, $A$2:$A$6, 0)))
```

A shorter IF blanks every zero, including a real stock of 0. Use it only when 0 and blank mean the same thing in your sheet:

```excel
=IF(VLOOKUP(F2, $A$2:$D$6, 3, FALSE)=0, "", VLOOKUP(F2, $A$2:$D$6, 3, FALSE))
```

`&""` is a last resort, not a blank. Appending `""` turns the result into text, so a price of 54.9 becomes the text "54.9" and an empty cell becomes the text "0". You still see a zero, and you can no longer sum the column. It is useful only when the next step is text, for example forcing a code to match text with `F2&""`.

Prefer [XLOOKUP](../xlookup-excel/) when the file opens in Microsoft 365, Excel 2021 or later, or Google Sheets. The `if_not_found` argument covers a missing key only. To also keep an empty price blank, and still return a real 0, blank the return range first:

```excel
=XLOOKUP(F2, $A$2:$A$6, IF($C$2:$C$6="", "", $C$2:$C$6), "")
```

The fourth argument `""` is what you show when F2 is not in the list. Use `"Not found"` if you would rather see words than a blank cell.

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

## Google Sheets-specific notes

Google Sheets uses the same arguments as Excel, but the fourth one is called `is_sorted`. To fill a whole column of results with one formula, wrap it in ARRAYFORMULA and use an open-ended range, for example `=ARRAYFORMULA(IF(F2:F="", "", VLOOKUP(F2:F, $A$2:$D$6, 3, FALSE)))`. The IF part keeps empty rows blank instead of showing #N/A. Sheets also has XLOOKUP, so you can look up columns to the left without rearranging your data.

**Fill an entire column with one formula**

```excel
=ARRAYFORMULA(IF(F2:F="", "", VLOOKUP(F2:F, $A$2:$D$6, 3, FALSE)))
```


## Excel version

The same formula works unchanged in Excel:

```excel
=VLOOKUP(F2, $A$2:$D$6, 3, FALSE)
```

Excel's VLOOKUP syntax is identical. In Microsoft 365 a range as the first argument spills results automatically, without ARRAYFORMULA.

<!--SIBLING-->


## Common errors and how to fix them

- **#N/A** — The lookup value is not in the first column, often because of an extra space or because one side is a number and the other is text that looks like a number. **Fix:** Check the value with `=LEN(F2)`, clean it with TRIM, or convert it with VALUE / TEXT so both sides match. Wrap the formula in IFNA to show a friendly message: `=IFNA(VLOOKUP(...), "Not found")`.
- **#REF!** — The column number is larger than the number of columns in the table range (for example 5 for A2:D6). **Fix:** Use a column number that exists inside the range, or widen the range.
- **Wrong value returned, no error** — The fourth argument was omitted or set to TRUE, so an approximate match was used on unsorted data. **Fix:** Always end the formula with FALSE unless you deliberately want a range lookup on sorted data (for example tax brackets).
- **Results break after inserting a column** — The column number is a hard-coded 3, so inserting a column inside the table shifts the data but not the number. **Fix:** Use `MATCH("Price", $A$1:$D$1, 0)` as the column number, or switch to XLOOKUP / INDEX MATCH.

<!--CTA_AFTER_ERRORS-->

## FAQ

### Can VLOOKUP look to the left?

No. VLOOKUP only searches the first column of the range and returns values to its right. Use XLOOKUP or INDEX with MATCH to return a column on the left.

### Is VLOOKUP case-sensitive?

No. "p-104" and "P-104" are treated as the same value. For a case-sensitive lookup, use INDEX and MATCH with EXACT inside an array formula.

### What is the difference between TRUE and FALSE in VLOOKUP?

FALSE returns only exact matches. TRUE (or leaving the argument out) does an approximate match and requires the first column to be sorted in ascending order; it returns the largest value less than or equal to the lookup value.

### Why does VLOOKUP return 0?

The lookup found a row, and the cell it returned was empty. Excel and Google Sheets turn that empty cell into 0. A missing key is a different result, #N/A. IFERROR and IFNA only replace errors, so they leave the 0 in place. Use the INDEX test or XLOOKUP with a blanked return range, in the section above, when you need a blank cell instead.

## Related formulas

<!--RELATED-->
