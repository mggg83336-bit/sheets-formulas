---
title: How to Use the SORT Function in Google Sheets
slug: sort-google-sheets
date: '2026-10-25'
summary: SORT returns a sorted copy of a range that updates whenever the source changes,
  so the original data never has to be rearranged. This guide shows sorting one column,
  sorting a table by any column in descending order, multi-level sorting, and how
  the arguments differ between Excel and Google Sheets.
tags:
- Lookup & reference
- Google Sheets
keyword: sort-google-sheets
niche: sheets-formulas
provider: structured
entry_id: sort
platform: Google Sheets
category: lookup
faq:
- q: How do I sort and remove duplicates at the same time?
  a: Wrap UNIQUE in SORT, e.g. =SORT(UNIQUE(A2:A7)). This works the same way in Excel
    365 and Google Sheets.
- q: Can SORT sort by a column that is not in the result?
  a: Not in Excel; use SORTBY, e.g. =SORTBY(A2:A7, C2:C7, -1). Google Sheets' SORT
    can, e.g. =SORT(A2:A7, C2:C7, FALSE).
- q: Does SORT change my original data?
  a: No. It returns a sorted copy in a new place. Use Data > Sort only when you want
    to rearrange the source rows permanently.
related:
- - unique-google-sheets
  - unique-excel
- - filter-google-sheets
  - filter-excel
- - remove-duplicates-formula-google-sheets
  - remove-duplicates-formula-excel
- - xlookup-google-sheets
  - xlookup-excel
sibling: sort-excel
---
SORT returns a sorted copy of a range that updates whenever the source changes, so the original data never has to be rearranged. This guide shows sorting one column, sorting a table by any column in descending order, multi-level sorting, and how the arguments differ between Excel and Google Sheets.

## Quick answer

Use this formula in Google Sheets:

```excel
=SORT(A2:C7, 3, FALSE)
```

Google Sheets syntax is `SORT(range, sort_column, is_ascending, [sort_column2, is_ascending2, ...])`. Sort by column 3; FALSE means descending.

## The problem

A score sheet is kept in the order people were added. You want an alphabetical name list, a leaderboard sorted by score from highest to lowest, and a view grouped by department with the best score first in each group, all without using Data > Sort, which would reorder the source rows every time.

## Worked example

Six people with department and score; the source rows stay in their original order.

| | A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Name** | **Dept** | **Score** |  | **A to Z** |  | **Name** | **Dept** | **Score** |
| 2 | Mia | Sales | 82 |  | **Ana** |  | **Leo** | **Ops** | **95** |
| 3 | Leo | Ops | 95 |  | **Ivan** |  | **Ana** | **HR** | **91** |
| 4 | Zoe | Sales | 77 |  | **Leo** |  | **Ivan** | **Ops** | **88** |
| 5 | Ivan | Ops | 88 |  | **Mia** |  | **Mia** | **Sales** | **82** |
| 6 | Ana | HR | 91 |  | **Raj** |  | **Zoe** | **Sales** | **77** |
| 7 | Raj | HR | 70 |  | **Zoe** |  | **Raj** | **HR** | **70** |
| 8 |  |  |  |  |  |  |  |  |  |
| 9 | By Dept A to Z, then Score high to low |  |  |  |  |  |  |  |  |
| 10 | **Ana** | **HR** | **91** |  |  |  |  |  |  |
| 11 | **Raj** | **HR** | **70** |  |  |  |  |  |  |
| 12 | **Leo** | **Ops** | **95** |  |  |  |  |  |  |
| 13 | **Ivan** | **Ops** | **88** |  |  |  |  |  |  |
| 14 | **Mia** | **Sales** | **82** |  |  |  |  |  |  |
| 15 | **Zoe** | **Sales** | **77** |  |  |  |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**E2** — names sorted alphabetically

```excel
=SORT(A2:A7)
```

Results: **Ana**, **Ivan**, **Leo**, **Mia**, **Raj**, **Zoe**

**G2** — leaderboard by score, highest first (spills into G2:I7)

```excel
=SORT(A2:C7, 3, FALSE)
```

