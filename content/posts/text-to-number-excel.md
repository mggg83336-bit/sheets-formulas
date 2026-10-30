---
title: How to Convert Text to Numbers in Excel
slug: text-to-number-excel
date: '2026-10-30'
summary: Numbers stored as text look normal but are ignored by SUM, break lookups
  and sort in the wrong order. VALUE, the double minus (--) and multiplying by 1 turn
  them back into real numbers. The formulas are the same in Excel and Google Sheets;
  Excel also offers a one-click Convert to Number fix, and She
tags:
- Text formulas
- Excel
keyword: text-to-number-excel
niche: sheets-formulas
provider: structured
entry_id: text-to-number
platform: Excel
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
- - trim-excel
  - trim-google-sheets
- - substitute-excel
  - substitute-google-sheets
- - extract-numbers-excel
  - extract-numbers-google-sheets
- - len-excel
  - len-google-sheets
sibling: text-to-number-google-sheets
---
Numbers stored as text look normal but are ignored by SUM, break lookups and sort in the wrong order. VALUE, the double minus (--) and multiplying by 1 turn them back into real numbers. The formulas are the same in Excel and Google Sheets; Excel also offers a one-click Convert to Number fix, and Sheets adds REGEXREPLACE for messy values.

## Quick answer

Use this formula in Excel:

```excel
=VALUE(A2)
```

Syntax: `VALUE(text)`. Converts the text in A2 to a number, so "00123" becomes 123 and "1250.5" becomes 1250.5. If the text cannot be read as a number, VALUE returns #VALUE!.

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

## Excel-specific notes

Three formulas do the same job: `=VALUE(A2)`, `=--A2` and `=A2*1`. The double minus is popular inside SUMPRODUCT because it is short. Wrap the text in TRIM when it has extra spaces, and in SUBSTITUTE when it contains a non-breaking space or a currency sign. Excel also has NUMBERVALUE, which lets you name the decimal and group separators: `=NUMBERVALUE(A2, ",", ".")` reads European values such as 1.250,50. Without formulas, select the cells, click the warning icon and choose Convert to Number, or use Data > Text to Columns > Finish, which converts a whole column in place. Leading zeros are lost after conversion, so keep the text version if the zeros matter, for example in product codes or postal codes.

**Double minus**

```excel
=--A2
```

**Remove extra spaces first**

```excel
=VALUE(TRIM(A2))
```

**European separators**

```excel
=NUMBERVALUE(A2, ",", ".")
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=VALUE(A2)
```

Excel adds NUMBERVALUE for custom separators, the Convert to Number warning button and Text to Columns; Sheets relies on ARRAYFORMULA and REGEXREPLACE.

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
