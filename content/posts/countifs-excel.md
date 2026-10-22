---
title: COUNTIFS with Multiple Criteria in Excel
slug: countifs-excel
date: '2026-10-22'
summary: COUNTIFS counts rows that meet several conditions at once, such as deals
  that are both won and above a certain size, or values between two numbers. Includes
  a worked pipeline example and how to do OR logic.
tags:
- Conditional sums & counts
- Excel
keyword: countifs-excel
niche: sheets-formulas
provider: structured
entry_id: countifs
platform: Excel
category: conditional
faq:
- q: Is there a limit to the number of conditions?
  a: COUNTIFS accepts up to 127 range/criteria pairs in Excel; you will rarely need
    more than a few.
- q: How do I count rows where two columns are equal?
  a: COUNTIFS cannot compare columns to each other. Use =SUMPRODUCT(--(B2:B8=C2:C8)).
- q: How do I count rows between two dates?
  a: 'Use the date column twice: =COUNTIFS(A2:A100, ">="&E1, A2:A100, "<="&E2), where
    E1 and E2 hold the start and end dates. Join the operator and the cell with &,
    exactly as with numbers.'
- q: Can COUNTIFS use wildcards?
  a: Yes. =COUNTIFS(A2:A8, "K*", D2:D8, "Won") counts won deals for reps whose name
    starts with K. Use * for any number of characters and ? for exactly one character.
related:
- - countif-excel
  - countif-google-sheets
- - sumifs-excel
  - sumifs-google-sheets
- - count-unique-excel
  - count-unique-google-sheets
- - maxifs-minifs-excel
  - maxifs-minifs-google-sheets
sibling: countifs-google-sheets
---
COUNTIFS counts rows that meet several conditions at once, such as deals that are both won and above a certain size, or values between two numbers. Includes a worked pipeline example and how to do OR logic.

## Quick answer

Use this formula in Excel:

```excel
=COUNTIFS(B2:B8, "East", D2:D8, "Won")
```

Syntax: `COUNTIFS(criteria_range1, criteria1, [criteria_range2, criteria2], ...)`. A row is counted only if every condition is true.

## The problem

In a sales pipeline you want to count won deals in the East, won deals worth at least 10,000, and deals between 5,000 and 10,000.

## Worked example

A small sales pipeline.

| | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| 1 | **Rep** | **Region** | **Deal size** | **Stage** |  | **Question** | **Count** |
| 2 | Kim | East | 12000 | Won |  | East and Won | **3** |
| 3 | Ruiz | West | 8000 | Lost |  | Won and >= 10,000 | **4** |
| 4 | Patel | East | 15000 | Won |  | 5,000 to 10,000 | **2** |
| 5 | Lee | North | 11000 | Won |  |  |  |
| 6 | Kim | East | 3000 | Lost |  |  |  |
| 7 | Ruiz | West | 22000 | Won |  |  |  |
| 8 | Patel | East | 9000 | Won |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**G2**

```excel
=COUNTIFS(B2:B8, "East", D2:D8, "Won")
```

Result: **3**

**G3**

```excel
=COUNTIFS(D2:D8, "Won", C2:C8, ">=10000")
```

Result: **4**

**G4**

```excel
=COUNTIFS(C2:C8, ">=5000", C2:C8, "<=10000")
```

Result: **2**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Each pair is a range and a condition. `B2:B8, "East"` keeps East rows.
2. `D2:D8, "Won"` keeps only won deals among those. Kim (12,000), Patel (15,000) and Patel (9,000) remain: 3.
3. Conditions on numbers use quoted operators: `">=10000"`.
4. Using the same column twice creates a range: at least 5,000 and at most 10,000 matches 8,000 and 9,000.

## Excel-specific notes

To count values between two numbers, use the same column twice with two conditions. For OR logic (Won OR Lost in East), use an array constant and SUM: `=SUM(COUNTIFS(B2:B8, "East", D2:D8, {"Won","Lost"}))`. All ranges must be the same shape; unlike SUMIFS there is no separate range to add.


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=COUNTIFS(B2:B8, "East", D2:D8, "Won")
```

Google Sheets uses the same syntax, but array constants for OR logic need ARRAYFORMULA.

<!--SIBLING-->


## Common errors and how to fix them

- **#VALUE!** — The criteria ranges are different sizes. **Fix:** Make every range cover the same rows.
- **Count too high with "<>"** — "<>Won" also counts blank cells. **Fix:** Add another condition that excludes blanks: D2:D8, "<>".
- **Count is 0** — Numbers stored as text or trailing spaces. **Fix:** Clean and convert the data, then re-check each condition separately with COUNTIF.

## FAQ

### Is there a limit to the number of conditions?

COUNTIFS accepts up to 127 range/criteria pairs in Excel; you will rarely need more than a few.

### How do I count rows where two columns are equal?

COUNTIFS cannot compare columns to each other. Use =SUMPRODUCT(--(B2:B8=C2:C8)).

### How do I count rows between two dates?

Use the date column twice: =COUNTIFS(A2:A100, ">="&E1, A2:A100, "<="&E2), where E1 and E2 hold the start and end dates. Join the operator and the cell with &, exactly as with numbers.

### Can COUNTIFS use wildcards?

Yes. =COUNTIFS(A2:A8, "K*", D2:D8, "Won") counts won deals for reps whose name starts with K. Use * for any number of characters and ? for exactly one character.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
