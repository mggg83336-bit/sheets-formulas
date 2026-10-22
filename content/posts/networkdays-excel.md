---
title: How to Count Working Days with NETWORKDAYS in Excel
slug: networkdays-excel
date: '2026-10-22'
summary: NETWORKDAYS counts the working days (Monday to Friday) between two dates,
  including both ends, and can subtract a list of holidays. NETWORKDAYS.INTL handles
  other weekends. Worked example with a real holiday list.
tags:
- Dates & times
- Excel
keyword: networkdays-excel
niche: sheets-formulas
provider: structured
entry_id: networkdays
platform: Excel
category: date
faq:
- q: Does NETWORKDAYS count the start date?
  a: Yes, both the start and the end date are included if they are working days.
- q: How do I count working hours?
  a: Multiply the working days by the hours per day, and adjust the first and last
    day if they are partial.
- q: How do I count only Mondays, or only weekend days?
  a: 'Use NETWORKDAYS.INTL with a 7-character weekend string where 1 means excluded:
    =NETWORKDAYS.INTL(B2, C2, "0111111") counts only Mondays, and "1111100" counts
    only Saturdays and Sundays.'
related:
- - days-between-dates-excel
  - days-between-dates-google-sheets
- - eomonth-excel
  - eomonth-google-sheets
- - datedif-age-excel
  - datedif-age-google-sheets
- - sum-hours-excel
  - sum-hours-google-sheets
sibling: networkdays-google-sheets
---
NETWORKDAYS counts the working days (Monday to Friday) between two dates, including both ends, and can subtract a list of holidays. NETWORKDAYS.INTL handles other weekends. Worked example with a real holiday list.

## Quick answer

Use this formula in Excel:

```excel
=NETWORKDAYS(B2, C2, $G$2:$G$4)
```

Syntax: `NETWORKDAYS(start_date, end_date, [holidays])`. Counts Monday to Friday between B2 and C2 inclusive, excluding any dates listed in G2:G4.

## The problem

For project planning you need the number of business days between start and end dates, minus public holidays.

## Worked example

Holidays are listed in G2:G4.

| | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| 1 | **Project** | **Start** | **End** | **Workdays** | **Minus holidays** |  | **Holidays** |
| 2 | Website | 2026-03-02 | 2026-03-27 | **20** | **20** |  | 2026-04-03 |
| 3 | Audit | 2026-04-01 | 2026-04-30 | **22** | **21** |  | 2026-12-25 |
| 4 | Launch | 2026-12-21 | 2027-01-08 | **15** | **13** |  | 2027-01-01 |

Formulas used in the example (results shown in **bold** in the table above):

**D2 (filled to D4)** — filled down

```excel
=NETWORKDAYS(B2, C2)
```

Results: **20**, **22**, **15**

**E2 (filled to E4)** — filled down

```excel
=NETWORKDAYS(B2, C2, $G$2:$G$4)
```

Results: **20**, **21**, **13**

<!--AD_IN_ARTICLE-->

## How the formula works

1. NETWORKDAYS counts every Monday to Friday from the start date to the end date, including both.
2. March 2 to March 27, 2026 is exactly four Monday-to-Friday weeks, so 20 days.
3. The holiday list removes dates that fall on weekdays inside the period. April 3 removes one day from the Audit; December 25 and January 1 remove two from the Launch.
4. Holidays that fall on a weekend are ignored automatically, so they are never subtracted twice.

## Excel-specific notes

Keep holidays in a separate range or table and lock the reference with $ so you can fill the formula down. For a different weekend use NETWORKDAYS.INTL: weekend code 7 means Friday and Saturday, 11 means Sunday only, or pass a 7-character string such as "0000011" where 1 marks a day off (Monday first). WORKDAY does the reverse calculation: it returns the date that is a given number of working days after a start date.

**Friday-Saturday weekend**

```excel
=NETWORKDAYS.INTL(B2, C2, 7, $G$2:$G$4)
```

**Due date 10 working days after the start**

```excel
=WORKDAY(B2, 10, $G$2:$G$4)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=NETWORKDAYS(B2, C2, $G$2:$G$4)
```

Google Sheets has the same NETWORKDAYS, NETWORKDAYS.INTL and WORKDAY functions.

<!--SIBLING-->


## Common errors and how to fix them

- **#VALUE!** — A start, end or holiday value is text instead of a date. **Fix:** Convert the cells to real dates.
- **Result one day too high or low** — NETWORKDAYS counts both the start and end day. **Fix:** Subtract 1 if the start day should not count.
- **Holidays not subtracted after filling down** — The holiday range was not locked, so it moved down with each row. **Fix:** Use $G$2:$G$4.

## FAQ

### Does NETWORKDAYS count the start date?

Yes, both the start and the end date are included if they are working days.

### How do I count working hours?

Multiply the working days by the hours per day, and adjust the first and last day if they are partial.

### How do I count only Mondays, or only weekend days?

Use NETWORKDAYS.INTL with a 7-character weekend string where 1 means excluded: =NETWORKDAYS.INTL(B2, C2, "0111111") counts only Mondays, and "1111100" counts only Saturdays and Sundays.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
