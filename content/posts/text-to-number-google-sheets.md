---
title: How to Convert Text to Numbers in Google Sheets
slug: text-to-number-google-sheets
date: '2026-10-30'
summary: Numbers stored as text look normal but are ignored by SUM, break lookups
  and sort in the wrong order. VALUE, the double minus (--) and multiplying by 1 turn
  them back into real numbers. The formulas are the same in Excel and Google Sheets;
  Excel also offers a one-click Convert to Number fix, and She
tags:
- Text formulas
- Google Sheets
keyword: text-to-number-google-sheets
niche: sheets-formulas
provider: structured
entry_id: text-to-number
platform: Google Sheets
category: text
faq:
- q: How can I tell if a number is stored as text?
  a: Use =ISTEXT(A2) or =ISNUMBER(A2). Text numbers are left-aligned by default, and
    Excel marks them with a small green triangle.
- q: What is the difference between VALUE and the double minus?
  a: The result is the same. VALUE is easier to read; -- is shorter and common inside
    SUMPRODUCT and array formulas.
- q: How do I keep leading zeros?
  a: Do not convert those values. Codes such as 00123 are identifiers, not quantities,
    so leave them as text or format the number with a custom format like 00000.
related:
- - trim-google-sheets
  - trim-excel
- - substitute-google-sheets
  - substitute-excel
- - extract-numbers-google-sheets
  - extract-numbers-excel
- - len-google-sheets
  - len-excel
sibling: text-to-number-excel
---
Numbers stored as text look normal but are ignored by SUM, break lookups and sort in the wrong order. VALUE, the double minus (--) and multiplying by 1 turn them back into real numbers. The formulas are the same in Excel and Google Sheets; Excel also offers a one-click Convert to Number fix, and Sheets adds REGEXREPLACE for messy values.

## Quick answer

Use this formula in Google Sheets:

```excel
=VALUE(A2)
```

VALUE works the same way in Google Sheets: it converts the text in A2 to a real number and returns #VALUE! when the text is not a number.

## The problem

Data pasted from a website, CSV export or accounting system shows numbers aligned to the left, a green triangle in the corner, or a SUM that returns 0. The values are text, and you need real numbers you can add, compare and look up.

## Worked example

Column A holds numbers stored as text. SUM ignores them until they are converted.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Text value** | **VALUE** | **Double minus** | **Times 1** | **Totals** |
| 2 | 00123 | **123** |  |  | **0** |
| 3 | 1250.5 | **1250.5** |  | **1250.5** | **1419** |
| 4 | `" 42 "` | **42** |  |  |  |
| 5 | 3.5 |  | **3.5** |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**B2** — leading zeros dropped

```excel
=VALUE(A2)
```

Result: **123**

**B3** — decimal text

```excel
=VALUE(A3)
```

Result: **1250.5**

**B4** — trim spaces first

```excel
=VALUE(TRIM(A4))
```

Result: **42**

**C5** — double minus

```excel
=--A5
```

Result: **3.5**

**D3** — multiply by 1

```excel
=A3*1
```

Result: **1250.5**

**E2** — SUM ignores text numbers

```excel
=SUM(A2:A5)
```

Result: **0**

**E3** — convert inside SUMPRODUCT

```excel
=SUMPRODUCT(--TRIM(A2:A5))
```

Result: **1419**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Check that the values really are text. =ISTEXT(A2) returns TRUE, and the numbers are usually left-aligned.
2. In a helper column type `=VALUE(A2)` (or `=--A2`) and press Enter.
3. If some values have extra spaces, use `=VALUE(TRIM(A2))` instead.
4. Fill the formula down, then copy the helper column and use Paste special > Values over the original data if you want to replace it.
5. To total text numbers without a helper column, convert them inside the sum: `=SUMPRODUCT(--TRIM(A2:A5))`.

## Google Sheets-specific notes

In Google Sheets, numbers usually become text when they come in through IMPORTRANGE, IMPORTHTML, a form or a CSV with a Plain text format. The fastest fix for one column is Format > Number > Automatic, followed by re-entering the values, but a formula is more reliable: `=ARRAYFORMULA(IF(A2:A="", "", VALUE(TRIM(A2:A))))` converts the whole column at once. For values with units or currency signs, strip everything that is not a digit, a dot or a minus sign: `=VALUE(REGEXREPLACE(A2, "[^0-9.\-]", ""))`. The decimal separator follows the spreadsheet locale in File > Settings, so "1,5" is a number in a German locale but text in a US locale.

**Whole column at once**

```excel
=ARRAYFORMULA(IF(A2:A="", "", VALUE(TRIM(A2:A))))
```

**Strip currency signs and units**

```excel
=VALUE(REGEXREPLACE(A2, "[^0-9.\-]", ""))
```

**Double minus**

```excel
=--A2
```


## Excel version

The same formula works unchanged in Excel:

```excel
=VALUE(A2)
```

Google Sheets uses the same VALUE, -- and *1 formulas, and handles a whole column with ARRAYFORMULA; for messy text it often uses REGEXREPLACE before VALUE.

<!--SIBLING-->


## Common errors and how to fix them

- **#VALUE!** — The text contains characters that are not part of a number, such as a currency sign, a unit or a non-breaking space. **Fix:** Remove them first with SUBSTITUTE (for example `=VALUE(SUBSTITUTE(A2, CHAR(160), ""))`) or, in Sheets, with REGEXREPLACE.
- **SUM returns 0 or a too-small total** — Some or all of the values are text, and SUM ignores text. **Fix:** Convert them with VALUE in a helper column, or use =SUMPRODUCT(--A2:A5).
- **Wrong decimals, for example 1,5 becomes 15 or an error** — The decimal separator in the text does not match the regional settings. **Fix:** In Excel use NUMBERVALUE with explicit separators; in Sheets change the locale in File > Settings or SUBSTITUTE the comma with a dot.

## FAQ

### How can I tell if a number is stored as text?

Use =ISTEXT(A2) or =ISNUMBER(A2). Text numbers are left-aligned by default, and Excel marks them with a small green triangle.

### What is the difference between VALUE and the double minus?

The result is the same. VALUE is easier to read; -- is shorter and common inside SUMPRODUCT and array formulas.

### How do I keep leading zeros?

Do not convert those values. Codes such as 00123 are identifiers, not quantities, so leave them as text or format the number with a custom format like 00000.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
