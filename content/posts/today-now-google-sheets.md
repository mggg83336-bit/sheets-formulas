---
title: How to Use TODAY and NOW in Google Sheets
slug: today-now-google-sheets
date: '2026-10-31'
summary: TODAY returns the current date and NOW the current date and time. Both update
  automatically, which makes them perfect for countdowns, overdue flags and ages,
  but useless as a fixed time stamp. This page shows both functions, how to freeze
  the date, and how Excel and Google Sheets decide when to upda
tags:
- Dates & times
- Google Sheets
keyword: today-now-google-sheets
niche: sheets-formulas
provider: structured
entry_id: today-now
platform: Google Sheets
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
- - date-google-sheets
  - date-excel
- - days-between-dates-google-sheets
  - days-between-dates-excel
- - datedif-age-google-sheets
  - datedif-age-excel
- - workday-google-sheets
  - workday-excel
sibling: today-now-excel
---
TODAY returns the current date and NOW the current date and time. Both update automatically, which makes them perfect for countdowns, overdue flags and ages, but useless as a fixed time stamp. This page shows both functions, how to freeze the date, and how Excel and Google Sheets decide when to update them.

## Quick answer

Use this formula in Google Sheets:

```excel
=TODAY()
```

TODAY and NOW work the same way in Google Sheets: TODAY gives the date and NOW the date and time, and both update on their own.

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

## Google Sheets-specific notes

Google Sheets takes the time from the spreadsheet time zone in File > Settings, not from your computer, so check it if NOW looks hours off. In the same Settings dialog, the Calculation tab lets you recalculate on change, every minute or every hour, which keeps a NOW clock moving even when nobody edits the sheet. Ctrl+; and Ctrl+Shift+; insert a fixed date and time, just like in Excel. To compute days left for a whole column at once, use ARRAYFORMULA, and TO_DATE turns the result of INT(NOW()) back into a date format.

**Days left for the whole column**

```excel
=ARRAYFORMULA(IF(B2:B="", "", B2:B-TODAY()))
```

**Date part of NOW as a date**

```excel
=TO_DATE(INT(NOW()))
```

**Date and time as text**

```excel
=TEXT(NOW(), "yyyy-mm-dd hh:mm")
```


## Excel version

The same formula works unchanged in Excel:

```excel
=TODAY()
```

Google Sheets has the same TODAY and NOW, but uses the spreadsheet time zone and lets you choose how often they recalculate.

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
