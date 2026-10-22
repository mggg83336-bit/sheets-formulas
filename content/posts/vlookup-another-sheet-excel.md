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
- - index-match-excel
  - index-match-google-sheets
- - ref-error-excel
  - ref-error-google-sheets
- - na-error-excel
  - na-error-google-sheets
sibling: vlookup-another-sheet-google-sheets
---
To look up a value on a different tab, put the sheet name and an exclamation mark in front of the range. This guide shows the exact quoting rules for sheet names with spaces, how to point at another file, and why the result sometimes turns into #REF!.

## Quick answer

Use this formula in Excel:

```excel
=VLOOKUP(B2, 'Price List'!$A$2:$C$5, 3, FALSE)
```

`'Price List'!$A$2:$C$5` means range A2:C5 on the tab named Price List. The single quotes are required because the name contains a space.

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

## FAQ

### Do I need quotes around the sheet name?

Only when the name contains spaces or special characters, but quotes never hurt, so 'Prices'!A2:C5 also works.

### Can VLOOKUP search several sheets at once?

Not by itself. Nest lookups with IFNA, e.g. =IFNA(VLOOKUP(B2,Sheet1!A:C,3,FALSE), VLOOKUP(B2,Sheet2!A:C,3,FALSE)), or combine the sheets first (VSTACK in Excel 365 and Google Sheets).

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
