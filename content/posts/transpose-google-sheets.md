---
title: How to Use the TRANSPOSE Formula in Google Sheets
slug: transpose-google-sheets
date: '2026-10-26'
summary: TRANSPOSE flips a range so rows become columns and columns become rows, and
  the result stays linked to the source. This guide shows the formula in Microsoft
  365 and older Excel, how it works in Google Sheets, how to transpose only part of
  a table, and when Paste Special is the better choice.
tags:
- Lookup & reference
- Google Sheets
keyword: transpose-google-sheets
niche: sheets-formulas
provider: structured
entry_id: transpose
platform: Google Sheets
category: lookup
faq:
- q: How do I transpose without a formula?
  a: Copy the range, right-click the destination and choose Paste Special > Transpose
    (Excel) or Paste special > Transposed (Google Sheets). The result is static and
    will not update.
- q: Can I edit one cell of a TRANSPOSE result?
  a: No. The output belongs to one formula, so editing a single cell gives an error
    or breaks the spill. Edit the source range instead, or convert the result to values
    first.
- q: Does TRANSPOSE work with another sheet?
  a: Yes, e.g. =TRANSPOSE(Report!A1:C4). In Google Sheets you can also transpose data
    from another file with =TRANSPOSE(IMPORTRANGE(url, "Report!A1:C4")).
related:
- - sequence-google-sheets
  - sequence-excel
- - sortby-excel
- - filter-google-sheets
  - filter-excel
- - unique-google-sheets
  - unique-excel
- - sort-google-sheets
  - sort-excel
sibling: transpose-excel
---
TRANSPOSE flips a range so rows become columns and columns become rows, and the result stays linked to the source. This guide shows the formula in Microsoft 365 and older Excel, how it works in Google Sheets, how to transpose only part of a table, and when Paste Special is the better choice.

## Quick answer

Use this formula in Google Sheets:

```excel
=TRANSPOSE(A1:C4)
```

Google Sheets uses the same `TRANSPOSE(range)` and expands the result automatically from the cell you type it in; no special keys are needed.

## The problem

Your monthly report has months down the rows and measures (Sales, Cost) across the columns, but the dashboard needs the months across the top. Copying and pasting with Paste Special > Transpose works once, but it does not update when the numbers change. You want a flipped copy that always matches the source table.

## Worked example

A 4-row by 3-column report (A1:C4). The formula in E1 returns it flipped to 3 rows by 4 columns.

| | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| 1 | **Month** | **Sales** | **Cost** |  | **Month** | **Jan** | **Feb** | **Mar** |
| 2 | Jan | 120 | 80 |  | **Sales** | **120** | **150** | **90** |
| 3 | Feb | 150 | 95 |  | **Cost** | **80** | **95** | **70** |
| 4 | Mar | 90 | 70 |  |  |  |  |  |
| 5 |  |  |  |  |  |  |  |  |
| 6 |  |  |  |  | Months over 100 | **Jan** | **Feb** |  |
| 7 |  |  |  |  |  |  |  |  |
| 8 |  |  |  |  | **360** |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**E1** — whole table flipped (fills E1:H3)

```excel
=TRANSPOSE(A1:C4)
```

Results: **Month**, **Jan**, **Feb**, **Mar**, **Sales**, **120**, **150**, **90**, **Cost**, **80**, **95**, **70**

**F6** — only the months with sales over 100, as a row

```excel
=TRANSPOSE(FILTER(A2:A4, B2:B4>100))
```

Results: **Jan**, **Feb**

**E8** — total sales from the transposed row

```excel
=SUM(F2:H2)
```

Result: **360**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Count the source size first: A1:C4 is 4 rows by 3 columns, so the transposed result needs 3 rows by 4 columns (E1:H3).
2. Type `=TRANSPOSE(A1:C4)` in E1. In Microsoft 365, Excel 2021 and Google Sheets it fills E1:H3 on its own. In Excel 2019 or older, select E1:H3 first, type the formula and press Ctrl+Shift+Enter.
3. Row 1 of the source (Month, Sales, Cost) becomes column E, and column A (Month, Jan, Feb, Mar) becomes row 1: Month, Jan, Feb, Mar.
4. The result is linked. Change Feb sales in B3 from 150 to 160 and G2 updates; `=SUM(F2:H2)` in E8 then changes from 360 to 370.
5. To flip only part of the data, filter first: `TRANSPOSE(FILTER(A2:A4, B2:B4>100))` keeps Jan (120) and Feb (150) and returns them across F6:G6.

## Google Sheets-specific notes

Google Sheets has always expanded TRANSPOSE without Ctrl+Shift+Enter. If cells in the target area are not empty, it shows #REF! ("Array result was not expanded because it would overwrite data"). Empty source cells stay empty instead of turning into 0. TRANSPOSE is often combined with Sheets-only functions: `=TRANSPOSE(SPLIT("Jan,Feb,Mar", ","))` turns a comma list into a column, and `=TRANSPOSE(UNIQUE(A2:A))` turns a column of names into a header row. To link a transposed range from another file, wrap IMPORTRANGE in TRANSPOSE.

**Comma list into a column**

```excel
=TRANSPOSE(SPLIT("Jan,Feb,Mar", ","))
```

**Unique names as a header row**

```excel
=TRANSPOSE(UNIQUE(A2:A))
```

**Transpose a filtered list**

```excel
=TRANSPOSE(FILTER(A2:A4, B2:B4>100))
```


## Excel version

The same formula works unchanged in Excel:

```excel
=TRANSPOSE(A1:C4)
```

Microsoft 365 spills TRANSPOSE automatically; Excel 2019 and older need a pre-selected range and Ctrl+Shift+Enter.

<!--SIBLING-->


## Common errors and how to fix them

- **#SPILL! (Excel) / #REF! (Google Sheets)** — The cells the flipped range needs already contain values. **Fix:** Clear the area to the right of and below the formula cell.
- **#VALUE! or only one value appears (Excel 2019 and older)** — The formula was confirmed with Enter instead of entered as an array formula. **Fix:** Select the full output range, type the formula and press Ctrl+Shift+Enter.
- **Blank cells show 0** — In Excel TRANSPOSE returns 0 for empty source cells. **Fix:** Use =TRANSPOSE(IF(A1:C4="", "", A1:C4)).
- **Dates show as numbers** — TRANSPOSE copies values, not number formats. **Fix:** Apply a date format to the result range.

## FAQ

### How do I transpose without a formula?

Copy the range, right-click the destination and choose Paste Special > Transpose (Excel) or Paste special > Transposed (Google Sheets). The result is static and will not update.

### Can I edit one cell of a TRANSPOSE result?

No. The output belongs to one formula, so editing a single cell gives an error or breaks the spill. Edit the source range instead, or convert the result to values first.

### Does TRANSPOSE work with another sheet?

Yes, e.g. =TRANSPOSE(Report!A1:C4). In Google Sheets you can also transpose data from another file with =TRANSPOSE(IMPORTRANGE(url, "Report!A1:C4")).

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
