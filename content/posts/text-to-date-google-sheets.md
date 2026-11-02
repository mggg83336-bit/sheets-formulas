---
title: How to Convert Text to a Date (DATEVALUE) in Google Sheets
slug: text-to-date-google-sheets
date: '2026-11-02'
summary: DATEVALUE turns a date written as text into a real spreadsheet date so WEEKDAY,
  EDATE and PivotTables can use it. When the text is not in a locale-friendly order,
  build the date with DATE plus LEFT, MID and RIGHT instead. This page shows both
  patterns with worked results.
tags:
- Dates & times
- Google Sheets
keyword: text-to-date-google-sheets
niche: sheets-formulas
provider: structured
entry_id: text-to-date
platform: Google Sheets
category: date
faq:
- q: When should I use DATE instead of DATEVALUE?
  a: Use DATE when the year, month and day sit in fixed character positions (for example
    yyyymmdd) or when slash order is ambiguous across locales. Use DATEVALUE for already
    locale-friendly or ISO date text.
- q: Does DATEVALUE keep a time portion?
  a: No. DATEVALUE returns a pure date serial. If the text includes a time, parse
    the date and time separately or use VALUE on a full date-time string your locale
    understands.
- q: How do I convert a whole column in Google Sheets?
  a: Use =ARRAYFORMULA(IF(A2:A="", "", DATEVALUE(A2:A))) and format the column as
    Date.
related:
- - date-google-sheets
  - date-excel
- - text-to-number-google-sheets
  - text-to-number-excel
- - weekday-google-sheets
  - weekday-excel
- - text-function-google-sheets
  - text-function-excel
sibling: text-to-date-excel
---
DATEVALUE turns a date written as text into a real spreadsheet date so WEEKDAY, EDATE and PivotTables can use it. When the text is not in a locale-friendly order, build the date with DATE plus LEFT, MID and RIGHT instead. This page shows both patterns with worked results.

## Quick answer

Use this formula in Google Sheets:

```excel
=DATEVALUE(A2)
```

DATEVALUE in Google Sheets converts date text to a date serial using the File > Settings locale. Format the result with Format > Number > Date.

## The problem

Exports arrive with dates as plain text ("2026-11-02", "11/02/2026", "20261102"). Sorting, filtering and date formulas treat them as text, so month totals and weekday flags come out wrong until the values become real dates.

## Worked example

Mixed text dates. DATEVALUE handles the ISO and month-name forms; the compact yyyymmdd value is rebuilt with DATE. Results are shown as calendar dates.

| | A | B | C |
|---|---|---|---|
| 1 | **Text date** | **DATEVALUE** | **DATE from digits** |
| 2 | 2026-11-02 | **2026-11-02** |  |
| 3 | 02-Nov-2026 | **2026-11-02** |  |
| 4 | 20261102 |  | **2026-11-02** |
| 5 | 2026-01-15 | **2026-01-15** |  |

Formulas used in the example (results shown in **bold** in the table above):

**B2 (filled to B3)** — DATEVALUE on parseable text

```excel
=DATEVALUE(A2)
```

Results: **2026-11-02**, **2026-11-02**

**B5** — DATEVALUE on another ISO date

```excel
=DATEVALUE(A5)
```

Result: **2026-01-15**

**C4** — DATE parts for yyyymmdd

```excel
=DATE(LEFT(A4,4), MID(A4,5,2), RIGHT(A4,2))
```

Result: **2026-11-02**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Put the text dates in column A. Prefer ISO `yyyy-mm-dd` when you can control the export.
2. Type `=DATEVALUE(A2)` and format the result as a Date, then fill down for locale-friendly text.
3. For compact `yyyymmdd` values use `=DATE(LEFT(A2,4), MID(A2,5,2), RIGHT(A2,2))` instead.
4. Replace the original text with Paste Special > Values once the convert column looks correct.
5. Confirm with WEEKDAY or MONTH on the converted cells to prove they are real dates.

## Google Sheets-specific notes

Set the spreadsheet locale to match the text order before relying on DATEVALUE for slash-separated dates. ISO `yyyy-mm-dd` is the safest import format across locales. For a whole column use `=ARRAYFORMULA(IF(A2:A="", "", DATEVALUE(A2:A)))`. Compact `yyyymmdd` strings still need DATE with LEFT/MID/RIGHT because DATEVALUE does not split bare digits. If DATEVALUE returns #VALUE!, check for extra spaces (TRIM first) or a time stamp glued to the date; split on space or use REGEXEXTRACT when the pattern is consistent. After a successful convert, paste values over the text column when formulas should no longer depend on the raw export.

**Whole column convert**

```excel
=ARRAYFORMULA(IF(A2:A="", "", DATEVALUE(A2:A)))
```

**Parse yyyymmdd digits**

```excel
=DATE(LEFT(A2,4), MID(A2,5,2), RIGHT(A2,2))
```

**Trim then convert**

```excel
=DATEVALUE(TRIM(A2))
```


## Excel version

The same formula works unchanged in Excel:

```excel
=DATEVALUE(A2)
```

Google Sheets DATEVALUE follows the spreadsheet locale under File > Settings, and also accepts many ISO strings. ARRAYFORMULA can convert a whole column in one step.

<!--SIBLING-->


## Common errors and how to fix them

- **#VALUE! from DATEVALUE** — The text order does not match the locale, or the string is bare digits / a non-date value. **Fix:** Switch locale, standardize on ISO text, or parse with DATE and LEFT/MID/RIGHT.
- **11/02/2026 becomes February instead of November** — The locale reads dates as DMY while the text was written as MDY (or the reverse). **Fix:** Use ISO text, or parse known positions with DATE so month and day cannot swap.
- **Converted date looks like 46328** — The cell is still formatted as a number. **Fix:** Format it as a Date.
- **Leading spaces break the parse** — Imported text includes stray spaces or non-breaking spaces. **Fix:** Wrap with TRIM (and SUBSTITUTE for CHAR(160) when needed) before DATEVALUE.

## FAQ

### When should I use DATE instead of DATEVALUE?

Use DATE when the year, month and day sit in fixed character positions (for example yyyymmdd) or when slash order is ambiguous across locales. Use DATEVALUE for already locale-friendly or ISO date text.

### Does DATEVALUE keep a time portion?

No. DATEVALUE returns a pure date serial. If the text includes a time, parse the date and time separately or use VALUE on a full date-time string your locale understands.

### How do I convert a whole column in Google Sheets?

Use =ARRAYFORMULA(IF(A2:A="", "", DATEVALUE(A2:A))) and format the column as Date.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
