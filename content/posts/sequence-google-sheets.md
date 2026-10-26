---
title: How to Use the SEQUENCE Function in Google Sheets
slug: sequence-google-sheets
date: '2026-10-26'
summary: 'SEQUENCE generates a list or grid of numbers with one formula: row numbers,
  steps of 10, a numbered grid, or a series of dates. This guide covers the four arguments,
  numbering a list that grows, step and start values, two-dimensional grids, and how
  Excel and Google Sheets differ.'
tags:
- Lookup & reference
- Google Sheets
keyword: sequence-google-sheets
niche: sheets-formulas
provider: structured
entry_id: sequence
platform: Google Sheets
category: lookup
faq:
- q: How do I make a list of dates with SEQUENCE?
  a: Add SEQUENCE to a start date, e.g. =DATE(2026,11,2)+SEQUENCE(7,1,0,1) for seven
    consecutive days, or use step 7 for weekly dates. Format the cells as dates. In
    Google Sheets wrap it in ARRAYFORMULA if it does not spill.
- q: Can SEQUENCE count down?
  a: Yes, use a negative step. =SEQUENCE(5, 1, 5, -1) returns 5, 4, 3, 2, 1 in both
    Excel and Google Sheets.
- q: What is the difference between SEQUENCE and ROW?
  a: ROW returns the row number of a cell, so =ROW()-1 must be filled down and breaks
    when rows move. SEQUENCE builds the whole list from one cell and can set any start,
    step and number of columns.
related:
- - sortby-excel
- - sort-google-sheets
  - sort-excel
- - unique-google-sheets
  - unique-excel
- - filter-google-sheets
  - filter-excel
- - transpose-google-sheets
  - transpose-excel
sibling: sequence-excel
---
SEQUENCE generates a list or grid of numbers with one formula: row numbers, steps of 10, a numbered grid, or a series of dates. This guide covers the four arguments, numbering a list that grows, step and start values, two-dimensional grids, and how Excel and Google Sheets differ.

## Quick answer

Use this formula in Google Sheets:

```excel
=SEQUENCE(COUNTA(A2:A))
```

Same arguments in Google Sheets: `SEQUENCE(rows, [columns], [start], [step])`. The open-ended range A2:A counts every task in the column, so the numbering grows as you add rows.

## The problem

You keep a task list and want a number column next to it that stays correct when tasks are added, without dragging the fill handle every time. You also need a column of round numbers (10, 20, 30...), a small numbered grid for a seating plan, and a quick way to add up a series without typing it out. SEQUENCE does all of these from one cell.

## Worked example

A five-task list in column A. Each formula is typed once in row 2 and spills.

| | A | B | C | D | E | F | G | H | I | J |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Task** | **No.** |  | **Step 10** |  | **Grid** |  |  |  | **Sum 1..10** |
| 2 | Write | **1** |  | **10** |  | **1** | **2** | **3** |  | **55** |
| 3 | Review | **2** |  | **20** |  | **4** | **5** | **6** |  |  |
| 4 | Test | **3** |  | **30** |  |  |  |  |  |  |
| 5 | Ship | **4** |  | **40** |  |  |  |  |  |  |
| 6 | Docs | **5** |  | **50** |  |  |  |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**B2** — number the tasks 1 to 5

```excel
=SEQUENCE(COUNTA(A2:A6))
```

Results: **1**, **2**, **3**, **4**, **5**

**D2** — start at 10, step by 10

```excel
=SEQUENCE(5, 1, 10, 10)
```

Results: **10**, **20**, **30**, **40**, **50**

**F2** — a 2-row by 3-column grid (fills across, then down)

```excel
=SEQUENCE(2, 3)
```

Results: **1**, **2**, **3**, **4**, **5**, **6**

**J2** — add up 1 to 10 without typing the numbers

```excel
=SUM(SEQUENCE(10))
```

