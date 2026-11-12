---
title: How to Use the CHOOSE Function in Google Sheets
slug: choose-google-sheets
date: '2026-11-12'
summary: 'CHOOSE returns the value in position n from a list of arguments, so a 1,
  2 or 3 in a cell can pick a label, a number, or even a whole range to feed into
  SUM or AVERAGE. It is the positional cousin of SWITCH, which matches on a value
  instead of a position. The same function works in Excel and Google '
tags:
- Lookup & reference
- Google Sheets
keyword: choose-google-sheets
niche: sheets-formulas
provider: structured
entry_id: choose
platform: Google Sheets
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
- - switch-google-sheets
  - switch-excel
- - ifs-google-sheets
  - ifs-excel
- - nested-if-google-sheets
  - nested-if-excel
- - index-match-google-sheets
  - index-match-excel
- - if-google-sheets
  - if-excel
sibling: choose-excel
---
CHOOSE returns the value in position n from a list of arguments, so a 1, 2 or 3 in a cell can pick a label, a number, or even a whole range to feed into SUM or AVERAGE. It is the positional cousin of SWITCH, which matches on a value instead of a position. The same function works in Excel and Google Sheets; SWITCH or IFS is often clearer when you are mapping codes rather than positions.

## Quick answer

Use this formula in Google Sheets:

```excel
=CHOOSE(D2, "East", "West")
```

Identical syntax in Google Sheets: `CHOOSE(index, value1, [value2], …)` returns the value at that position. With D2 equal to 2 the result is "West".

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
5. If you would rather match a name or a code than a position, switch to [SWITCH](../switch-google-sheets/) or a lookup table. Use [IFS](../ifs-google-sheets/) when each branch is a condition, such as a score band, rather than an index number.

## Google Sheets-specific notes

Sheets CHOOSE matches Excel for positional picks, truncated non-integer indexes, and `#VALUE!` when the index is out of range. Range arguments work the same way, so `=SUM(CHOOSE(D2, B2:B5, C2:C5))` is a valid way to total the selected region. Two Sheets-specific habits are worth knowing. First, to label a whole column from one cell, wrap CHOOSE in ARRAYFORMULA and blank-check the index column, for example `=ARRAYFORMULA(IF(D2:D="", "", CHOOSE(D2:D, "East", "West")))`. CHOOSE inside ARRAYFORMULA can be picky with range-returning arguments, so keep those wraps on the simple, single-value form and use a helper cell for the SUM pattern. Second, SWITCH is usually the better Sheets formula when the input is a code or a name rather than a position, and IFS is better for numeric bands. INDEX on a literal array (`=INDEX({"East","West"}, D2)`) is a concise alternative that also works inside ARRAYFORMULA. CHOOSECOLS and CHOOSEROWS exist in current Sheets and, as in Excel, they select from an array rather than from a list of CHOOSE arguments — do not confuse them with CHOOSE. If the file must open in older Excel, stay with plain CHOOSE and skip ARRAYFORMULA.

**Whole column of labels with ARRAYFORMULA**

```excel
=ARRAYFORMULA(IF(D2:D="", "", CHOOSE(D2:D, "East", "West")))
```

**SWITCH with a default for an unknown index**

```excel
=SWITCH(D2, 1, "East", 2, "West", "Unknown")
```

**Sum of the column picked by the index**

```excel
=SUM(CHOOSE(D2, B2:B5, C2:C5))
```


## Excel version

The same formula works unchanged in Excel:

```excel
=CHOOSE(D2, "East", "West")
```

Google Sheets uses the same CHOOSE syntax, including a range as a value argument. SWITCH and IFS are available in Sheets too. For a whole-column fill, Sheets wraps CHOOSE in ARRAYFORMULA; Microsoft 365 can spill from a range of indexes instead.

<!--SIBLING-->


## Common errors and how to fix them

- **#VALUE!** — The index is 0, negative, blank, text that is not a number, or larger than the number of value arguments. CHOOSE has no default fallback. **Fix:** Validate the index (for example with IF or IFERROR) or use SWITCH, which accepts a final default argument such as "Unknown".
- **#NAME?** — The function was misspelled, or it was confused with CHOOSEROWS / CHOOSECOLS, which are separate functions and need a current Excel 365 or Sheets version. **Fix:** Use `CHOOSE` for a list of arguments. Use CHOOSEROWS or CHOOSECOLS only when you are picking from an existing array.
- **The wrong column is summed, or only the first cell is returned** — The index is off by one (people often treat 0 as the first item), or CHOOSE was not wrapped in SUM / AVERAGE so only the first cell of the range is displayed. **Fix:** Remember that CHOOSE is 1-based. Wrap a range result in the aggregate you want, and check the index with a helper cell if needed.
- **A decimal index such as 2.9 returns the second value** — CHOOSE truncates the index toward zero rather than rounding. **Fix:** Wrap the index in ROUND if you want 2.9 to mean 3, or use INT only when truncation is the intended rule.

## FAQ

### When should I use CHOOSE instead of SWITCH or IFS?

Use CHOOSE when the input is already a position (1, 2, 3) or when you want to hand a whole range to SUM. Use [SWITCH](../switch-google-sheets/) to map exact codes or names to labels, and [IFS](../ifs-google-sheets/) or [nested IF](../nested-if-google-sheets/) when each branch is a different condition.

### Can CHOOSE return a range, not just a single value?

Yes. `=SUM(CHOOSE(D2, B2:B5, C2:C5))` is the standard pattern in both Excel and Google Sheets. That is the main trick CHOOSE still has over SWITCH, which is better at labels than at returning a range.

### What happens if the index is out of range?

You get `#VALUE!`. Unlike SWITCH, CHOOSE has no trailing default. Guard it with `=IFERROR(CHOOSE(D2, "East", "West"), "Unknown")`, or validate the index first.

### Is CHOOSE the same as CHOOSEROWS or CHOOSECOLS?

No. CHOOSE picks from a list of arguments you type into the formula. CHOOSEROWS and CHOOSECOLS pick rows or columns out of an existing array and are separate functions in Microsoft 365 and current Google Sheets.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
