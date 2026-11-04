---
title: How to Convert Minutes to Hours (and Back) in Google Sheets
slug: minutes-to-hours-google-sheets
date: '2026-11-04'
summary: Divide minutes by 60 for decimal hours, multiply decimal hours by 60 to get
  minutes back, or build a clock-style hours:minutes value with TIME or INT/MOD. This
  page covers payroll-friendly decimal hours, overnight totals in minutes, and whole-column
  ARRAYFORMULA patterns in Sheets.
tags:
- Dates & times
- Google Sheets
keyword: minutes-to-hours-google-sheets
niche: sheets-formulas
provider: structured
entry_id: minutes-to-hours
platform: Google Sheets
category: date
faq:
- q: How do I convert minutes to hours and minutes as two columns?
  a: Use =INT(A2/60) for whole hours and =MOD(A2,60) for the leftover minutes.
- q: How do I convert a time of day like 1:30 into decimal hours?
  a: Multiply the time by 24, for example =(C2)*24 when C2 is a real time value. That
    is different from dividing a minute count by 60.
- q: How do overnight shift minutes fit in?
  a: First get a positive day-fraction with the overnight-safe pattern on the time-difference
    page, then multiply by 1440 for minutes or by 24 for decimal hours.
related:
- - time-difference-google-sheets
  - time-difference-excel
- - sum-hours-google-sheets
  - sum-hours-excel
- - text-to-date-google-sheets
  - text-to-date-excel
- - weekday-google-sheets
  - weekday-excel
sibling: minutes-to-hours-excel
---
Divide minutes by 60 for decimal hours, multiply decimal hours by 60 to get minutes back, or build a clock-style hours:minutes value with TIME or INT/MOD. This page covers payroll-friendly decimal hours, overnight totals in minutes, and whole-column ARRAYFORMULA patterns in Sheets.

## Quick answer

Use this formula in Google Sheets:

```excel
=A2/60
```

Same conversion in Google Sheets: minutes divided by 60 become decimal hours for pay and charts.

## The problem

A timesheet or GPS export lists duration in minutes (90, 135, 480). Payroll and invoices need decimal hours (1.5, 2.25, 8), while some dashboards still want a 1:30 clock display. Hand dividing drifts, and mixing text "1:30" with real numbers breaks SUM.

## Worked example

Four minute totals from a timesheet, plus a decimal-hours column converted back to minutes. Clock display uses TIME for values under 24 hours.

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **Minutes** | **Decimal hours** | **Clock (h:mm)** | **Back to minutes** |
| 2 | 90 | **1.5** | **1:30** | **90** |
| 3 | 45 | **0.75** | **0:45** | **45** |
| 4 | 135 | **2.25** | **2:15** | **135** |
| 5 | 480 | **8** | **8:00** | **480** |

Formulas used in the example (results shown in **bold** in the table above):

**B2 (filled to B5)** — minutes / 60 filled down

```excel
=A2/60
```

Results: **1.5**, **0.75**, **2.25**, **8**

**C2 (filled to C5)** — TIME clock from minutes

```excel
=TIME(0, A2, 0)
```

Results: **1:30**, **0:45**, **2:15**, **8:00**

**D2 (filled to D5)** — decimal hours * 60 back to minutes

```excel
=B2*60
```

Results: **90**, **45**, **135**, **480**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Enter minute counts as numbers in column A (90 for an hour and a half, not text "90 min").
2. Type `=A2/60` for decimal hours and format the cell as a Number.
3. Add `=TIME(0, A2, 0)` when you need an h:mm clock display for values under 24 hours.
4. Convert decimal hours back with `=B2*60`, or combine Hours+Minutes columns with `=A2+B2/60`.
5. Sum the decimal-hours column for payroll; keep minute totals only when a system requires them.

## Google Sheets-specific notes

Format the decimal-hours column as a Number (Format > Number > Number). For a whole column use `=ARRAYFORMULA(IF(A2:A="", "", A2:A/60))`. Clock-style display from minutes works with `=ARRAYFORMULA(IF(A2:A="", "", TIME(0, A2:A, 0)))` plus Format > Number > Time, or use Duration when the value is already a day-fraction. Durations past 24 hours should stay as decimal hours or use Duration on a day-fraction total — TIME alone wraps at 24:00. Convert decimal hours back with `=ARRAYFORMULA(IF(B2:B="", "", B2:B*60))`. If people paste minutes as text, coerce with VALUE or N before dividing. Pair the decimal-hours column with SUM for payroll, matching the sum-hours pattern.

**Whole column of decimal hours**

```excel
=ARRAYFORMULA(IF(A2:A="", "", A2:A/60))
```

**Whole column back to minutes**

```excel
=ARRAYFORMULA(IF(B2:B="", "", B2:B*60))
```

**Minutes as clock time**

```excel
=TIME(0, A2, 0)
```

**Hours + minutes columns to decimal hours**

```excel
=A2+B2/60
```


## Excel version

The same formula works unchanged in Excel:

```excel
=A2/60
```

Google Sheets uses the same /60 and *60 arithmetic. Prefer ARRAYFORMULA for whole columns and Format > Number > Duration when you want a clock-style duration display.

<!--SIBLING-->


## Common errors and how to fix them

- **Result shows as a time like 1:30 instead of 1.5** — The decimal-hours cell inherited a Time format, or you used TIME when you wanted /60. **Fix:** Use =A2/60 and format as Number for pay calculations.
- **Clock shows 0:00 or wraps oddly above 24 hours** — TIME only represents a time of day and resets after 1440 minutes. **Fix:** Keep totals as decimal hours, or format a day-fraction with [h]:mm / Duration instead of TIME.
- **#VALUE!** — The minutes cell is text such as "90 min" or "1:30". **Fix:** Store a pure number of minutes, or parse text before dividing.
- **Back-conversion does not match the original minutes** — The decimal-hours cell was rounded for display and that rounded value was multiplied by 60. **Fix:** Multiply the full-precision formula result (or the source minutes column), not a hand-typed rounded hour.

## FAQ

### How do I convert minutes to hours and minutes as two columns?

Use =INT(A2/60) for whole hours and =MOD(A2,60) for the leftover minutes.

### How do I convert a time of day like 1:30 into decimal hours?

Multiply the time by 24, for example =(C2)*24 when C2 is a real time value. That is different from dividing a minute count by 60.

### How do overnight shift minutes fit in?

First get a positive day-fraction with the overnight-safe pattern on the time-difference page, then multiply by 1440 for minutes or by 24 for decimal hours.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
