---
title: How to Use the MATCH Function in Excel
slug: match-excel
date: '2026-11-13'
summary: MATCH returns the position of a value in a row or column, not the value itself.
  Use match type 0 for an exact match, 1 for the largest value less than or equal
  to the lookup in an ascending list, and -1 for the smallest value greater than or
  equal to it in a descending list. Pair MATCH with INDEX to
tags:
- Lookup & reference
- Excel
keyword: match-excel
niche: sheets-formulas
provider: structured
entry_id: match
platform: Excel
category: lookup
faq:
- q: What is the difference between MATCH and XMATCH?
  a: MATCH defaults to an approximate match (type 1) if you omit the last argument,
    which is a frequent source of wrong results. XMATCH defaults to an exact match
    and can search from the last item first. Use MATCH when the file must open in
    older Excel; otherwise XMATCH or XLOOKUP is safer.
- q: Does MATCH return the worksheet row number?
  a: No. It returns the position inside the lookup array. If the array is B2:B6 and
    the match is in B3, the result is 2. Add ROW(B2)-1 only when you deliberately
    want a worksheet row, and prefer INDEX MATCH when the goal is to return a value.
- q: Is MATCH case-sensitive?
  a: No. In Excel and Google Sheets, "a15" and "A15" are treated as the same text.
    To force a case-sensitive search, a common workaround is to combine EXACT with
    an array formula, or to use a helper column.
- q: Can MATCH look up a value to the left?
  a: MATCH only returns a position. To return a value from any column, wrap it in
    INDEX, as in the worked example, or use XLOOKUP or VLOOKUP when the return column
    sits to the right of the search column.
related:
- - index-match-excel
  - index-match-google-sheets
- - xlookup-excel
  - xlookup-google-sheets
- - vlookup-excel
  - vlookup-google-sheets
- - hlookup-excel
  - hlookup-google-sheets
- - na-error-excel
  - na-error-google-sheets
- - iferror-excel
  - iferror-google-sheets
sibling: match-google-sheets
---
MATCH returns the position of a value in a row or column, not the value itself. Use match type 0 for an exact match, 1 for the largest value less than or equal to the lookup in an ascending list, and -1 for the smallest value greater than or equal to it in a descending list. Pair MATCH with INDEX to return a related cell, or use it alone when you need a position to feed into another function. The same syntax works in Excel and Google Sheets; Microsoft 365 and current Sheets also offer XMATCH, which defaults to an exact match and can search from the end of the list.

## Quick answer

Use this formula in Excel:

```excel
=MATCH(D2, B2:B6, 0)
```

Syntax: `MATCH(lookup_value, lookup_array, [match_type])`. With D2 equal to A15, MATCH searches B2:B6 and returns 2 because A15 is the second code. Always pass 0 as the third argument for an exact match. If you omit it, Excel defaults to 1 and assumes the list is sorted ascending, which silently returns the wrong position on an unsorted list.

## The problem

You have a list of product codes and quantities and need the position of a typed code so you can hand it to INDEX, a wildcard search for the first code that starts with a given letter, and an approximate match on a descending quantity list.

## Worked example

Five products with codes and quantities. D2 holds the code A15. E2 returns its position in the code list, E3 the item name, E4 the position of the first code starting with B, and E5 an approximate match for a quantity of 20 on the descending quantity column.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Item** | **Code** | **Qty** | **Lookup** | **Result** |
| 2 | Apples | A12 | 40 | A15 | **2** |
| 3 | Bananas | A15 | 22 |  | **Bananas** |
| 4 | Cherries | B03 | 18 |  | **3** |
| 5 | Dates | B07 | 12 |  | **2** |
| 6 | Figs | C01 | 8 |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**E2** — position of code A15 in B2:B6

```excel
=MATCH(D2, B2:B6, 0)
```

Result: **2**

**E3** — item name for that code, via INDEX

```excel
=INDEX(A2:A6, MATCH(D2, B2:B6, 0))
```

Result: **Bananas**

**E4** — first code that starts with B

```excel
=MATCH("B*", B2:B6, 0)
```

Result: **3**

**E5** — smallest quantity greater than or equal to 20 (descending list)

```excel
=MATCH(20, C2:C6, -1)
```

Result: **2**

<!--AD_IN_ARTICLE-->

## How the formula works

