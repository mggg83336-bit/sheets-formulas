---
title: How to Calculate Age with DATEDIF in Excel
slug: datedif-age-excel
date: '2026-10-22'
summary: DATEDIF returns the number of complete years, months or days between two
  dates, which makes it the standard way to calculate age from a birth date. This
  page shows age in years, years plus months, and the quirks of this partly hidden
  function.
tags:
- Dates & times
- Excel
keyword: datedif-age-excel
niche: sheets-formulas
provider: structured
entry_id: datedif-age
platform: Excel
category: date
faq:
- q: Why not just use (TODAY()-B2)/365?
  a: Leap years make that slightly wrong around birthdays. DATEDIF counts real calendar
    years.
- q: How do I get the age on a specific date?
  a: Put that date in a cell and use it as the second argument, as in the example.
related:
- - days-between-dates-excel
  - days-between-dates-google-sheets
- - eomonth-excel
  - eomonth-google-sheets
- - networkdays-excel
  - networkdays-google-sheets
sibling: datedif-age-google-sheets
---
DATEDIF returns the number of complete years, months or days between two dates, which makes it the standard way to calculate age from a birth date. This page shows age in years, years plus months, and the quirks of this partly hidden function.

## Quick answer

Use this formula in Excel:

```excel
=DATEDIF(B2, TODAY(), "Y")
```

Syntax: `DATEDIF(start_date, end_date, unit)`. "Y" returns complete years between the birth date and today.

## The problem

You have employees' birth dates and need their current age in complete years, plus a "35 years, 11 months" style label for an HR report.

## Worked example

To make the example reproducible, ages are calculated as of the date in F2 (June 30, 2026). In a live sheet use TODAY() instead of $F$2.

| | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 1 | **Name** | **Birth date** | **Age** | **Years and months** |  | **As of** |
| 2 | Ana | 1990-07-14 | **35** | **35 years, 11 months** |  | 2026-06-30 |
| 3 | Ben | 1985-12-03 | **40** | **40 years, 6 months** |  |  |
| 4 | Chloe | 2001-02-28 | **25** | **25 years, 4 months** |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**C2 (filled to C4)** — filled down

```excel
=DATEDIF(B2, $F$2, "Y")
```

Results: **35**, **40**, **25**

**D2 (filled to D4)** — filled down

```excel
=DATEDIF(B2, $F$2, "Y")&" years, "&DATEDIF(B2, $F$2, "YM")&" months"
```

Results: **35 years, 11 months**, **40 years, 6 months**, **25 years, 4 months**

<!--AD_IN_ARTICLE-->

## How the formula works

1. "Y" counts complete years. Ana turns 36 on July 14, 2026, so on June 30 she is still 35.
2. "YM" counts the complete months after the last full year: from July 14, 2025 to June 30, 2026 is 11 months.
3. The start date must be earlier than the end date; otherwise DATEDIF returns
4. Replace $F$2 with TODAY() for an age that updates automatically.

## Excel-specific notes

DATEDIF is a legacy function kept for Lotus compatibility: it works in all Excel versions but does not appear in autocomplete or the Insert Function dialog, so you have to type it in full. Microsoft documents that the "MD" unit can return wrong results, so avoid it and use "YM" for months. YEARFRAC is an alternative (`=INT(YEARFRAC(B2, TODAY(), 1))`), but its day-count basis can make it off by one around birthdays in leap years.

**Years and months**

```excel
=DATEDIF(B2, TODAY(), "Y")&" years, "&DATEDIF(B2, TODAY(), "YM")&" months"
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=DATEDIF(B2, TODAY(), "Y")
```

Google Sheets has the same DATEDIF function and shows it in autocomplete.

<!--SIBLING-->


## Common errors and how to fix them

- **#NUM!** — The birth date is after the end date (often a typo in the year, or swapped arguments). **Fix:** Check the order: DATEDIF(earlier date, later date, unit).
- **#NAME? / formula not suggested (Excel)** — Excel hides DATEDIF from autocomplete, so it is easy to misspell. **Fix:** Type =DATEDIF( in full; it still works.
- **#VALUE!** — The birth date is text, not a real date. **Fix:** Convert with DATEVALUE or re-enter the date.

## FAQ

### Why not just use (TODAY()-B2)/365?

Leap years make that slightly wrong around birthdays. DATEDIF counts real calendar years.

### How do I get the age on a specific date?

Put that date in a cell and use it as the second argument, as in the example.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
