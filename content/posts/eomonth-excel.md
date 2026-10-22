---
title: How to Use EOMONTH (End of Month) in Excel
slug: eomonth-excel
date: '2026-10-22'
summary: EOMONTH returns the last day of a month a given number of months before or
  after a date. It is the easiest way to get month-end dates, end-of-next-month due
  dates and the first day of a month.
tags:
- Dates & times
- Excel
keyword: eomonth-excel
niche: sheets-formulas
provider: structured
entry_id: eomonth
platform: Excel
category: date
faq:
- q: How do I get the number of days in a month?
  a: Use =DAY(EOMONTH(A2, 0)).
- q: What is the difference between EOMONTH and EDATE?
  a: EOMONTH always returns a month-end date; EDATE keeps the same day number (or
    the last day if that day does not exist).
- q: How do I get the last working day of the month?
  a: 'Combine EOMONTH with WORKDAY: =WORKDAY(EOMONTH(A2, 0)+1, -1) starts from the
    first day of the next month and steps back one working day, skipping weekends.
    Add a holiday range as the third argument if needed.'
related:
- - sum-by-month-excel
  - sum-by-month-google-sheets
- - days-between-dates-excel
  - days-between-dates-google-sheets
- - networkdays-excel
  - networkdays-google-sheets
- - sumifs-between-dates-excel
  - sumifs-between-dates-google-sheets
sibling: eomonth-google-sheets
---
EOMONTH returns the last day of a month a given number of months before or after a date. It is the easiest way to get month-end dates, end-of-next-month due dates and the first day of a month.

## Quick answer

Use this formula in Excel:

```excel
=EOMONTH(A2, 0)
```

Syntax: `EOMONTH(start_date, months)`. 0 returns the last day of the same month, 1 the last day of the next month, -1 the last day of the previous month.

## The problem

Invoices are due at the end of the month after they are issued, and a report needs the first and last day of each invoice's month.

## Worked example

Month boundaries and due dates for three invoices.

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **Invoice date** | **End of month** | **Due (end of next month)** | **First of month** |
| 2 | 2026-01-15 | **2026-01-31** | **2026-02-28** | **2026-01-01** |
| 3 | 2026-02-10 | **2026-02-28** | **2026-03-31** | **2026-02-01** |
| 4 | 2026-11-30 | **2026-11-30** | **2026-12-31** | **2026-11-01** |

Formulas used in the example (results shown in **bold** in the table above):

**B2 (filled to B4)**

```excel
=EOMONTH(A2, 0)
```

Results: **2026-01-31**, **2026-02-28**, **2026-11-30**

**C2 (filled to C4)**

```excel
=EOMONTH(A2, 1)
```

Results: **2026-02-28**, **2026-03-31**, **2026-12-31**

**D2 (filled to D4)**

```excel
=EOMONTH(A2, -1)+1
```

Results: **2026-01-01**, **2026-02-01**, **2026-11-01**

<!--AD_IN_ARTICLE-->

## How the formula works

1. EOMONTH moves the given number of months from the start date and returns the last day of that month.
2. With 0 it stays in the same month: January 15 becomes January 31.
3. With 1 it moves to the next month and handles month lengths automatically, including February.
4. Going back one month and adding one day gives the first day of the original month.

## Excel-specific notes

EOMONTH returns a serial number, so format the cell as a date (Ctrl+1 > Date). The first day of a month is the end of the previous month plus one: `=EOMONTH(A2, -1)+1`. To add calendar months while keeping the day, use EDATE instead; EDATE(Jan 31, 1) returns Feb 28 because February has no 31st. Both functions ignore any time part of the start date.

**Same day next month**

```excel
=EDATE(A2, 1)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=EOMONTH(A2, 0)
```

Google Sheets uses the same EOMONTH and EDATE functions.

<!--SIBLING-->


## Common errors and how to fix them

- **Result shows a number like 46053** — The cell is not formatted as a date. **Fix:** Format it as a date.
- **#VALUE!** — The start date is text. **Fix:** Convert it to a real date.
- **Decimal months ignored** — EOMONTH truncates the months argument, so 1.9 is treated as 1. **Fix:** Pass whole numbers.

## FAQ

### How do I get the number of days in a month?

Use =DAY(EOMONTH(A2, 0)).

### What is the difference between EOMONTH and EDATE?

EOMONTH always returns a month-end date; EDATE keeps the same day number (or the last day if that day does not exist).

### How do I get the last working day of the month?

Combine EOMONTH with WORKDAY: =WORKDAY(EOMONTH(A2, 0)+1, -1) starts from the first day of the next month and steps back one working day, skipping weekends. Add a holiday range as the third argument if needed.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
