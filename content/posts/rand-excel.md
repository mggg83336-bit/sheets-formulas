---
title: How to Use RAND to Shuffle or Sample a List in Excel
slug: rand-excel
date: '2026-11-11'
summary: RAND returns a random decimal that is greater than or equal to 0 and strictly
  less than 1. Scale it for a continuous range, or use it (or RANDARRAY) as a sort
  key to shuffle a list and to sample rows without replacement. This is a different
  job from RANDBETWEEN, which returns integers in a fixed ban
tags:
- Financial & percentages
- Excel
keyword: rand-excel
niche: sheets-formulas
provider: structured
entry_id: rand
platform: Excel
category: financial
faq:
- q: What is the difference between RAND and RANDBETWEEN?
  a: RAND returns a decimal in [0, 1). RANDBETWEEN returns a whole number between
    two bounds, inclusive. Use RAND (or RANDARRAY) to shuffle or sample a list and
    to scale a continuous value. Use RANDBETWEEN when you specifically want random
    integers in a range.
- q: Why not just fill RAND() down and sort by hand?
  a: That is the right method in Excel 2019 and older, and it still works. SORTBY
    or SORT plus RANDARRAY does the same shuffle with one formula and updates if the
    list length changes. Either way, paste values once you like the order.
- q: Can I use RANDARRAY to get random integers in Google Sheets?
  a: Not with Excel’s five-argument form. Sheets RANDARRAY only returns 0–1 decimals.
    Scale it (=INT(RANDARRAY(n, 1)*(top-bottom+1))+bottom) or use RANDBETWEEN / ARRAYFORMULA
    instead.
- q: Is a helper column of RAND() worse than RANDARRAY?
  a: The distribution is the same. RANDARRAY is easier to maintain because you do
    not have to remember to fill extra rows. A helper column is the portable option
    when the file must open in older Excel, or when you want to inspect the random
    keys before sorting.
related:
- - unique-excel
  - unique-google-sheets
- - sort-excel
  - sort-google-sheets
- - sortby-excel
- - filter-excel
  - filter-google-sheets
- - sequence-excel
  - sequence-google-sheets
sibling: rand-google-sheets
---
RAND returns a random decimal that is greater than or equal to 0 and strictly less than 1. Scale it for a continuous range, or use it (or RANDARRAY) as a sort key to shuffle a list and to sample rows without replacement. This is a different job from RANDBETWEEN, which returns integers in a fixed band. Worked example included.

## Quick answer

Use this formula in Excel:

```excel
=SORTBY(A2:A6, RANDARRAY(COUNTA(A2:A6)))
```

`RAND()` is a single decimal in the half-open interval [0, 1). `RANDARRAY(n)` spills n such decimals. Feeding that spill into SORTBY reorders the region list by a fresh random key, which is a shuffle without a helper column. The same RAND values can be ranked, scaled, or used to pick one row.

## The problem

You have five regions in a list and want a fair shuffle, a single random pick, and a way to map a RAND draw onto a 10–20 scale. You also need a pattern that works when you do not have Microsoft 365, and a Google Sheets version that does not assume Excel’s RANDARRAY arguments.

## Worked example

Five regions with a frozen RAND draw already typed in column B, as if live RAND() results had been pasted as values. The scale, INT, RANK, INDEX and AVERAGE formulas use those fixed numbers so they can be machine-verified. The live RAND in E9 changes on every recalc and is not compared to a fixed result.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Region** | **Frozen RAND** |  | **Item** | **Value** |
| 2 | North | 0.42 |  | Low | 10 |
| 3 | East | 0.07 |  | High | 20 |
| 4 | South | 0.91 |  | Scaled stand-in | **14.2** |
| 5 | West | 0.33 |  | INT mapping | **1** |
| 6 | Central | 0.68 |  | Rank of North | **3** |
| 7 |  |  |  | Random pick (lowest RAND) | **East** |
| 8 |  |  |  | Average of draws | **0.482** |
| 9 |  |  |  | Live RAND | **(changes on every recalc)** |

Formulas used in the example (results shown in **bold** in the table above):

**E4** — scale the 0.42 stand-in onto 10–20

```excel
=E2+(E3-E2)*B2
```

Result: **14.2**

**E5** — map the 0.07 stand-in to a 1–10 integer

```excel
=INT(B3*10)+1
```

Result: **1**

**E6** — ascending rank of North's draw

```excel
=RANK(B2, B2:B6, 1)
```

Result: **3**

**E7** — region with the lowest frozen RAND

```excel
=INDEX(A2:A6, MATCH(MIN(B2:B6), B2:B6, 0))
```

Result: **East**

**E8** — average of the frozen draws

```excel
=AVERAGE(B2:B6)
```

Result: **0.482**

**E9** — live RAND decimal (volatile)

```excel
=RAND()
```

