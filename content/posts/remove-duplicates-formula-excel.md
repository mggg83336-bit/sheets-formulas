---
title: Remove Duplicates with a Formula in Excel
slug: remove-duplicates-formula-excel
date: '2026-10-25'
summary: List each distinct value from a column without using the Remove Duplicates
  button, so the unique list updates when the source data changes. This page covers
  UNIQUE in modern Excel, the same function in Google Sheets, sorting the result,
  and pulling values that appear only once.
tags:
- Conditional sums & counts
- Excel
keyword: remove-duplicates-formula-excel
niche: sheets-formulas
provider: structured
entry_id: remove-duplicates-formula
platform: Excel
category: conditional
faq:
- q: Does UNIQUE remove duplicate rows across several columns?
  a: Yes. Give it a multi-column range such as A2:B20 and it returns distinct combinations
    of those columns.
- q: How is this different from Data > Remove Duplicates?
  a: The button permanently deletes rows from the sheet. UNIQUE leaves the source
    alone and builds a live list elsewhere.
- q: How do I count duplicates instead of removing them?
  a: Use COUNTIF, e.g. =COUNTIF(A:A, A2) in a helper column, or see the count-unique
    page for distinct counts.
related:
- - count-unique-excel
  - count-unique-google-sheets
- - textjoin-excel
  - textjoin-google-sheets
- - lookup-multiple-values-excel
  - lookup-multiple-values-google-sheets
- - countif-excel
  - countif-google-sheets
sibling: remove-duplicates-formula-google-sheets
---
List each distinct value from a column without using the Remove Duplicates button, so the unique list updates when the source data changes. This page covers UNIQUE in modern Excel, the same function in Google Sheets, sorting the result, and pulling values that appear only once.

## Quick answer

Use this formula in Excel:

```excel
=UNIQUE(A2:A9)
```

UNIQUE returns each distinct value from A2:A9 once, in the order first seen, and spills the list down the column.

## The problem

A city column repeats names across many rows. You need a clean list of cities for a dropdown or summary, and you want it to stay correct when new rows are added, without running Data > Remove Duplicates by hand each time.

## Worked example

Eight city rows with repeats; the unique list should keep first-seen order.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **City** |  | **Unique** | **Sorted** | **Once only** |
| 2 | Seattle |  | **Seattle** | **Austin** | **Austin** |
| 3 | Portland |  | **Portland** | **Denver** |  |
| 4 | Seattle |  | **Denver** | **Portland** |  |
| 5 | Denver |  | **Austin** | **Seattle** |  |
| 6 | Portland |  |  |  |  |
| 7 | Austin |  |  |  |  |
| 8 | Seattle |  |  |  |  |
| 9 | Denver |  |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**C2** — unique list in first-seen order

```excel
=UNIQUE(A2:A9)
```

Results: **Seattle**, **Portland**, **Denver**, **Austin**

**D2** — alphabetical unique list

```excel
=SORT(UNIQUE(A2:A9))
```

Results: **Austin**, **Denver**, **Portland**, **Seattle**

**E2** — cities that appear exactly once

```excel
=UNIQUE(A2:A9, FALSE, TRUE)
```

Result: **Austin**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `UNIQUE(A2:A9)` scans the city column and keeps the first occurrence of each name: Seattle, Portland, Denver, Austin.
2. Later repeats of Seattle, Portland and Denver are dropped. The result spills into C2:C5; only C2 holds the formula.
3. `SORT(UNIQUE(A2:A9))` returns the same four cities in alphabetical order: Austin, Denver, Portland, Seattle.
4. The third argument TRUE means exactly_once. Only Austin appears once in the source, so E2 shows Austin alone.
5. When the source gains a new city, the spilled list grows automatically. Clear cells below the formula so the spill is not blocked.

## Excel-specific notes

UNIQUE needs Microsoft 365 or Excel 2021. Blanks inside the range count as one unique value, so filter them out when needed: `=UNIQUE(FILTER(A2:A100, A2:A100<>""))`. The second argument `by_col` is rarely needed for a single column; the third, `exactly_once`, keeps only values that appear one time. Wrap with SORT for an alphabetical list: `=SORT(UNIQUE(A2:A9))`. Older Excel has no UNIQUE; use a helper column with COUNTIF, or the Data > Remove Duplicates command for a one-off static list. UNIQUE of several columns returns distinct row combinations, which is useful for unique city/region pairs.

**Alphabetical unique list**

```excel
=SORT(UNIQUE(A2:A9))
```

**Values that appear exactly once**

```excel
=UNIQUE(A2:A9, FALSE, TRUE)
```

**Skip blanks**

```excel
=UNIQUE(FILTER(A2:A9, A2:A9<>""))
```


## Google Sheets version

In Google Sheets, use:

```excel
=UNIQUE(FILTER(A2:A9, A2:A9<>""))
```

Google Sheets uses UNIQUE the same way and also supports QUERY for distinct values. Open-ended ranges inside FILTER keep the list up to date as rows are added.

<!--SIBLING-->


## Common errors and how to fix them

- **#SPILL!** — A cell in the spill range already has a value, or the formula sits inside an Excel Table column that cannot spill. **Fix:** Clear the blocking cells, or move the formula outside the table.
- **Extra blank in the unique list** — The source range includes empty cells, and UNIQUE treats blank as a value. **Fix:** Wrap the range in FILTER(..., range<>"") before UNIQUE.
- **#NAME?** — Excel 2019 or older does not have UNIQUE. **Fix:** Use Microsoft 365 / Excel 2021, or build a static list with Data > Remove Duplicates.

## FAQ

### Does UNIQUE remove duplicate rows across several columns?

Yes. Give it a multi-column range such as A2:B20 and it returns distinct combinations of those columns.

### How is this different from Data > Remove Duplicates?

The button permanently deletes rows from the sheet. UNIQUE leaves the source alone and builds a live list elsewhere.

### How do I count duplicates instead of removing them?

Use COUNTIF, e.g. =COUNTIF(A:A, A2) in a helper column, or see the count-unique page for distinct counts.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
