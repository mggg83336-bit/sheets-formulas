---
title: How to Use the ROW and COLUMN Functions in Google Sheets
slug: row-column-google-sheets
date: '2026-11-13'
summary: ROW returns the row number of a cell, and COLUMN returns its column number
  (A is 1, B is 2, and so on). Omit the argument to get the number of the cell that
  holds the formula. The related functions ROWS and COLUMNS (plural) count how many
  rows or columns a range spans, which is useful for sizing a f
tags:
- Lookup & reference
- Google Sheets
keyword: row-column-google-sheets
niche: sheets-formulas
provider: structured
entry_id: row-column
platform: Google Sheets
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
- - index-match-google-sheets
  - index-match-excel
- - offset-google-sheets
  - offset-excel
- - indirect-google-sheets
  - indirect-excel
- - sequence-google-sheets
  - sequence-excel
- - last-value-google-sheets
  - last-value-excel
sibling: row-column-excel
---
ROW returns the row number of a cell, and COLUMN returns its column number (A is 1, B is 2, and so on). Omit the argument to get the number of the cell that holds the formula. The related functions ROWS and COLUMNS (plural) count how many rows or columns a range spans, which is useful for sizing a formula or checking that two ranges line up. In Microsoft 365, `ROW(A2:A5)` spills the numbers 2 through 5; in Google Sheets you wrap the same idea in ARRAYFORMULA. These functions work in every Excel version and in Sheets.

## Quick answer

Use this formula in Google Sheets:

```excel
=ROW(A2)
```

Identical syntax in Google Sheets: `ROW([cell_reference])` returns the row number, here 2. `COLUMN([cell_reference])` returns the column number, so `=COLUMN(B2)` is 2. `ROWS` and `COLUMNS` count the size of a range.

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
4. In Microsoft 365, `=ROW(A2:A5)` spills 2, 3, 4 and 5 in one cell. In Google Sheets the same idea is `=ARRAYFORMULA(ROW(A2:A5))`. When you want 1, 2, 3 rather than worksheet rows, [SEQUENCE](../sequence-google-sheets/) is often clearer: `=SEQUENCE(ROWS(A2:A5))`.
5. ROW and COLUMN also feed other functions. [INDEX](../index-match-excel/) and [OFFSET](../offset-google-sheets/) can use them as a row or column index, and [INDIRECT](../indirect-google-sheets/) can build a reference from a column number. Prefer a structured table or a bounded range over a volatile construction when you can.

## Google Sheets-specific notes

Sheets ROW and COLUMN match Excel for a single-cell reference, for the no-argument form that reads the formula's own cell, and for ROWS / COLUMNS counts. The difference is how you fill a column of numbers from one cell. Use ARRAYFORMULA, for example `=ARRAYFORMULA(ROW(A2:A5))` to return 2, 3, 4 and 5, or `=ARRAYFORMULA(IF(A2:A="", "", ROW(A2:A)-ROW(A2)+1))` to number only the filled rows and to keep the sequence correct if rows are inserted above. Open-ended ranges such as A2:A work inside ARRAYFORMULA, but they will also number a total or note at the bottom of the column, so a bounded range or a blank check is safer. SEQUENCE exists in current Sheets and is a clean way to build 1, 2, 3 when you do not need the actual worksheet row. INDEX, OFFSET, and INDIRECT often take ROW or COLUMN as an argument in Sheets the same way they do in Excel. If the file must open in older Excel, stay with the single-cell forms `=ROW(A2)` and `=ROW(A2)-ROW($A$2)+1` and skip ARRAYFORMULA.

**Whole column of row numbers with ARRAYFORMULA**

```excel
=ARRAYFORMULA(ROW(A2:A5))
```

**Item numbers for filled rows only**

```excel
=ARRAYFORMULA(IF(A2:A="", "", ROW(A2:A)-ROW(A2)+1))
```

**Column number of B2**

```excel
=COLUMN(B2)
```

**How many data rows in the list**

```excel
=ROWS(A2:A5)
```


## Excel version

The same formula works unchanged in Excel:

```excel
=ROW(A2)
```

Google Sheets uses the same ROW, COLUMN, ROWS, and COLUMNS functions. To fill a column of row numbers from one cell, wrap ROW in ARRAYFORMULA; Excel 365 can spill from `ROW(A2:A5)` instead.

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

Use [SEQUENCE](../sequence-google-sheets/) when you want an independent list of numbers (1, 2, 3 or a custom start and step) and you are on Microsoft 365 or current Sheets. Use ROW when you need the actual worksheet row, for example to build a reference or to number rows relative to a fixed start cell.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
