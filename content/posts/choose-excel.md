---
title: How to Use the CHOOSE Function in Excel
slug: choose-excel
date: '2026-11-12'
summary: 'CHOOSE returns the value in position n from a list of arguments, so a 1,
  2 or 3 in a cell can pick a label, a number, or even a whole range to feed into
  SUM or AVERAGE. It is the positional cousin of SWITCH, which matches on a value
  instead of a position. The same function works in Excel and Google '
tags:
- Lookup & reference
- Excel
keyword: choose-excel
niche: sheets-formulas
provider: structured
entry_id: choose
platform: Excel
category: lookup
faq:
- q: When should I use CHOOSE instead of SWITCH or IFS?
  a: Use CHOOSE when the input is already a position (1, 2, 3) or when you want to
    hand a whole range to SUM. Use SWITCH to map exact codes or names to labels, and
    IFS or nested IF when each branch is a different condition.
- q: Can CHOOSE return a range, not just a single value?
  a: Yes. =SUM(CHOOSE(D2, B2:B5, C2:C5)) is the standard pattern in both Excel and
    Google Sheets. That is the main trick CHOOSE still has over SWITCH, which is better
    at labels than at returning a range.
- q: What happens if the index is out of range?
  a: 'You get #VALUE!. Unlike SWITCH, CHOOSE has no trailing default. Guard it with
    =IFERROR(CHOOSE(D2, "East", "West"), "Unknown"), or validate the index first.'
- q: Is CHOOSE the same as CHOOSEROWS or CHOOSECOLS?
  a: No. CHOOSE picks from a list of arguments you type into the formula. CHOOSEROWS
    and CHOOSECOLS pick rows or columns out of an existing array and are separate
    functions in Microsoft 365 and current Google Sheets.
related:
- - switch-excel
  - switch-google-sheets
- - ifs-excel
  - ifs-google-sheets
- - nested-if-excel
  - nested-if-google-sheets
- - index-match-excel
  - index-match-google-sheets
- - if-excel
  - if-google-sheets
sibling: choose-google-sheets
---
CHOOSE returns the value in position n from a list of arguments, so a 1, 2 or 3 in a cell can pick a label, a number, or even a whole range to feed into SUM or AVERAGE. It is the positional cousin of SWITCH, which matches on a value instead of a position. The same function works in Excel and Google Sheets; SWITCH or IFS is often clearer when you are mapping codes rather than positions.

## Quick answer

Use this formula in Excel:

```excel
=CHOOSE(D2, "East", "West")
```

Syntax: `CHOOSE(index_num, value1, [value2], …)`. `index_num` is a number from 1 to the number of value arguments (up to 254 in Excel). With D2 equal to 2, CHOOSE returns the second value, "West". Each value can be a constant, a cell, a formula, or a range; when it is a range, you can wrap CHOOSE in SUM or AVERAGE to aggregate the chosen column.

## The problem

A report lets you type 1 or 2 to pick the East or West column, and you also want a status number such as 3 to show as “Delivered”. You need one formula that can return a label and another that can hand an entire column to SUM, without a nested IF.

## Worked example

East and West quantities for four fruits, with a region choice of 2 in D2. E2 returns the region name, E3 the sum of the chosen column, E4 a status label from a fixed index of 3, and E5 the average of the East column.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Item** | **East** | **West** | **Choice** | **Result** |
| 2 | Apples | 40 | 55 | 2 | **West** |
| 3 | Bananas | 22 | 30 |  | **126** |
| 4 | Cherries | 18 | 25 |  | **Delivered** |
| 5 | Dates | 12 | 16 |  | **23** |

Formulas used in the example (results shown in **bold** in the table above):

**E2** — region name picked by the index in D2

```excel
=CHOOSE(D2, "East", "West")
```

Result: **West**

**E3** — sum of the column picked by D2

```excel
=SUM(CHOOSE(D2, B2:B5, C2:C5))
```

Result: **126**

**E4** — status label for a fixed index of 3

```excel
=CHOOSE(3, "Pending", "Shipped", "Delivered", "Returned")
```

Result: **Delivered**

**E5** — average of the East column (index 1)

```excel
=AVERAGE(CHOOSE(1, B2:B5, C2:C5))
```

Result: **23**

<!--AD_IN_ARTICLE-->

## How the formula works