Result: **55**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `COUNTA(A2:A6)` counts the non-empty task cells, which is 5. `SEQUENCE(5)` then returns 1, 2, 3, 4, 5 into B2:B6.
2. The third and fourth arguments set the first value and the step. `SEQUENCE(5, 1, 10, 10)` returns 5 rows and 1 column starting at 10 and adding 10 each time: 10, 20, 30, 40, 50.
3. With two dimensions SEQUENCE fills across the row first and then moves down. `SEQUENCE(2, 3)` puts 1, 2, 3 in F2:H2 and 4, 5, 6 in F3:H3.
4. SEQUENCE can feed other functions without spilling at all. `SUM(SEQUENCE(10))` adds 1 to 10 and returns 55 in a single cell.
5. Add a task in A7 and widen the COUNTA range (or use A2:A in Google Sheets): the numbering updates by itself, with no fill handle.

## Google Sheets-specific notes

Google Sheets supports SEQUENCE in every version and accepts open-ended ranges such as A2:A, which makes self-extending numbering very easy. If the result would overwrite data, Sheets shows #REF! ("Array result was not expanded") instead of #SPILL!. Before SEQUENCE existed, the common Sheets pattern was `=ARRAYFORMULA(ROW(A2:A6)-1)`, which you will still see in older templates. To number only rows that are filled in a column with gaps, use `=ARRAYFORMULA(IF(A2:A="", "", COUNTIFS(A2:A, "<>", ROW(A2:A), "<="&ROW(A2:A))))`.

**Older ARRAYFORMULA pattern**

```excel
=ARRAYFORMULA(ROW(A2:A6)-1)
```

**Five dates one week apart**

```excel
=ARRAYFORMULA(DATE(2026,11,2)+SEQUENCE(5,1,0,7))
```

**Number only filled rows (gaps allowed)**

```excel
=ARRAYFORMULA(IF(A2:A="", "", COUNTIFS(A2:A, "<>", ROW(A2:A), "<="&ROW(A2:A))))
```


## Excel version

In Excel, use:

```excel
=SEQUENCE(COUNTA(A2:A6))
```

Excel spills the result and shows #SPILL! when the target cells are not empty. It is not available in Excel 2019 or older, where the usual workaround is =ROW()-1 filled down.

<!--SIBLING-->


## Common errors and how to fix them

- **#SPILL! (Excel) / #REF! (Google Sheets)** — Something is already typed in the cells the sequence needs. **Fix:** Clear the cells below or to the right of the formula, or move the formula.
- **#VALUE!** — rows or columns is 0, negative or text, for example when COUNTA counts an empty range. **Fix:** Make sure the count is at least 1, e.g. =IF(COUNTA(A2:A6)=0, "", SEQUENCE(COUNTA(A2:A6))).
- **#NAME?** — The file is opened in Excel 2019 or older, which has no SEQUENCE. **Fix:** Use =ROW()-1 filled down, or open the file in Microsoft 365, Excel 2021+ or Google Sheets.
- **Numbering counts too many rows** — In Google Sheets, A2:A also counts cells that only contain spaces or formulas returning "". **Fix:** Count real values only, e.g. =SEQUENCE(COUNTIF(A2:A, "?*")) for text entries.

## FAQ

### How do I make a list of dates with SEQUENCE?

Add SEQUENCE to a start date, e.g. =DATE(2026,11,2)+SEQUENCE(7,1,0,1) for seven consecutive days, or use step 7 for weekly dates. Format the cells as dates. In Google Sheets wrap it in ARRAYFORMULA if it does not spill.

### Can SEQUENCE count down?

Yes, use a negative step. =SEQUENCE(5, 1, 5, -1) returns 5, 4, 3, 2, 1 in both Excel and Google Sheets.

### What is the difference between SEQUENCE and ROW?

ROW returns the row number of a cell, so =ROW()-1 must be filled down and breaks when rows move. SEQUENCE builds the whole list from one cell and can set any start, step and number of columns.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
