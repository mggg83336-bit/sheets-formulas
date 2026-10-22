---
title: How to Lookup the Last Value in a Column in Excel
slug: last-value-excel
date: '2026-10-22'
summary: Need the most recent entry in a log, a running balance or a meter reading?
  These formulas return the last non-empty value in a column, even when there are
  blank cells in between, plus the matching date from the next column.
tags:
- Lookup & reference
- Excel
keyword: last-value-excel
niche: sheets-formulas
provider: structured
entry_id: last-value
platform: Excel
category: lookup
faq:
- q: Does this work with text values?
  a: Yes. The LOOKUP(2, 1/(...)) pattern returns the last non-empty value whether
    it is a number or text.
- q: How do I get the last value that meets a condition?
  a: Multiply in the condition, e.g. =LOOKUP(2, 1/((B2:B100<>"")*(C2:C100="Paid")),
    B2:B100).
related:
- - xlookup-excel
  - xlookup-google-sheets
- - index-match-excel
  - index-match-google-sheets
- - lookup-multiple-values-excel
  - lookup-multiple-values-google-sheets
- - eomonth-excel
  - eomonth-google-sheets
sibling: last-value-google-sheets
---
Need the most recent entry in a log, a running balance or a meter reading? These formulas return the last non-empty value in a column, even when there are blank cells in between, plus the matching date from the next column.

## Quick answer

Use this formula in Excel:

```excel
=LOOKUP(2, 1/(B2:B100<>""), B2:B100)
```

1/(B2:B100<>"") gives 1 for filled cells and #DIV/0! for blanks. LOOKUP searches for 2, cannot find it, and falls back to the last numeric value, which is the last filled row.

## The problem

You record a reading every day in column B, sometimes skipping a day. A dashboard cell should always show the latest reading and its date without editing the formula when new rows are added.

## Worked example

Readings with gaps. D2 returns the last reading and D3 the date it was recorded.

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **Date** | **Reading** |  | **Latest** |
| 2 | 2026-03-02 | 412 |  | **421** |
| 3 | 2026-03-03 | 398 |  | **2026-03-06** |
| 4 | 2026-03-04 |  |  |  |
| 5 | 2026-03-05 | 405 |  |  |
| 6 | 2026-03-06 | 421 |  |  |
| 7 | 2026-03-07 |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**D2** — last reading

```excel
=LOOKUP(2, 1/(B2:B7<>""), B2:B7)
```

Result: **421**

**D3** — date of that reading (format the cell as a date)

```excel
=LOOKUP(2, 1/(B2:B7<>""), A2:A7)
```

Result: **2026-03-06**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `B2:B7<>""` returns TRUE for filled cells and FALSE for blanks.
2. `1/(...)` turns TRUE into 1 and FALSE into a #DIV/0! error.
3. LOOKUP looks for 2 in that array. Because 2 is larger than every value, it returns the position of the last number it can find and skips the errors, so blanks never count.
4. The third argument decides what to return from that position, B for the reading or A for the date.

## Excel-specific notes

This LOOKUP trick works in every Excel version without Ctrl+Shift+Enter and ignores gaps. In Microsoft 365 there is a more readable option: `=XLOOKUP(TRUE, B2:B100<>"", B2:B100, , 0, -1)` searches from the bottom up. Avoid whole-column references like B:B inside these array calculations in big workbooks; a generous fixed range such as B2:B5000 is faster.

**Microsoft 365 with XLOOKUP (search from the bottom)**

```excel
=XLOOKUP(TRUE, B2:B100<>"", B2:B100, , 0, -1)
```

**Microsoft 365 with TAKE and FILTER**

```excel
=TAKE(FILTER(B2:B100, B2:B100<>""), -1)
```


## Google Sheets version

In Google Sheets, use:

```excel
=CHOOSEROWS(FILTER(B2:B, B2:B<>""), -1)
```

FILTER plus CHOOSEROWS is easier to read in Google Sheets and works with open-ended ranges. TAKE is not available in Sheets.

<!--SIBLING-->


## Common errors and how to fix them

- **Returns 0 or an old value** — Cells that look empty contain a formula returning "" or a space, so they count as filled. **Fix:** Test with `TRIM(B2:B100)<>""` instead of `B2:B100<>""`, or make the source formulas return truly empty values.
- **#N/A** — The whole range is empty. **Fix:** Wrap the formula in IFNA, e.g. =IFNA(LOOKUP(2, 1/(B2:B100<>""), B2:B100), "No data").
- **Slow workbook** — Whole-column references (B:B) in array calculations evaluate a million rows. **Fix:** Use a bounded range like B2:B5000, or an Excel Table column reference.

## FAQ

### Does this work with text values?

Yes. The LOOKUP(2, 1/(...)) pattern returns the last non-empty value whether it is a number or text.

### How do I get the last value that meets a condition?

Multiply in the condition, e.g. =LOOKUP(2, 1/((B2:B100<>"")*(C2:C100="Paid")), B2:B100).

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
