---
title: How to Use the RANK Function in Excel
slug: rank-excel
date: '2026-11-05'
summary: RANK returns a value’s position in a list. Order 0 (or omitted) ranks largest
  first; order 1 ranks smallest first. Tied values receive the same rank, and the
  next rank skips ahead (competition ranking). Excel also offers RANK.EQ and RANK.AVG.
tags:
- Financial & percentages
- Excel
keyword: rank-excel
niche: sheets-formulas
provider: structured
entry_id: rank
platform: Excel
category: financial
faq:
- q: What is the difference between RANK, RANK.EQ, and RANK.AVG?
  a: RANK and RANK.EQ are competition ranks (ties share a place, next place skips).
    RANK.AVG gives tied values the average of the places they span. Google Sheets
    focuses on RANK.
- q: How do I rank with no gaps after ties?
  a: Use a dense-rank pattern such as =COUNTIF($B$2:$B$8, ">"&B2)+1 for descending
    places.
- q: Does RANK change when I sort the sheet?
  a: No. RANK looks at values in ref, not at visual row order, so sorting alone does
    not change each score’s rank.
- q: How do I get the 2nd-highest value instead of its rank?
  a: Use =LARGE(range, 2) or =SMALL(range, 2). RANK answers “what place?”, LARGE/SMALL
    answer “what value?”.
related:
- - average-excel
  - average-google-sheets
- - median-mode-excel
  - median-mode-google-sheets
- - sort-excel
  - sort-google-sheets
- - sortby-excel
sibling: rank-google-sheets
---
RANK returns a value’s position in a list. Order 0 (or omitted) ranks largest first; order 1 ranks smallest first. Tied values receive the same rank, and the next rank skips ahead (competition ranking). Excel also offers RANK.EQ and RANK.AVG.

## Quick answer

Use this formula in Excel:

```excel
=RANK(B2, $B$2:$B$8, 0)
```

Syntax: `RANK(number, ref, [order])`. `number` is the value to rank, `ref` is the full list (lock it with $ when filling down). Order 0 or omitted = descending (best/largest = 1); order 1 = ascending (smallest = 1).

## The problem

A leaderboard needs each score’s place among the class. People sort the sheet manually, break formulas when rows move, or expect dense ranks (1,2,3) when ties should share a place and skip the next number.

## Worked example

Seven scores with a three-way tie at 88. Descending RANK gives 1 for 95, 2 for 91, 3 for each 88, then 6 and 7. Ascending RANK gives 1 to the lowest score.

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **Student** | **Score** | **Rank desc** | **Rank asc** |
| 2 | Ava | 72 | **6** | **2** |
| 3 | Ben | 88 | **3** | **3** |
| 4 | Cara | 95 | **1** | **7** |
| 5 | Drew | 88 | **3** | **3** |
| 6 | Eve | 64 | **7** | **1** |
| 7 | Finn | 91 | **2** | **6** |
| 8 | Gia | 88 | **3** | **3** |
| 9 |  |  |  |  |
| 10 |  |  | **1** |  |
| 11 |  |  | **3** |  |

Formulas used in the example (results shown in **bold** in the table above):

**C2 (filled to C8)** — descending rank filled down

```excel
=RANK(B2, $B$2:$B$8, 0)
```

Results: **6**, **3**, **1**, **3**, **7**, **2**, **3**

**D2 (filled to D8)** — ascending rank filled down

```excel
=RANK(B2, $B$2:$B$8, 1)
```

Results: **2**, **3**, **7**, **3**, **1**, **6**, **3**

**C10** — rank of the top score against the list

```excel
=RANK(95, B2:B8, 0)
```

Result: **1**

**C11** — dense descending rank for Ben (88)

```excel
=COUNTIF($B$2:$B$8, ">"&B3)+1
```

Result: **3**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Put every comparable score in one locked range (for example $B$2:$B$8).
2. In the first rank cell type `=RANK(B2, $B$2:$B$8, 0)` for largest-first leaderboards.
3. Fill the formula down so each row keeps the same absolute ref.
4. Use order 1 when the smallest value should be rank 1 (race times, golf scores).
5. Switch to a COUNTIF dense-rank formula when ties must not create gaps.

## Excel-specific notes

RANK and RANK.EQ use competition ranking: if two scores tie for 2nd, both get 2 and the next score gets 4. RANK.AVG would assign 2.5 to those ties instead. Absolute-reference the list (`$B$2:$B$8`) so each row ranks against the same set when you fill down. RANK ignores text and blanks inside ref. For a filtered visible-only rank, helper columns or more advanced constructs are needed — plain RANK always sees the full ref. Pair RANK with COUNTIF when you want a dense rank (1,2,3 with no gaps): `=COUNTIF($B$2:$B$8, ">"&B2)+1` for descending dense ranks. Keep RANK for classic leaderboards; switch to LARGE/SMALL when you need the nth value itself rather than a place.

**Ascending rank (smallest = 1)**

```excel
=RANK(B2, $B$2:$B$8, 1)
```

**Excel RANK.EQ (same as RANK)**

```excel
=RANK.EQ(B2, $B$2:$B$8, 0)
```

**Dense descending rank via COUNTIF**

```excel
=COUNTIF($B$2:$B$8, ">"&B2)+1
```

**Value of the top score**

```excel
=LARGE($B$2:$B$8, 1)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=RANK(B2, $B$2:$B$8, 0)
```

Excel adds RANK.EQ and RANK.AVG aliases; fill down instead of ARRAYFORMULA for a rank column.

<!--SIBLING-->


## Common errors and how to fix them

- **Every row ranks only against itself after fill-down** — The ref was relative (B2:B8) and shifted with each row. **Fix:** Lock the list with $B$2:$B$8 before filling.
- **Ties show ranks 3,3,4 instead of 3,3,5** — Expecting ordinal labels differently, or mixing dense-rank logic with RANK. **Fix:** RANK uses competition ranking (skip after ties). Use COUNTIF for dense ranks.
- **#N/A or unexpected rank** — The number is not in ref, or ref includes errors/text that break the list. **Fix:** Ensure the value exists in a clean numeric ref.
- **Ranking looks reversed** — Order argument wrong (0 vs 1) for the sport or metric. **Fix:** Use 0 when higher is better; use 1 when lower is better.

## FAQ

### What is the difference between RANK, RANK.EQ, and RANK.AVG?

RANK and RANK.EQ are competition ranks (ties share a place, next place skips). RANK.AVG gives tied values the average of the places they span. Google Sheets focuses on RANK.

### How do I rank with no gaps after ties?

Use a dense-rank pattern such as =COUNTIF($B$2:$B$8, ">"&B2)+1 for descending places.

### Does RANK change when I sort the sheet?

No. RANK looks at values in ref, not at visual row order, so sorting alone does not change each score’s rank.

### How do I get the 2nd-highest value instead of its rank?

Use =LARGE(range, 2) or =SMALL(range, 2). RANK answers “what place?”, LARGE/SMALL answer “what value?”.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