Result: **(changes on every recalc)**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `RAND()` (and each cell of `RANDARRAY`) returns a decimal in [0, 1), never 1. Column B is a frozen sample of five such draws, already pasted as values so the rest of the example is stable.
2. A continuous scale is `low+(high-low)*RAND()`. With the 0.42 stand-in, `=E2+(E3-E2)*B2` is 14.2, which stays below 20 because the stand-in is below 1.
3. The older integer mapping `=INT(RAND()*(high-low+1))+low` is what RANDBETWEEN hides. `=INT(B3*10)+1` with 0.07 equals 1, the bottom of a 1–10 band.
4. To shuffle, sort the list by a random key. In current Excel that is `=SORTBY(A2:A6, RANDARRAY(COUNTA(A2:A6)))`. Ranking the frozen draws (`=RANK(B2, B2:B6, 1)` is 3 for North) is the same idea in a helper column.
5. A single random pick is the item whose RAND is the smallest (or largest): `=INDEX(A2:A6, MATCH(MIN(B2:B6), B2:B6, 0))` returns East. A sample of several items is a shuffle followed by TAKE or SORTN, not several independent RAND calls, if you must not repeat a row.

## Excel-specific notes

RAND and RANDARRAY are volatile: every recalculation, including opening the file or pressing F9, reshuffles the list. When the order must stick (a published draw, a seating plan, an assigned review queue), copy the result and paste values. RAND never returns 1, which is what keeps `=low+(high-low)*RAND()` inside the upper bound and keeps `=INT(RAND()*(high-low+1))+low` from overshooting the top integer. In Microsoft 365 / Excel 2021, RANDARRAY is the clean way to generate many draws at once (`=RANDARRAY(5)` or `=RANDARRAY(5, 2)` for a grid) and SORTBY is the clean shuffle; `=TAKE(SORTBY(A2:A6, RANDARRAY(COUNTA(A2:A6))), 3)` is a random sample of three without replacement. Excel 2019 and older have RAND but not RANDARRAY or SORTBY: put `=RAND()` in a helper column, then sort the list by that column (or use RANK / INDEX to pull the first n). Fill-down of RAND() and a single RANDARRAY spill are equivalent in distribution; the spill is just easier to maintain. Do not use RAND as a stable unique ID, and do not treat a uniform RAND as a normal (bell-curve) sample — if you need that, use `=NORM.INV(RAND(), mean, sd)` on a frozen draw.

**One random decimal**

```excel
=RAND()
```

**Scale a draw onto 10–20 (continuous)**

```excel
=E2+(E3-E2)*RAND()
```

**Random sample of three regions**

```excel
=TAKE(SORTBY(A2:A6, RANDARRAY(COUNTA(A2:A6))), 3)
```

**Helper-column RAND (Excel 2019 and older)**

```excel
=RAND()
```


## Google Sheets version

In Google Sheets, use:

```excel
=SORT(A2:A6, RANDARRAY(COUNTA(A2:A6), 1), TRUE)
```

Excel 365 shuffles with SORTBY and RANDARRAY, and can request integer or bounded RANDARRAY results. Sheets RANDARRAY is 0–1 only; use SORT or SORTN for the list, and a scale formula when you need another range. Excel has no SORTN or ARRAYFORMULA.

<!--SIBLING-->


## Common errors and how to fix them

- **The list order (or the “random” pick) keeps changing** — RAND, RANDARRAY, SORTBY and SORT of a random key are all volatile and recalculate together. **Fix:** Paste the shuffled list (or the pick) as values when the result needs to be permanent.
- **A scale formula sometimes equals the high bound, or steps one past it** — The formula used a closed interval that can reach 1, or INT was applied without the +1 / +low offset. **Fix:** Keep RAND in [0, 1). For a continuous 10–20 range use `=10+(20-10)*RAND()`. For integers use RANDBETWEEN or `=INT(RAND()*(top-bottom+1))+bottom`.
- **#SPILL! or #REF! on the shuffle** — The spill range for SORTBY, SORT, or RANDARRAY is not empty, or (Sheets) the array would overwrite existing cells. **Fix:** Clear the cells the shuffle needs, or move the formula so it has room to expand.
- **The same region appears twice in a “sample of three”** — RAND was used independently on each row (sampling with replacement), or the same item exists twice in the source list. **Fix:** Shuffle once with SORTBY or SORT and take the first n rows (TAKE or SORTN). That samples without replacement.

## FAQ

### What is the difference between RAND and RANDBETWEEN?

RAND returns a decimal in [0, 1). RANDBETWEEN returns a whole number between two bounds, inclusive. Use RAND (or RANDARRAY) to shuffle or sample a list and to scale a continuous value. Use RANDBETWEEN when you specifically want random integers in a range.

### Why not just fill RAND() down and sort by hand?

That is the right method in Excel 2019 and older, and it still works. SORTBY or SORT plus RANDARRAY does the same shuffle with one formula and updates if the list length changes. Either way, paste values once you like the order.

### Can I use RANDARRAY to get random integers in Google Sheets?

Not with Excel’s five-argument form. Sheets RANDARRAY only returns 0–1 decimals. Scale it (`=INT(RANDARRAY(n, 1)*(top-bottom+1))+bottom`) or use RANDBETWEEN / ARRAYFORMULA instead.

### Is a helper column of RAND() worse than RANDARRAY?

The distribution is the same. RANDARRAY is easier to maintain because you do not have to remember to fill extra rows. A helper column is the portable option when the file must open in older Excel, or when you want to inspect the random keys before sorting.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
