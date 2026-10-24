---
title: How to Use the IFS Function in Google Sheets
slug: ifs-google-sheets
date: '2026-10-24'
summary: 'IFS tests several conditions in order and returns the value for the first
  one that is true. It replaces long nested IF formulas for grade bands, commission
  tiers, and status labels. This page walks through a sales-tier example, shows how
  to add a catch-all default, and explains what happens when no '
tags:
- Logic & error handling
- Google Sheets
keyword: ifs-google-sheets
niche: sheets-formulas
provider: structured
entry_id: ifs
platform: Google Sheets
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
- - nested-if-google-sheets
  - nested-if-excel
- - if-google-sheets
  - if-excel
- - if-and-or-google-sheets
  - if-and-or-excel
- - switch-google-sheets
  - switch-excel
sibling: ifs-excel
---
IFS tests several conditions in order and returns the value for the first one that is true. It replaces long nested IF formulas for grade bands, commission tiers, and status labels. This page walks through a sales-tier example, shows how to add a catch-all default, and explains what happens when no condition matches.

## Quick answer

Use this formula in Google Sheets:

```excel
=IFS(B2>=100000, "Platinum", B2>=50000, "Gold", B2>=20000, "Silver", TRUE, "Bronze")
```

Same syntax in Google Sheets: pairs of condition and value, evaluated left to right until one is true.

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

## Google Sheets-specific notes

Google Sheets has supported IFS for years. Like Excel, an unmatched value returns #N/A unless you end with TRUE and a default. To fill an entire column from one cell, wrap IFS in ARRAYFORMULA and skip blank sales rows so empty lines stay empty: `=ARRAYFORMULA(IF(A2:A="", "", IFS(B2:B>=100000, "Platinum", B2:B>=50000, "Gold", B2:B>=20000, "Silver", TRUE, "Bronze")))`. Be careful that IFS still evaluates later conditions; a division in a later pair can throw an error even when an earlier pair already matched. For many bands, a LOOKUP against a small threshold table inside ARRAYFORMULA is often cleaner than a long IFS.

**Whole column with ARRAYFORMULA**

```excel
=ARRAYFORMULA(IF(A2:A="", "", IFS(B2:B>=100000, "Platinum", B2:B>=50000, "Gold", B2:B>=20000, "Silver", TRUE, "Bronze")))
```

**Lookup table instead of IFS**

```excel
=ARRAYFORMULA(IF(B2:B="", "", LOOKUP(B2:B, {0,20000,50000,100000}, {"Bronze","Silver","Gold","Platinum"})))
```


## Excel version

The same formula works unchanged in Excel:

```excel
=IFS(B2>=100000, "Platinum", B2>=50000, "Gold", B2>=20000, "Silver", TRUE, "Bronze")
```

Excel uses the same IFS syntax from Excel 2019 onward. Microsoft 365 can spill a whole column of results from one formula.

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
