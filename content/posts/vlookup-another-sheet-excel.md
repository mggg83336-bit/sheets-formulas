---
title: VLOOKUP from Another Sheet in Excel
slug: vlookup-another-sheet-excel
date: '2026-10-22'
summary: 'To look up a value on a different tab, put the sheet name and an exclamation
  mark in front of the range. This guide shows the exact quoting rules for sheet names
  with spaces, how to point at another file, and why the result sometimes turns into
  #REF!.'
tags:
- Lookup & reference
- Excel
keyword: vlookup-another-sheet-excel
niche: sheets-formulas
provider: structured
entry_id: vlookup-another-sheet
platform: Excel
category: lookup
faq:
- q: Do I need quotes around the sheet name?
  a: Only when the name contains spaces or special characters, but quotes never hurt,
    so 'Prices'!A2:C5 also works.
- q: Can VLOOKUP search several sheets at once?
  a: Not by itself. Nest lookups with IFNA, e.g. =IFNA(VLOOKUP(B2,Sheet1!A:C,3,FALSE),
    VLOOKUP(B2,Sheet2!A:C,3,FALSE)), or combine the sheets first (VSTACK in Excel
    365 and Google Sheets).
related:
- - vlookup-excel
  - vlookup-google-sheets
- - xlookup-excel
  - xlookup-google-sheets
- - na-error-excel
  - na-error-google-sheets
- - trim-excel
  - trim-google-sheets
- - index-match-excel
  - index-match-google-sheets
- - ref-error-excel
  - ref-error-google-sheets
sibling: vlookup-another-sheet-google-sheets
---
To look up a value on a different tab, put the sheet name and an exclamation mark in front of the range. This guide shows the exact quoting rules for sheet names with spaces, how to point at another file, and why the result sometimes turns into #REF!.

## Quick answer

Use this formula in Excel:

```excel
=VLOOKUP(B2, 'Price List'!$A$2:$C$5, 3, FALSE)
```

`'Price List'!$A$2:$C$5` means range A2:C5 on the tab named Price List. The single quotes are required because the name contains a space.

<!--CTA_PROMINENT-->

## VLOOKUP from another workbook

A different file uses the workbook name in square brackets, then the sheet:

```excel
=VLOOKUP(B2, '[Prices.xlsx]Price List'!$A$2:$C$100, 3, FALSE)
```

Quote the whole `[workbook]sheet` name when the sheet name has a space. Lock the table with `$` so filling the formula down does not walk off the price list.

- **Closed workbook.** Desktop Excel keeps the last saved values for an external link. If the link is broken, the sheet was renamed, or Excel asks you to update values, the lookup returns #N/A or #REF! until you open Prices.xlsx or repair the path. Use Data > Edit Links > Update Values. A formula that names a sheet which is not in any open workbook makes Excel ask you to pick a file.
- **The path is part of the formula.** After you close the source file, Excel rewrites the reference to include the drive and folder. Moving either file breaks that path. Edit Links is where you point it at the new location.
- **Excel for the web and Google Sheets** do not calculate a closed .xlsx on your computer. For another Google Sheets file, use IMPORTRANGE, shown on the Sheets version of this guide.

The same brackets work with [XLOOKUP](../xlookup-excel/): one range for the lookup column and one for the prices, both starting with `'[Prices.xlsx]Price List'!`. A #N/A that survives opening the file is usually text versus numbers or stray spaces, covered under [the #N/A error](../na-error-excel/).

## VLOOKUP not working between sheets

Work down this list when the formula was fine on one tab and fails as soon as the range points at another.

