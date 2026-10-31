---
title: How to Add Business Days with WORKDAY in Excel
slug: workday-excel
date: '2026-10-31'
summary: WORKDAY returns the date that is a given number of working days after (or
  before) a start date, skipping weekends and an optional list of holidays. It is
  the standard way to compute due dates, delivery dates and SLA deadlines. WORKDAY.INTL
  does the same for other weekends.
tags:
- Dates & times
- Excel
keyword: workday-excel
niche: sheets-formulas
provider: structured
entry_id: workday
platform: Excel
category: date
faq:
- q: What is the difference between WORKDAY and NETWORKDAYS?
  a: WORKDAY returns a date a number of working days away; NETWORKDAYS counts the
    working days between two dates.
- q: How do I add working hours instead of days?
  a: Divide the hours by the hours in a working day and pass the whole days to WORKDAY,
    then add the remaining hours to the start time.
- q: How do I get the last working day of a month?
  a: =WORKDAY(EOMONTH(A2, 0)+1, -1) goes to the first day of the next month and steps
    back one working day.
related:
- - networkdays-excel
  - networkdays-google-sheets
- - eomonth-excel
  - eomonth-google-sheets
- - days-between-dates-excel
  - days-between-dates-google-sheets
- - today-now-excel
  - today-now-google-sheets
sibling: workday-google-sheets
---
WORKDAY returns the date that is a given number of working days after (or before) a start date, skipping weekends and an optional list of holidays. It is the standard way to compute due dates, delivery dates and SLA deadlines. WORKDAY.INTL does the same for other weekends.

## Quick answer

Use this formula in Excel:

```excel
=WORKDAY(A2, B2, $F$2:$F$4)
```

Syntax: `WORKDAY(start_date, days, [holidays])`. It moves forward from A2 by B2 working days (Monday to Friday), skipping any dates listed in F2:F4. The start date itself is not counted. A negative number of days moves backward.

## The problem

Orders ship 5 business days after they are placed, and contracts are due 10 working days after signing. Adding 5 to the date counts weekends and public holidays, so the due date comes out too early.

## Worked example

Start dates and working days to add, with three public holidays in F2:F4 (November 26 and December 25, 2026, and January 1, 2027).

| | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 1 | **Start** | **Days** | **Due (weekends only)** | **Due (with holidays)** |  | **Holidays** |
| 2 | 2026-11-02 | 10 | **2026-11-16** | **2026-11-16** |  | 2026-11-26 |
| 3 | 2026-11-20 | 5 | **2026-11-27** | **2026-11-30** |  | 2026-12-25 |
| 4 | 2026-12-18 | 7 | **2026-12-29** | **2026-12-30** | **2026-12-28** | 2027-01-01 |
| 5 | 2026-12-31 | -3 | **2026-12-28** | **2026-12-28** |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**C2 (filled to C5)** — weekends skipped, filled down

```excel
=WORKDAY(A2, B2)
```

Results: **2026-11-16**, **2026-11-27**, **2026-12-29**, **2026-12-28**

**D2 (filled to D5)** — weekends and holidays skipped, filled down

```excel
=WORKDAY(A2, B2, $F$2:$F$4)
```

Results: **2026-11-16**, **2026-11-30**, **2026-12-30**, **2026-12-28**

**E4** — Friday-Saturday weekend

```excel
=WORKDAY.INTL(A4, B4, 7, $F$2:$F$4)
```

Result: **2026-12-28**

<!--AD_IN_ARTICLE-->

## How the formula works

1. List the start dates in column A and the number of working days in column B.
2. Put the public holidays in their own range, here F2:F4, as real dates.
3. Type `=WORKDAY(A2, B2, $F$2:$F$4)` and fill it down.
4. Monday, November 2 plus 10 working days is Monday, November 16. Friday, November 20 plus 5 is Friday, November 27, but Thanksgiving on November 26 pushes it to Monday, November 30.
5. A negative number counts backwards, so 3 working days before Thursday, December 31 is Monday, December 28.

## Excel-specific notes

Format the result as a date, because WORKDAY returns a serial number. Keep holidays in their own range and lock it with $ so the formula can be filled down. For another weekend use WORKDAY.INTL: weekend code 7 means Friday and Saturday, 11 means Sunday only, and a 7-character string such as "0000011" marks days off with 1, starting on Monday. To count the working days between two dates instead, use NETWORKDAYS. If the start date falls on a weekend, WORKDAY still counts from it, so a Saturday plus 1 working day is Monday.

**Friday-Saturday weekend**

```excel
=WORKDAY.INTL(A2, B2, 7, $F$2:$F$4)
```

**Three working days before a date**

```excel
=WORKDAY(A2, -3, $F$2:$F$4)
```

**Next working day if the date is on a weekend**

```excel
=WORKDAY(A2-1, 1, $F$2:$F$4)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=WORKDAY(A2, B2, $F$2:$F$4)
```

Excel uses the same functions; point the holidays argument at a fixed range or a table column instead of an open-ended range.

<!--SIBLING-->


## Common errors and how to fix them

- **The due date ignores a holiday** — The holiday is typed as text, or the holiday range moved when the formula was filled down. **Fix:** Enter holidays as real dates and lock the range with $.
- **Result shows a number like 46342** — The cell is formatted as a number. **Fix:** Format it as a date.
- **#NUM!** — The weekend code in WORKDAY.INTL is invalid, for example "1111111" with no working days. **Fix:** Use a valid code from 1 to 7 or 11 to 17, or a string with at least one 0.
- **Due date one day later than expected** — You expected the start date to count as day 1. **Fix:** WORKDAY never counts the start date; use B2-1 days if your rule counts it.

## FAQ

### What is the difference between WORKDAY and NETWORKDAYS?

WORKDAY returns a date a number of working days away; NETWORKDAYS counts the working days between two dates.

### How do I add working hours instead of days?

Divide the hours by the hours in a working day and pass the whole days to WORKDAY, then add the remaining hours to the start time.

### How do I get the last working day of a month?

=WORKDAY(EOMONTH(A2, 0)+1, -1) goes to the first day of the next month and steps back one working day.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
