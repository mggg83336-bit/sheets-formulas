---
title: How to Use the FILTER Function in Google Sheets
slug: filter-google-sheets
date: '2026-10-25'
summary: FILTER returns only the rows of a range that meet your conditions and keeps
  the result live as the data changes. This page covers the syntax, AND and OR conditions,
  returning whole rows, a message for no matches, and the important differences between
  FILTER in Excel and Google Sheets.
tags:
- Lookup & reference
- Google Sheets
keyword: filter-google-sheets
niche: sheets-formulas
provider: structured
entry_id: filter
platform: Google Sheets
category: lookup
faq:
- q: Can FILTER return only some columns?
  a: Yes. Filter just the columns you need, e.g. =FILTER(A2:A8, ...) for one column.
    In Excel 365 you can also wrap the result in CHOOSECOLS, and in Google Sheets
    QUERY lets you pick columns by letter.
- q: Is FILTER case-sensitive?
  a: No. B2:B8="east" matches East. For a case-sensitive test use EXACT, e.g. =FILTER(A2:A8,
    EXACT(B2:B8, "East")).
- q: How do I filter values that contain a word?
  a: Use ISNUMBER(SEARCH("pen", C2:C8)) as the condition, which keeps every row whose
    product contains "pen".
related:
- - lookup-multiple-values-google-sheets
  - lookup-multiple-values-excel
- - unique-google-sheets
  - unique-excel
- - sort-google-sheets
  - sort-excel
- - vlookup-multiple-criteria-google-sheets
  - vlookup-multiple-criteria-excel
- - contains-text-google-sheets
  - contains-text-excel
sibling: filter-excel
---
FILTER returns only the rows of a range that meet your conditions and keeps the result live as the data changes. This page covers the syntax, AND and OR conditions, returning whole rows, a message for no matches, and the important differences between FILTER in Excel and Google Sheets.

## Quick answer

Use this formula in Google Sheets:

```excel
=FILTER(A2:A8, B2:B8=F2)
```

Google Sheets syntax is `FILTER(range, condition1, [condition2, ...])`. Each extra condition is another argument, and all of them must be true for a row to be kept.

## The problem

An order list mixes every region and product. You want separate live views: the orders of one region, the large orders of that region, orders that match either of two conditions, and every order above a threshold with all of its columns, without copying rows by hand or re-applying AutoFilter.

## Worked example

Seven orders; F2 holds the region and G2 the minimum amount used by the formulas.

| | A | B | C | D | E | F | G | H | I | J | K |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Order** | **Region** | **Product** | **Amount** |  | **Region** | **Min amount** | **East orders** | **East >= 200** | **West or Ink** | **South orders** |
| 2 | 1001 | East | Pens | 120 |  | East | 200 | **1001** | **1003** | **1002** | **No match** |
| 3 | 1002 | West | Paper | 340 |  |  |  | **1003** | **1005** | **1005** |  |
| 4 | 1003 | East | Paper | 260 |  |  |  | **1005** |  | **1006** |  |
| 5 | 1004 | North | Pens | 90 |  |  |  |  |  |  |  |
| 6 | 1005 | East | Ink | 410 |  |  |  |  |  |  |  |
| 7 | 1006 | West | Pens | 150 |  |  |  |  |  |  |  |
| 8 | 1007 | North | Paper | 300 |  |  |  |  |  |  |  |
| 9 |  |  |  |  |  |  |  |  |  |  |  |
| 10 | Orders of 300 or more (all columns) |  |  |  |  |  |  |  |  |  |  |
| 11 | **1002** | **West** | **Paper** | **340** |  |  |  |  |  |  |  |
| 12 | **1005** | **East** | **Ink** | **410** |  |  |  |  |  |  |  |
| 13 | **1007** | **North** | **Paper** | **300** |  |  |  |  |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**H2** — orders in the region typed in F2

```excel
=FILTER(A2:A8, B2:B8=F2)
```

Results: **1001**, **1003**, **1005**

**I2** — region in F2 AND amount at least G2

```excel
=FILTER(A2:A8, (B2:B8=F2)*(D2:D8>=G2))
```

Results: **1003**, **1005**

**J2** — region West OR product Ink

```excel
=FILTER(A2:A8, (B2:B8="West")+(C2:C8="Ink"))
```

