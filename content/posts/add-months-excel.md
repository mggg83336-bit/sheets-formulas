---
title: How to Add Months to a Date (EDATE) in Excel
slug: add-months-excel
date: '2026-11-01'
summary: EDATE shifts a date by a whole number of calendar months and keeps the same
  day of the month when that day exists. It is the clean way to add or subtract months
  for renewals, billing cycles and contract end dates. When the day does not exist
  in the target month, EDATE lands on the last day of that m
tags:
- Dates & times
- Excel
keyword: add-months-excel
niche: sheets-formulas
provider: structured
entry_id: add-months
platform: Excel
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
- - eomonth-excel
  - eomonth-google-sheets
- - workday-excel
  - workday-google-sheets
- - date-excel
  - date-google-sheets
- - today-now-excel
  - today-now-google-sheets
sibling: add-months-google-sheets
---
EDATE shifts a date by a whole number of calendar months and keeps the same day of the month when that day exists. It is the clean way to add or subtract months for renewals, billing cycles and contract end dates. When the day does not exist in the target month, EDATE lands on the last day of that month instead of spilling into the next one.

## Quick answer

Use this formula in Excel:

```excel
=EDATE(A2, B2)
```

Syntax: `EDATE(start_date, months)`. A2 is the start date and B2 is how many months to move (positive forward, negative backward). EDATE returns a date serial, so format the cell as a Date. January 31 plus 1 month becomes February 28 (or 29 in a leap year), not March 3.

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

## Excel-specific notes

Prefer EDATE over `=DATE(YEAR(A2), MONTH(A2)+B2, DAY(A2))` whenever the day of the month might not exist in the target month. The DATE construction rolls overflowing days into the next month, so Jan 31 + 1 becomes March 3 in a non-leap year, while EDATE clamps to the last day of February. Format the result as a date because EDATE returns a serial number. EOMONTH is better when you always want month-end due dates; combine both when a rule is "same day next month, else last day of month" which is exactly what EDATE already does. Negative months work the same way for going backward.

**Same day next month**

```excel
=EDATE(A2, 1)
```

**Three months earlier**

```excel
=EDATE(A2, -3)
```

**DATE construction (rolls over missing days)**

```excel
=DATE(YEAR(A2), MONTH(A2)+B2, DAY(A2))
```

**End of the month n months away**

```excel
=EOMONTH(A2, B2)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=EDATE(A2, B2)
```

Excel uses the same EDATE function; fill the formula down or spill it in Microsoft 365 instead of wrapping it in ARRAYFORMULA.

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