1. D2 holds the code A15. `=MATCH(D2, B2:B6, 0)` searches the code column and returns 2, because A15 is the second item in B2:B6, not because it sits in worksheet row 3.
2. `=INDEX(A2:A6, MATCH(D2, B2:B6, 0))` uses that position to return Bananas from the Item column. This is the standard [INDEX MATCH](../index-match-excel/) left lookup.
3. With match type 0 you can also use wildcards. `=MATCH("B*", B2:B6, 0)` finds the first code that starts with B, which is B03 in the third position.
4. The quantity column C2:C6 is already in descending order (40, 22, 18, 12, 8). `=MATCH(20, C2:C6, -1)` returns 2, the position of 22, which is the smallest quantity greater than or equal to 20.
5. If the code is missing, MATCH returns [#N/A](../na-error-excel/). Wrap the formula in [IFERROR](../iferror-excel/) or IFNA when you want a blank or a custom message instead. For a single-step lookup in Microsoft 365 or current Sheets, [XLOOKUP](../xlookup-excel/) is usually clearer than MATCH on its own.

## Excel-specific notes

MATCH is available in every Excel version. The number it returns is the position inside the lookup array, not the worksheet row: if the array is B2:B6 and the match is in B3, the result is 2, not 3. That relative position is what INDEX expects, which is why `=INDEX(A2:A6, MATCH(D2, B2:B6, 0))` is the classic left-lookup. Match type 0 also accepts the wildcards `*` (any run of characters) and `?` (one character), so `=MATCH("B*", B2:B6, 0)` finds the first code that starts with B. Types 1 and -1 are approximate: 1 needs an ascending list and returns the largest value less than or equal to the lookup; -1 needs a descending list and returns the smallest value greater than or equal to it. A missing exact match is `#N/A`. Text matches are case-insensitive. A common trap is a lookup array that is two-dimensional — MATCH needs a single row or a single column. In Microsoft 365, XMATCH is usually the better default because it is exact unless you ask otherwise, and it can search last-to-first. For a one-step return of a related value in 365, prefer XLOOKUP over INDEX+MATCH.

**Return the item name with INDEX**

```excel
=INDEX(A2:A6, MATCH(D2, B2:B6, 0))
```

**First code that starts with B (wildcard)**

```excel
=MATCH("B*", B2:B6, 0)
```

**Approximate match on a descending quantity list**

```excel
=MATCH(20, C2:C6, -1)
```

**Microsoft 365 XMATCH, exact by default**

```excel
=XMATCH(D2, B2:B6)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=MATCH(D2, B2:B6, 0)
```

Excel uses the same MATCH formula. Whole-column fills in Excel 365 spill from a range of lookups; in Sheets you wrap MATCH in ARRAYFORMULA. XMATCH needs Microsoft 365 in Excel, and is available in current Sheets.

<!--SIBLING-->


## Common errors and how to fix them

- **#N/A** — No exact match was found, or the third argument was omitted so MATCH ran an approximate search on an unsorted list and could not settle on a value. **Fix:** Pass 0 as the match type for an exact match. Clean extra spaces with TRIM, and make sure the lookup and the list are the same type (both text or both numbers).
- **The wrong position, or a match from the wrong row** — The default match type 1 was used on an unsorted list, or the MATCH range and the INDEX range start on different rows. **Fix:** Always use 0 unless you truly want an approximate match on a sorted list. Keep the MATCH array and the INDEX array aligned on the same rows or columns.
- **#N/A on a wildcard such as "B*"** — Wildcards only work with match type 0. Type 1 or -1 treats `*` as a literal character. **Fix:** Use `=MATCH("B*", B2:B6, 0)`. For a search from the end of the list, switch to XMATCH.
- **#VALUE! or a two-dimensional range that will not match** — The lookup array is a block (more than one row and one column). MATCH can search a single row or a single column only. **Fix:** Point MATCH at one row or one column, such as B2:B6 or B1:F1, not B2:C6.

## FAQ

### What is the difference between MATCH and XMATCH?

MATCH defaults to an approximate match (type 1) if you omit the last argument, which is a frequent source of wrong results. XMATCH defaults to an exact match and can search from the last item first. Use MATCH when the file must open in older Excel; otherwise XMATCH or [XLOOKUP](../xlookup-excel/) is safer.

### Does MATCH return the worksheet row number?

No. It returns the position inside the lookup array. If the array is B2:B6 and the match is in B3, the result is 2. Add `ROW(B2)-1` only when you deliberately want a worksheet row, and prefer [INDEX MATCH](../index-match-excel/) when the goal is to return a value.

### Is MATCH case-sensitive?

No. In Excel and Google Sheets, "a15" and "A15" are treated as the same text. To force a case-sensitive search, a common workaround is to combine EXACT with an array formula, or to use a helper column.

### Can MATCH look up a value to the left?

MATCH only returns a position. To return a value from any column, wrap it in INDEX, as in the worked example, or use [XLOOKUP](../xlookup-excel/) or [VLOOKUP](../vlookup-excel/) when the return column sits to the right of the search column.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
