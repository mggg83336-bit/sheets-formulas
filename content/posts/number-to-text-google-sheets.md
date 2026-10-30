---
title: How to Convert Numbers to Text in Google Sheets
slug: number-to-text-google-sheets
date: '2026-10-30'
summary: Converting a number to text lets you keep leading zeros, show a fixed number
  of decimals, add thousands separators or a currency sign, and join numbers into
  sentences without losing the formatting. TEXT and the &"" trick work in Excel and
  Google Sheets; Sheets also has TO_TEXT, and Excel 365 has VAL
tags:
- Text formulas
- Google Sheets
keyword: number-to-text-google-sheets
niche: sheets-formulas
provider: structured
entry_id: number-to-text
platform: Google Sheets
category: text
faq:
- q: Is formatting a cell the same as converting the number to text?
  a: No. Cell formatting changes only the display. The value stays a number. TEXT
    and &"" create a real text value.
- q: How do I join a number to text and keep two decimals?
  a: 'Use TEXT inside the join: ="Total: "&TEXT(A2, "#,##0.00").'
- q: How do I convert text back to a number?
  a: Use VALUE or the double minus, for example =VALUE(A2) or =--A2.
related:
- - text-to-number-google-sheets
  - text-to-number-excel
- - leading-zeros-google-sheets
  - leading-zeros-excel
- - concatenate-google-sheets
  - concatenate-excel
- - len-google-sheets
  - len-excel
sibling: number-to-text-excel
---
Converting a number to text lets you keep leading zeros, show a fixed number of decimals, add thousands separators or a currency sign, and join numbers into sentences without losing the formatting. TEXT and the &"" trick work in Excel and Google Sheets; Sheets also has TO_TEXT, and Excel 365 has VALUETOTEXT.

## Quick answer

Use this formula in Google Sheets:

```excel
=TEXT(A2, "00000")
```

TEXT works the same way in Google Sheets: "00000" pads 123 to the text 00123, and the other format codes add separators, decimals and currency signs.

## The problem

You need a number as text: an ID that must keep its leading zeros, a price shown as $1,250.50 inside a sentence, or a key that must match a text column in a lookup. Joining the number directly drops the formatting, and changing the cell format does not change the value.

## Worked example

Real numbers in column A converted to text in different layouts.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Number** | **Plain text** | **Padded** | **Formatted** | **Check** |
| 2 | 123 | **123** | **00123** |  | **TRUE** |
| 3 | 1250.5 |  |  | **$1,250.50** | **TRUE** |
| 4 | 1234567 |  |  | **1,234,567** |  |
| 5 | 0.256 |  |  | **Share: 25.6%** |  |

Formulas used in the example (results shown in **bold** in the table above):

**B2** — plain conversion

```excel
=A2&""
```

Result: **123**

**C2** — leading zeros

```excel
=TEXT(A2, "00000")
```

Result: **00123**

**D3** — currency

```excel
=TEXT(A3, "$#,##0.00")
```

Result: **$1,250.50**

**D4** — thousands separator

```excel
=TEXT(A4, "#,##0")
```

Result: **1,234,567**

**D5** — percentage inside a label

```excel
="Share: "&TEXT(A5, "0.0%")
```

Result: **Share: 25.6%**

**E2** — the result is text

```excel
=ISTEXT(C2)
```

Result: **TRUE**

**E3** — the source is still a number

```excel
=ISNUMBER(A3)
```

Result: **TRUE**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Decide how the text should look, for example five digits with leading zeros or a price with two decimals.
2. In a helper column type `=TEXT(A2, "00000")` and press Enter.
3. Change the format code as needed: "$#,##0.00" for currency, "#,##0" for thousands, "0.0%" for percentages.
4. For a plain conversion without formatting, use `=A2&""`.
5. Fill the formula down, and keep the original numbers for any calculations.

## Google Sheets-specific notes

Google Sheets has its own function for a plain conversion: `=TO_TEXT(A2)` returns the number as text and keeps the look of the cell format, so a cell showing $19.99 becomes the text "$19.99". The &"" trick also works. To convert a whole column use `=ARRAYFORMULA(IF(A2:A="", "", TEXT(A2:A, "00000")))`. If you type the values yourself, Format > Number > Plain text stores everything you enter as text, and an apostrophe in front of a single value (for example '00123) does the same. Remember that SUM and other math functions ignore the resulting text.

**Plain conversion with TO_TEXT**

```excel
=TO_TEXT(A2)
```

**Whole column with leading zeros**

```excel
=ARRAYFORMULA(IF(A2:A="", "", TEXT(A2:A, "00000")))
```

**Currency with thousands separator**

```excel
=TEXT(A2, "$#,##0.00")
```


## Excel version

The same formula works unchanged in Excel:

```excel
=TEXT(A2, "00000")
```

Google Sheets uses the same TEXT codes and the &"" trick, and adds TO_TEXT; it has no VALUETOTEXT.

<!--SIBLING-->


## Common errors and how to fix them

- **Leading zeros disappear** — The value was converted with &"" or typed as a number, which never stores leading zeros. **Fix:** Use TEXT with zeros in the code, for example `=TEXT(A2, "00000")`.
- **SUM of the converted column is 0** — The converted values are text, and SUM ignores text. **Fix:** Sum the original numbers instead, or convert back with VALUE.
- **Lookup still does not match** — One side is text and the other a number, or the text has a different number of digits. **Fix:** Convert both sides the same way, for example TEXT(A2, "00000") on both, or use VALUE on the text side.

## FAQ

### Is formatting a cell the same as converting the number to text?

No. Cell formatting changes only the display. The value stays a number. TEXT and &"" create a real text value.

### How do I join a number to text and keep two decimals?

Use TEXT inside the join: `="Total: "&TEXT(A2, "#,##0.00")`.

### How do I convert text back to a number?

Use VALUE or the double minus, for example =VALUE(A2) or =--A2.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
