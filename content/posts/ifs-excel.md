---
title: How to Use the IFS Function in Excel
slug: ifs-excel
date: '2026-10-24'
summary: 'IFS tests several conditions in order and returns the value for the first
  one that is true. It replaces long nested IF formulas for grade bands, commission
  tiers, and status labels. This page walks through a sales-tier example, shows how
  to add a catch-all default, and explains what happens when no '
tags:
- Logic & error handling
- Excel
keyword: ifs-excel
niche: sheets-formulas
provider: structured
entry_id: ifs
platform: Excel
category: logic
faq:
- q: What is the difference between IFS and nested IF?
  a: Nested IF wraps one IF inside another. IFS lists flat condition/value pairs,
    which is easier to read when you have several outcomes.
- q: Can IFS test text as well as numbers?
  a: Yes. Any expression that returns TRUE or FALSE works, e.g. =IFS(A2="VIP", 0.2,
    A2="Member", 0.1, TRUE, 0).
- q: How many conditions can IFS have?
  a: Excel allows up to 127 condition/value pairs. Google Sheets has no small fixed
    limit, but a lookup table is clearer once the list gets long.
related:
- - nested-if-excel
  - nested-if-google-sheets
- - if-excel
  - if-google-sheets
- - if-and-or-excel
  - if-and-or-google-sheets
- - switch-excel
  - switch-google-sheets
sibling: ifs-google-sheets
---
IFS tests several conditions in order and returns the value for the first one that is true. It replaces long nested IF formulas for grade bands, commission tiers, and status labels. This page walks through a sales-tier example, shows how to add a catch-all default, and explains what happens when no condition matches.

## Quick answer

Use this formula in Excel:

```excel
=IFS(B2>=100000, "Platinum", B2>=50000, "Gold", B2>=20000, "Silver", TRUE, "Bronze")
```

Syntax: `IFS(condition1, value1, [condition2, value2], …)`. Conditions are checked from left to right; the matching value is returned and the rest are ignored. Ending with `TRUE, "Bronze"` makes Bronze the default when every earlier test is false.

## The problem

You classify each salesperson into Platinum, Gold, Silver, or Bronze from their sales total. A nested IF works but is hard to edit when the thresholds change. You want a flat list of condition and result pairs instead.

## Worked example

Six salespeople; tiers are Platinum (≥100000), Gold (≥50000), Silver (≥20000), else Bronze.

| | A | B | C |
|---|---|---|---|
| 1 | **Rep** | **Sales** | **Tier** |
| 2 | Ana | 120000 | **Platinum** |
| 3 | Ben | 75000 | **Gold** |
| 4 | Chloe | 45000 | **Silver** |
| 5 | Dev | 18000 | **Bronze** |
| 6 | Eva | 50000 | **Gold** |
| 7 | Frank | 20000 | **Silver** |

Formulas used in the example (results shown in **bold** in the table above):

**C2 (filled to C7)** — IFS tiers, filled down

```excel
=IFS(B2>=100000, "Platinum", B2>=50000, "Gold", B2>=20000, "Silver", TRUE, "Bronze")
```

Results: **Platinum**, **Gold**, **Silver**, **Bronze**, **Gold**, **Silver**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `B2>=100000` is tested first. Ana's 120000 matches, so IFS returns "Platinum" and stops using further pairs for that row.
2. Ben's 75000 fails the first test, then matches `B2>=50000`, so the result is "Gold".
3. Chloe matches at `B2>=20000` and becomes "Silver". Dev's 18000 fails every sales test, so the final TRUE pair returns "Bronze".
4. Boundary values matter: Eva is exactly 50000 (Gold) and Frank is exactly 20000 (Silver) because the tests use >=.
5. Without the final `TRUE, "Bronze"` pair, Dev would show #N/A instead of a tier.

## Excel-specific notes

IFS needs Excel 2019 or Microsoft 365. Without a final TRUE catch-all, an unmatched value returns #N/A. Put the highest threshold first when using >= tests, otherwise a lower band catches everything above it. IFS evaluates every condition even after one matches, so avoid putting expensive or error-prone expressions in later pairs. For thresholds stored in a table, LOOKUP or approximate-match XLOOKUP is usually easier to maintain than editing the formula. In Microsoft 365 you can pass a whole range and IFS spills one tier per row.

**Nested IF equivalent**

```excel
=IF(B2>=100000, "Platinum", IF(B2>=50000, "Gold", IF(B2>=20000, "Silver", "Bronze")))
```

**Whole column spill (Microsoft 365)**

```excel
=IFS(B2:B7>=100000, "Platinum", B2:B7>=50000, "Gold", B2:B7>=20000, "Silver", TRUE, "Bronze")
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=IFS(B2>=100000, "Platinum", B2>=50000, "Gold", B2>=20000, "Silver", TRUE, "Bronze")
```

Google Sheets uses the same IFS pairs. Wrap the formula in ARRAYFORMULA to fill a whole column from one cell.

<!--SIBLING-->


## Common errors and how to fix them

- **#N/A** — No condition was TRUE and there was no catch-all pair. **Fix:** End IFS with TRUE and a default value, e.g. TRUE, "Bronze".
- **Everyone gets the lowest tier** — Conditions were written in the wrong order (e.g. >=20000 before >=100000), so the first matching band catches high values too. **Fix:** List the strictest or highest threshold first when using >= tests.
- **#NAME?** — Excel 2016 or older does not have IFS. **Fix:** Use nested IF, or upgrade to Excel 2019 / Microsoft 365.

## FAQ

### What is the difference between IFS and nested IF?

Nested IF wraps one IF inside another. IFS lists flat condition/value pairs, which is easier to read when you have several outcomes.

### Can IFS test text as well as numbers?

Yes. Any expression that returns TRUE or FALSE works, e.g. =IFS(A2="VIP", 0.2, A2="Member", 0.1, TRUE, 0).

### How many conditions can IFS have?

Excel allows up to 127 condition/value pairs. Google Sheets has no small fixed limit, but a lookup table is clearer once the list gets long.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
