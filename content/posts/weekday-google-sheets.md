---
title: How to Get the Weekday of a Date (WEEKDAY) in Google Sheets
slug: weekday-google-sheets
date: '2026-11-01'
summary: WEEKDAY returns a number for the day of the week so you can flag weekends,
  build workday rules and sort by Monday-first calendars. Pair it with TEXT(..., "dddd")
  when you need the weekday name instead of a number. The second argument controls
  whether the week starts on Sunday or Monday.
tags:
- Dates & times
- Google Sheets
keyword: weekday-google-sheets
niche: sheets-formulas
provider: structured
entry_id: weekday
platform: Google Sheets
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
- - workday-google-sheets
  - workday-excel
- - networkdays-google-sheets
  - networkdays-excel
- - text-function-google-sheets
  - text-function-excel
- - today-now-google-sheets
  - today-now-excel
sibling: weekday-excel
---
WEEKDAY returns a number for the day of the week so you can flag weekends, build workday rules and sort by Monday-first calendars. Pair it with TEXT(..., "dddd") when you need the weekday name instead of a number. The second argument controls whether the week starts on Sunday or Monday.

## Quick answer

Use this formula in Google Sheets:

```excel
=WEEKDAY(A2, 2)
```

WEEKDAY in Google Sheets uses the same return_type codes: 2 for Monday = 1 through Sunday = 7, and 1 for Sunday = 1.

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

## Google Sheets-specific notes

Sheets reads English TEXT codes in every locale, but the weekday *names* still follow the File > Settings locale, so "dddd" may return a translated name. For a whole column use `=ARRAYFORMULA(IF(A2:A="", "", WEEKDAY(A2:A, 2)))`. Weekend highlighting is often easier with conditional formatting and a custom formula `=WEEKDAY(A2, 2)>=6` applied to the date range. If you only need the name for a label, TEXT is enough; keep WEEKDAY when formulas must branch on the number. Empty date cells return 0 from WEEKDAY in some contexts, so guard with IF(A2="", "", WEEKDAY(A2, 2)).

**Whole column of weekday numbers**

```excel
=ARRAYFORMULA(IF(A2:A="", "", WEEKDAY(A2:A, 2)))
```

**Weekday name**

```excel
=TEXT(A2, "dddd")
```

**Weekend flag**

```excel
=IF(WEEKDAY(A2, 2)>=6, "Weekend", "Weekday")
```


## Excel version

The same formula works unchanged in Excel:

```excel
=WEEKDAY(A2, 2)
```

Google Sheets supports the same WEEKDAY return types and the same TEXT weekday codes.

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
