---
title: How to Use TODAY and NOW in Excel
slug: today-now-excel
date: '2026-10-31'
summary: TODAY returns the current date and NOW the current date and time. Both update
  automatically, which makes them perfect for countdowns, overdue flags and ages,
  but useless as a fixed time stamp. This page shows both functions, how to freeze
  the date, and how Excel and Google Sheets decide when to upda
tags:
- Dates & times
- Excel
keyword: today-now-excel
niche: sheets-formulas
provider: structured
entry_id: today-now
platform: Excel
category: date
faq:
- q: How do I calculate someone's age from a birth date?
  a: 'Use DATEDIF with TODAY: =DATEDIF(A2, TODAY(), "y") returns full years.'
- q: Does TODAY update if the file is closed?
  a: No. It updates the next time the file is opened or recalculated, so a printed
    or exported copy keeps the old date.
- q: How do I show today's date inside a sentence?
  a: 'Format it with TEXT: ="Report date: "&TEXT(TODAY(), "mmmm d, yyyy").'
related:
- - date-excel
  - date-google-sheets
- - days-between-dates-excel
  - days-between-dates-google-sheets
- - datedif-age-excel
  - datedif-age-google-sheets
- - workday-excel
  - workday-google-sheets
sibling: today-now-google-sheets
---
TODAY returns the current date and NOW the current date and time. Both update automatically, which makes them perfect for countdowns, overdue flags and ages, but useless as a fixed time stamp. This page shows both functions, how to freeze the date, and how Excel and Google Sheets decide when to update them.

## Quick answer

Use this formula in Excel:

```excel
=TODAY()
```

TODAY and NOW take no arguments. `=TODAY()` returns today's date with no time part, and `=NOW()` returns the date plus the current time, for example 2026-10-31 14:30.

## The problem

You want a task list that shows how many days are left until each deadline and flags overdue items, without retyping today's date every morning. You also need a fixed time stamp for when a row was entered, which TODAY and NOW cannot give you.

## Worked example

A deadline list. On a live sheet F2 holds =TODAY(); here it is frozen at Saturday, October 31, 2026 so the results are reproducible. Column G shows checks that are true on any day.

| | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| 1 | **Task** | **Due date** | **Days left** | **Status** |  | **Today** | **Check** |
| 2 | Invoice | 2026-11-10 | **10** | **Open** |  | 2026-10-31 | **TRUE** |
| 3 | Report | 2026-10-25 | **-6** | **Overdue** |  |  | **TRUE** |
| 4 | Review | 2026-10-31 | **0** | **Due today** |  |  | **TRUE** |

Formulas used in the example (results shown in **bold** in the table above):

**C2 (filled to C4)** — days left, filled down

```excel
=B2-$F$2
```

Results: **10**, **-6**, **0**

**D2 (filled to D4)** — status, filled down

```excel
=IF(B2<$F$2, "Overdue", IF(B2=$F$2, "Due today", "Open"))
```

Results: **Open**, **Overdue**, **Due today**

**G2** — TODAY is a whole number of days

```excel
=TODAY()=INT(TODAY())
```

Result: **TRUE**

**G3** — the date part of NOW is TODAY

```excel
=INT(NOW())=TODAY()
```

Result: **TRUE**

**G4** — NOW minus TODAY is the time of day, always under 1

```excel
=NOW()-TODAY()<1
```

Result: **TRUE**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Type `=TODAY()` in a spare cell such as F2, so every formula refers to the same date.
2. Subtract it from each due date: `=B2-$F$2` gives 10 days left for the invoice, -6 for the overdue report and 0 for the review.
3. Turn the number into a label with IF: past dates are Overdue, today is Due today, later dates are Open.
4. Use NOW instead of TODAY when the time matters, for example to count hours until a deadline with (B2-NOW())*24.
5. For a time stamp that must never change, type it with Ctrl+; (date) or Ctrl+Shift+; (time) instead of a formula.

## Excel-specific notes

Both functions are volatile: Excel recalculates them every time the workbook is opened or anything is edited, and when you press F9. Put =TODAY() in one cell and refer to that cell, so every formula uses the same date. For a fixed value that never changes, press Ctrl+; to type today's date or Ctrl+Shift+; for the current time. NOW uses the clock and time zone of your computer. The time part of NOW is `=NOW()-TODAY()`, and `=INT(NOW())` equals TODAY.

**Days until a due date**

```excel
=B2-TODAY()
```

**Current time only**

```excel
=NOW()-TODAY()
```

**Date and time as text**

```excel
=TEXT(NOW(), "yyyy-mm-dd hh:mm")
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=TODAY()
```

Excel uses the computer clock and recalculates on every edit or F9; there is no every-minute setting and no TO_DATE.

<!--SIBLING-->


## Common errors and how to fix them

- **The time stamp changes every day** — TODAY and NOW are volatile and always show the current date and time. **Fix:** Insert a fixed value with Ctrl+; or copy the cell and paste it as values.
- **Days left shows a date like 1/10/1900** — The result cell inherited a date format from the due date. **Fix:** Format the days-left cell as Number.
- **Comparing a date with NOW() never matches** — NOW includes the time, so it is never equal to a date at midnight. **Fix:** Compare with TODAY(), or use INT(NOW()).
- **NOW is a few hours off in Google Sheets** — The spreadsheet time zone differs from your own. **Fix:** Change it in File > Settings > Time zone.

## FAQ

### How do I calculate someone's age from a birth date?

Use DATEDIF with TODAY: =DATEDIF(A2, TODAY(), "y") returns full years.

### Does TODAY update if the file is closed?

No. It updates the next time the file is opened or recalculated, so a printed or exported copy keeps the old date.

### How do I show today's date inside a sentence?

Format it with TEXT: ="Report date: "&TEXT(TODAY(), "mmmm d, yyyy").

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