1. D2 holds the position, 2. `=CHOOSE(D2, "East", "West")` returns the second label, West. Changing D2 to 1 would return East.
2. A value argument can be a range. `=SUM(CHOOSE(D2, B2:B5, C2:C5))` selects the West column (C2:C5) and adds 55 + 30 + 25 + 16 = 126.
3. The index can also be typed into the formula. `=CHOOSE(3, "Pending", "Shipped", "Delivered", "Returned")` returns Delivered, the third label, which is a handy way to turn a status number into a word.
4. `=AVERAGE(CHOOSE(1, B2:B5, C2:C5))` forces the first column and returns 23, the average of 40, 22, 18 and 12. The same pattern works with MIN, MAX or COUNTA.
5. If you would rather match a name or a code than a position, switch to [SWITCH](../switch-excel/) or a lookup table. Use [IFS](../ifs-excel/) when each branch is a condition, such as a score band, rather than an index number.

## Excel-specific notes

CHOOSE is available in every Excel version, which makes it useful in workbooks that still have to open in Excel 2016. It is a poor fit for mapping codes such as "P" or "A" to labels — that is what SWITCH (Excel 2019 / Microsoft 365) or a lookup table is for, because CHOOSE only understands a position number. There is no default argument: an index of 0, a negative number, or a number larger than the list returns `#VALUE!`. A non-integer index is truncated (2.9 is treated as 2). The classic power-user trick is to return a range: `=SUM(CHOOSE(D2, B2:B5, C2:C5))` adds whichever column the index points at, and the same pattern works with AVERAGE, MIN, or a chart series. In Microsoft 365, SWITCH, IFS, and INDEX on a horizontal list often read more clearly for labels, and CHOOSEROWS / CHOOSECOLS (different functions) pick rows or columns out of an array rather than from a list of arguments. For a long, maintained list of options, put the values in a range and use INDEX; editing a 20-argument CHOOSE formula is brittle.

**Sum of the column picked by the index**

```excel
=SUM(CHOOSE(D2, B2:B5, C2:C5))
```

**SWITCH when you match a label, not a position**

```excel
=SWITCH(D2, 1, "East", 2, "West", "Unknown")
```

**INDEX on a horizontal list of labels**

```excel
=INDEX({"East","West"}, D2)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=CHOOSE(D2, "East", "West")
```

Excel uses the same CHOOSE formula. Whole-column fills in Excel 365 spill from a range of indexes; in Sheets you wrap CHOOSE in ARRAYFORMULA. SWITCH needs Excel 2019 or later, but is available in Sheets.

<!--SIBLING-->


## Common errors and how to fix them

- **#VALUE!** — The index is 0, negative, blank, text that is not a number, or larger than the number of value arguments. CHOOSE has no default fallback. **Fix:** Validate the index (for example with IF or IFERROR) or use SWITCH, which accepts a final default argument such as "Unknown".
- **#NAME?** — The function was misspelled, or it was confused with CHOOSEROWS / CHOOSECOLS, which are separate functions and need a current Excel 365 or Sheets version. **Fix:** Use `CHOOSE` for a list of arguments. Use CHOOSEROWS or CHOOSECOLS only when you are picking from an existing array.
- **The wrong column is summed, or only the first cell is returned** — The index is off by one (people often treat 0 as the first item), or CHOOSE was not wrapped in SUM / AVERAGE so only the first cell of the range is displayed. **Fix:** Remember that CHOOSE is 1-based. Wrap a range result in the aggregate you want, and check the index with a helper cell if needed.
- **A decimal index such as 2.9 returns the second value** — CHOOSE truncates the index toward zero rather than rounding. **Fix:** Wrap the index in ROUND if you want 2.9 to mean 3, or use INT only when truncation is the intended rule.

## FAQ

### When should I use CHOOSE instead of SWITCH or IFS?

Use CHOOSE when the input is already a position (1, 2, 3) or when you want to hand a whole range to SUM. Use [SWITCH](../switch-excel/) to map exact codes or names to labels, and [IFS](../ifs-excel/) or [nested IF](../nested-if-excel/) when each branch is a different condition.

### Can CHOOSE return a range, not just a single value?

Yes. `=SUM(CHOOSE(D2, B2:B5, C2:C5))` is the standard pattern in both Excel and Google Sheets. That is the main trick CHOOSE still has over SWITCH, which is better at labels than at returning a range.

### What happens if the index is out of range?

You get `#VALUE!`. Unlike SWITCH, CHOOSE has no trailing default. Guard it with `=IFERROR(CHOOSE(D2, "East", "West"), "Unknown")`, or validate the index first.

### Is CHOOSE the same as CHOOSEROWS or CHOOSECOLS?

No. CHOOSE picks from a list of arguments you type into the formula. CHOOSEROWS and CHOOSECOLS pick rows or columns out of an existing array and are separate functions in Microsoft 365 and current Google Sheets.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
