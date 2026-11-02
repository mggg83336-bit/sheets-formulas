---
title: How to Calculate the Difference Between Two Times in Google Sheets
slug: time-difference-google-sheets
date: '2026-11-02'
summary: Subtracting two time values returns the elapsed duration as a fraction of
  a day. Multiply by 24 for decimal hours, and add 1 when the shift crosses midnight
  so overnight end times stay positive. This page shows same-day and overnight examples
  with verified hour totals.
tags:
- Dates & times
- Google Sheets
keyword: time-difference-google-sheets
niche: sheets-formulas
provider: structured
entry_id: time-difference
platform: Google Sheets
category: date
faq:
- q: Why multiply by 24?
  a: Spreadsheet times are fractions of a 24-hour day, so multiplying the duration
    by 24 converts that fraction into decimal hours.
- q: How do I get minutes instead of hours?
  a: Multiply the day-fraction by 1440 (24×60) instead of 24.
- q: What if the timesheet also has dates?
  a: Store full date-times in start and end, then use =(B2-A2)*24. The midnight adjustment
    is unnecessary when the date part already moves to the next day.
related:
- - sum-hours-google-sheets
  - sum-hours-excel
- - weekday-google-sheets
  - weekday-excel
- - today-now-google-sheets
  - today-now-excel
- - text-to-date-google-sheets
  - text-to-date-excel
sibling: time-difference-excel
---
Subtracting two time values returns the elapsed duration as a fraction of a day. Multiply by 24 for decimal hours, and add 1 when the shift crosses midnight so overnight end times stay positive. This page shows same-day and overnight examples with verified hour totals.

## Quick answer

Use this formula in Google Sheets:

```excel
=IF(B2<A2, B2+1-A2, B2-A2)*24
```

Same overnight-safe pattern in Google Sheets: adjust across midnight when needed, then multiply by 24 for decimal hours.

## The problem

A timesheet stores clock-in and clock-out times. A simple end-minus-start formula works for day shifts but turns negative or wraps oddly when someone works past midnight, and payroll needs decimal hours rather than a clock format.

## Worked example

Four shifts: a normal day, an overnight shift, a short morning block, and a zero-length edge case. Decimal hours use the overnight-safe formula.

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **Start** | **End** | **Plain hours** | **Overnight-safe hours** |
| 2 | 09:00 | 17:30 | **8.5** | **8.5** |
| 3 | 22:00 | 06:30 | **-15.5** | **8.5** |
| 4 | 08:15 | 12:45 | **4.5** | **4.5** |
| 5 | 09:00 | 09:00 | **0** | **0** |

Formulas used in the example (results shown in **bold** in the table above):

**C2 (filled to C5)** — plain (end-start)*24 filled down

```excel
=(B2-A2)*24
```

Results: **8.5**, **-15.5**, **4.5**, **0**

**D2 (filled to D5)** — overnight-safe hours filled down

```excel
=IF(B2<A2, B2+1-A2, B2-A2)*24
```

Results: **8.5**, **8.5**, **4.5**, **0**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Enter start times in column A and end times in column B as real Time values.
2. Type `=(B2-A2)*24` for same-day shifts and format the result as a Number.
3. Switch to `=IF(B2<A2, B2+1-A2, B2-A2)*24` so overnight rows stay positive.
4. Fill down the timesheet; empty start cells can be guarded with IF(A2="", "", ...).
5. Sum the decimal-hours column for payroll, or keep a Duration-formatted column for display.

## Google Sheets-specific notes

Format start and end columns as Time (Format > Number > Time). For the raw difference, Format > Number > Duration shows hours and minutes clearly, including values past 24 hours when you sum several days. Whole-column version: `=ARRAYFORMULA(IF(A2:A="", "", IF(B2:B<A2:A, B2:B+1-A2:A, B2:B-A2:A)*24))`. If people type times as text, coerce with TIMEVALUE first. When both date and time live in the same cell, subtract the full date-times and multiply by 24; the midnight IF is only required for time-only columns. Pair with SUM on the decimal-hours column for payroll totals.

**Whole column of decimal hours**

```excel
=ARRAYFORMULA(IF(A2:A="", "", IF(B2:B<A2:A, B2:B+1-A2:A, B2:B-A2:A)*24))
```

**Duration display (day fraction)**

```excel
=IF(B2<A2, B2+1-A2, B2-A2)
```

**Same-day decimal hours**

```excel
=(B2-A2)*24
```


## Excel version

The same formula works unchanged in Excel:

```excel
=IF(B2<A2, B2+1-A2, B2-A2)*24
```

Google Sheets uses the same day-fraction arithmetic. Format > Number > Duration is a handy display option for the raw difference, and ARRAYFORMULA can fill a whole timesheet column.

<!--SIBLING-->


## Common errors and how to fix them

- **Overnight shift shows negative hours** — The formula used plain end-start without adding a day when end < start. **Fix:** Use IF(B2<A2, B2+1-A2, B2-A2) before multiplying by 24.
- **Result looks like 0.354 or a clock time** — The cell still uses a Time format after you wanted decimal hours, or you forgot *24. **Fix:** Multiply by 24 and format as a Number (or keep Time/Duration only for the day-fraction column).
- **#VALUE!** — Start or end is text that only looks like a time. **Fix:** Recode with TIMEVALUE or enter the values as real times.
- **Total over several days wraps to a small clock value** — The total cell uses h:mm instead of elapsed-hour formatting. **Fix:** Use [h]:mm in Excel or Format > Number > Duration in Sheets on the total (see sum-hours).

## FAQ

### Why multiply by 24?

Spreadsheet times are fractions of a 24-hour day, so multiplying the duration by 24 converts that fraction into decimal hours.

### How do I get minutes instead of hours?

Multiply the day-fraction by 1440 (24×60) instead of 24.

### What if the timesheet also has dates?

Store full date-times in start and end, then use =(B2-A2)*24. The midnight adjustment is unnecessary when the date part already moves to the next day.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
