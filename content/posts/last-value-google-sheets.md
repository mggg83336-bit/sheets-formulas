---
title: How to Lookup the Last Value in a Column in Google Sheets
slug: last-value-google-sheets
date: '2026-10-27'
summary: Need the most recent entry in a log, a running balance or a meter reading?
  These formulas return the last non-empty value in a column, even when there are
  blank cells in between, plus the matching date from the next column.
tags:
- Lookup & reference
- Google Sheets
keyword: last-value-google-sheets
niche: sheets-formulas
provider: structured
entry_id: last-value
platform: Google Sheets
category: lookup
faq:
- q: Does this work with text values?
  a: Yes. The LOOKUP(2, 1/(...)) pattern returns the last non-empty value whether
    it is a number or text.
- q: How do I get the last value that meets a condition?
  a: Multiply in the condition, e.g. =LOOKUP(2, 1/((B2:B100<>"")*(C2:C100="Paid")),
    B2:B100).
related:
- - xlookup-google-sheets
  - xlookup-excel
- - index-match-google-sheets
  - index-match-excel
- - lookup-multiple-values-google-sheets
  - lookup-multiple-values-excel
- - eomonth-google-sheets
  - eomonth-excel
sibling: last-value-excel
---
Need the most recent entry in a log, a running balance or a meter reading? These formulas return the last non-empty value in a column, even when there are blank cells in between, plus the matching date from the next column.

## Quick answer

Use this formula in Google Sheets:

```excel
=CHOOSEROWS(FILTER(B2:B, B2:B<>""), -1)
```

FILTER keeps the non-empty cells and CHOOSEROWS with -1 returns the last of them.

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
=CHOOSEROWS(FILTER(B2:B7, B2:B7<>""), -1)
```

Result: **421**

**D3** — date of that reading (format the cell as a date)

```excel
=CHOOSEROWS(FILTER(A2:A7, B2:B7<>""), -1)
```

Result: **2026-03-06**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `B2:B7<>""` returns TRUE for filled cells and FALSE for blanks.
2. `1/(...)` turns TRUE into 1 and FALSE into a #DIV/0! error.
3. LOOKUP looks for 2 in that array. Because 2 is larger than every value, it returns the position of the last number it can find and skips the errors, so blanks never count.
4. The third argument decides what to return from that position, B for the reading or A for the date.

## Google Sheets-specific notes

In Google Sheets, open-ended ranges such as B2:B are normal and grow automatically as you add rows. FILTER plus CHOOSEROWS is the clearest way to get the last entry. If you prefer a formula that works in very old sheets too, use INDEX with COUNTA, which works as long as there are no blank cells in the column. Note that TAKE, which Excel users often reach for, does not exist in Google Sheets.

**INDEX + COUNTA (column without gaps)**

```excel
=INDEX(B2:B, COUNTA(B2:B))
```

**Matching date of the last reading**

```excel
=CHOOSEROWS(FILTER(A2:A, B2:B<>""), -1)
```


## Excel version

In Excel, use:

```excel
=LOOKUP(2, 1/(B2:B100<>""), B2:B100)
```

The classic LOOKUP(2, 1/...) trick works in every Excel version. CHOOSEROWS also exists in Excel 365.

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
