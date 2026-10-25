---
title: How to Use the SWITCH Function in Excel
slug: switch-excel
date: '2026-10-25'
summary: SWITCH compares one expression to a list of exact values and returns the
  matching result. It is the clean alternative to nested IF when you map codes to
  labels, such as status letters to full words. This page shows a worked status example,
  a default fallback, and when IFS is a better fit than SWITCH
tags:
- Logic & error handling
- Excel
keyword: switch-excel
niche: sheets-formulas
provider: structured
entry_id: switch
platform: Excel
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
- - ifs-excel
  - ifs-google-sheets
- - nested-if-excel
  - nested-if-google-sheets
- - if-excel
  - if-google-sheets
- - iferror-excel
  - iferror-google-sheets
sibling: switch-google-sheets
---
SWITCH compares one expression to a list of exact values and returns the matching result. It is the clean alternative to nested IF when you map codes to labels, such as status letters to full words. This page shows a worked status example, a default fallback, and when IFS is a better fit than SWITCH.

## Quick answer

Use this formula in Excel:

```excel
=SWITCH(A2, "P", "Pending", "A", "Approved", "R", "Rejected", "Unknown")
```

Syntax: `SWITCH(expression, value1, result1, [value2, result2], …, [default])`. The expression in A2 is compared for equality to each value in turn. The first match wins; if nothing matches, the optional default ("Unknown") is returned.

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

## Excel-specific notes

SWITCH needs Excel 2019 or Microsoft 365. Comparisons are exact and not case-sensitive for text ("p" matches "P"). SWITCH cannot test ranges such as >=50; use IFS or nested IF for bands. The default is a single trailing argument with no paired value — do not wrap it as TRUE, "Unknown" the way you would in IFS. In Microsoft 365, SWITCH can take a range for the expression and spill one label per row. For large code lists, a VLOOKUP or XLOOKUP against a mapping table is usually easier to maintain than a long SWITCH.

**Nested IF equivalent**

```excel
=IF(A2="P", "Pending", IF(A2="A", "Approved", IF(A2="R", "Rejected", "Unknown")))
```

**Whole column spill (Microsoft 365)**

```excel
=SWITCH(A2:A7, "P", "Pending", "A", "Approved", "R", "Rejected", "Unknown")
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=SWITCH(A2, "P", "Pending", "A", "Approved", "R", "Rejected", "Unknown")
```

Google Sheets uses the same SWITCH formula. Wrap it in ARRAYFORMULA to fill a whole column from one cell.

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