1. **Sheet name with spaces or punctuation.** `Price List` must be quoted: `'Price List'!$A$2:$C$100`. A hyphen, or a name that starts with a number, needs quotes too. A simple name (`Prices!A2:C100`) does not. If Excel opens an Update values dialog, the name in the formula does not match any tab in an open workbook.
2. **Absolute references.** Filling down without dollar signs shifts the table onto the wrong rows. Lock it: `$A$2:$C$100`. Leave the lookup cell (B2) relative so each order row looks up its own SKU.
3. **Closed workbook.** If the source file is closed and the result is #N/A, #REF!, or an Update values prompt, open the file or fix the link. Details are in the workbook section above.
4. **Exact match.** The last argument must be FALSE. Leaving it out runs an approximate match on the other sheet and can return the wrong price with no error.
5. **Text, spaces, and numbers.** A SKU that looks the same can still fail. [TRIM](../trim-excel/) removes ordinary spaces. [How to fix #N/A](../na-error-excel/) covers numbers stored as text.
6. **Column index.** 3 means the third column of the range on the other sheet, counting from the first column of that range, not from column A of the sheet.

## The problem

Your orders are on one tab and the price list lives on a separate tab called "Price List". You want each order row to pull its unit price from that tab automatically.

## Worked example

The Orders tab (below) looks up each SKU on the Price List tab.

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **Order** | **SKU** | **Qty** | **Unit price** |
| 2 | 1001 | SKU-03 | 2 | **12** |
| 3 | 1002 | SKU-01 | 10 | **3.5** |
| 4 | 1003 | SKU-04 | 25 | **1.8** |

Sheet **Price List**:

| | A | B | C |
|---|---|---|---|
| 1 | SKU | Description | Unit Price |
| 2 | SKU-01 | Notebook | 3.5 |
| 3 | SKU-02 | Pen pack | 4.25 |
| 4 | SKU-03 | Stapler | 12 |
| 5 | SKU-04 | Folder | 1.8 |

Formulas used in the example (results shown in **bold** in the table above):

**D2 (filled to D4)** — filled down to D4

```excel
=VLOOKUP(B2, 'Price List'!$A$2:$C$5, 3, FALSE)
```

Results: **12**, **3.5**, **1.8**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `B2` is the SKU on the current (Orders) tab.
2. `'Price List'!` switches the reference to the other tab. Use quotes whenever the tab name has a space, hyphen or starts with a number; quotes are optional for simple names like Prices!A2:C5.
3. `$A$2:$C$5` is locked with dollar signs so it stays the same when you fill the formula down.
4. `3, FALSE` returns the third column (Unit Price) with an exact match.

## Excel-specific notes

The easiest way to get the reference right is to type `=VLOOKUP(B2,` then click the other tab and select the range; Excel writes the quotes for you. To look up from another workbook, the reference includes the file name in square brackets, for example `'[Prices.xlsx]Price List'!$A$2:$C$5`. While the source file is closed Excel stores the full path and shows the last saved values; open it and refresh with Data > Edit Links if values look stale.

**Lookup from another workbook**

```excel
=VLOOKUP(B2, '[Prices.xlsx]Price List'!$A$2:$C$5, 3, FALSE)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=VLOOKUP(B2, 'Price List'!$A$2:$C$5, 3, FALSE)
```

Google Sheets uses the same tab reference. For another file, wrap the range in IMPORTRANGE("file URL", "Price List!A2:C5") and click Allow access once.

<!--SIBLING-->


## Common errors and how to fix them

- **#REF!** — The tab was renamed in a way the formula could not follow, the tab was deleted, or (Google Sheets) IMPORTRANGE access has not been granted yet. **Fix:** Re-select the range on the correct tab, or click Allow access on the IMPORTRANGE cell.
- **Excel asks you to pick a file / "Update values" dialog** — The tab name in the formula does not exist, so Excel thinks it is an external file. **Fix:** Check the spelling of the tab name and the quotes, or build the reference by clicking.
- **#N/A** — The SKU is not found on the other tab (spaces, different case of codes, number vs text). **Fix:** Compare the two values with =B2='Price List'!A2 and clean with TRIM or VALUE.

<!--CTA_AFTER_ERRORS-->

## FAQ

### Do I need quotes around the sheet name?

Only when the name contains spaces or special characters, but quotes never hurt, so 'Prices'!A2:C5 also works.

### Can VLOOKUP search several sheets at once?

Not by itself. Nest lookups with IFNA, e.g. =IFNA(VLOOKUP(B2,Sheet1!A:C,3,FALSE), VLOOKUP(B2,Sheet2!A:C,3,FALSE)), or combine the sheets first (VSTACK in Excel 365 and Google Sheets).

## Related formulas

<!--RELATED-->
