---
title: Remove Duplicates with a Formula in Google Sheets
slug: remove-duplicates-formula-google-sheets
date: '2026-10-25'
summary: List each distinct value from a column without using the Remove Duplicates
  button, so the unique list updates when the source data changes. This page covers
  UNIQUE in modern Excel, the same function in Google Sheets, sorting the result,
  and pulling values that appear only once.
tags:
- Conditional sums & counts
- Google Sheets
keyword: remove-duplicates-formula-google-sheets
niche: sheets-formulas
provider: structured
entry_id: remove-duplicates-formula
platform: Google Sheets
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
- - count-unique-google-sheets
  - count-unique-excel
- - textjoin-google-sheets
  - textjoin-excel
- - lookup-multiple-values-google-sheets
  - lookup-multiple-values-excel
- - countif-google-sheets
  - countif-excel
sibling: remove-duplicates-formula-excel
---
List each distinct value from a column without using the Remove Duplicates button, so the unique list updates when the source data changes. This page covers UNIQUE in modern Excel, the same function in Google Sheets, sorting the result, and pulling values that appear only once.

## Quick answer

Use this formula in Google Sheets:

```excel
=UNIQUE(FILTER(A2:A9, A2:A9<>""))
```

FILTER drops blank cells first, then UNIQUE returns each remaining city once in first-seen order.

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

## Google Sheets-specific notes

Google Sheets has had UNIQUE for a long time and accepts open-ended ranges such as A2:A, so new rows are included automatically when you use `=UNIQUE(FILTER(A2:A, A2:A<>""))`. The arguments match Excel: `UNIQUE(range, [by_col], [exactly_once])`. For a sorted distinct list you can also use QUERY: `=QUERY(A2:A9, "select A where A is not null group by A order by A", 0)`. QUERY is handy when you want distinct values plus a count in one step. Data > Data cleanup > Remove duplicates still exists for a one-time static cleanup, but a formula stays live.

**Open-ended range for growing lists**

```excel
=UNIQUE(FILTER(A2:A, A2:A<>""))
```

**Distinct cities sorted with QUERY**

```excel
=QUERY(A2:A9, "select A where A is not null group by A order by A", 0)
```

**Values that appear exactly once**

```excel
=UNIQUE(A2:A9, FALSE, TRUE)
```


## Excel version

In Excel, use:

```excel
=UNIQUE(A2:A9)
```

In Excel, UNIQUE is available in Microsoft 365 and Excel 2021. Older versions need a helper column or the Remove Duplicates command on the Data tab.

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