Results: **1002**, **1005**, **1006**

**K2** — no South orders, so the fallback text appears

```excel
=IFERROR(FILTER(A2:A8, B2:B8="South"), "No match")
```

Result: **No match**

**A11** — whole rows with Amount of 300 or more (spills into A11:D13)

```excel
=FILTER(A2:D8, D2:D8>=300)
```

Results: **1002**, **West**, **Paper**, **340**, **1005**, **East**, **Ink**, **410**, **1007**, **North**, **Paper**, **300**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `B2:B8=F2` is tested on every row and produces TRUE for the three East orders, so H2 spills 1001, 1003 and 1005.
2. For AND, `(B2:B8=F2)*(D2:D8>=G2)` multiplies the two TRUE/FALSE arrays. A row gives 1 only when both are TRUE: 1003 (260) and 1005 (410). Order 1001 is East but only 120, so it drops out.
3. For OR, `(B2:B8="West")+(C2:C8="Ink")` adds the arrays. Any row with a total of 1 or more is kept: 1002 and 1006 (West) and 1005 (Ink).
4. No order is in South, so the include array is all FALSE. Excel shows the if_empty text "No match"; in Google Sheets IFERROR supplies the same message.
5. `FILTER(A2:D8, D2:D8>=300)` passes four columns as the array, so each qualifying order comes back as a full row: 1002, 1005 and 1007 fill A11:D13.
6. Change F2 to West or G2 to 100 and every result recalculates immediately, which is the main advantage over AutoFilter.

## Google Sheets-specific notes

Google Sheets' FILTER is different from Excel's in two ways. First, extra arguments are additional conditions joined with AND, so `=FILTER(A2:A8, B2:B8=F2, D2:D8>=G2)` keeps East orders of at least 200. The Excel style `(cond1)*(cond2)` also works in Sheets, and OR still needs `+`. Second, there is no if_empty argument: when nothing matches, Sheets returns #N/A ("No matches are found in FILTER evaluation"), so wrap the formula in IFNA or IFERROR to show your own message. Open-ended ranges such as A2:A keep the filter current as rows are added, and QUERY is a handy alternative when you also want to pick or sort columns.

**Two conditions as separate arguments (AND)**

```excel
=FILTER(A2:A8, B2:B8=F2, D2:D8>=G2)
```

**Custom message when nothing matches**

```excel
=IFNA(FILTER(A2:A8, B2:B8="South"), "No match")
```

**QUERY version with chosen columns**

```excel
=QUERY(A2:D8, "select A, D where B = 'East' and D >= 200", 0)
```


## Excel version

In Excel, use:

```excel
=FILTER(A2:A8, B2:B8=F2, "No match")
```

Excel's FILTER takes a single include argument (combine conditions with * and +) and has a built-in if_empty third argument. It is not available in Excel 2019 or older.

<!--SIBLING-->


## Common errors and how to fix them

- **#CALC! (Excel) / #N/A (Google Sheets)** — No row meets the conditions and no fallback was given. **Fix:** Add the if_empty argument in Excel, or wrap the formula in IFNA/IFERROR in Google Sheets.
- **#VALUE!** — The include range has a different number of rows than the array, e.g. A2:A8 with B2:B9. **Fix:** Make every condition cover exactly the same rows as the array.
- **#SPILL! (Excel) / #REF! (Google Sheets)** — Cells where the results need to go are not empty. **Fix:** Clear the cells below and to the right of the formula.
- **AND/OR returns the wrong rows** — Conditions were joined with the AND() or OR() functions, which return one single value instead of one result per row. **Fix:** Use (cond1)*(cond2) for AND and (cond1)+(cond2) for OR, each in parentheses.

## FAQ

### Can FILTER return only some columns?

Yes. Filter just the columns you need, e.g. =FILTER(A2:A8, ...) for one column. In Excel 365 you can also wrap the result in CHOOSECOLS, and in Google Sheets QUERY lets you pick columns by letter.

### Is FILTER case-sensitive?

No. B2:B8="east" matches East. For a case-sensitive test use EXACT, e.g. =FILTER(A2:A8, EXACT(B2:B8, "East")).

### How do I filter values that contain a word?

Use ISNUMBER(SEARCH("pen", C2:C8)) as the condition, which keeps every row whose product contains "pen".

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
