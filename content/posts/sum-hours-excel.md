---
title: How to Sum Hours Over 24 in Excel
slug: sum-hours-excel
date: '2026-10-22'
summary: When you add up time values, the total resets after 24 hours unless the cell
  uses an elapsed time format. This page shows the [h]:mm format, the duration format
  in Google Sheets, and how to convert the total to decimal hours for pay calculations.
tags:
- Dates & times
- Excel
keyword: sum-hours-excel
niche: sheets-formulas
provider: structured
entry_id: sum-hours
platform: Excel
category: date
faq:
- q: How do I calculate pay from hours?
  a: Multiply the decimal hours by the rate, e.g. =SUM(B2:B6)*24*C1.
- q: How do I show minutes only?
  a: Use the custom format [m] to display the total in minutes.
- q: How do I calculate hours for a shift that passes midnight?
  a: 'If the end time is smaller than the start time, add 1 day: =MOD(C2-B2, 1) returns
    the correct duration for both normal and overnight shifts, for example 22:00 to
    06:00 gives 8:00.'
related:
- - networkdays-excel
  - networkdays-google-sheets
- - days-between-dates-excel
  - days-between-dates-google-sheets
- - percentage-change-excel
  - percentage-change-google-sheets
sibling: sum-hours-google-sheets
---
When you add up time values, the total resets after 24 hours unless the cell uses an elapsed time format. This page shows the [h]:mm format, the duration format in Google Sheets, and how to convert the total to decimal hours for pay calculations.

## Quick answer

Use this formula in Excel:

```excel
=SUM(B2:B6)
```

The SUM is correct; the display is the problem. Format the total cell with the custom format [h]:mm so hours above 24 are shown.

## The problem

Your timesheet adds up a week of daily hours, but the total shows 18:00 instead of 42:00.

## Worked example

A week of daily hours. B7 uses the [h]:mm format; C7 converts to decimal hours.

| | A | B | C |
|---|---|---|---|
| 1 | **Day** | **Hours** | **Decimal hours** |
| 2 | Mon | 8:30 |  |
| 3 | Tue | 9:15 |  |
| 4 | Wed | 7:45 |  |
| 5 | Thu | 10:00 |  |
| 6 | Fri | 6:30 |  |
| 7 | Total | **42:00** | **42** |

Formulas used in the example (results shown in **bold** in the table above):

**B7** — formatted as [h]:mm (shows 18:00 with plain h:mm)

```excel
=SUM(B2:B6)
```

Result: **42:00**

**C7** — decimal hours for pay calculations

```excel
=SUM(B2:B6)*24
```

Result: **42**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Each time is a fraction of a day; 8:30 is 0.354166...
2. SUM adds the fractions: 1.75 days, which is 42 hours.
3. The [h] in the format tells the spreadsheet to show total elapsed hours instead of the hour of the day.
4. Multiplying by 24 converts days to hours, giving 42 for pay and overtime calculations.

## Excel-specific notes

Excel stores time as a fraction of a day (12:00 is 0.5), so 42 hours is 1.75. The regular h:mm format shows only the part after the full days, which is why 42 hours appears as 18:00. Select the cell, press Ctrl+1, choose Custom and enter [h]:mm. To pay by the hour, convert the total to a decimal number with *24 and format that cell as a number, not a time.

**Display total as text in [h]:mm form**

```excel
=TEXT(SUM(B2:B6), "[h]:mm")
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=SUM(B2:B6)
```

In Google Sheets use the same SUM and apply Format > Number > Duration to the total.

<!--SIBLING-->


## Common errors and how to fix them

- **Total shows 18:00** — The total cell uses h:mm, which wraps every 24 hours. **Fix:** Use [h]:mm (Excel) or Duration (Google Sheets).
- **Decimal result shows as a time** — The *24 cell inherited a time format. **Fix:** Format it as Number.
- **Total is 0** — The hours were typed as text (e.g. "8.30" or "8h30"). **Fix:** Re-enter them as h:mm, or convert with TIMEVALUE.

## FAQ

### How do I calculate pay from hours?

Multiply the decimal hours by the rate, e.g. =SUM(B2:B6)*24*C1.

### How do I show minutes only?

Use the custom format [m] to display the total in minutes.

### How do I calculate hours for a shift that passes midnight?

If the end time is smaller than the start time, add 1 day: =MOD(C2-B2, 1) returns the correct duration for both normal and overnight shifts, for example 22:00 to 06:00 gives 8:00.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
