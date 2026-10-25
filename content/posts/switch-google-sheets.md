---
title: How to Use the SWITCH Function in Google Sheets
slug: switch-google-sheets
date: '2026-10-25'
summary: SWITCH compares one expression to a list of exact values and returns the
  matching result. It is the clean alternative to nested IF when you map codes to
  labels, such as status letters to full words. This page shows a worked status example,
  a default fallback, and when IFS is a better fit than SWITCH
tags:
- Logic & error handling
- Google Sheets
keyword: switch-google-sheets
niche: sheets-formulas
provider: structured
entry_id: switch
platform: Google Sheets
category: logic
faq:
- q: When should I use SWITCH instead of IFS?
  a: Use SWITCH for exact value mapping (codes to labels). Use IFS when each branch
    is a different condition, such as score >= 90.
- q: Is SWITCH case-sensitive?
  a: No. In Excel and Google Sheets, "p" and "P" are treated as the same text match.
- q: Can the default be another formula?
  a: Yes. The final argument can be a formula or cell reference, not only a fixed
    string.
related:
- - ifs-google-sheets
  - ifs-excel
- - nested-if-google-sheets
  - nested-if-excel
- - if-google-sheets
  - if-excel
- - iferror-google-sheets
  - iferror-excel
sibling: switch-excel
---
SWITCH compares one expression to a list of exact values and returns the matching result. It is the clean alternative to nested IF when you map codes to labels, such as status letters to full words. This page shows a worked status example, a default fallback, and when IFS is a better fit than SWITCH.

## Quick answer

Use this formula in Google Sheets:

```excel
=SWITCH(A2, "P", "Pending", "A", "Approved", "R", "Rejected", "Unknown")
```

Identical syntax in Google Sheets: one expression, then value/result pairs, then an optional default.

## The problem

Your order sheet stores status as short codes (P, A, R). Reports need readable labels like Pending, Approved, and Rejected, including a sensible default when someone types an unknown code.

## Worked example

Six order status codes; unknown codes should show Unknown.

| | A | B |
|---|---|---|
| 1 | **Code** | **Label** |
| 2 | P | **Pending** |
| 3 | A | **Approved** |
| 4 | R | **Rejected** |
| 5 | P | **Pending** |
| 6 | X | **Unknown** |
| 7 | A | **Approved** |

Formulas used in the example (results shown in **bold** in the table above):

**B2 (filled to B7)** — SWITCH labels, filled down

```excel
=SWITCH(A2, "P", "Pending", "A", "Approved", "R", "Rejected", "Unknown")
```

Results: **Pending**, **Approved**, **Rejected**, **Pending**, **Unknown**, **Approved**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `A2` holds the expression to match. For the first row it is the text "P".
2. SWITCH compares "P" to each listed value. The first pair matches, so the result is "Pending".
3. Row 3 matches "R" and returns "Rejected". Row 5 has "X", which matches none of the codes, so the default "Unknown" is returned.
4. Only exact equality is tested. To map numeric ranges (for example score bands), use IFS instead.
5. You can nest a formula as the expression, e.g. `=SWITCH(LEFT(A2,1), "P", …)`, when the code is part of a longer string.

## Google Sheets-specific notes

Google Sheets SWITCH works the same way for exact matches. To label an entire column from one cell, wrap it in ARRAYFORMULA and blank-check the code column: `=ARRAYFORMULA(IF(A2:A="", "", SWITCH(A2:A, "P", "Pending", "A", "Approved", "R", "Rejected", "Unknown")))`. Sheets comparisons are also case-insensitive for plain text. If your codes live in a separate mapping sheet, prefer VLOOKUP or a MAP/LAMBDA pattern over a huge SWITCH, so new codes can be added without editing every formula. SWITCH is a poor fit for numeric bands; use IFS there.

**Whole column with ARRAYFORMULA**

```excel
=ARRAYFORMULA(IF(A2:A="", "", SWITCH(A2:A, "P", "Pending", "A", "Approved", "R", "Rejected", "Unknown")))
```

**Lookup from a mapping table**

```excel
=IFERROR(VLOOKUP(A2, {"P","Pending";"A","Approved";"R","Rejected"}, 2, FALSE), "Unknown")
```


## Excel version

The same formula works unchanged in Excel:

```excel
=SWITCH(A2, "P", "Pending", "A", "Approved", "R", "Rejected", "Unknown")
```

Excel uses the same SWITCH syntax from Excel 2019 onward. Microsoft 365 can spill labels for a whole column from one formula.

<!--SIBLING-->


## Common errors and how to fix them

- **#N/A** — No value matched and no default argument was supplied. **Fix:** Add a final default argument such as "Unknown", or wrap SWITCH in IFERROR.
- **#NAME?** — Excel 2016 or older does not include SWITCH. **Fix:** Use nested IF, or upgrade to Excel 2019 / Microsoft 365.
- **Wrong label for a code you can see** — Extra spaces in the cell ("P ") or looking up a number when the list is text. **Fix:** TRIM the codes and make sure both sides are the same type; =A2="P" should be TRUE.

## FAQ

### When should I use SWITCH instead of IFS?

Use SWITCH for exact value mapping (codes to labels). Use IFS when each branch is a different condition, such as score >= 90.

### Is SWITCH case-sensitive?

No. In Excel and Google Sheets, "p" and "P" are treated as the same text match.

### Can the default be another formula?

Yes. The final argument can be a formula or cell reference, not only a fixed string.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
