---
title: How to Format Dates with the TEXT Function in Excel
slug: text-function-excel
date: '2026-10-30'
summary: TEXT turns a real date into a text string in exactly the layout you choose,
  such as 2026-03-05, March 5, 2026 or Thursday. It is the standard way to put a nicely
  formatted date inside a sentence, a file name or a label. Excel and Google Sheets
  share the TEXT syntax, but Excel's format codes depend o
tags:
- Dates & times
- Excel
keyword: text-function-excel
niche: sheets-formulas
provider: structured
entry_id: text-function
platform: Excel
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
- - days-between-dates-excel
  - days-between-dates-google-sheets
- - eomonth-excel
  - eomonth-google-sheets
- - datedif-age-excel
  - datedif-age-google-sheets
- - networkdays-excel
  - networkdays-google-sheets
sibling: text-function-google-sheets
---
TEXT turns a real date into a text string in exactly the layout you choose, such as 2026-03-05, March 5, 2026 or Thursday. It is the standard way to put a nicely formatted date inside a sentence, a file name or a label. Excel and Google Sheets share the TEXT syntax, but Excel's format codes depend on the language of your Excel installation, while Google Sheets always reads English codes.

## Quick answer

Use this formula in Excel:

```excel
=TEXT(A2, "yyyy-mm-dd")
```

Syntax: `TEXT(value, format_text)`. A2 holds a real date (a serial number behind the scenes); the format code "yyyy-mm-dd" returns it as the text 2026-03-05. The result is text, so it no longer sorts or calculates like a date.

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

## Excel-specific notes

The most useful date codes are yyyy (four-digit year), yy (two-digit year), m or mm (month number), mmm (Jan), mmmm (January), d or dd (day number), ddd (Thu) and dddd (Thursday). In Excel the codes are localised: a German Excel expects "JJJJ-MM-TT" and a French Excel "aaaa-mm-jj", so a workbook built with English codes can show the wrong result when it is opened in another language version. If you only want the cell to look different, use Format Cells > Number > Custom instead of TEXT, because cell formatting keeps the value a real date. In Microsoft 365, TEXT spills over a range: `=TEXT(A2:A10, "mmm yyyy")` returns one label per row.

**Readable date inside a sentence**

```excel
="Due on "&TEXT(A2, "mmmm d, yyyy")
```

**Weekday name**

```excel
=TEXT(A2, "dddd")
```

**Spill labels for a range (Excel 365)**

```excel
=TEXT(A2:A10, "mmm yyyy")
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=TEXT(A2, "yyyy-mm-dd")
```

Excel expects format codes in the language of the Excel installation and spills over ranges; Sheets always uses English codes and needs ARRAYFORMULA for a column.

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
