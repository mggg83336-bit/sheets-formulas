---
title: How to Use the SORTBY Function in Excel
slug: sortby-excel
date: '2026-10-26'
summary: SORTBY returns a sorted copy of a range, ordered by one or more other ranges
  that do not have to appear in the result. This guide shows how to list names by
  a sales column you do not want to display, how to sort by two keys, how to apply
  a custom order such as West, East, North, and what to use in G
tags:
- Lookup & reference
- Excel
keyword: sortby-excel
niche: sheets-formulas
provider: structured
entry_id: sortby
platform: Excel
category: lookup
faq:
- q: What is the difference between SORT and SORTBY in Excel?
  a: SORT sorts by a column index inside its own result, e.g. =SORT(A2:C7, 3, -1).
    SORTBY sorts by separate ranges, so the key does not have to be returned. Use
    SORTBY to show names only, to sort by a calculated key, or to apply a custom order.
- q: Is there a SORTBY function in Google Sheets?
  a: No. Google Sheets' SORT already accepts outside ranges as sort columns, so =SORT(A2:A7,
    C2:C7, FALSE) does the same job as =SORTBY(A2:A7, C2:C7, -1).
- q: How do I get only the top 3 with SORTBY?
  a: In Microsoft 365 wrap it in TAKE, e.g. =TAKE(SORTBY(A2:A7, C2:C7, -1), 3). In
    Excel 2021, use =INDEX(SORTBY(A2:A7, C2:C7, -1), SEQUENCE(3)).
related:
- - sort-excel
  - sort-google-sheets
- - filter-excel
  - filter-google-sheets
- - unique-excel
  - unique-google-sheets
- - sequence-excel
  - sequence-google-sheets
- - xlookup-excel
  - xlookup-google-sheets
sibling: null
---
SORTBY returns a sorted copy of a range, ordered by one or more other ranges that do not have to appear in the result. This guide shows how to list names by a sales column you do not want to display, how to sort by two keys, how to apply a custom order such as West, East, North, and what to use in Google Sheets, which has no SORTBY function.

## Quick answer

Use this formula in Excel:

```excel
=SORTBY(A2:A7, C2:C7, -1)
```

Syntax: `SORTBY(array, by_array1, [sort_order1], [by_array2, sort_order2], ...)`. Return the names in A2:A7, ordered by the sales figures in C2:C7; -1 means largest first. The sales column is used as the key but is not part of the output.

## The problem

A small sales table holds each rep's name, region, sales and units. Your manager wants a plain list of names ranked by sales, without the numbers next to them. You also need a list ranked by units with sales as the tie-breaker, and a report grouped by region in a fixed business order rather than alphabetically. SORT can only sort by a column that is part of its own result, so it cannot do the first and last jobs cleanly. SORTBY can.

## Worked example

Six sales reps with region, sales and units sold. The source rows stay in their original order.

| | A | B | C | D | E | F | G | H | I | J | K | L |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Name** | **Region** | **Sales** | **Units** |  | **By sales** | **By units** | **Name** | **Region** |  |  | **Custom order** |
| 2 | Mia | East | 820 | 14 |  | **Leo** | **Zoe** | **Mia** | **East** |  |  | **Leo** |
| 3 | Leo | West | 950 | 9 |  | **Ana** | **Ana** | **Zoe** | **East** |  |  | **Ana** |
| 4 | Zoe | East | 770 | 21 |  | **Ivan** | **Mia** | **Ivan** | **North** |  |  | **Mia** |
| 5 | Ivan | North | 880 | 12 |  | **Mia** | **Ivan** | **Raj** | **North** |  |  | **Zoe** |
| 6 | Ana | West | 910 | 17 |  | **Zoe** | **Leo** | **Leo** | **West** |  |  | **Ivan** |
| 7 | Raj | North | 700 | 9 |  | **Raj** | **Raj** | **Ana** | **West** |  |  | **Raj** |

Formulas used in the example (results shown in **bold** in the table above):

**F2** — names ordered by sales, highest first

```excel
=SORTBY(A2:A7, C2:C7, -1)
```

Results: **Leo**, **Ana**, **Ivan**, **Mia**, **Zoe**, **Raj**

**G2** — names by units (high to low), ties broken by sales

```excel
=SORTBY(A2:A7, D2:D7, -1, C2:C7, -1)
```

Results: **Zoe**, **Ana**, **Mia**, **Ivan**, **Leo**, **Raj**

**H2** — name and region, regions A to Z, sales high to low inside each region

```excel
=SORTBY(A2:B7, B2:B7, 1, C2:C7, -1)
```

