---
title: How to Use LARGE and SMALL in Google Sheets
slug: large-small-google-sheets
date: '2026-11-06'
summary: LARGE returns the nth largest value in a list; SMALL returns the nth smallest.
  Use them when you need the value itself (top score, second-lowest cost) rather than
  a rank place. Pair with MAX/MIN for the extremes and RANK when you need position
  numbers instead of the underlying amounts.
tags:
- Financial & percentages
- Google Sheets
keyword: large-small-google-sheets
niche: sheets-formulas
provider: structured
entry_id: large-small
platform: Google Sheets
category: financial
faq:
- q: What is the difference between LARGE and RANK?
  a: RANK returns a place number for a known value. LARGE/SMALL return the value that
    sits at place k. Use both when a dashboard needs the amount and its rank.
- q: Does LARGE(range, 1) equal MAX(range)?
  a: Yes for a plain numeric list. Prefer MAX/MIN when you only need the single extreme;
    use LARGE/SMALL when k may be 2, 3, or more.
- q: How do ties work?
  a: Duplicate values each take a slot in the ordered list. If two scores equal 88,
    LARGE(...,3) and LARGE(...,4) can both return 88.
- q: Can I get the largest value that meets a condition?
  a: Use MAXIFS for the single conditional maximum. For the nth conditional value,
    filter the list first (FILTER in Excel 365 / Sheets) then apply LARGE.
related:
- - rank-google-sheets
  - rank-excel
- - average-google-sheets
  - average-excel
- - median-mode-google-sheets
  - median-mode-excel
- - maxifs-minifs-google-sheets
  - maxifs-minifs-excel
- - weighted-average-google-sheets
  - weighted-average-excel
sibling: large-small-excel
---
LARGE returns the nth largest value in a list; SMALL returns the nth smallest. Use them when you need the value itself (top score, second-lowest cost) rather than a rank place. Pair with MAX/MIN for the extremes and RANK when you need position numbers instead of the underlying amounts.

## Quick answer

Use this formula in Google Sheets:

```excel
=LARGE(B2:B8, 2)
```

Same LARGE/SMALL syntax in Google Sheets. k=1 is the extreme; higher k walks inward from that end of the sorted list.

## The problem

A scoreboard or sales list needs the top three amounts and the two lowest values for review. Sorting the sheet breaks other formulas, MAX/MIN only give the single extreme, and RANK answers “what place?” when the real question is “what number sits in that place?”.

## Worked example

Seven student scores. LARGE pulls the top places; SMALL pulls the bottom. MAX/MIN match LARGE/SMALL with k=1. A three-way pattern at 88 shows ties returning the same value twice.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Student** | **Score** |  | **Metric** | **Value** |
| 2 | Ava | 72 |  |  | **95** |
| 3 | Ben | 88 |  |  | **91** |
| 4 | Cara | 95 |  |  | **88** |
| 5 | Drew | 88 |  |  | **64** |
| 6 | Eve | 64 |  |  | **72** |
| 7 | Finn | 91 |  |  | **95** |
| 8 | Gia | 80 |  |  | **64** |

Formulas used in the example (results shown in **bold** in the table above):

**E2** — largest score

```excel
=LARGE(B2:B8, 1)
```

Result: **95**

**E3** — second-largest score

```excel
=LARGE(B2:B8, 2)
```

Result: **91**

**E4** — third-largest score

```excel
=LARGE(B2:B8, 3)
```

Result: **88**

**E5** — smallest score

```excel
=SMALL(B2:B8, 1)
```

Result: **64**

**E6** — second-smallest score

```excel
=SMALL(B2:B8, 2)
```

Result: **72**

**E7** — MAX matches LARGE k=1

```excel
=MAX(B2:B8)
```

Result: **95**

**E8** — MIN matches SMALL k=1

```excel
=MIN(B2:B8)
```

Result: **64**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Put the comparable numbers in one column (scores, sales, costs).
2. Type `=LARGE(B2:B8, 1)` for the highest value or `=SMALL(B2:B8, 1)` for the lowest.
3. Raise k to walk down the leaderboard: `=LARGE(B2:B8, 2)` is second place by value.
4. Lock the range with $ if you fill a top-N column that must always read the same list.
5. Use RANK when you need each row’s place number instead of the nth value itself.

## Google Sheets-specific notes

Open-ended ranges such as `=LARGE(B2:B, 2)` grow as new scores are entered while blanks stay ignored. Build a live top-N spill with `=ARRAYFORMULA(LARGE(B2:B8, SEQUENCE(3)))` for the three largest values in one formula — useful on dashboards that should not rely on fill-down. SORTN is another Sheets-friendly way to return the top rows with names attached: `=SORTN(A2:B8, 3, 0, 2, FALSE)`. When the workbook must open in Excel, stick to LARGE/SMALL and INDEX/MATCH; avoid SORTN if collaborators use desktop Excel. Locale settings change how decimals display, not which value LARGE selects. If k exceeds the numeric count, Sheets returns #NUM! just like Excel — guard with IF or MIN(k, COUNT(range)).

**Top three values spilled**

```excel
=ARRAYFORMULA(LARGE(B2:B8, SEQUENCE(3)))
```

**Top three rows with names (SORTN)**

```excel
=SORTN(A2:B8, 3, 0, 2, FALSE)
```

**Lowest value**

```excel
=SMALL(B2:B8, 1)
```

**Growing-column second largest**

```excel
=LARGE(B2:B, 2)
```


## Excel version

The same formula works unchanged in Excel:

```excel
=LARGE(B2:B8, 2)
```

Google Sheets supports the same LARGE and SMALL functions with identical k behaviour.

<!--SIBLING-->


## Common errors and how to fix them

- **#NUM!** — k is less than 1, or larger than the count of numeric values in the array. **Fix:** Use a k between 1 and COUNT(range), or wrap with IF to show a blank when k is out of range.
- **Top-N table shifts after fill-down** — The array reference was relative and moved with each row. **Fix:** Absolute-reference the list ($B$2:$B$8) and put 1,2,3 in a helper column for k.
- **Wrong name next to a LARGE value** — MATCH finds the first tie, so duplicate scores can attach the wrong label. **Fix:** Deduplicate carefully, or use a more advanced INDEX/FILTER pattern for nth match.
- **Result differs from a sorted view** — Hidden rows or filtered lists — LARGE still sees the full array, not only visible cells. **Fix:** Copy visible cells to a clean range, or use SUBTOTAL-based helpers for visible-only work.

## FAQ

### What is the difference between LARGE and RANK?

RANK returns a place number for a known value. LARGE/SMALL return the value that sits at place k. Use both when a dashboard needs the amount and its rank.

### Does LARGE(range, 1) equal MAX(range)?

Yes for a plain numeric list. Prefer MAX/MIN when you only need the single extreme; use LARGE/SMALL when k may be 2, 3, or more.

### How do ties work?

Duplicate values each take a slot in the ordered list. If two scores equal 88, LARGE(...,3) and LARGE(...,4) can both return 88.

### Can I get the largest value that meets a condition?

Use MAXIFS for the single conditional maximum. For the nth conditional value, filter the list first (FILTER in Excel 365 / Sheets) then apply LARGE.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
