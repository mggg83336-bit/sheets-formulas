---
title: How to Get Month and Year from a Date in Excel
slug: month-year-excel
date: '2026-11-01'
summary: 'Pull a month-year label, the month number and the year from a real date
  so you can group invoices, build pivot keys and label charts. TEXT gives a readable
  "2026-11" or "Nov 2026" string; MONTH and YEAR return the numbers; DATE(YEAR, MONTH,
  1) gives the first day of that month for sorting and range '
tags:
- Dates & times
- Excel
keyword: month-year-excel
niche: sheets-formulas
provider: structured
entry_id: month-year
platform: Excel
category: date
faq:
- q: Should I use TEXT or MONTH and YEAR for grouping?
  a: Use TEXT("yyyy-mm") for a single readable key. Use MONTH and YEAR when you need
    the numbers separately, or DATE(YEAR, MONTH, 1) when the helper must remain a
    date.
- q: How do I sum amounts by month-year?
  a: Add a helper column with =TEXT(A2, "yyyy-mm") and use SUMIF on that column, or
    pivot on =DATE(YEAR(A2), MONTH(A2), 1).
- q: Why is TEXT better than Format Cells for a lookup key?
  a: Format Cells only changes how the value looks; VLOOKUP and SUMIF still see the
    full date. TEXT returns a real text key that matches across rows in the same month.
related:
- - text-function-excel
  - text-function-google-sheets
- - eomonth-excel
  - eomonth-google-sheets
- - date-excel
  - date-google-sheets
- - sum-by-month-excel
  - sum-by-month-google-sheets
sibling: month-year-google-sheets
---
Pull a month-year label, the month number and the year from a real date so you can group invoices, build pivot keys and label charts. TEXT gives a readable "2026-11" or "Nov 2026" string; MONTH and YEAR return the numbers; DATE(YEAR, MONTH, 1) gives the first day of that month for sorting and range lookups.

## Quick answer

Use this formula in Excel:

```excel
=TEXT(A2, "yyyy-mm")
```

Syntax: `TEXT(value, format_text)`. With "yyyy-mm" the date in A2 becomes the text 2026-11, which sorts correctly as text and works as a SUMIF / COUNTIF key. Use MONTH(A2) and YEAR(A2) when you need the numbers, or DATE(YEAR(A2), MONTH(A2), 1) when you need a real first-of-month date.

## The problem

A sales log has full dates, but the report needs one row per calendar month. Sorting by the month name as text puts April before February, and joining YEAR and MONTH with & without zero-padding breaks chronological order.

## Worked example

Four invoice dates turned into a month-year key, month number, year and first-of-month date.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Invoice date** | **Month-year** | **Month** | **Year** | **First of month** |
| 2 | 2026-01-15 | **2026-01** | **1** | **2026** | **2026-01-01** |
| 3 | 2026-03-31 | **2026-03** | **3** | **2026** | **2026-03-01** |
| 4 | 2026-11-01 | **2026-11** | **11** | **2026** | **2026-11-01** |
| 5 | 2026-12-25 | **2026-12** | **12** | **2026** | **2026-12-01** |

Formulas used in the example (results shown in **bold** in the table above):

**B2 (filled to B5)** — yyyy-mm text key

```excel
=TEXT(A2, "yyyy-mm")
```

Results: **2026-01**, **2026-03**, **2026-11**, **2026-12**

**C2 (filled to C5)** — month number

```excel
=MONTH(A2)
```

Results: **1**, **3**, **11**, **12**

**D2 (filled to D5)** — year number

```excel
=YEAR(A2)
```

Results: **2026**, **2026**, **2026**, **2026**

**E2 (filled to E5)** — first day of month

```excel
=DATE(YEAR(A2), MONTH(A2), 1)
```

Results: **2026-01-01**, **2026-03-01**, **2026-11-01**, **2026-12-01**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Confirm column A holds real dates (=ISNUMBER(A2) is TRUE).
2. Type `=TEXT(A2, "yyyy-mm")` for a sortable month-year key and fill it down.
3. Add `=MONTH(A2)` and `=YEAR(A2)` when you need the numbers for filters or charts.
4. Use `=DATE(YEAR(A2), MONTH(A2), 1)` when the helper column must stay a real date for SUMIFS or pivots.
5. Group or pivot on the key column; ISO keys keep months in calendar order.

## Excel-specific notes

Prefer the ISO layout "yyyy-mm" for grouping keys because it sorts in calendar order as text. "mmm yyyy" is nicer for chart labels but sorts alphabetically. MONTH returns 1 to 12 and YEAR returns the four-digit year; neither needs special formatting. When you need a value that still behaves like a date (for example as the start of a SUMIFS range), use `=DATE(YEAR(A2), MONTH(A2), 1)` and format it as MMM YYYY. In Excel the TEXT format codes follow the installation language, so a German Excel expects different letters for year and day. If you only want a different look without changing the value, use Format Cells instead of TEXT.

**Month number**

```excel
=MONTH(A2)
```

**Year number**

```excel
=YEAR(A2)
```

**First day of the month**

```excel
=DATE(YEAR(A2), MONTH(A2), 1)
```

**Short month-year label**

```excel
=TEXT(A2, "mmm yyyy")
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=TEXT(A2, "yyyy-mm")
```

Excel spills TEXT over a range in Microsoft 365 and localises format codes; Sheets uses ARRAYFORMULA and always reads English codes.

<!--SIBLING-->


## Common errors and how to fix them

- **Month names sort as April, August, February** — The key used "mmm yyyy" or the month name alone, which sorts alphabetically. **Fix:** Use "yyyy-mm" or a real first-of-month date column for sorting.
- **Result shows a serial number when joined to text** — The date was concatenated with & without TEXT. **Fix:** Wrap it: `="Month "&TEXT(A2, "yyyy-mm")`.
- **TEXT returns the input unchanged** — The cell holds text that looks like a date. **Fix:** Convert with DATEVALUE first, then apply TEXT or MONTH.
- **Wrong year near New Year** — A fiscal-year rule was expected, but YEAR returns the calendar year. **Fix:** Build a fiscal key with IF(MONTH(A2)>=start_month, YEAR(A2)+1, YEAR(A2)) or similar.

## FAQ

### Should I use TEXT or MONTH and YEAR for grouping?

Use TEXT("yyyy-mm") for a single readable key. Use MONTH and YEAR when you need the numbers separately, or DATE(YEAR, MONTH, 1) when the helper must remain a date.

### How do I sum amounts by month-year?

Add a helper column with =TEXT(A2, "yyyy-mm") and use SUMIF on that column, or pivot on =DATE(YEAR(A2), MONTH(A2), 1).

### Why is TEXT better than Format Cells for a lookup key?

Format Cells only changes how the value looks; VLOOKUP and SUMIF still see the full date. TEXT returns a real text key that matches across rows in the same month.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
