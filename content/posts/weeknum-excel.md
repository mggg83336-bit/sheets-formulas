---
title: How to Get the Week Number of a Date (WEEKNUM) in Excel
slug: weeknum-excel
date: '2026-11-02'
summary: WEEKNUM returns which week of the year a date falls in. The second argument
  chooses Sunday-first, Monday-first, or ISO week numbering, so the same date can
  show week 1 or week 53 depending on the system you pick. Use it for week-based reports,
  ISO calendars and week-over-week dashboards.
tags:
- Dates & times
- Excel
keyword: weeknum-excel
niche: sheets-formulas
provider: structured
entry_id: weeknum
platform: Excel
category: date
faq:
- q: What is the difference between WEEKNUM and ISOWEEKNUM?
  a: ISOWEEKNUM always uses the ISO-8601 rule (Monday start, week 1 has at least four
    days in the new year). WEEKNUM needs return_type 21 to match that; types 1 and
    2 use simpler "week containing January 1" rules.
- q: Which return_type should I use?
  a: Use 2 for typical Monday-first business sheets. Use 21 (or ISOWEEKNUM) when partners
    expect ISO week numbers. Use 1 only when you specifically need Sunday-first weeks.
- q: How do I get the week start date from a week number?
  a: Store real dates and group with WEEKNUM, or compute the Monday of the week with
    a formula based on the date (for example date - WEEKDAY(date, 2) + 1). Avoid reconstructing
    dates from a week number alone when the year boundary is ambiguous.
related:
- - weekday-excel
  - weekday-google-sheets
- - workday-excel
  - workday-google-sheets
- - networkdays-excel
  - networkdays-google-sheets
- - today-now-excel
  - today-now-google-sheets
sibling: weeknum-google-sheets
---
WEEKNUM returns which week of the year a date falls in. The second argument chooses Sunday-first, Monday-first, or ISO week numbering, so the same date can show week 1 or week 53 depending on the system you pick. Use it for week-based reports, ISO calendars and week-over-week dashboards.

## Quick answer

Use this formula in Excel:

```excel
=WEEKNUM(A2, 2)
```

Syntax: `WEEKNUM(serial_number, [return_type])`. With return_type 2 the week starts on Monday and the week that contains January 1 is week 1. Return_type 1 (the default) starts the week on Sunday. Return_type 21 follows the ISO-8601 rule (Monday start, week 1 is the first week with at least four days in the new year), which matches ISOWEEKNUM.

## The problem

A sales workbook needs a Week column so PivotTables and charts can group by week. Typing the week by hand drifts when the year rolls, and teams disagree on whether weeks start on Sunday or Monday and whether late December belongs to week 53 or week 1.

## Worked example

Five dates spanning early January, a mid-year Monday, and late December. Columns compare return_type 1 (Sunday start), return_type 2 (Monday start) and return_type 21 (ISO).

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **Date** | **WEEKNUM type 1** | **WEEKNUM type 2** | **WEEKNUM type 21 (ISO)** |
| 2 | 2026-01-01 | **1** | **1** | **1** |
| 3 | 2026-01-04 | **2** | **1** | **1** |
| 4 | 2026-01-05 | **2** | **2** | **2** |
| 5 | 2026-11-02 | **45** | **45** | **45** |
| 6 | 2026-12-28 | **1** | **1** | **53** |

Formulas used in the example (results shown in **bold** in the table above):

**B2 (filled to B6)** — Sunday-first week numbers

```excel
=WEEKNUM(A2, 1)
```

Results: **1**, **2**, **2**, **45**, **1**

**C2 (filled to C6)** — Monday-first system week numbers

```excel
=WEEKNUM(A2, 2)
```

Results: **1**, **1**, **2**, **45**, **1**

**D2 (filled to D6)** — ISO week numbers

```excel
=WEEKNUM(A2, 21)
```

Results: **1**, **1**, **2**, **45**, **53**

<!--AD_IN_ARTICLE-->

## How the formula works

1. List the dates in column A as real dates, not text.
2. Type `=WEEKNUM(A2, 2)` for Monday-start system weeks and fill down.
3. Add `=WEEKNUM(A2, 1)` when you need the Sunday-first numbering for comparison.
4. Use `=WEEKNUM(A2, 21)` (or ISOWEEKNUM) when the report must follow ISO-8601 weeks.
5. Build a year-week key with YEAR and TEXT if the same week number appears in more than one year.

## Excel-specific notes

Pick one return_type for the whole workbook and stick to it; mixing 1 and 21 is the usual source of off-by-one week charts. Return_type 2 is a good default for Monday-to-Friday business sheets that are not strict ISO. When auditors or European partners expect ISO weeks, use 21 (or ISOWEEKNUM in Microsoft 365). WEEKNUM ignores any time portion of a date-time value. Format the result as a number. Pair with YEAR or a helper like `=YEAR(A2)&"-W"&TEXT(WEEKNUM(A2,21),"00")` when you need a unique week key across years. Empty date cells can return 0, so guard with IF(A2="", "", WEEKNUM(A2, 2)).

**Sunday-first week number (Excel default)**

```excel
=WEEKNUM(A2, 1)
```

**ISO week number**

```excel
=WEEKNUM(A2, 21)
```

**ISOWEEKNUM (Microsoft 365)**

```excel
=ISOWEEKNUM(A2)
```

**Year-week key for pivots**

```excel
=YEAR(A2)&"-W"&TEXT(WEEKNUM(A2, 21), "00")
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=WEEKNUM(A2, 2)
```

Excel uses the same WEEKNUM return types; fill down or spill instead of ARRAYFORMULA, and use ISOWEEKNUM in Microsoft 365 as a clearer alias for return_type 21.

<!--SIBLING-->


## Common errors and how to fix them

- **Late December shows week 1 instead of 53** — Return_type 1 or 2 treats the week that contains the next January 1 as week 1 of the new numbering, while ISO (21) keeps week 53 when that week still belongs to the old ISO year. **Fix:** Switch to return_type 21 or ISOWEEKNUM when you need ISO week 53 for late December dates such as 2026-12-28.
- **Monday and Sunday give different week numbers for the same date** — Return_type 1 starts weeks on Sunday; return_type 2 starts on Monday, so Sunday dates often sit in different week buckets. **Fix:** Agree on one return_type for the file and document it next to the Week column header.
- **#VALUE!** — The cell holds text that only looks like a date. **Fix:** Convert it with DATEVALUE or DATE before WEEKNUM.
- **Week chart merges two years** — The summary keyed only on WEEKNUM without the year. **Fix:** Include YEAR in the grouping key, for example YEAR&"-W"&TEXT(WEEKNUM(...),"00").

## FAQ

### What is the difference between WEEKNUM and ISOWEEKNUM?

ISOWEEKNUM always uses the ISO-8601 rule (Monday start, week 1 has at least four days in the new year). WEEKNUM needs return_type 21 to match that; types 1 and 2 use simpler "week containing January 1" rules.

### Which return_type should I use?

Use 2 for typical Monday-first business sheets. Use 21 (or ISOWEEKNUM) when partners expect ISO week numbers. Use 1 only when you specifically need Sunday-first weeks.

### How do I get the week start date from a week number?

Store real dates and group with WEEKNUM, or compute the Monday of the week with a formula based on the date (for example date - WEEKDAY(date, 2) + 1). Avoid reconstructing dates from a week number alone when the year boundary is ambiguous.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
