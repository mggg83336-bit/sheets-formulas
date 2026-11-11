---
title: How to Use INDIRECT to Build a Reference from Text in Google Sheets
slug: indirect-google-sheets
date: '2026-11-11'
summary: INDIRECT turns a text string into a live cell or range reference, so a drop-down
  can pick a sheet, a row number can build an address, or a stored A1/R1C1 string
  can be evaluated. It is volatile and will not read a closed Excel workbook. Google
  Sheets uses the same function for in-file references, bu
tags:
- Lookup & reference
- Google Sheets
keyword: indirect-google-sheets
niche: sheets-formulas
provider: structured
entry_id: indirect
platform: Google Sheets
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
- - vlookup-google-sheets
  - vlookup-excel
- - index-match-google-sheets
  - index-match-excel
- - vlookup-another-sheet-google-sheets
  - vlookup-another-sheet-excel
- - last-value-google-sheets
  - last-value-excel
sibling: indirect-excel
---
INDIRECT turns a text string into a live cell or range reference, so a drop-down can pick a sheet, a row number can build an address, or a stored A1/R1C1 string can be evaluated. It is volatile and will not read a closed Excel workbook. Google Sheets uses the same function for in-file references, but another spreadsheet file needs IMPORTRANGE, not INDIRECT.

## Quick answer

Use this formula in Google Sheets:

```excel
=INDIRECT("'"&B3&"'!B3")
```

Same idea in Google Sheets: `INDIRECT(cell_reference_as_string, [is_A1_notation])` turns text into a reference. Omit the second argument (or pass TRUE) for A1 style; pass FALSE for R1C1. Quote sheet names that contain a space.

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

## Google Sheets-specific notes

In-file INDIRECT behaviour matches Excel for A1, R1C1, and quoted sheet names, with two Sheets-specific rules. First, tab names are case-sensitive: `Rate Table` and `rate table` are not interchangeable, and a mismatched INDIRECT string returns `#REF!`. Second, Sheets accepts open-ended ranges that Excel does not, so `=SUM(INDIRECT("'"&B3&"'!B2:B"))` can grow with the column — keep an eye on trailing totals. INDIRECT cannot read another Google spreadsheet or a closed .xlsx; put the file URL and a range string in IMPORTRANGE instead (`=IMPORTRANGE("https://docs.google.com/spreadsheets/d/FILE_ID", B3&"!B3")`). The range argument is already text, so wrapping IMPORTRANGE in INDIRECT is almost never required. A well-known limitation is that INDIRECT inside ARRAYFORMULA does not evaluate a different address per row; use a MAP/LAMBDA in current Sheets, or a helper column of ordinary INDIRECT formulas. INDIRECT is still volatile, so a heavy dashboard of constructed references will recalc often. If Excel collaborators will open the file, stay with closed ranges and skip IMPORTRANGE and MAP.

**Open-ended sum on the chosen tab**

```excel
=SUM(INDIRECT("'"&B3&"'!B2:B"))
```

**Address sitting in a cell**

```excel
=INDIRECT(B2)
```

**R1C1 address from row and column numbers**

```excel
=INDIRECT("R"&B4&"C"&B5, FALSE)
```

**Value from another Google Sheets file**

```excel
=IMPORTRANGE("https://docs.google.com/spreadsheets/d/FILE_ID", B3&"!B3")
```


## Excel version

The same formula works unchanged in Excel:

```excel
=INDIRECT("'"&B3&"'!B3")
```

Google Sheets uses the same INDIRECT syntax for tabs in this file, including R1C1. It cannot reach another spreadsheet; use IMPORTRANGE, which already takes the range as text. Sheets also allows open-ended addresses such as `'Rate Table'!B2:B`.

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
