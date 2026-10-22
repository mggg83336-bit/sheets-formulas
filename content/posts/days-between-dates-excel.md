---
title: How to Calculate Days Between Two Dates in Excel
slug: days-between-dates-excel
date: '2026-10-22'
summary: Dates are stored as serial numbers, so subtracting one date from another
  gives the number of days between them. This page covers simple subtraction, the
  DAYS function, counting both the start and end day, and why the answer sometimes
  appears as a date.
tags:
- Dates & times
- Excel
keyword: days-between-dates-excel
niche: sheets-formulas
provider: structured
entry_id: days-between-dates
platform: Excel
category: date
faq:
- q: How do I count only weekdays?
  a: Use NETWORKDAYS(start, end), which excludes Saturdays, Sundays and optional holidays.
- q: How do I calculate days from a date until today?
  a: Use =TODAY()-A2. The result updates every day.
- q: How do I calculate the difference in years or months?
  a: 'Use DATEDIF: =DATEDIF(A2, B2, "M") returns complete months and =DATEDIF(A2,
    B2, "Y") complete years. For a decimal number of years, use =YEARFRAC(A2, B2).'
related:
- - networkdays-excel
  - networkdays-google-sheets
- - datedif-age-excel
  - datedif-age-google-sheets
- - eomonth-excel
  - eomonth-google-sheets
- - sumifs-between-dates-excel
  - sumifs-between-dates-google-sheets
sibling: days-between-dates-google-sheets
---
Dates are stored as serial numbers, so subtracting one date from another gives the number of days between them. This page covers simple subtraction, the DAYS function, counting both the start and end day, and why the answer sometimes appears as a date.

## Quick answer

Use this formula in Excel:

```excel
=B2-A2
```

Excel stores each date as the number of days since January 1, 1900, so the difference of two dates is a number of days.

## The problem

For each project you know the start and end date and need the duration in days, both exclusive (difference) and inclusive (counting both days).

## Worked example

Duration of three periods.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Start** | **End** | **Days (B-A)** | **DAYS** | **Inclusive** |
| 2 | 2026-01-15 | 2026-03-02 | **46** | **46** | **47** |
| 3 | 2026-02-01 | 2026-02-28 | **27** | **27** | **28** |
| 4 | 2025-12-20 | 2026-01-05 | **16** | **16** | **17** |

Formulas used in the example (results shown in **bold** in the table above):

**C2 (filled to C4)**

```excel
=B2-A2
```

Results: **46**, **27**, **16**

**D2 (filled to D4)**

```excel
=DAYS(B2, A2)
```

Results: **46**, **27**, **16**

**E2 (filled to E4)** — counts both the start and end day

```excel
=B2-A2+1
```

Results: **47**, **28**, **17**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Each date is a whole number behind the scenes (2026-01-15 is 46037).
2. Subtracting gives the gap in days. January 15 to March 2, 2026 is 16 days left in January + 28 in February + 2 in March = 46.
3. Add 1 when both the first and the last day should count, for example for hotel nights vs. days of a trip.
4. DAYS(end, start) does the same subtraction; note that the end date comes first.

## Excel-specific notes

If the result looks like a date (e.g. 1/15/1900), the cell inherited a date format; set it to General or Number. DAYS(end, start) gives the same result and makes the order of arguments explicit. For whole months or years between dates use DATEDIF, and for working days use NETWORKDAYS. If either date includes a time, wrap them in INT to count calendar days only.

**DAYS function**

```excel
=DAYS(B2, A2)
```

**Calendar days when the values include times**

```excel
=INT(B2)-INT(A2)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=B2-A2
```

The same subtraction works in Google Sheets; if the result shows as a date, use Format > Number > Number.

<!--SIBLING-->


## Common errors and how to fix them

- **Result shows as a date** — The result cell is formatted as a date. **Fix:** Format it as General / Number.
- **#VALUE!** — One of the dates is text, not a real date. **Fix:** Convert with DATEVALUE or re-enter it; =ISNUMBER(A2) should be TRUE.
- **Negative number** — The start and end dates are reversed. **Fix:** Swap the references, or use =ABS(B2-A2).

## FAQ

### How do I count only weekdays?

Use NETWORKDAYS(start, end), which excludes Saturdays, Sundays and optional holidays.

### How do I calculate days from a date until today?

Use =TODAY()-A2. The result updates every day.

### How do I calculate the difference in years or months?

Use DATEDIF: =DATEDIF(A2, B2, "M") returns complete months and =DATEDIF(A2, B2, "Y") complete years. For a decimal number of years, use =YEARFRAC(A2, B2).

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
