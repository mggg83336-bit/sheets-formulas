---
title: How to Use the IF Function in Excel
slug: if-excel
date: '2026-10-24'
summary: 'IF checks a condition and returns one value when it is true and another
  when it is false. It is the building block of almost every decision in a spreadsheet:
  pass or fail, free or paid shipping, open or done. This guide covers the syntax,
  three worked examples on an order list, and the mistakes that'
tags:
- Logic & error handling
- Excel
keyword: if-excel
niche: sheets-formulas
provider: structured
entry_id: if
platform: Excel
category: logic
faq:
- q: How do I use IF with more than two outcomes?
  a: Nest one IF inside another, e.g. =IF(B2>=100, "Large", IF(B2>=50, "Medium", "Small")),
    or use IFS in Excel 2019+ and Google Sheets.
- q: How do I check if a cell is blank with IF?
  a: Use =IF(C2="", "Missing", "OK") or =IF(ISBLANK(C2), "Missing", "OK").
- q: Can IF test several conditions at once?
  a: Yes, combine it with AND or OR, e.g. =IF(AND(B2>=50, C2="Yes"), "Free", "Paid").
related:
- - if-and-or-excel
  - if-and-or-google-sheets
- - nested-if-excel
  - nested-if-google-sheets
- - iferror-excel
  - iferror-google-sheets
- - countif-excel
  - countif-google-sheets
- - sumif-excel
  - sumif-google-sheets
sibling: if-google-sheets
---
IF checks a condition and returns one value when it is true and another when it is false. It is the building block of almost every decision in a spreadsheet: pass or fail, free or paid shipping, open or done. This guide covers the syntax, three worked examples on an order list, and the mistakes that make IF return the wrong answer.

## Quick answer

Use this formula in Excel:

```excel
=IF(B2>=50, 0, 5.99)
```

Syntax: `IF(logical_test, value_if_true, [value_if_false])`. If the amount in B2 is at least 50, return 0 (free shipping); otherwise return 5.99.

## The problem

You have an order list with an amount and a shipped flag. Orders of 50 or more ship free, smaller ones pay 5.99, and you want a status column and a total that includes shipping, calculated automatically for every row.

## Worked example

Five orders. Free shipping from 50; order A-104 has no shipped flag yet.

| | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 1 | **Order** | **Amount** | **Shipped** | **Shipping** | **Status** | **Total** |
| 2 | A-101 | 72 | Yes | **0** | **Shipped** | **72** |
| 3 | A-102 | 35 | No | **5.99** | **Open** | **40.99** |
| 4 | A-103 | 50 | Yes | **0** | **Shipped** | **50** |
| 5 | A-104 | 18.5 |  | **5.99** | **Open** | **24.49** |
| 6 | A-105 | 120 | No | **0** | **Open** | **120** |

Formulas used in the example (results shown in **bold** in the table above):

**D2 (filled to D6)** — shipping fee, filled down

```excel
=IF(B2>=50, 0, 5.99)
```

Results: **0**, **5.99**, **0**, **5.99**, **0**

**E2 (filled to E6)** — text result, filled down

```excel
=IF(C2="Yes", "Shipped", "Open")
```

Results: **Shipped**, **Open**, **Shipped**, **Open**, **Open**

**F2 (filled to F6)** — IF inside a calculation, filled down

```excel
=B2+IF(B2>=50, 0, 5.99)
```

Results: **72**, **40.99**, **50**, **24.49**, **120**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `B2>=50` is the logical test. For A-101 it is TRUE because 72 is at least 50.
2. The second argument, `0`, is returned when the test is TRUE. The third, `5.99`, is returned when it is FALSE, as for A-102 (35).
3. A-103 is exactly 50, and `>=` includes the boundary, so it ships free. Use `>` if 50 itself should pay.
4. `C2="Yes"` compares text. Text in the test and in the results must be in double quotes. The comparison is not case-sensitive, so "yes" also counts.
5. A-104 has an empty Shipped cell; the test is FALSE, so it shows "Open".
6. IF can be part of a larger formula: `=B2+IF(B2>=50, 0, 5.99)` adds the fee to the amount, so A-102 totals 40.99.

## Excel-specific notes

The test can be any comparison that returns TRUE or FALSE: `=`, `<>`, `>`, `<`, `>=`, `<=`. Text values in the result arguments must be in double quotes, numbers must not be, otherwise "0" becomes text that SUM ignores. If you leave out the third argument and the test is false, IF returns FALSE. IF can be placed inside a calculation, as in `=B2+IF(B2>=50, 0, 5.99)`. In Microsoft 365 you can give IF a whole range and it spills one result per row: `=IF(B2:B6>=50, 0, 5.99)`. For more than two outcomes, use nested IF or IFS.

**One spilling formula for all rows (Microsoft 365)**

```excel
=IF(B2:B6>=50, 0, 5.99)
```

**IF inside a calculation**

```excel
=B2+IF(B2>=50, 0, 5.99)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=IF(B2>=50, 0, 5.99)
```

Google Sheets uses the identical IF formula. To calculate a whole column from one cell, wrap it in ARRAYFORMULA.

<!--SIBLING-->


## Common errors and how to fix them

- **#NAME?** — Text in the formula is missing its quotes, e.g. =IF(C2=Yes, Shipped, Open). **Fix:** Put every text value in straight double quotes, e.g. "Yes".
- **IF returns FALSE** — The value_if_false argument was left out and the test was false. **Fix:** Add a third argument, even an empty string "", to control what is shown.
- **Test is always FALSE for numbers** — The amounts are stored as text (for example after an import), or the number in the test is in quotes, as in B2>="50". **Fix:** Convert the column to numbers and remove the quotes around numbers in the test; =ISNUMBER(B2) should return TRUE.

## FAQ

### How do I use IF with more than two outcomes?

Nest one IF inside another, e.g. =IF(B2>=100, "Large", IF(B2>=50, "Medium", "Small")), or use IFS in Excel 2019+ and Google Sheets.

### How do I check if a cell is blank with IF?

Use =IF(C2="", "Missing", "OK") or =IF(ISBLANK(C2), "Missing", "OK").

### Can IF test several conditions at once?

Yes, combine it with AND or OR, e.g. =IF(AND(B2>=50, C2="Yes"), "Free", "Paid").

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
