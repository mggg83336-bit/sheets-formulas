---
title: How to Get the Week Number of a Date (WEEKNUM) in Google Sheets
slug: weeknum-google-sheets
date: '2026-11-02'
summary: WEEKNUM returns which week of the year a date falls in. The second argument
  chooses Sunday-first, Monday-first, or ISO week numbering, so the same date can
  show week 1 or week 53 depending on the system you pick. Use it for week-based reports,
  ISO calendars and week-over-week dashboards.
tags:
- Dates & times
- Google Sheets
keyword: weeknum-google-sheets
niche: sheets-formulas
provider: structured
entry_id: weeknum
platform: Google Sheets
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
- - weekday-google-sheets
  - weekday-excel
- - workday-google-sheets
  - workday-excel
- - networkdays-google-sheets
  - networkdays-excel
- - today-now-google-sheets
  - today-now-excel
sibling: weeknum-excel
---
WEEKNUM returns which week of the year a date falls in. The second argument chooses Sunday-first, Monday-first, or ISO week numbering, so the same date can show week 1 or week 53 depending on the system you pick. Use it for week-based reports, ISO calendars and week-over-week dashboards.

## Quick answer

Use this formula in Google Sheets:

```excel
=WEEKNUM(A2, 2)
```

WEEKNUM in Google Sheets uses the same return_type codes: 2 for Monday-start system weeks, 1 for Sunday-start, and 21 for ISO week numbers.

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

## Google Sheets-specific notes

For a whole column use `=ARRAYFORMULA(IF(A2:A="", "", WEEKNUM(A2:A, 2)))`. Sheets also has ISOWEEKNUM for the ISO-8601 week, which matches WEEKNUM with return_type 21. File > Settings locale does not change WEEKNUM's numbering rules, but it does affect how dates are parsed when you type them as text. Keep source values as real dates (Format > Number > Date) so week numbers stay stable after locale changes. When building a week label for charts, combine YEAR with TEXT around WEEKNUM so week 5 of 2026 does not collide with week 5 of 2027.

**Whole column of week numbers**

```excel
=ARRAYFORMULA(IF(A2:A="", "", WEEKNUM(A2:A, 2)))
```

**ISO week with ISOWEEKNUM**

```excel
=ISOWEEKNUM(A2)
```

**Sunday-first week number**

```excel
=WEEKNUM(A2, 1)
```

**Year-week key**

```excel
=ARRAYFORMULA(IF(A2:A="", "", YEAR(A2:A)&"-W"&TEXT(WEEKNUM(A2:A, 21), "00")))
```


## Excel version

The same formula works unchanged in Excel:

```excel
=WEEKNUM(A2, 2)
```

Google Sheets supports the same WEEKNUM return types. ISOWEEKNUM is also available there; use ARRAYFORMULA when filling a whole column.

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
