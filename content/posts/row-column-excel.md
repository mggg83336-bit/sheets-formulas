---
title: How to Use the ROW and COLUMN Functions in Excel
slug: row-column-excel
date: '2026-11-13'
summary: ROW returns the row number of a cell, and COLUMN returns its column number
  (A is 1, B is 2, and so on). Omit the argument to get the number of the cell that
  holds the formula. The related functions ROWS and COLUMNS (plural) count how many
  rows or columns a range spans, which is useful for sizing a f
tags:
- Lookup & reference
- Excel
keyword: row-column-excel
niche: sheets-formulas
provider: structured
entry_id: row-column
platform: Excel
category: lookup
faq:
- q: What is the difference between ROW and ROWS?
  a: ROW returns a position (the row number of a cell). ROWS returns a count (how
    many rows a range spans). The same split applies to COLUMN and COLUMNS. In the
    worked example, ROW(A2) is 2 and ROWS(A2:A5) is 4.
- q: How do I number a list starting at 1?
  a: Use =ROW(A2)-ROW($A$2)+1 on the first data row and copy it down. In Microsoft
    365, =SEQUENCE(ROWS(A2:A5)) or =ROW(A2:A5)-ROW(A2)+1 will spill the same numbers.
    In Sheets, wrap the second form in ARRAYFORMULA.
- q: Can ROW return every row number in a range at once?
  a: Yes in Microsoft 365, where =ROW(A2:A5) spills. In Google Sheets, use =ARRAYFORMULA(ROW(A2:A5)).
    In older Excel you have to copy a single-cell formula down.
- q: When should I use SEQUENCE instead of ROW?
  a: Use SEQUENCE when you want an independent list of numbers (1, 2, 3 or a custom
    start and step) and you are on Microsoft 365 or current Sheets. Use ROW when you
    need the actual worksheet row, for example to build a reference or to number rows
    relative to a fixed start cell.
related:
- - index-match-excel
  - index-match-google-sheets
- - offset-excel
  - offset-google-sheets
- - indirect-excel
  - indirect-google-sheets
- - sequence-excel
  - sequence-google-sheets
- - last-value-excel
  - last-value-google-sheets
sibling: row-column-google-sheets
---
ROW returns the row number of a cell, and COLUMN returns its column number (A is 1, B is 2, and so on). Omit the argument to get the number of the cell that holds the formula. The related functions ROWS and COLUMNS (plural) count how many rows or columns a range spans, which is useful for sizing a formula or checking that two ranges line up. In Microsoft 365, `ROW(A2:A5)` spills the numbers 2 through 5; in Google Sheets you wrap the same idea in ARRAYFORMULA. These functions work in every Excel version and in Sheets.

## Quick answer

Use this formula in Excel:

```excel
=ROW(A2)
```

Syntax: `ROW([reference])` returns the row number of that cell — here 2. `COLUMN([reference])` does the same for columns, so `=COLUMN(B2)` returns 2. With no argument, `=ROW()` and `=COLUMN()` return the position of the formula's own cell. `ROWS(range)` and `COLUMNS(range)` return the height and width of a range, not a sheet position.

## The problem

You want serial numbers that stay correct when rows are inserted, the column number of a header, and the height or width of a block, without typing 1, 2, 3 by hand each time the list changes.

## Worked example

Four names and amounts. D2 returns the row number of A2, D3 the column number of B2, D4 the number of data rows, and D5 the number of columns in A1:C5. C2 shows a serial number that stays correct if you insert rows above the list.

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **Name** | **Amount** | **Item #** | **Result** |
| 2 | Ann | 100 | **1** | **2** |
| 3 | Ben | 85 |  | **2** |
| 4 | Cara | 120 |  | **4** |
| 5 | Dan | 60 |  | **3** |

Formulas used in the example (results shown in **bold** in the table above):

**D2** — row number of A2

```excel
=ROW(A2)
```

Result: **2**

**D3** — column number of B2

```excel
=COLUMN(B2)
```

Result: **2**

**D4** — how many data rows

```excel
=ROWS(A2:A5)
```

Result: **4**

**D5** — how many columns in A1:C5

```excel
=COLUMNS(A1:C5)
```

Result: **3**

**C2** — item number that survives inserted rows

```excel
=ROW(A2)-ROW($A$2)+1
```

Result: **1**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `=ROW(A2)` returns 2, the worksheet row that holds Ann. `=COLUMN(B2)` returns 2, because column B is the second column.
2. `=ROWS(A2:A5)` counts the rows in that block and returns 4. `=COLUMNS(A1:C5)` counts the columns and returns 3. These two functions measure size, not position.
3. `=ROW(A2)-ROW($A$2)+1` returns 1, a serial number for the first data row. Copy it down and Ben, Cara and Dan become 2, 3 and 4. If you insert a row above the table, both ROW calls move together, so the numbers stay 1 through 4.
4. In Microsoft 365, `=ROW(A2:A5)` spills 2, 3, 4 and 5 in one cell. In Google Sheets the same idea is `=ARRAYFORMULA(ROW(A2:A5))`. When you want 1, 2, 3 rather than worksheet rows, [SEQUENCE](../sequence-excel/) is often clearer: `=SEQUENCE(ROWS(A2:A5))`.
5. ROW and COLUMN also feed other functions. [INDEX](../index-match-excel/) and [OFFSET](../offset-excel/) can use them as a row or column index, and [INDIRECT](../indirect-excel/) can build a reference from a column number. Prefer a structured table or a bounded range over a volatile construction when you can.

