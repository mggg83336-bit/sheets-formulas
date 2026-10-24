---
title: How to Use INDEX MATCH in Excel
slug: index-match-excel
date: '2026-10-22'
summary: 'INDEX MATCH is the classic flexible lookup: MATCH finds the row number and
  INDEX returns the value at that position. It can look left, does not break when
  columns are inserted, and works in every version of Excel and Google Sheets. This
  guide covers the one-way and two-way forms.'
tags:
- Lookup & reference
- Excel
keyword: index-match-excel
niche: sheets-formulas
provider: structured
entry_id: index-match
platform: Excel
category: lookup
faq:
- q: Why use INDEX MATCH instead of VLOOKUP?
  a: It can return a column to the left, it does not depend on a hard-coded column
    number, and it only reads the two columns it needs.
- q: Is INDEX MATCH faster than XLOOKUP?
  a: The difference is negligible on normal-sized sheets. Choose XLOOKUP for readability
    in Microsoft 365 and Google Sheets, and INDEX MATCH for compatibility with older
    Excel.
- q: When is INDEX MATCH better than VLOOKUP?
  a: When the value you want is to the left of the column you search, or when you
    do not want a hard-coded column number. The country example on this page looks
    up the code CA in column C and returns Canada from column A. VLOOKUP cannot do
    that. See the left-lookup section above.
related:
- - xlookup-excel
  - xlookup-google-sheets
- - vlookup-excel
  - vlookup-google-sheets
- - lookup-multiple-values-excel
  - lookup-multiple-values-google-sheets
- - iferror-excel
  - iferror-google-sheets
- - hlookup-excel
  - hlookup-google-sheets
- - vlookup-multiple-criteria-excel
  - vlookup-multiple-criteria-google-sheets
- - na-error-excel
  - na-error-google-sheets
sibling: index-match-google-sheets
---
INDEX MATCH is the classic flexible lookup: MATCH finds the row number and INDEX returns the value at that position. It can look left, does not break when columns are inserted, and works in every version of Excel and Google Sheets. This guide covers the one-way and two-way forms.

## Quick answer

Use this formula in Excel:

```excel
=INDEX(A2:A6, MATCH(E2, C2:C6, 0))
```

MATCH(E2, C2:C6, 0) returns the position of the code in C2:C6. INDEX(A2:A6, position) returns the country in that position.

<!--CTA_PROMINENT-->

## INDEX MATCH vs VLOOKUP (left lookup)

[VLOOKUP](../vlookup-excel/) searches the first column of its range and can only return a column to the right. INDEX and MATCH split the job, so the column you return can sit to the left of the column you search.

In the worked example further down, the code is in column C and the country name is in column A. The code typed in E2 is CA. MATCH finds CA in the 4th row of C2:C6, and INDEX returns Canada from A2:A6:

```excel
=INDEX(A2:A6, MATCH(E2, C2:C6, 0))
```

Result: Canada. That is the left lookup. The same idea with [XLOOKUP](../xlookup-excel/) is `=XLOOKUP(E2, C2:C6, A2:A6)`. Keep INDEX MATCH when the workbook has to open in older Excel.

A missing code is [#N/A](../na-error-excel/). [IFERROR](../iferror-excel/) will hide it, but IFNA is safer, so a wrong range still shows. To return every matching row instead of the first one, use [lookup multiple values](../lookup-multiple-values-excel/). For a horizontal table, headers across a row and the values underneath, [HLOOKUP](../hlookup-excel/) is the one-direction equivalent of VLOOKUP.

## The problem

You have a table of countries with their ISO code in the last column. You want to type a code and get the country name, which sits to the left of the code, and you also want a formula that can pick any column by its header.

## Worked example

Find the country (column A) for the code in E2, and the capital using the header name.

| | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 1 | **Country** | **Capital** | **Code** |  | **Code** | **Result** |
| 2 | France | Paris | FR |  | CA | **Canada** |
| 3 | Japan | Tokyo | JP |  |  | **Ottawa** |
| 4 | Brazil | Brasília | BR |  |  |  |
| 5 | Canada | Ottawa | CA |  |  |  |
| 6 | Kenya | Nairobi | KE |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**F2** — country for code CA (left lookup)

```excel
=INDEX(A2:A6, MATCH(E2, C2:C6, 0))
```

Result: **Canada**

**F3** — two-way lookup, column chosen by its header

```excel
=INDEX(A2:C6, MATCH(E2, C2:C6, 0), MATCH("Capital", A1:C1, 0))
```

Result: **Ottawa**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `MATCH(E2, C2:C6, 0)` searches C2:C6 for "CA" and returns 4, because CA is the 4th item.
2. `INDEX(A2:A6, 4)` returns the 4th item of A2:A6: Canada.
3. In the two-way version, INDEX gets a row number and a column number: the second MATCH looks up the header "Capital" in A1:C1 and returns 2.
4. Because the return column is referenced directly, inserting a new column inside the table does not break the formula.

## Excel-specific notes

INDEX MATCH works in every Excel version, which makes it the safest lookup for workbooks shared with people on Excel 2016 or 2019. In Microsoft 365, XMATCH can replace MATCH and adds a search-from-the-end mode. Always use 0 as the last MATCH argument for an exact match; 1 (the default) assumes sorted data.

**Microsoft 365 equivalent with XLOOKUP**

```excel
=XLOOKUP(E2, C2:C6, A2:A6)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=INDEX(A2:A6, MATCH(E2, C2:C6, 0))
```

Google Sheets uses the identical formula.

<!--SIBLING-->


## Common errors and how to fix them

- **#N/A** — MATCH did not find the value (extra spaces, text vs number) or the last argument was omitted, so MATCH ran an approximate search. **Fix:** Use 0 as the third MATCH argument and clean the data with TRIM / VALUE.
- **Wrong row returned** — The INDEX range and the MATCH range start on different rows, e.g. A1:A6 vs C2:C6. **Fix:** Make both ranges start and end on the same rows.
- **#REF!** — The row or column number from MATCH is larger than the INDEX range. **Fix:** Make the INDEX range at least as large as the ranges searched by MATCH.

<!--CTA_AFTER_ERRORS-->

## FAQ

### Why use INDEX MATCH instead of VLOOKUP?

It can return a column to the left, it does not depend on a hard-coded column number, and it only reads the two columns it needs.

### Is INDEX MATCH faster than XLOOKUP?

The difference is negligible on normal-sized sheets. Choose XLOOKUP for readability in Microsoft 365 and Google Sheets, and INDEX MATCH for compatibility with older Excel.

### When is INDEX MATCH better than VLOOKUP?

When the value you want is to the left of the column you search, or when you do not want a hard-coded column number. The country example on this page looks up the code CA in column C and returns Canada from column A. VLOOKUP cannot do that. See the left-lookup section above.

## Related formulas

<!--RELATED-->
