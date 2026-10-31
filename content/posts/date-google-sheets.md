---
title: How to Use the DATE Function in Google Sheets
slug: date-google-sheets
date: '2026-10-31'
summary: DATE builds a real date from a year, a month and a day number. It is the
  safest way to put a date inside a formula, to rebuild dates from separate columns
  or from text codes such as 20260704, and to move a date by whole months or years.
  Works the same in Excel and Google Sheets, with a few Sheets-on
tags:
- Dates & times
- Google Sheets
keyword: date-google-sheets
niche: sheets-formulas
provider: structured
entry_id: date-function
platform: Google Sheets
category: date
faq:
- q: How do I get the first day of the month with DATE?
  a: 'Use day 1: =DATE(YEAR(A2), MONTH(A2), 1).'
- q: How do I add years to a date?
  a: 'Add to the year part: =DATE(YEAR(A2)+1, MONTH(A2), DAY(A2)). February 29 then
    rolls to March 1 in a non-leap year.'
- q: Why use DATE instead of typing "3/15/2026" in a formula?
  a: A typed date string is read according to the regional settings, so it can mean
    a different date or an error on another computer. DATE always means the same day.
related:
- - eomonth-google-sheets
  - eomonth-excel
- - days-between-dates-google-sheets
  - days-between-dates-excel
- - today-now-google-sheets
  - today-now-excel
- - sum-by-month-google-sheets
  - sum-by-month-excel
sibling: date-excel
---
DATE builds a real date from a year, a month and a day number. It is the safest way to put a date inside a formula, to rebuild dates from separate columns or from text codes such as 20260704, and to move a date by whole months or years. Works the same in Excel and Google Sheets, with a few Sheets-only helpers.

## Quick answer

Use this formula in Google Sheets:

```excel
=DATE(A2, B2, C2)
```

DATE works the same way in Google Sheets: year, month and day become a real date, and month or day numbers outside the normal range roll over into the next or previous month.

## The problem

Your export has the year, month and day in three separate columns, or a date written as a code like 20260704, and you need a real date that sorts, filters and works with other date functions. Typing a date as text inside a formula also breaks when someone opens the file with different regional settings.

## Worked example

Year, month and day numbers in columns A to C, and text date codes in column F. Row 3 uses month 14 and row 4 uses day 0 to show how DATE rolls over.

| | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| 1 | **Year** | **Month** | **Day** | **Date** | **Next month** | **Text code** | **From code** | **Days in month** |
| 2 | 2026 | 3 | 15 | **2026-03-15** | **2026-04-15** | 20260704 | **2026-07-04** | **31** |
| 3 | 2026 | 14 | 1 | **2027-02-01** |  | 20261231 | **2026-12-31** |  |
| 4 | 2026 | 3 | 0 | **2026-02-28** |  | 20270115 | **2027-01-15** |  |

Formulas used in the example (results shown in **bold** in the table above):

**D2 (filled to D4)** — filled down

```excel
=DATE(A2, B2, C2)
```

Results: **2026-03-15**, **2027-02-01**, **2026-02-28**

**E2** — same day one month later

```excel
=DATE(YEAR(D2), MONTH(D2)+1, DAY(D2))
```

Result: **2026-04-15**

**G2 (filled to G4)** — text code to date, filled down

```excel
=DATE(LEFT(F2, 4), MID(F2, 5, 2), RIGHT(F2, 2))
```

Results: **2026-07-04**, **2026-12-31**, **2027-01-15**

**H2** — days in March 2026

```excel
=DAY(DATE(A2, B2+1, 0))
```

Result: **31**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Put the year, month and day in separate cells, or point DATE at the columns you already have.
2. Type `=DATE(A2, B2, C2)` in the first result cell and press Enter.
3. If the result shows a number, format the cell as a date.
4. Fill the formula down. Month 14 in row 3 rolls into February 2027, and day 0 in row 4 returns the last day of February 2026.
5. For text codes, cut the code into pieces with LEFT, MID and RIGHT and pass them to DATE: 20260704 becomes July 4, 2026.

## Google Sheets-specific notes

Google Sheets usually formats the result as a date automatically; if you see a number such as 46096, use Format > Number > Date. To build a whole column at once, wrap the formula in ARRAYFORMULA and leave empty rows blank with IF. TO_DATE turns a serial number back into a date without changing the cell format, which is handy after math on dates. Sheets also adds 1900 to two-digit years, so type four digits. Unlike Excel, a Google Sheets cell can hold dates before 1900, but DATE itself still treats years below 1900 as offsets.

**Whole column with ARRAYFORMULA**

```excel
=ARRAYFORMULA(IF(A2:A="", "", DATE(A2:A, B2:B, C2:C)))
```

**Serial number to date**

```excel
=TO_DATE(46096)
```

**From a text code like 20260704**

```excel
=DATE(LEFT(F2, 4), MID(F2, 5, 2), RIGHT(F2, 2))
```


## Excel version

The same formula works unchanged in Excel:

```excel
=DATE(A2, B2, C2)
```

Google Sheets has the same DATE function and the same roll-over rules, plus TO_DATE and ARRAYFORMULA for whole columns.

<!--SIBLING-->


## Common errors and how to fix them

- **Result shows a number like 46096** — The cell is formatted as a number, and dates are stored as serial numbers. **Fix:** Format the cell as a date.
- **The year comes out as 1926** — A two-digit year was used, and years from 0 to 1899 are added to 1900. **Fix:** Always pass a four-digit year, for example 2026.
- **#VALUE!** — One of the arguments is text that cannot be read as a number, such as "March". **Fix:** Use the month number, or convert the text first, for example with MONTH(DATEVALUE("1 "&B2&" 2026")).
- **#NUM!** — The resulting date is before 1900 in Excel, for example a negative year. **Fix:** Check the year column for empty or wrong values.

## FAQ

### How do I get the first day of the month with DATE?

Use day 1: =DATE(YEAR(A2), MONTH(A2), 1).

### How do I add years to a date?

Add to the year part: =DATE(YEAR(A2)+1, MONTH(A2), DAY(A2)). February 29 then rolls to March 1 in a non-leap year.

### Why use DATE instead of typing "3/15/2026" in a formula?

A typed date string is read according to the regional settings, so it can mean a different date or an error on another computer. DATE always means the same day.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
