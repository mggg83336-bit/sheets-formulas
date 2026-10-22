---
title: 'How to Fix the #REF! Error in Excel'
slug: ref-error-excel
date: '2026-10-22'
summary: '#REF! means a formula points to a cell that does not exist: it was deleted,
  or the formula asks for a column or row outside its range. In Google Sheets #REF!
  has extra meanings, such as a blocked array or missing IMPORTRANGE permission. Here
  is how to tell which one you have.'
tags:
- Fixing formula errors
- Excel
keyword: ref-error-excel
niche: sheets-formulas
provider: structured
entry_id: ref-error
platform: Excel
category: errors
faq:
- q: Can I recover a formula after
  a: Only with Undo or version history (File > Info > Version History in Excel, File
    > Version history in Google Sheets). The original address is not stored anywhere
    else.
- q: How do I prevent
  a: Use whole ranges, Excel Tables (structured references) or XLOOKUP / INDEX MATCH
    instead of hard-coded column numbers.
related:
- - vlookup-excel
  - vlookup-google-sheets
- - index-match-excel
  - index-match-google-sheets
- - vlookup-another-sheet-excel
  - vlookup-another-sheet-google-sheets
- - iferror-excel
  - iferror-google-sheets
- - na-error-excel
  - na-error-google-sheets
sibling: ref-error-google-sheets
---
#REF! means a formula points to a cell that does not exist: it was deleted, or the formula asks for a column or row outside its range. In Google Sheets #REF! has extra meanings, such as a blocked array or missing IMPORTRANGE permission. Here is how to tell which one you have.

## Quick answer

Use this formula in Excel:

```excel
=VLOOKUP("South", A2:C4, 3, FALSE)
```

The fixed lookup asks for column 3, which exists in the 3-column range A2:C4. Asking for column 4 is what produced the #REF!.

## The problem

After deleting a column, several totals show #REF!. Elsewhere a VLOOKUP shows #REF! even though nothing was deleted.

## Worked example

A 3-column table. The broken formulas ask for a column or row that is not inside the range.

| | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 1 | **Region** | **Q1** | **Q2** |  | **Broken** | **Fixed** |
| 2 | North | 100 | 120 |  | **#REF!** | **95** |
| 3 | South | 90 | 95 |  | **#REF!** | **70** |
| 4 | West | 70 | 88 |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**E2** — column 4 of a 3-column range

```excel
=VLOOKUP("South", A2:C4, 4, FALSE)
```

Result: **#REF!**

**F2**

```excel
=VLOOKUP("South", A2:C4, 3, FALSE)
```

Result: **95**

**E3** — row 4 of a 3-row range

```excel
=INDEX(B2:B4, 4)
```

Result: **#REF!**

**F3**

```excel
=INDEX(B2:B4, 3)
```

Result: **70**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Click the cell and look at the formula. If it literally contains "#REF!", a referenced cell, column or sheet was deleted.
2. If it does not, the formula is asking for a position outside its range, like column 4 of A2:C4 or row 4 of B2:B4.
3. Fix deleted references by undoing the deletion or re-selecting the correct cells.
4. Fix out-of-range positions by correcting the index or widening the range, e.g. A2:D4 if a fourth column really exists.

## Excel-specific notes

When you delete a row, column or sheet that a formula uses, Excel replaces the reference with #REF! inside the formula itself (for example `=SUM(B2,#REF!)`); undo (Ctrl+Z) right away is the quickest fix. Use Find & Select > Find with "#REF!" and Look in: Formulas to list every broken formula. Ranges such as SUM(B2:B10) survive deleting a row inside them; individual references like B2+B3+B4 do not. Excel shows #SPILL!, not #REF!, when a dynamic array is blocked.


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=VLOOKUP("South", A2:C4, 3, FALSE)
```

Google Sheets also uses #REF! for blocked array results, circular dependencies and IMPORTRANGE permission; hover to read the exact message.

<!--SIBLING-->


## Common errors and how to fix them

- **Deleted row, column or sheet** — A formula referenced a cell that was removed. **Fix:** Undo, or rewrite the reference; use ranges rather than single-cell references so deletions inside them are absorbed.
- **Index out of range** — VLOOKUP column number, INDEX row/column or OFFSET points outside the range. **Fix:** Correct the number or enlarge the range.
- **Copied formula moved off the sheet** — Copying =A1 upward or leftward from row 1 or column A would need a cell that does not exist. **Fix:** Use absolute references ($A$1) where the reference should not move.
- **Closed external workbook (Excel) / missing access (Sheets)** — INDIRECT to a closed workbook, or IMPORTRANGE without permission. **Fix:** Open the source workbook, or click Allow access in Google Sheets.

## FAQ

### Can I recover a formula after

Only with Undo or version history (File > Info > Version History in Excel, File > Version history in Google Sheets). The original address is not stored anywhere else.

### How do I prevent

Use whole ranges, Excel Tables (structured references) or XLOOKUP / INDEX MATCH instead of hard-coded column numbers.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