Results: **Mia**, **East**, **Zoe**, **East**, **Ivan**, **North**, **Raj**, **North**, **Leo**, **West**, **Ana**, **West**

**L2** — names in a custom region order (West, East, North)

```excel
=SORTBY(A2:A7, MATCH(B2:B7, {"West","East","North"}, 0), 1)
```

Results: **Leo**, **Ana**, **Mia**, **Zoe**, **Ivan**, **Raj**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `SORTBY(A2:A7, C2:C7, -1)` takes the names as the array and the sales column as the key. Sales from highest to lowest are 950, 910, 880, 820, 770 and 700, so the names come back as Leo, Ana, Ivan, Mia, Zoe, Raj. The sales numbers themselves are not shown.
2. For two keys add a second pair. `SORTBY(A2:A7, D2:D7, -1, C2:C7, -1)` sorts by units first: Zoe 21, Ana 17, Mia 14, Ivan 12. Leo and Raj both sold 9 units, so the second key, sales, decides: Leo (950) comes before Raj (700).
3. The array can have several columns. In H2 the formula returns name and region side by side, ordered by region A to Z and, inside each region, by sales from high to low: East (Mia, Zoe), North (Ivan, Raj), West (Leo, Ana).
4. For an order that is neither alphabetical nor numeric, turn each value into a position with MATCH. `MATCH(B2:B7, {"West","East","North"}, 0)` gives West 1, East 2 and North 3, and SORTBY sorts by those numbers ascending.
5. Every by_array must be exactly as tall as the array (here 6 rows). The source table is never changed, so when a figure changes all four lists reorder immediately.

## Excel-specific notes

SORTBY is available in Microsoft 365 and Excel 2021 or later. Each by_array must be a single row or single column with the same number of rows as the array, otherwise the result is #VALUE!. Sort orders are 1 (ascending, the default) and -1 (descending). Add more key and order pairs for tie-breakers; Excel applies them left to right. The sort is stable, so rows with equal keys keep their original order. The key can also be a calculated array, which is how you build a custom sort order with MATCH or sort by text length with LEN.

**Units high to low, then sales high to low**

```excel
=SORTBY(A2:A7, D2:D7, -1, C2:C7, -1)
```

**Whole table by region A to Z, then sales high to low**

```excel
=SORTBY(A2:C7, B2:B7, 1, C2:C7, -1)
```

**Custom region order (West, East, North)**

```excel
=SORTBY(A2:A7, MATCH(B2:B7, {"West","East","North"}, 0), 1)
```

**Shortest names first**

```excel
=SORTBY(A2:A7, LEN(A2:A7), 1)
```


## Google Sheets version

In Google Sheets, use:

```excel
=SORT(A2:A7, C2:C7, FALSE)
```

Google Sheets uses SORT with an outside range instead of SORTBY, and TRUE/FALSE instead of 1/-1 for the order.

<!--SIBLING-->


## Common errors and how to fix them

- **#VALUE!** — A by_array has a different number of rows than the array, or it is more than one column wide. **Fix:** Make every key range the same height as the array, e.g. A2:A7 with C2:C7, and use one column per key.
- **#NAME?** — The workbook is opened in Excel 2019 or older, which has no SORTBY, or the function is used in Google Sheets. **Fix:** Use Microsoft 365 or Excel 2021+. In Google Sheets use SORT with an outside range, e.g. =SORT(A2:A7, C2:C7, FALSE).
- **#SPILL!** — Cells in the area the result needs already contain data. **Fix:** Clear the cells below (and to the right of) the formula.
- **#N/A rows at the top or bottom of a custom order** — A value in the key range is missing from the MATCH list, so MATCH returns **Fix:** Add the missing value to the list, or wrap MATCH in IFERROR with a large number to push unknown values to the end.

## FAQ

### What is the difference between SORT and SORTBY in Excel?

SORT sorts by a column index inside its own result, e.g. =SORT(A2:C7, 3, -1). SORTBY sorts by separate ranges, so the key does not have to be returned. Use SORTBY to show names only, to sort by a calculated key, or to apply a custom order.

### Is there a SORTBY function in Google Sheets?

No. Google Sheets' SORT already accepts outside ranges as sort columns, so =SORT(A2:A7, C2:C7, FALSE) does the same job as =SORTBY(A2:A7, C2:C7, -1).

### How do I get only the top 3 with SORTBY?

In Microsoft 365 wrap it in TAKE, e.g. =TAKE(SORTBY(A2:A7, C2:C7, -1), 3). In Excel 2021, use =INDEX(SORTBY(A2:A7, C2:C7, -1), SEQUENCE(3)).

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