Results: **Leo**, **Ops**, **95**, **Ana**, **HR**, **91**, **Ivan**, **Ops**, **88**, **Mia**, **Sales**, **82**, **Zoe**, **Sales**, **77**, **Raj**, **HR**, **70**

**A10** — two sort levels (spills into A10:C15)

```excel
=SORT(A2:C7, 2, TRUE, 3, FALSE)
```

Results: **Ana**, **HR**, **91**, **Raj**, **HR**, **70**, **Leo**, **Ops**, **95**, **Ivan**, **Ops**, **88**, **Mia**, **Sales**, **82**, **Zoe**, **Sales**, **77**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `SORT(A2:A7)` with no other arguments sorts the single name column A to Z: Ana, Ivan, Leo, Mia, Raj, Zoe.
2. `SORT(A2:C7, 3, -1)` keeps each row together and orders the rows by the third column of the range, Score, from 95 down to 70. In Google Sheets the same sort is written with FALSE.
3. The sort index counts columns inside the range, not sheet columns. Column 3 of A2:C7 is C; if the range started at B, index 3 would be D.
4. For two levels, Excel takes `{2,3}` and `{1,-1}`: first Dept ascending (HR, Ops, Sales), then Score descending within each department. Google Sheets lists the pairs one after another: 2, TRUE, 3, FALSE.
5. Within HR, Ana (91) comes before Raj (70); within Ops, Leo (95) before Ivan (88); within Sales, Mia (82) before Zoe (77).
6. The source table A2:C7 is never changed. Edit a score and all three sorted views reorder instantly.

## Google Sheets-specific notes

Google Sheets' SORT uses TRUE/FALSE instead of 1/-1 for the order, and it handles multiple sort levels with extra pairs of arguments instead of array constants: `=SORT(A2:C7, 2, TRUE, 3, FALSE)` sorts by Dept A to Z, then Score high to low. Do not copy the Excel form `=SORT(A2:C7, 3, -1)`: Sheets reads -1 as TRUE and sorts ascending. The sort column can also be a range outside the result, such as `=SORT(A2:A7, C2:C7, FALSE)`, which returns names in score order, so Sheets needs no SORTBY. For a top-N list combine SORT with ARRAY_CONSTRAIN, or use SORTN.

**Multi-level sort with argument pairs**

```excel
=SORT(A2:C7, 2, TRUE, 3, FALSE)
```

**Names only, ordered by score**

```excel
=SORT(A2:A7, C2:C7, FALSE)
```

**Top 3 scores with SORTN**

```excel
=SORTN(A2:C7, 3, 0, 3, FALSE)
```


## Excel version

In Excel, use:

```excel
=SORT(A2:C7, 3, -1)
```

Excel's SORT uses 1 / -1 for the order and array constants such as {2,3} for multi-level sorts. It is not available in Excel 2019 or older.

<!--SIBLING-->


## Common errors and how to fix them

- **#VALUE!** — In Excel, sort_order is something other than 1 or -1, or sort_index is larger than the number of columns in the array. **Fix:** Use 1 or -1 for the order and a column number within the range.
- **Sorted ascending instead of descending (Google Sheets)** — The Excel form -1 was used. Sheets treats any non-zero number as TRUE, which means ascending. **Fix:** Use FALSE (or 0) for descending in Google Sheets.
- **#SPILL! (Excel) / #REF! (Google Sheets)** — The cells the sorted result needs are not empty. **Fix:** Clear the area below and to the right of the formula.
- **Numbers sort in the wrong order** — Some values are stored as text, so 100 sorts before 20. **Fix:** Convert the text to numbers, e.g. with VALUE or Data > Text to Columns.

## FAQ

### How do I sort and remove duplicates at the same time?

Wrap UNIQUE in SORT, e.g. =SORT(UNIQUE(A2:A7)). This works the same way in Excel 365 and Google Sheets.

### Can SORT sort by a column that is not in the result?

Not in Excel; use SORTBY, e.g. =SORTBY(A2:A7, C2:C7, -1). Google Sheets' SORT can, e.g. =SORT(A2:A7, C2:C7, FALSE).

### Does SORT change my original data?

No. It returns a sorted copy in a new place. Use Data > Sort only when you want to rearrange the source rows permanently.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