## Excel-specific notes

ROW and COLUMN are available in every Excel version, including older ones that lack SEQUENCE. A reliable way to number a list is `=ROW(A2)-ROW($A$2)+1`, which returns 1 on the first data row and keeps working if you insert rows above the table, because both ROW calls shift together. `=ROW()` with no argument is shorter but breaks if you later move the formula to a helper column on a different row. In Microsoft 365, `=ROW(A2:A5)` spills {2;3;4;5}, and `=SEQUENCE(ROWS(A2:A5))` is often clearer when you want 1, 2, 3 rather than worksheet row numbers. COLUMN is the usual tool when a formula needs a numeric column index, for example inside INDEX or OFFSET, or when you convert a number to a column letter with `=SUBSTITUTE(ADDRESS(1, COLUMN(B2), 4), "1", "")`, which returns B. `#REF!` appears if the reference points at a deleted cell. Do not confuse ROW with ROWS: `ROW(A2:A5)` in older Excel returns only 2 (the first row of the range) unless the formula is entered as an array or, in 365, allowed to spill.

**Column number of B2**

```excel
=COLUMN(B2)
```

**How many data rows in the list**

```excel
=ROWS(A2:A5)
```

**How many columns in A1:C5**

```excel
=COLUMNS(A1:C5)
```

**Item number that survives inserted rows**

```excel
=ROW(A2)-ROW($A$2)+1
```

**Microsoft 365 spill of row numbers**

```excel
=ROW(A2:A5)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=ROW(A2)
```

Excel uses the same ROW and COLUMN formulas. Whole-column fills in Excel 365 spill from `ROW(A2:A5)`; in Sheets you wrap ROW in ARRAYFORMULA. SEQUENCE is available in current Sheets and in Microsoft 365, but not in older Excel.

<!--SIBLING-->


## Common errors and how to fix them

- **Serial numbers jump after you insert or delete rows** — The formula used `=ROW()` or `=ROW()-1` with no reference, so it is tied to the formula's current worksheet row, not to the data row. **Fix:** Use `=ROW(A2)-ROW($A$2)+1` (adjust A2 to the first data cell) so both references shift together when rows are inserted above.
- **ROW(A2:A5) returns only 2, not a list of numbers** — In older Excel, ROW and COLUMN return the first row or column of a multi-cell range unless the formula is entered as an array. Excel 365 will spill; older versions will not. **Fix:** In Microsoft 365, confirm the formula can spill. In older Excel, copy `=ROW(A2)` down the column. In Google Sheets, wrap the range form in ARRAYFORMULA.
- **#REF!** — The reference argument points at a cell that was deleted, or at a closed workbook. **Fix:** Point ROW or COLUMN at a cell that still exists on the sheet, or use the no-argument form if you only need the formula's own position.
- **COLUMN returns 3 when you expected 2** — Columns were inserted to the left, or the reference is not the cell you thought (for example COLUMN(C2) when you meant B2). **Fix:** Check the reference. COLUMN counts from A = 1, so C is always 3 unless you subtract a starting column, such as `=COLUMN(C2)-COLUMN($A$2)+1`.

## FAQ

### What is the difference between ROW and ROWS?

ROW returns a position (the row number of a cell). ROWS returns a count (how many rows a range spans). The same split applies to COLUMN and COLUMNS. In the worked example, `ROW(A2)` is 2 and `ROWS(A2:A5)` is 4.

### How do I number a list starting at 1?

Use `=ROW(A2)-ROW($A$2)+1` on the first data row and copy it down. In Microsoft 365, `=SEQUENCE(ROWS(A2:A5))` or `=ROW(A2:A5)-ROW(A2)+1` will spill the same numbers. In Sheets, wrap the second form in ARRAYFORMULA.

### Can ROW return every row number in a range at once?

Yes in Microsoft 365, where `=ROW(A2:A5)` spills. In Google Sheets, use `=ARRAYFORMULA(ROW(A2:A5))`. In older Excel you have to copy a single-cell formula down.

### When should I use SEQUENCE instead of ROW?

Use [SEQUENCE](../sequence-excel/) when you want an independent list of numbers (1, 2, 3 or a custom start and step) and you are on Microsoft 365 or current Sheets. Use ROW when you need the actual worksheet row, for example to build a reference or to number rows relative to a fixed start cell.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
