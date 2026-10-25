---
title: How to Use the SORT Function in Excel
slug: sort-excel
date: '2026-10-25'
summary: SORT returns a sorted copy of a range that updates whenever the source changes,
  so the original data never has to be rearranged. This guide shows sorting one column,
  sorting a table by any column in descending order, multi-level sorting, and how
  the arguments differ between Excel and Google Sheets.
tags:
- Lookup & reference
- Excel
keyword: sort-excel
niche: sheets-formulas
provider: structured
entry_id: sort
platform: Excel
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
- - unique-excel
  - unique-google-sheets
- - filter-excel
  - filter-google-sheets
- - remove-duplicates-formula-excel
  - remove-duplicates-formula-google-sheets
- - xlookup-excel
  - xlookup-google-sheets
sibling: sort-google-sheets
---
SORT returns a sorted copy of a range that updates whenever the source changes, so the original data never has to be rearranged. This guide shows sorting one column, sorting a table by any column in descending order, multi-level sorting, and how the arguments differ between Excel and Google Sheets.

## Quick answer

Use this formula in Excel:

```excel
=SORT(A2:C7, 3, -1)
```

Syntax: `SORT(array, [sort_index], [sort_order], [by_col])`. Sort the table A2:C7 by its third column (Score); -1 means descending. The result spills into as many rows and columns as the source.

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
=SORT(A2:C7, 3, -1)
```

Results: **Leo**, **Ops**, **95**, **Ana**, **HR**, **91**, **Ivan**, **Ops**, **88**, **Mia**, **Sales**, **82**, **Zoe**, **Sales**, **77**, **Raj**, **HR**, **70**

**A10** — two sort levels (spills into A10:C15)

```excel
=SORT(A2:C7, {2,3}, {1,-1})
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

## Excel-specific notes

SORT is available in Microsoft 365 and Excel 2021. Leave out sort_index and sort_order to sort by the first column in ascending order. sort_order is 1 for ascending and -1 for descending; other values return #VALUE!. For a multi-level sort pass array constants: `=SORT(A2:C7, {2,3}, {1,-1})` sorts by Dept A to Z, then by Score high to low. Set the fourth argument to TRUE to sort columns left to right instead of rows. When the sort key is not part of the result, use SORTBY, e.g. `=SORTBY(A2:A7, C2:C7, -1)` returns only names in score order.

**Multi-level sort (Dept, then Score descending)**

```excel
=SORT(A2:C7, {2,3}, {1,-1})
```

**Names only, ordered by score**

```excel
=SORTBY(A2:A7, C2:C7, -1)
```

**Top 3 scores (Microsoft 365)**

```excel
=TAKE(SORT(A2:C7, 3, -1), 3)
```


## Google Sheets version

In Google Sheets, use:

```excel
=SORT(A2:C7, 3, FALSE)
```

Google Sheets' SORT uses TRUE/FALSE for the order and extra column/order pairs for multi-level sorts; it can sort by an outside range, so SORTBY is not needed.

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
