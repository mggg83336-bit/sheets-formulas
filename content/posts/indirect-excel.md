---
title: How to Use INDIRECT to Build a Reference from Text in Excel
slug: indirect-excel
date: '2026-11-11'
summary: INDIRECT turns a text string into a live cell or range reference, so a drop-down
  can pick a sheet, a row number can build an address, or a stored A1/R1C1 string
  can be evaluated. It is volatile and will not read a closed Excel workbook. Google
  Sheets uses the same function for in-file references, bu
tags:
- Lookup & reference
- Excel
keyword: indirect-excel
niche: sheets-formulas
provider: structured
entry_id: indirect
platform: Excel
category: lookup
faq:
- q: When should I use INDIRECT rather than INDEX or a normal sheet reference?
  a: Use INDIRECT when the address itself arrives as text — a drop-down of tab names,
    a cell that stores “B8”, or a row and column number you want to read as R1C1.
    If you already know the sheet and only the row changes, INDEX (or a regular 'Rate
    Table'!B3) is simpler and is not volatile.
- q: How do I quote a sheet name that contains a space?
  a: 'Wrap the name in single quotes inside the text you pass to INDIRECT: =INDIRECT("''"&A1&"''!B3")
    when A1 holds Rate Table. Quotes are optional for a simple name such as Rates,
    but they never hurt. Google Sheets tab names are also case-sensitive.'
- q: Can INDIRECT read another workbook or another Google spreadsheet?
  a: 'In desktop Excel, only while that workbook is open; a closed file is #REF!,
    and Excel for the web does not support the case. Google Sheets cannot do it at
    all. Use IMPORTRANGE with the other file’s URL and a range string, and click Allow
    access the first time.'
- q: What does the second argument do?
  a: 'TRUE or omitted means the text is A1 style (B8 or ''Rate Table''!B3). FALSE
    means R1C1 style (R8C2). Mixing the two — for example passing B8 with FALSE —
    returns #REF!.'
related:
- - vlookup-excel
  - vlookup-google-sheets
- - index-match-excel
  - index-match-google-sheets
- - vlookup-another-sheet-excel
  - vlookup-another-sheet-google-sheets
- - last-value-excel
  - last-value-google-sheets
sibling: indirect-google-sheets
---
INDIRECT turns a text string into a live cell or range reference, so a drop-down can pick a sheet, a row number can build an address, or a stored A1/R1C1 string can be evaluated. It is volatile and will not read a closed Excel workbook. Google Sheets uses the same function for in-file references, but another spreadsheet file needs IMPORTRANGE, not INDIRECT.

## Quick answer

Use this formula in Excel:

```excel
=INDIRECT("'"&B3&"'!B3")
```

Syntax: `INDIRECT(ref_text, [a1])`. `ref_text` is an address, a sheet-qualified address, or a defined name, written as text. When `a1` is TRUE or omitted the text is A1 style (`B8`, `'Rate Table'!B3`); when FALSE it is R1C1 style (`R8C2`). Sheet names that contain a space must be wrapped in single quotes inside the string.

## The problem

You want one formula that can follow an address typed in a cell, pull a rate from a tab whose name sits in a drop-down, and also understand an R1C1-style address built from a row number and a column number. The reference should update when those inputs change, without rewriting the formula.

## Worked example

B2 holds the text address B8, B3 holds the tab name Rate Table, and B4/B5 are a row and column number. B8 is the posted amount 250. Each result cell builds a reference from those inputs. The Rate Table tab holds three bands and rates.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Item** | **Value** |  | **Result** | **Amount** |
| 2 | Address text | B8 |  | From address text | **250** |
| 3 | Tab name | Rate Table |  | From chosen tab | **0.22** |
| 4 | Row number | 8 |  | R1C1 from row and column | **250** |
| 5 | Column number | 2 |  | Built A1 address | **250** |
| 6 |  |  |  | Sum of rates | **0.68** |
| 7 |  |  |  |  |  |
| 8 | Posted amount | 250 |  |  |  |

Sheet **Rate Table**:

| | A | B |
|---|---|---|
| 1 | Band | Rate |
| 2 | Standard | 0.15 |
| 3 | Priority | 0.22 |
| 4 | Express | 0.31 |

Formulas used in the example (results shown in **bold** in the table above):

**E2** — INDIRECT of the address stored in B2

```excel
=INDIRECT(B2)
```

Result: **250**

**E3** — Priority rate on the chosen tab

```excel
=INDIRECT("'"&B3&"'!B3")
```

Result: **0.22**

**E4** — R1C1 reference built from B4 and B5

```excel
=INDIRECT("R"&B4&"C"&B5, FALSE)
```

Result: **250**

**E5** — A1 address built from a row number

```excel
=INDIRECT("B"&B4)
```

Result: **250**

**E6** — sum of the three rates on Rate Table

```excel
=SUM(INDIRECT("'"&B3&"'!B2:B4"))
```

Result: **0.68**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `=INDIRECT(B2)` reads the text `B8` and returns the posted amount in B8, 250. Changing B2 to another address is enough to point the formula somewhere else.
2. To reach another tab, join the name, an exclamation mark, and the cell. Because Rate Table contains a space, the name is quoted: `=INDIRECT("'"&B3&"'!B3")` returns 0.22, the Priority rate on that sheet.
3. R1C1 is useful when you have numbers instead of a column letter. `=INDIRECT("R"&B4&"C"&B5, FALSE)` with row 8 and column 2 is the same as B8 and also returns 250. The FALSE argument is required; without it the text would be read as A1 and fail.
4. `=INDIRECT("B"&B4)` builds the A1 form of the same address from the row number alone. `=SUM(INDIRECT("'"&B3&"'!B2:B4"))` uses the same quoting pattern on a range and adds 0.15 + 0.22 + 0.31 = 0.68.
5. When INDIRECT is only selecting a row in a known column, `=INDEX(B:B, B4)` does the same job without volatility. Keep INDIRECT for cases the address really does come in as text — a sheet name from a drop-down, a stored A1 string, or R1C1 pieces.

## Excel-specific notes

INDIRECT is the usual way to let a drop-down choose a tab (`=INDIRECT("'"&B3&"'!B3")`) or to build a cell from pieces (`=INDIRECT("B"&B4)`). Because the address is text, inserting rows will not shift it the way a normal `=B8` reference would — that is either the point, or a silent footgun, depending on what you wanted. The function is volatile and recalculates with every workbook change, so a column of INDIRECT calls over large ranges can slow a model; if the address is known and only the row or column varies, INDEX is often cheaper (`=INDEX(B:B, B4)`). Named ranges work: if `Rates` is a defined name, `=SUM(INDIRECT("Rates"))` follows it. External references are the sharp edge: `=INDIRECT("'[Budget.xlsx]Sheet1'!A1")` calculates only while Budget.xlsx is open in the same Excel session; a closed workbook returns `#REF!`, and Excel for the web does not support that external case at all. Prefer a direct link, Power Query, or (when you only need a tab in *this* file) a straight `'Rate Table'!B3` without INDIRECT. `#REF!` also appears when the sheet name is misspelled, the quotes are missing around a spaced name, or R1C1 text is parsed as A1 (or the other way around).

**Address sitting in a cell**

```excel
=INDIRECT(B2)
```

**Built A1 address from a row number**

```excel
=INDIRECT("B"&B4)
```

**R1C1 address from row and column numbers**

```excel
=INDIRECT("R"&B4&"C"&B5, FALSE)
```

**INDEX when only the row changes (non-volatile)**

```excel
=INDEX(B:B, B4)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=INDIRECT("'"&B3&"'!B3")
```

Excel uses the same in-file INDIRECT formulas but has no open-ended B2:B range and no IMPORTRANGE. It can read another *open* workbook with INDIRECT; Sheets never can.

<!--SIBLING-->


## Common errors and how to fix them

- **#REF!** — The text is not a valid address — a typo, a missing `!`, missing quotes around a sheet name that has a space, a deleted or renamed tab, R1C1 text parsed as A1, or (Excel) a closed external workbook. **Fix:** Build the string in a helper cell and inspect it. Quote spaced names as `"'"&B3&"'!B3"`. For another Google Sheets file use IMPORTRANGE, not INDIRECT. For another Excel workbook, open it or use a direct link instead.
- **The formula does not follow inserted rows** — The address is text (`"B8"`), so Excel and Sheets will not shift it when you insert or delete rows the way a normal `=B8` reference would. **Fix:** If you want the reference to travel with the cell, use a regular reference or INDEX on a range. Use INDIRECT only when you want the address to stay exactly as written.
- **ARRAYFORMULA + INDIRECT returns the same cell on every row, or `#REF!`** — In Google Sheets, INDIRECT inside ARRAYFORMULA is evaluated once and does not build a different address per row. **Fix:** Use MAP/LAMBDA in current Sheets, or a helper column with one INDIRECT per row. INDEX or FILTER is often cleaner if you do not actually need a text address.
- **The workbook became slow** — INDIRECT is volatile, so a long column of constructed references recalculates on every change. **Fix:** Switch to INDEX, a direct sheet reference, or a defined name wherever the address does not have to be built from text.

## FAQ

### When should I use INDIRECT rather than INDEX or a normal sheet reference?

Use INDIRECT when the address itself arrives as text — a drop-down of tab names, a cell that stores “B8”, or a row and column number you want to read as R1C1. If you already know the sheet and only the row changes, INDEX (or a regular `'Rate Table'!B3`) is simpler and is not volatile.

### How do I quote a sheet name that contains a space?

Wrap the name in single quotes inside the text you pass to INDIRECT: `=INDIRECT("'"&A1&"'!B3")` when A1 holds Rate Table. Quotes are optional for a simple name such as Rates, but they never hurt. Google Sheets tab names are also case-sensitive.

### Can INDIRECT read another workbook or another Google spreadsheet?

In desktop Excel, only while that workbook is open; a closed file is `#REF!`, and Excel for the web does not support the case. Google Sheets cannot do it at all. Use IMPORTRANGE with the other file’s URL and a range string, and click Allow access the first time.

### What does the second argument do?

TRUE or omitted means the text is A1 style (`B8` or `'Rate Table'!B3`). FALSE means R1C1 style (`R8C2`). Mixing the two — for example passing `B8` with FALSE — returns `#REF!`.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
