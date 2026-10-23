---
title: How to Use HLOOKUP in Excel
slug: hlookup-excel
date: '2026-10-23'
summary: HLOOKUP finds a value in the top row of a table and returns the value from
  a row below it. It is the horizontal twin of VLOOKUP and is the natural choice when
  your months, products or years run across the columns. Below are the syntax, a worked
  monthly report with four lookups, and fixes for the err
tags:
- Lookup & reference
- Excel
keyword: hlookup-excel
niche: sheets-formulas
provider: structured
entry_id: hlookup
platform: Excel
category: lookup
faq:
- q: What is the difference between HLOOKUP and VLOOKUP?
  a: VLOOKUP searches the first column and returns a value from a column to the right;
    HLOOKUP searches the first row and returns a value from a row below. Use the one
    that matches how your headers are laid out.
- q: Can HLOOKUP return a value from a row above the lookup row?
  a: No, it only looks down. Use INDEX with MATCH, or XLOOKUP, which can return from
    any row.
- q: Is HLOOKUP case-sensitive?
  a: No. "mar" and "Mar" match. For a case-sensitive lookup use INDEX and MATCH with
    EXACT.
- q: Should I use XLOOKUP instead of HLOOKUP?
  a: If everyone who opens the file has Microsoft 365, Excel 2021 or Google Sheets,
    XLOOKUP is easier because it does not need a row number and does not break when
    rows are inserted. HLOOKUP is still the most compatible choice for older Excel
    versions.
related:
- - vlookup-excel
  - vlookup-google-sheets
- - xlookup-excel
  - xlookup-google-sheets
- - index-match-excel
  - index-match-google-sheets
- - iferror-excel
  - iferror-google-sheets
- - na-error-excel
  - na-error-google-sheets
sibling: hlookup-google-sheets
---
HLOOKUP finds a value in the top row of a table and returns the value from a row below it. It is the horizontal twin of VLOOKUP and is the natural choice when your months, products or years run across the columns. Below are the syntax, a worked monthly report with four lookups, and fixes for the errors people hit most often.

## Quick answer

Use this formula in Excel:

```excel
=HLOOKUP(A7, $A$1:$E$4, 2, FALSE)
```

Syntax: `HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup])`. Look for the month in A7 in the first row of A1:E4 and return the value from row 2 of that table (Sales). `FALSE` means exact match.

## The problem

Your monthly report has the months across row 1 and metrics such as Sales, Costs and Units down column A. You want to type a month and a metric and get the matching figure, without scrolling across the sheet or rebuilding the table vertically.

## Worked example

A monthly report with months across the top. Rows 7 to 10 hold four lookups; May is not in the table.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Metric** | **Jan** | **Feb** | **Mar** | **Apr** |
| 2 | Sales | 1200 | 1450 | 980 | 1610 |
| 3 | Costs | 700 | 820 | 650 | 900 |
| 4 | Units | 48 | 58 | 39 | 64 |
| 5 |  |  |  |  |  |
| 6 | Month | Metric | Result |  |  |
| 7 | Mar | Sales | **980** |  |  |
| 8 | Feb | Costs | **820** |  |  |
| 9 | Apr | Units | **64** |  |  |
| 10 | May | Sales | **Not found** |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**C7** — Mar sales (row 2 of the table)

```excel
=HLOOKUP(A7, $A$1:$E$4, 2, FALSE)
```

Result: **980**

**C8** — Feb costs (row 3 of the table)

```excel
=HLOOKUP(A8, $A$1:$E$4, 3, FALSE)
```

Result: **820**

**C9** — row number found with MATCH

```excel
=HLOOKUP(A9, $A$1:$E$4, MATCH(B9, $A$1:$A$4, 0), FALSE)
```

Result: **64**

**C10** — month that is not in the table

```excel
=IFERROR(HLOOKUP(A10, $A$1:$E$4, 2, FALSE), "Not found")
```

Result: **Not found**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `A7` is the value to find. HLOOKUP searches for it only in the first row of the table, A1:E1, and finds Mar in column D.
2. `$A$1:$E$4` is the whole table, including the header row and every row you may want to return. The dollar signs keep it fixed when you copy the formula down.
3. `2` is the row to return, counted from the top of the table: 1 is the month row, 2 is Sales, 3 is Costs, 4 is Units. Mar sales is 980.
4. `FALSE` forces an exact match, so "Mar" must appear exactly (case does not matter).
5. Instead of typing the row number, `MATCH(B9, $A$1:$A$4, 0)` finds which row holds "Units" (row 4), so the formula keeps working if you insert a new metric row.
6. Wrapping the formula in IFERROR replaces the #N/A for May with a friendly "Not found".

## Excel-specific notes

HLOOKUP only searches the first row of the table and can only return values from rows below it. The row number is counted inside the table, not on the sheet, so row 2 of A1:E4 is sheet row 2 only because the table starts in row 1. Always pass FALSE (or 0) as the last argument unless the first row is sorted ascending and you really want an approximate match; leaving it out means TRUE. In Microsoft 365 and Excel 2021, XLOOKUP is the more flexible replacement: `=XLOOKUP(A7, $B$1:$E$1, $B$2:$E$2)` does not need a row number and returns a clear "not found" value through its fourth argument.

**XLOOKUP instead of HLOOKUP (Microsoft 365 / Excel 2021)**

```excel
=XLOOKUP(A7, $B$1:$E$1, $B$2:$E$2, "Not found")
```

**INDEX and MATCH in both directions**

```excel
=INDEX($A$1:$E$4, MATCH(B7, $A$1:$A$4, 0), MATCH(A7, $A$1:$E$1, 0))
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=HLOOKUP(A7, $A$1:$E$4, 2, FALSE)
```

Google Sheets uses the same HLOOKUP formula. To return results for several lookup values or several rows at once, wrap it in ARRAYFORMULA.

<!--SIBLING-->


## Common errors and how to fix them

- **#N/A** — The lookup value is not in the first row of the table, or it differs slightly (extra space, number stored as text, "March" vs "Mar"). **Fix:** Check the header with =LEN(D1) or =EXACT(A7, D1), clean the data with TRIM, and wrap the formula in IFERROR for genuinely missing values.
- **#REF!** — The row index is larger than the number of rows in the table, e.g. 5 for A1:E4. **Fix:** Count rows inside the table, or let MATCH calculate the row number.
- **Wrong value returned** — The last argument was left out, so HLOOKUP used an approximate match on an unsorted header row. **Fix:** Always add FALSE (or 0) as the fourth argument for exact matches.
- **Results shift when the formula is copied** — The table range is relative (A1:E4) and moves down as you fill. **Fix:** Lock it with dollar signs, $A$1:$E$4, or press F4 on the reference.

## FAQ

### What is the difference between HLOOKUP and VLOOKUP?

VLOOKUP searches the first column and returns a value from a column to the right; HLOOKUP searches the first row and returns a value from a row below. Use the one that matches how your headers are laid out.

### Can HLOOKUP return a value from a row above the lookup row?

No, it only looks down. Use INDEX with MATCH, or XLOOKUP, which can return from any row.

### Is HLOOKUP case-sensitive?

No. "mar" and "Mar" match. For a case-sensitive lookup use INDEX and MATCH with EXACT.

### Should I use XLOOKUP instead of HLOOKUP?

If everyone who opens the file has Microsoft 365, Excel 2021 or Google Sheets, XLOOKUP is easier because it does not need a row number and does not break when rows are inserted. HLOOKUP is still the most compatible choice for older Excel versions.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
