---
title: How to Format Dates with the TEXT Function in Google Sheets
slug: text-function-google-sheets
date: '2026-10-30'
summary: TEXT turns a real date into a text string in exactly the layout you choose,
  such as 2026-03-05, March 5, 2026 or Thursday. It is the standard way to put a nicely
  formatted date inside a sentence, a file name or a label. Excel and Google Sheets
  share the TEXT syntax, but Excel's format codes depend o
tags:
- Dates & times
- Google Sheets
keyword: text-function-google-sheets
niche: sheets-formulas
provider: structured
entry_id: text-function
platform: Google Sheets
category: date
faq:
- q: Why does my date turn into a number when I combine it with text?
  a: Dates are stored as serial numbers, and & uses the stored value. Wrap the date
    in TEXT with a format code to keep it readable.
- q: Is TEXT the same as changing the cell format?
  a: No. Cell formatting changes only how the value looks and keeps it a real date.
    TEXT returns a new text value that no longer calculates like a date.
- q: How do I show the month name only?
  a: Use =TEXT(A2, "mmmm") for the full name or =TEXT(A2, "mmm") for the three-letter
    abbreviation.
related:
- - days-between-dates-google-sheets
  - days-between-dates-excel
- - eomonth-google-sheets
  - eomonth-excel
- - datedif-age-google-sheets
  - datedif-age-excel
- - networkdays-google-sheets
  - networkdays-excel
sibling: text-function-excel
---
TEXT turns a real date into a text string in exactly the layout you choose, such as 2026-03-05, March 5, 2026 or Thursday. It is the standard way to put a nicely formatted date inside a sentence, a file name or a label. Excel and Google Sheets share the TEXT syntax, but Excel's format codes depend on the language of your Excel installation, while Google Sheets always reads English codes.

## Quick answer

Use this formula in Google Sheets:

```excel
=TEXT(A2, "yyyy-mm-dd")
```

The same TEXT syntax works in Google Sheets: A2 must be a real date, and the format code decides how the returned text looks.

## The problem

You join a date to some text with & and get a meaningless serial number like 46086 instead of a readable date, or you need a date in one fixed layout (ISO, month name, weekday) for an export, a report title or a lookup key, regardless of how the cell itself is formatted.

## Worked example

Three real dates in column A turned into four common text layouts.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Date** | **ISO text** | **Long date** | **Weekday** | **Label** |
| 2 | 2026-03-05 | **2026-03-05** | **March 5, 2026** | **Thursday** | **Due Mar 2026** |
| 3 | 2026-12-25 | **2026-12-25** | **December 25, 2026** | **Friday** | **Due Dec 2026** |
| 4 | 2026-07-01 | **2026-07-01** | **July 1, 2026** | **Wednesday** | **Due Jul 2026** |

Formulas used in the example (results shown in **bold** in the table above):

**B2 (filled to B4)** — ISO 8601 layout

```excel
=TEXT(A2, "yyyy-mm-dd")
```

Results: **2026-03-05**, **2026-12-25**, **2026-07-01**

**C2 (filled to C4)** — full month name

```excel
=TEXT(A2, "mmmm d, yyyy")
```

Results: **March 5, 2026**, **December 25, 2026**, **July 1, 2026**

**D2 (filled to D4)** — weekday name

```excel
=TEXT(A2, "dddd")
```

Results: **Thursday**, **Friday**, **Wednesday**

**E2 (filled to E4)** — date joined to text

```excel
="Due "&TEXT(A2, "mmm yyyy")
```

Results: **Due Mar 2026**, **Due Dec 2026**, **Due Jul 2026**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Make sure column A holds real dates. =ISNUMBER(A2) should return TRUE.
2. In the result cell type `=TEXT(A2, "yyyy-mm-dd")` and press Enter.
3. Swap the format code for the layout you need: "mmmm d, yyyy" for March 5, 2026, "dddd" for the weekday, "mmm yyyy" for Mar 2026.
4. To use the date inside a sentence, join it with &: `="Due "&TEXT(A2, "mmm yyyy")`.
5. Fill the formula down (or spill it in Excel 365, or wrap it in ARRAYFORMULA in Google Sheets).

## Google Sheets-specific notes

Google Sheets always reads the English format codes (yyyy, mm, mmmm, dddd), whatever the spreadsheet locale is, so the formula is portable between accounts. The locale (File > Settings) only changes the language of month and weekday names in the result, for example "jeudi" instead of "Thursday" for a French locale. To format a whole column at once use `=ARRAYFORMULA(IF(A2:A="", "", TEXT(A2:A, "yyyy-mm-dd")))`. When you only want a different look, use Format > Number > Custom date and time, which keeps the value a real date. If TEXT returns the input unchanged, the cell holds text that only looks like a date; convert it with DATEVALUE first.

**Whole column of ISO dates**

```excel
=ARRAYFORMULA(IF(A2:A="", "", TEXT(A2:A, "yyyy-mm-dd")))
```

**Readable date inside a sentence**

```excel
="Due on "&TEXT(A2, "mmmm d, yyyy")
```

**Convert a text date first, then format**

```excel
=TEXT(DATEVALUE(A2), "dd mmm yyyy")
```


## Excel version

The same formula works unchanged in Excel:

```excel
=TEXT(A2, "yyyy-mm-dd")
```

Google Sheets uses the same TEXT function and the same English codes in every locale; it fills a column with ARRAYFORMULA instead of spilling.

<!--SIBLING-->


## Common errors and how to fix them

- **Result shows a number like 46086** — The date was joined with & without TEXT, so its serial number was used. **Fix:** Wrap the date in TEXT: `="Due "&TEXT(A2, "mmm yyyy")`.
- **Wrong or literal letters in the result (for example YYYY-03-05)** — In Excel the format codes follow the installation language, or the code uses a letter Excel does not know. **Fix:** Use the codes of your Excel language (for example JJJJ in German Excel), or keep the formatting in Format Cells instead of TEXT.
- **TEXT returns the value unchanged** — The cell holds text that looks like a date, not a real date. **Fix:** Convert it first with DATEVALUE, for example =TEXT(DATEVALUE(A2), "yyyy-mm-dd").
- **Sorting by the result is wrong** — TEXT returns text, so "April" sorts before "March". **Fix:** Sort by the original date column, or use the ISO layout yyyy-mm-dd, which sorts correctly as text.

## FAQ

### Why does my date turn into a number when I combine it with text?

Dates are stored as serial numbers, and & uses the stored value. Wrap the date in TEXT with a format code to keep it readable.

### Is TEXT the same as changing the cell format?

No. Cell formatting changes only how the value looks and keeps it a real date. TEXT returns a new text value that no longer calculates like a date.

### How do I show the month name only?

Use `=TEXT(A2, "mmmm")` for the full name or `=TEXT(A2, "mmm")` for the three-letter abbreviation.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
