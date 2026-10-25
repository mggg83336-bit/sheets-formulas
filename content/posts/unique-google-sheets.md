---
title: How to Use the UNIQUE Function in Google Sheets
slug: unique-google-sheets
date: '2026-10-25'
summary: UNIQUE returns the distinct values or distinct rows of a range as a live,
  spilling list. This guide explains every argument of UNIQUE, shows how to get unique
  combinations across two columns, how to count distinct entries with COUNTA, and
  how the function differs between Excel and Google Sheets.
tags:
- Lookup & reference
- Google Sheets
keyword: unique-google-sheets
niche: sheets-formulas
provider: structured
entry_id: unique
platform: Google Sheets
category: lookup
faq:
- q: Is UNIQUE case-sensitive?
  a: No. "east" and "East" are treated as the same value, and the first spelling found
    is the one returned.
- q: How do I get unique values from two columns combined into one list?
  a: In Excel 365 use =UNIQUE(VSTACK(A2:A9, B2:B9)). In Google Sheets use =UNIQUE({A2:A9;
    B2:B9}).
- q: What does the exactly_once argument do?
  a: With TRUE as the third argument, UNIQUE returns only values that occur a single
    time in the range, which is useful for spotting one-off entries.
related:
- - remove-duplicates-formula-google-sheets
  - remove-duplicates-formula-excel
- - count-unique-google-sheets
  - count-unique-excel
- - filter-google-sheets
  - filter-excel
- - sort-google-sheets
  - sort-excel
- - countif-google-sheets
  - countif-excel
sibling: unique-excel
---
UNIQUE returns the distinct values or distinct rows of a range as a live, spilling list. This guide explains every argument of UNIQUE, shows how to get unique combinations across two columns, how to count distinct entries with COUNTA, and how the function differs between Excel and Google Sheets.

## Quick answer

Use this formula in Google Sheets:

```excel
=UNIQUE(A2:A9)
```

Google Sheets uses the same syntax, `UNIQUE(range, [by_column], [exactly_once])`, and returns distinct values in first-seen order, expanding into the cells below.

## The problem

A sales log repeats the same regions and reps on many rows. You want a list of the regions that appear, the distinct region and rep pairs for a summary table, and the number of different reps, all updating automatically when new sales are entered.

## Worked example

Eight sales rows with repeated regions and reps.

| | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| 1 | **Region** | **Rep** | **Sales** |  | **Regions** | **Pair region** | **Pair rep** | **Distinct reps** |
| 2 | East | Ana | 120 |  | **East** | **East** | **Ana** | **4** |
| 3 | West | Ben | 90 |  | **West** | **West** | **Ben** |  |
| 4 | East | Ana | 75 |  | **North** | **North** | **Cara** |  |
| 5 | North | Cara | 200 |  |  | **West** | **Dev** |  |
| 6 | West | Dev | 60 |  |  | **East** | **Ben** |  |
| 7 | East | Ben | 150 |  |  |  |  |  |
| 8 | North | Cara | 80 |  |  |  |  |  |
| 9 | West | Ben | 110 |  |  |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**E2** — distinct regions in first-seen order

```excel
=UNIQUE(A2:A9)
```

Results: **East**, **West**, **North**

**F2** — distinct region and rep combinations (spills into F2:G6)

```excel
=UNIQUE(A2:B9)
```

Results: **East**, **Ana**, **West**, **Ben**, **North**, **Cara**, **West**, **Dev**, **East**, **Ben**

**H2** — number of different reps

```excel
=COUNTA(UNIQUE(B2:B9))
```

Result: **4**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `UNIQUE(A2:A9)` reads the region column top to bottom and keeps the first East, the first West and the first North. Later repeats are skipped, so E2:E4 shows East, West, North.
2. Only E2 contains the formula. The other cells are part of the spill range; select E2 and the blue border shows the whole result.
3. `UNIQUE(A2:B9)` compares both columns together. East/Ana appears twice and North/Cara twice, and West/Ben twice, so five distinct pairs remain: East/Ana, West/Ben, North/Cara, West/Dev and East/Ben.
4. Ben counts as a separate pair in West and in East because the combination differs, which is exactly what a region-by-rep summary needs.
5. `COUNTA(UNIQUE(B2:B9))` first builds the distinct rep list Ana, Ben, Cara, Dev, then COUNTA counts its four items.
6. Add a new sale at the bottom of the source range (or use an Excel Table or open-ended range) and every result updates without any manual step.

## Google Sheets-specific notes

Google Sheets has had UNIQUE much longer than Excel and it works in every version, so there is no compatibility concern. Two Sheets extras save time: open-ended ranges such as A2:A include rows you add later, and COUNTUNIQUE counts distinct values directly without wrapping UNIQUE in COUNTA. Because an open-ended range also contains empty rows, combine it with FILTER to drop blanks. QUERY can return distinct values together with a count per value, which UNIQUE alone cannot do. If the result shows #REF! with "Array result was not expanded", clear the cells below the formula.

**Count distinct reps with COUNTUNIQUE**

```excel
=COUNTUNIQUE(B2:B9)
```

**Open-ended range without blanks**

```excel
=UNIQUE(FILTER(A2:A, A2:A<>""))
```

**Distinct regions with a count of rows each**

```excel
=QUERY(A2:A9, "select A, count(A) where A is not null group by A", 0)
```


## Excel version

The same formula works unchanged in Excel:

```excel
=UNIQUE(A2:A9)
```

Excel has the same UNIQUE function with the same three arguments in Microsoft 365 and Excel 2021. Excel 2019 and older do not have it, and Excel needs COUNTA(UNIQUE()) because there is no COUNTUNIQUE.

<!--SIBLING-->


## Common errors and how to fix them

- **#SPILL! (Excel) / #REF! (Google Sheets)** — Cells in the area where the result needs to expand are not empty, or the formula sits inside an Excel Table. **Fix:** Clear the cells below and to the right of the formula, or move it outside the table.
- **Unexpected blank or 0 in the list** — The range includes empty cells, which UNIQUE returns as one extra value (shown as 0 in Excel). **Fix:** Filter blanks first, e.g. =UNIQUE(FILTER(A2:A100, A2:A100<>"")).
- **Near-duplicates still listed twice** — Values differ by a trailing space or invisible character, such as "East" and "East ". UNIQUE is not case-sensitive, but it does treat spaces as different text. **Fix:** Clean the source with TRIM, or use =UNIQUE(TRIM(A2:A9)) in Excel 365.
- **#NAME?** — The workbook is opened in Excel 2019 or older, which has no UNIQUE function. **Fix:** Use Microsoft 365 / Excel 2021, or Data > Remove Duplicates on a copy for a static list.

## FAQ

### Is UNIQUE case-sensitive?

No. "east" and "East" are treated as the same value, and the first spelling found is the one returned.

### How do I get unique values from two columns combined into one list?

In Excel 365 use =UNIQUE(VSTACK(A2:A9, B2:B9)). In Google Sheets use =UNIQUE({A2:A9; B2:B9}).

### What does the exactly_once argument do?

With TRUE as the third argument, UNIQUE returns only values that occur a single time in the range, which is useful for spotting one-off entries.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
