---
title: Nested IF Formulas (and Cleaner Alternatives) in Google Sheets
slug: nested-if-google-sheets
date: '2026-10-24'
summary: A nested IF puts one IF inside another to test several conditions in order,
  such as turning scores into letter grades. Here is a correct nested IF, the easier-to-read
  IFS version, and a lookup-table approach that avoids nesting altogether.
tags:
- Logic & error handling
- Google Sheets
keyword: nested-if-google-sheets
niche: sheets-formulas
provider: structured
entry_id: nested-if
platform: Google Sheets
category: logic
faq:
- q: How many IFs can be nested?
  a: 64 in Excel 2007 and later. Google Sheets has no fixed small limit, but readability
    suffers long before you reach any limit.
- q: When should I use SWITCH instead?
  a: SWITCH is for exact values (e.g. turning "N" into "North"), not ranges of numbers
    like grade thresholds.
related:
- - if-and-or-google-sheets
  - if-and-or-excel
- - iferror-google-sheets
  - iferror-excel
- - vlookup-google-sheets
  - vlookup-excel
- - xlookup-google-sheets
  - xlookup-excel
sibling: nested-if-excel
---
A nested IF puts one IF inside another to test several conditions in order, such as turning scores into letter grades. Here is a correct nested IF, the easier-to-read IFS version, and a lookup-table approach that avoids nesting altogether.

## Quick answer

Use this formula in Google Sheets:

```excel
=IF(B2>=90, "A", IF(B2>=80, "B", IF(B2>=70, "C", IF(B2>=60, "D", "F"))))
```

Identical in Google Sheets.

## The problem

You need to convert test scores into grades: 90 and above is A, 80 to 89 is B, 70 to 79 is C, 60 to 69 is D, and anything lower is F.

## Worked example

Scores in column B, three ways to get the grade.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Student** | **Score** | **Nested IF** | **IFS** | **LOOKUP** |
| 2 | Ava | 95 | **A** | **A** | **A** |
| 3 | Liam | 83 | **B** | **B** | **B** |
| 4 | Mia | 71 | **C** | **C** | **C** |
| 5 | Noah | 64 | **D** | **D** | **D** |
| 6 | Zoe | 52 | **F** | **F** | **F** |
| 7 | Eli | 80 | **B** | **B** | **B** |

Formulas used in the example (results shown in **bold** in the table above):

**C2 (filled to C7)**

```excel
=IF(B2>=90, "A", IF(B2>=80, "B", IF(B2>=70, "C", IF(B2>=60, "D", "F"))))
```

Results: **A**, **B**, **C**, **D**, **F**, **B**

**D2 (filled to D7)**

```excel
=IFS(B2>=90, "A", B2>=80, "B", B2>=70, "C", B2>=60, "D", TRUE, "F")
```

Results: **A**, **B**, **C**, **D**, **F**, **B**

**E2 (filled to E7)**

```excel
=LOOKUP(B2, {0,60,70,80,90}, {"F","D","C","B","A"})
```

Results: **A**, **B**, **C**, **D**, **F**, **B**

<!--AD_IN_ARTICLE-->

## How the formula works

1. The first IF checks the highest threshold. If B2 is 90 or more it returns "A" and stops.
2. Otherwise the next IF runs. It only needs `B2>=80` because anything 90+ was already handled.
3. The pattern continues down to the last IF, whose FALSE value ("F") catches everything else.
4. Note the boundary: Eli's 80 is a B because the test is >= 80. Use > if a score of exactly 80 should be a C.
5. LOOKUP finds the largest threshold that is less than or equal to the score in {0,60,70,80,90} and returns the grade in the same position.

## Google Sheets-specific notes

Google Sheets supports IFS and SWITCH as well. A nested IF cannot be applied to a whole column in Sheets without ARRAYFORMULA, but IFS inside ARRAYFORMULA can be awkward because IFS evaluates every pair. A cleaner whole-column option is the lookup approach: `=ARRAYFORMULA(IF(B2:B="", "", LOOKUP(B2:B, {0,60,70,80,90}, {"F","D","C","B","A"})))`. In locales that use a comma as the decimal separator, array constants use backslashes and semicolons instead of commas, e.g. {0\60\70}.

**Whole column of grades from one formula**

```excel
=ARRAYFORMULA(IF(B2:B="", "", LOOKUP(B2:B, {0,60,70,80,90}, {"F","D","C","B","A"})))
```


## Excel version

The same formula works unchanged in Excel:

```excel
=IF(B2>=90, "A", IF(B2>=80, "B", IF(B2>=70, "C", IF(B2>=60, "D", "F"))))
```

Excel uses the same nested IF. IFS needs Excel 2019 or Microsoft 365.

<!--SIBLING-->


## Common errors and how to fix them

- **Every score returns the same grade** — The tests are in the wrong order (e.g. >=60 checked first catches everything above 60). **Fix:** Test from the highest threshold down, or from the lowest up using < comparisons.
- **#N/A from IFS** — No condition was TRUE and there was no catch-all. **Fix:** End IFS with TRUE, "default value".
- **"You've entered too few arguments" / parse error** — A missing closing parenthesis or comma in a long nested IF. **Fix:** Count one closing parenthesis per IF at the end, or switch to IFS / LOOKUP.

## FAQ

### How many IFs can be nested?

64 in Excel 2007 and later. Google Sheets has no fixed small limit, but readability suffers long before you reach any limit.

### When should I use SWITCH instead?

SWITCH is for exact values (e.g. turning "N" into "North"), not ranges of numbers like grade thresholds.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
