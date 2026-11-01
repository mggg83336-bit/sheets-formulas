---
title: How to Get the Weekday of a Date (WEEKDAY) in Excel
slug: weekday-excel
date: '2026-11-01'
summary: WEEKDAY returns a number for the day of the week so you can flag weekends,
  build workday rules and sort by Monday-first calendars. Pair it with TEXT(..., "dddd")
  when you need the weekday name instead of a number. The second argument controls
  whether the week starts on Sunday or Monday.
tags:
- Dates & times
- Excel
keyword: weekday-excel
niche: sheets-formulas
provider: structured
entry_id: weekday
platform: Excel
category: date
faq:
- q: What return_type should I use?
  a: Use 2 when weeks start on Monday (common in business sheets). Use 1 only when
    you specifically need Sunday = 1.
- q: How do I get the weekday name instead of a number?
  a: Use =TEXT(A2, "dddd") for the full name or "ddd" for the three-letter form.
- q: How do I skip weekends when adding days?
  a: Prefer WORKDAY or WORKDAY.INTL over manual WEEKDAY loops; they skip weekends
    and optional holidays in one call.
related:
- - workday-excel
  - workday-google-sheets
- - networkdays-excel
  - networkdays-google-sheets
- - text-function-excel
  - text-function-google-sheets
- - today-now-excel
  - today-now-google-sheets
sibling: weekday-google-sheets
---
WEEKDAY returns a number for the day of the week so you can flag weekends, build workday rules and sort by Monday-first calendars. Pair it with TEXT(..., "dddd") when you need the weekday name instead of a number. The second argument controls whether the week starts on Sunday or Monday.

## Quick answer

Use this formula in Excel:

```excel
=WEEKDAY(A2, 2)
```

Syntax: `WEEKDAY(serial_number, [return_type])`. With return_type 2, Monday is 1 and Sunday is 7, which matches most business calendars. Return_type 1 (the default) makes Sunday 1 and Saturday 7. The result is a number; use TEXT(A2, "dddd") when you need the name.

## The problem

A schedule needs to mark Saturdays and Sundays, or shift a due date when it falls on a weekend. Comparing the date formatted as "Saturday" as text is brittle across locales, and the default WEEKDAY numbering (Sunday = 1) surprises people who expect Monday = 1.

## Worked example

Four dates in late 2026 with WEEKDAY return_type 1 (Sunday = 1), return_type 2 (Monday = 1) and the weekday name from TEXT.

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **Date** | **WEEKDAY type 1** | **WEEKDAY type 2** | **Weekday name** |
| 2 | 2026-11-01 | **1** | **7** | **Sunday** |
| 3 | 2026-11-02 | **2** | **1** | **Monday** |
| 4 | 2026-11-07 | **7** | **6** | **Saturday** |
| 5 | 2026-12-25 | **6** | **5** | **Friday** |

Formulas used in the example (results shown in **bold** in the table above):

**B2 (filled to B5)** — Sunday=1 numbering

```excel
=WEEKDAY(A2, 1)
```

Results: **1**, **2**, **7**, **6**

**C2 (filled to C5)** — Monday=1 numbering

```excel
=WEEKDAY(A2, 2)
```

Results: **7**, **1**, **6**, **5**

**D2 (filled to D5)** — weekday name

```excel
=TEXT(A2, "dddd")
```

Results: **Sunday**, **Monday**, **Saturday**, **Friday**

<!--AD_IN_ARTICLE-->

## How the formula works

1. List the dates in column A as real dates.
2. Type `=WEEKDAY(A2, 2)` for Monday-first numbers and fill down.
3. Add `=WEEKDAY(A2, 1)` if you need the Sunday-first numbering for comparison.
4. Use `=TEXT(A2, "dddd")` when you want the name instead of a number.
5. Flag weekends with `=WEEKDAY(A2, 2)>=6`, or move a weekend date with WORKDAY.

## Excel-specific notes

Return_type 2 is the usual choice for Monday-to-Friday logic: weekend tests become `=WEEKDAY(A2, 2)>=6`. Return_type 1 is the Excel default and matches some US calendars. Return_type 11 to 17 mirror the WORKDAY.INTL weekend codes if you need another start day. WEEKDAY ignores any time portion of a date-time value. Format the result as a number, not a date. For the weekday name use TEXT with "ddd" or "dddd"; those codes follow the Excel installation language, so a French Excel may show "lundi" instead of "Monday". To push a weekend date to the next Monday, use WORKDAY or a small IF around WEEKDAY.

**Sunday = 1 (Excel default)**

```excel
=WEEKDAY(A2, 1)
```

**Weekday name**

```excel
=TEXT(A2, "dddd")
```

**Weekend flag (Mon=1)**

```excel
=IF(WEEKDAY(A2, 2)>=6, "Weekend", "Weekday")
```

**Next Monday if weekend**

```excel
=IF(WEEKDAY(A2, 2)>=6, A2+(8-WEEKDAY(A2, 2)), A2)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=WEEKDAY(A2, 2)
```

Excel uses the same WEEKDAY return types; fill down or spill instead of ARRAYFORMULA, and remember that TEXT weekday names follow the Excel UI language.

<!--SIBLING-->


## Common errors and how to fix them

- **Monday comes back as 2 instead of 1** — The formula used the default return_type 1, where Sunday is 1. **Fix:** Pass 2 as the second argument for Monday = 1.
- **Weekday name is in another language** — TEXT uses the Excel UI language or the Sheets spreadsheet locale for names. **Fix:** Change the locale, or map WEEKDAY numbers to English names with CHOOSE or SWITCH.
- **#VALUE!** — The cell holds text that only looks like a date. **Fix:** Convert it with DATEVALUE before WEEKDAY.
- **Weekend test marks Friday as a weekend** — The test used return_type 1 with >=6, which treats Friday (6) and Saturday (7) as the weekend. **Fix:** Use return_type 2, where Saturday and Sunday are 6 and 7.

## FAQ

### What return_type should I use?

Use 2 when weeks start on Monday (common in business sheets). Use 1 only when you specifically need Sunday = 1.

### How do I get the weekday name instead of a number?

Use =TEXT(A2, "dddd") for the full name or "ddd" for the three-letter form.

### How do I skip weekends when adding days?

Prefer WORKDAY or WORKDAY.INTL over manual WEEKDAY loops; they skip weekends and optional holidays in one call.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
