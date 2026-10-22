---
title: How to Add Leading Zeros in Excel
slug: leading-zeros-excel
date: '2026-10-22'
summary: Pad numbers with zeros to a fixed length, such as 00042 for employee IDs
  or ZIP codes. Choose between a custom number format (value stays a number) and TEXT
  or RIGHT formulas (value becomes text), and learn how to stop the zeros disappearing
  in the first place.
tags:
- Text formulas
- Excel
keyword: leading-zeros-excel
niche: sheets-formulas
provider: structured
entry_id: leading-zeros
platform: Excel
category: text
faq:
- q: Format or formula, which should I use?
  a: Use a custom number format if the values are numbers you calculate with. Use
    TEXT/RIGHT if you need text, for example for an export or for joining with other
    text.
- q: How do I pad to a variable length?
  a: Use =REPT("0", n-LEN(A2))&A2, where n is the target length.
related:
- - trim-excel
  - trim-google-sheets
- - textjoin-excel
  - textjoin-google-sheets
- - value-error-excel
  - value-error-google-sheets
- - na-error-excel
  - na-error-google-sheets
sibling: leading-zeros-google-sheets
---
Pad numbers with zeros to a fixed length, such as 00042 for employee IDs or ZIP codes. Choose between a custom number format (value stays a number) and TEXT or RIGHT formulas (value becomes text), and learn how to stop the zeros disappearing in the first place.

## Quick answer

Use this formula in Excel:

```excel
=TEXT(A2, "00000")
```

Each 0 in the format is a required digit, so the number is padded to five digits. The result is text.

## The problem

Employee numbers must always have five digits for an import file, but the sheet shows 7, 42 and 315 because spreadsheets drop leading zeros from numbers.

## Worked example

Pad employee numbers to five digits.

| | A | B | C |
|---|---|---|---|
| 1 | **Employee no.** | **TEXT** | **RIGHT** |
| 2 | 7 | **00007** | **00007** |
| 3 | 42 | **00042** | **00042** |
| 4 | 315 | **00315** | **00315** |
| 5 | 1208 | **01208** | **01208** |

Formulas used in the example (results shown in **bold** in the table above):

**B2 (filled to B5)** — filled down

```excel
=TEXT(A2, "00000")
```

Results: **00007**, **00042**, **00315**, **01208**

**C2 (filled to C5)** — filled down

```excel
=RIGHT("00000"&A2, 5)
```

Results: **00007**, **00042**, **00315**, **01208**

<!--AD_IN_ARTICLE-->

## How the formula works

1. TEXT converts the number using the format "00000": every 0 is a digit placeholder that shows 0 if there is no digit.
2. RIGHT version: "00000"&A2 creates "0000042", and RIGHT(..., 5) keeps the last five characters, "00042".
3. Both results are text. Use a custom number format instead if the column must stay numeric.
4. Numbers longer than five digits are not truncated by TEXT, but RIGHT would cut them, so pick the length to match your longest ID.

## Excel-specific notes

If you only need the zeros to show, apply a custom number format instead: select the cells, press Ctrl+1, choose Custom and type 00000. The cells stay numbers, so they still sort and calculate correctly. To keep zeros when typing, format the column as Text first or start the entry with an apostrophe ('00042). In Microsoft 365, File > Options > Data > Automatic data conversion lets you stop Excel from removing leading zeros when opening CSV files.

**Padding with RIGHT (works for text IDs too)**

```excel
=RIGHT("00000"&A2, 5)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=TEXT(A2, "00000")
```

The same TEXT formula works in Google Sheets; the display-only version is under Format > Number > Custom number format.

<!--SIBLING-->


## Common errors and how to fix them

- **Zeros disappear after typing** — The cell is formatted as a number, which has no leading zeros. **Fix:** Format as Text before typing, use an apostrophe, or use a custom number format.
- **Lookups fail after padding** — The padded value is text and the lookup table contains numbers (or vice versa). **Fix:** Pad both sides, or compare with VALUE().
- **Zeros lost when the CSV is reopened** — CSV files store no formatting; the app converts 00042 to 42 when opening. **Fix:** Import with Data > From Text/CSV (Excel) or untick conversion in File > Import (Sheets) and set the column to Text.

## FAQ

### Format or formula, which should I use?

Use a custom number format if the values are numbers you calculate with. Use TEXT/RIGHT if you need text, for example for an export or for joining with other text.

### How do I pad to a variable length?

Use =REPT("0", n-LEN(A2))&A2, where n is the target length.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
