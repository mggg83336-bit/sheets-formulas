---
title: How to Add Months to a Date (EDATE) in Google Sheets
slug: add-months-google-sheets
date: '2026-11-01'
summary: EDATE shifts a date by a whole number of calendar months and keeps the same
  day of the month when that day exists. It is the clean way to add or subtract months
  for renewals, billing cycles and contract end dates. When the day does not exist
  in the target month, EDATE lands on the last day of that m
tags:
- Dates & times
- Google Sheets
keyword: add-months-google-sheets
niche: sheets-formulas
provider: structured
entry_id: add-months
platform: Google Sheets
category: date
faq:
- q: What is the difference between EDATE and EOMONTH?
  a: EDATE keeps the same day of the month (or the last day if that day is missing).
    EOMONTH always returns the last day of the target month.
- q: How do I add months and then land on the next working day?
  a: 'Wrap EDATE in WORKDAY: =WORKDAY(EDATE(A2, B2)-1, 1) moves to the renewal date
    and then to the next working day if needed.'
- q: Does EDATE keep the time portion of a date-time value?
  a: No. EDATE returns a pure date serial with no time. Add the original time back
    with +MOD(A2,1) if you need it.
related:
- - eomonth-google-sheets
  - eomonth-excel
- - workday-google-sheets
  - workday-excel
- - date-google-sheets
  - date-excel
- - today-now-google-sheets
  - today-now-excel
sibling: add-months-excel
---
EDATE shifts a date by a whole number of calendar months and keeps the same day of the month when that day exists. It is the clean way to add or subtract months for renewals, billing cycles and contract end dates. When the day does not exist in the target month, EDATE lands on the last day of that month instead of spilling into the next one.

## Quick answer

Use this formula in Google Sheets:

```excel
=EDATE(A2, B2)
```

EDATE works the same way in Google Sheets: it moves A2 by B2 calendar months and clamps to the last day of the month when the original day does not exist.

## The problem

A subscription renews every 3 months from the signup date, and some invoices fall on the 31st. Adding 90 days drifts off the calendar month, and DATE(YEAR, MONTH+n, DAY) turns January 31 plus one month into March 3 instead of February 28.

## Worked example

Start dates and months to add. Row 2 shows a normal mid-month shift; row 3 shows EDATE clamping January 31 to February 28 while the DATE construction rolls into March.

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **Start** | **Months** | **EDATE result** | **DATE construction** |
| 2 | 2026-01-15 | 3 | **2026-04-15** | **2026-04-15** |
| 3 | 2026-01-31 | 1 | **2026-02-28** | **2026-03-03** |
| 4 | 2026-11-01 | 2 | **2027-01-01** | **2027-01-01** |
| 5 | 2026-03-15 | -1 | **2026-02-15** | **2026-02-15** |

Formulas used in the example (results shown in **bold** in the table above):

**C2 (filled to C5)** — EDATE filled down

```excel
=EDATE(A2, B2)
```

Results: **2026-04-15**, **2026-02-28**, **2027-01-01**, **2026-02-15**

**D2 (filled to D5)** — DATE construction (rollover on missing days)

```excel
=DATE(YEAR(A2), MONTH(A2)+B2, DAY(A2))
```

Results: **2026-04-15**, **2026-03-03**, **2027-01-01**, **2026-02-15**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Put the start dates in column A and the number of months to move in column B.
2. Type `=EDATE(A2, B2)` and fill it down. Format column C as a date.
3. January 15 plus 3 months is April 15. January 31 plus 1 month is February 28, because February 2026 has no 31st.
4. Compare with `=DATE(YEAR(A2), MONTH(A2)+B2, DAY(A2))` on the same row: for January 31 it returns March 3 instead of February 28.
5. Negative months move backward, so March 15 minus 1 month is February 15.

## Google Sheets-specific notes

In Google Sheets, keep signup or invoice dates as real dates (Format > Number > Date) so EDATE can read them. Open-ended ranges such as A2:A work fine inside ARRAYFORMULA when you want a whole column of renewal dates: `=ARRAYFORMULA(IF(A2:A="", "", EDATE(A2:A, B2:B)))`. Empty cells in the months column are treated as zero, which returns the original date, so guard with IF when that is not what you want. EOMONTH is still the better choice for pure month-end deadlines. If the result looks like 46081, set Format > Number > Date on the formula column.

**Whole column of renewals**

```excel
=ARRAYFORMULA(IF(A2:A="", "", EDATE(A2:A, B2:B)))
```

**Same day next month**

```excel
=EDATE(A2, 1)
```

**End of month n months away**

```excel
=EOMONTH(A2, B2)
```


## Excel version

The same formula works unchanged in Excel:

```excel
=EDATE(A2, B2)
```

Google Sheets has the same EDATE and EOMONTH functions with identical month-end clamping.

<!--SIBLING-->


## Common errors and how to fix them

- **January 31 plus one month becomes March 3** — The formula used DATE(YEAR, MONTH+1, DAY) instead of EDATE, so the missing day spilled into March. **Fix:** Switch to EDATE, which clamps to the last day of February.
- **Result shows a number like 46081** — The cell is formatted as a number. **Fix:** Format it as a date.
- **#VALUE!** — The start date is text that looks like a date, or months is non-numeric text. **Fix:** Convert the date with DATEVALUE and make sure months is a number.
- **Renewal is one day off every other month** — The workbook added a fixed number of days (for example 30 or 90) instead of calendar months. **Fix:** Use EDATE with the real month count so month lengths are handled automatically.

## FAQ

### What is the difference between EDATE and EOMONTH?

EDATE keeps the same day of the month (or the last day if that day is missing). EOMONTH always returns the last day of the target month.

### How do I add months and then land on the next working day?

Wrap EDATE in WORKDAY: =WORKDAY(EDATE(A2, B2)-1, 1) moves to the renewal date and then to the next working day if needed.

### Does EDATE keep the time portion of a date-time value?

No. EDATE returns a pure date serial with no time. Add the original time back with +MOD(A2,1) if you need it.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
