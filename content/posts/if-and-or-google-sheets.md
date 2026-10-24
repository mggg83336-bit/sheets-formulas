---
title: IF with AND and OR in Google Sheets
slug: if-and-or-google-sheets
date: '2026-10-24'
summary: Combine IF with AND when every condition must be true, and with OR when any
  one of them is enough. A worked bonus-eligibility example shows both, plus the shorthand
  that multiplies and adds conditions for use inside array formulas.
tags:
- Logic & error handling
- Google Sheets
keyword: if-and-or-google-sheets
niche: sheets-formulas
provider: structured
entry_id: if-and-or
platform: Google Sheets
category: logic
faq:
- q: How many conditions can AND or OR have?
  a: Up to 255 in Excel and effectively unlimited in Google Sheets, but if you need
    many, a lookup table is usually clearer.
- q: Is there an XOR?
  a: Yes. XOR returns TRUE when an odd number of conditions are TRUE (with two conditions,
    exactly one). It exists in Excel 2013+ and Google Sheets.
related:
- - nested-if-google-sheets
  - nested-if-excel
- - iferror-google-sheets
  - iferror-excel
- - countifs-google-sheets
  - countifs-excel
- - sumifs-google-sheets
  - sumifs-excel
sibling: if-and-or-excel
---
Combine IF with AND when every condition must be true, and with OR when any one of them is enough. A worked bonus-eligibility example shows both, plus the shorthand that multiplies and adds conditions for use inside array formulas.

## Quick answer

Use this formula in Google Sheets:

```excel
=IF(AND(B2>=50000, C2>=2), "Bonus", "No bonus")
```

Identical syntax in Google Sheets.

## The problem

Employees get a bonus only if they sold at least 50,000 AND have at least 2 years of service. Separately, anyone who sold 50,000 OR has 5+ years should be flagged for a review.

## Worked example

Bonus requires both conditions; review requires either.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Employee** | **Sales** | **Years** | **Bonus** | **Review** |
| 2 | Ana | 52000 | 3 | **Bonus** | **Review** |
| 3 | Ben | 38000 | 6 | **No bonus** | **Review** |
| 4 | Chloe | 61000 | 1 | **No bonus** | **Review** |
| 5 | Dev | 29000 | 2 | **No bonus** | **No** |
| 6 | Eva | 45000 | 5 | **No bonus** | **Review** |

Formulas used in the example (results shown in **bold** in the table above):

**D2 (filled to D6)** — AND, filled down

```excel
=IF(AND(B2>=50000, C2>=2), "Bonus", "No bonus")
```

Results: **Bonus**, **No bonus**, **No bonus**, **No bonus**, **No bonus**

**E2 (filled to E6)** — OR, filled down

```excel
=IF(OR(B2>=50000, C2>=5), "Review", "No")
```

Results: **Review**, **Review**, **Review**, **No**, **Review**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `B2>=50000` and `C2>=2` are tests that return TRUE or FALSE.
2. `AND(...)` is TRUE only if both are TRUE. Ana qualifies; Chloe has the sales but only 1 year, so she does not.
3. `OR(...)` is TRUE if at least one test is TRUE. Ben qualifies for review on years alone, Chloe on sales alone.
4. IF returns the second argument for TRUE and the third for FALSE.
5. Combine them for rules such as "A and (B or C)": `=IF(AND(B2>=50000, OR(C2>=2, D2="VIP")), ...)`.

## Google Sheets-specific notes

In Google Sheets, to fill the whole column from one cell, wrap the multiplied version in ARRAYFORMULA and use open-ended ranges, adding a blank check so empty rows stay empty: `=ARRAYFORMULA(IF(A2:A="", "", IF((B2:B>=50000)*(C2:C>=2), "Bonus", "No bonus")))`. As in Excel, AND and OR cannot be used inside ARRAYFORMULA because they return a single value for the whole range.

**Whole column with ARRAYFORMULA**

```excel
=ARRAYFORMULA(IF(A2:A="", "", IF((B2:B>=50000)*(C2:C>=2), "Bonus", "No bonus")))
```


## Excel version

The same formula works unchanged in Excel:

```excel
=IF(AND(B2>=50000, C2>=2), "Bonus", "No bonus")
```

Excel uses the identical IF/AND/OR formula. In Microsoft 365 the multiplied version spills without any wrapper.

<!--SIBLING-->


## Common errors and how to fix them

- **Everything returns the FALSE value** — Numbers stored as text, so "52000" >= 50000 is FALSE (text is always greater than numbers in comparisons, but text never equals a number). **Fix:** Convert the column to numbers; =ISNUMBER(B2) should be TRUE.
- **#VALUE!** — One of the conditions refers to a cell containing an error, or a range was passed where a single value was expected. **Fix:** Check the referenced cells and use single cells (B2) when filling down.
- **Spilled formula gives one result for all rows** — AND/OR were used with ranges; they collapse to a single value. **Fix:** Use (test1)*(test2) for AND and (test1)+(test2) for OR in array formulas.

## FAQ

### How many conditions can AND or OR have?

Up to 255 in Excel and effectively unlimited in Google Sheets, but if you need many, a lookup table is usually clearer.

### Is there an XOR?

Yes. XOR returns TRUE when an odd number of conditions are TRUE (with two conditions, exactly one). It exists in Excel 2013+ and Google Sheets.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
