---
title: How to Use ISNUMBER and ISTEXT to Check Cell Types in Excel
slug: isnumber-istext-excel
date: '2026-11-14'
summary: 'ISNUMBER returns TRUE when a cell holds a real number — including dates
  and times, which Excel and Google Sheets store as serial numbers — and FALSE for
  text, blanks, and logical values. ISTEXT returns TRUE for any text, including a
  number stored as text such as "123" and a formula that returned an '
tags:
- Text formulas
- Excel
keyword: isnumber-istext-excel
niche: sheets-formulas
provider: structured
entry_id: isnumber-istext
platform: Excel
category: text
faq:
- q: Why is ISNUMBER false for "123"?
  a: Because the value is text, even if it looks like a number. ISTEXT is TRUE in
    that case, as the worked example shows for A3. Convert it with VALUE or the double
    minus when you need a real number.
- q: Is a date a number or text?
  a: A real date is a number (a serial). ISNUMBER is TRUE and ISTEXT is FALSE, which
    is why A6 returns TRUE for ISNUMBER. A date typed or imported as text, such as
    "2026-11-14", is text until you convert it with DATEVALUE or DATE.
- q: What do ISNUMBER and ISTEXT return for a blank, "", or TRUE?
  a: A blank is FALSE for both. A formula that returned "" is text, so ISTEXT is TRUE.
    Logical TRUE and FALSE are FALSE for both ISNUMBER and ISTEXT in Excel and Google
    Sheets; use ISLOGICAL to detect them.
- q: How do I flag a whole column at once?
  a: In Microsoft 365, =ISNUMBER(A2:A7) or =ISTEXT(A2:A7) spills. In Google Sheets,
    use =ARRAYFORMULA(IF(A2:A="", "", ISNUMBER(A2:A))), or the convert-and-keep pattern
    in the Sheets alternatives.
related:
- - text-to-number-excel
  - text-to-number-google-sheets
- - number-to-text-excel
  - number-to-text-google-sheets
- - isblank-excel
  - isblank-google-sheets
- - if-excel
  - if-google-sheets
- - leading-zeros-excel
  - leading-zeros-google-sheets
sibling: isnumber-istext-google-sheets
---
ISNUMBER returns TRUE when a cell holds a real number — including dates and times, which Excel and Google Sheets store as serial numbers — and FALSE for text, blanks, and logical values. ISTEXT returns TRUE for any text, including a number stored as text such as "123" and a formula that returned an empty string (""). A blank cell is neither a number nor text: both functions return FALSE, and [ISBLANK](../isblank-excel/) is the test for that case. Use the pair to catch values that look numeric but will break SUM or a lookup, or to decide whether to run VALUE. The functions are the same in Excel and Google Sheets; Sheets typically wraps them in ARRAYFORMULA to check a whole column, and also has ISDATE when you specifically need to test a date.

## Quick answer

Use this formula in Excel:

```excel
=ISNUMBER(A2)
```

Syntax: `ISNUMBER(value)` and `ISTEXT(value)`. `=ISNUMBER(A2)` is TRUE for the real number 123. `=ISTEXT(A3)` is TRUE for the text "123", which looks numeric but will be ignored by SUM until you convert it with VALUE. A date is a number, so ISNUMBER is TRUE for A6; a blank and a logical TRUE or FALSE are neither numbers nor text.

## The problem

A mixed list contains a real number, the text "123", a word, a blank, a date, and a formula that returned "". You need to flag which values are numbers you can add, which are text (including a number stored as text), and which are neither, before converting or looking them up.

## Worked example

A mixed column of values. A2 is a real number, A3 is the text "123", A4 is a word, A5 is blank, A6 holds DATE(2026,11,14) stored as the serial 46340, and A7 holds a formula that returns "". Column C tests ISNUMBER and column D tests ISTEXT on each row. E3 converts the text "123" back to a number.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Value** | **Description** | **ISNUMBER** | **ISTEXT** | **Converted** |
| 2 | 123 | number | **TRUE** | **FALSE** |  |
| 3 | 123 | text that looks like a number | **FALSE** | **TRUE** | **123** |
| 4 | hello | text | **FALSE** | **TRUE** |  |
| 5 |  | blank cell | **FALSE** | **FALSE** |  |
| 6 | **46340** | date | **TRUE** | **FALSE** |  |
| 7 | **** | empty string | **FALSE** | **TRUE** |  |

Formulas used in the example (results shown in **bold** in the table above):

**A6** — a date stored as a serial number

```excel
=DATE(2026,11,14)
```

Result: **46340**

**A7** — a formula that displays as blank

```excel
=""
```

Result: *(blank)*

**C2** — 123 is a number

```excel
=ISNUMBER(A2)
```

Result: **TRUE**

**D2** — 123 is not text

```excel
=ISTEXT(A2)
```

Result: **FALSE**

**C3** — the text 123 is not a number

```excel
=ISNUMBER(A3)
```

Result: **FALSE**

**D3** — the text 123 is text

```excel
=ISTEXT(A3)
```

Result: **TRUE**

**C4** — a word is not a number

```excel
=ISNUMBER(A4)
```

Result: **FALSE**

**D4** — a word is text

```excel
=ISTEXT(A4)
```

Result: **TRUE**

**C5** — a blank is not a number

```excel
=ISNUMBER(A5)
```

Result: **FALSE**

**D5** — a blank is not text

```excel
=ISTEXT(A5)
```

Result: **FALSE**

**C6** — a date is a number

```excel
=ISNUMBER(A6)
```

Result: **TRUE**

**D6** — a date is not text

```excel
=ISTEXT(A6)
```

Result: **FALSE**

**C7** — an empty string is not a number

```excel
=ISNUMBER(A7)
```

Result: **FALSE**

**D7** — an empty string is text

```excel
=ISTEXT(A7)
```

Result: **TRUE**

**E3** — convert the text 123 to a number

```excel
=VALUE(A3)
```

Result: **123**

<!--AD_IN_ARTICLE-->

## How the formula works

1. To test a value, type `=ISNUMBER(A2)` or `=ISTEXT(A2)` and press Enter. ISNUMBER is TRUE for the real number in A2; ISTEXT is FALSE.
2. On A3, which holds the text "123", the results flip: `=ISNUMBER(A3)` is FALSE and `=ISTEXT(A3)` is TRUE. The value looks numeric, but SUM will ignore it until you convert it.
3. A date is stored as a serial number, so `=ISNUMBER(A6)` is TRUE and `=ISTEXT(A6)` is FALSE. A6 shows 46340, the serial for 14 November 2026. That is why you can add days to a date.
4. A blank cell (A5) returns FALSE for both tests. A formula that returned `""` (A7) is text: ISTEXT is TRUE and ISBLANK is FALSE. Use ISBLANK when you need a truly empty cell, and ISTEXT or `A7=""` when a hidden formula should count as text or empty-looking.
5. Convert a text number with `=VALUE(A3)` (result 123) or `=IF(ISTEXT(A2), VALUE(A2), A2)` down a mixed column. In Excel 365, spill `=ISNUMBER(A2:A7)` or `=ISTEXT(A2:A7)`. In Google Sheets, wrap the same tests in ARRAYFORMULA. Logical TRUE and FALSE fail both tests in Excel and Sheets; use ISLOGICAL for those.

## Excel-specific notes

ISNUMBER and ISTEXT are available in every Excel version. They test the stored type, not how the cell is formatted: a number formatted as a date or as text still returns TRUE for ISNUMBER, and a number stored as text (left-aligned, often with a green triangle) returns TRUE for ISTEXT even when it looks like 123. Dates and times are serial numbers, so ISNUMBER is TRUE and ISTEXT is FALSE; that is why you can add days to a date. A formula that returns `""` is text, so ISTEXT is TRUE and [ISBLANK](../isblank-excel/) is FALSE. A truly empty cell returns FALSE for both. Logical values are a third type: `=ISNUMBER(TRUE)` and `=ISTEXT(TRUE)` are both FALSE in Excel (use ISLOGICAL if you need that test). `=ISNUMBER(VALUE(A3))` is the usual way to confirm that text can be converted, and `=IF(ISTEXT(A3), VALUE(A3), A3)` turns a mixed column into numbers. In Microsoft 365, `=ISNUMBER(A2:A7)` and `=ISTEXT(A2:A7)` spill a TRUE/FALSE flag for each row. ISNONTEXT is TRUE for numbers, blanks, logicals and errors; ISBLANK is the tighter test for an empty cell. Pair these checks with [text to number](../text-to-number-excel/) when you are ready to convert, and with [IF](../if-excel/) when the flag should become a label or a fallback value.

**Test for text, including "123"**

```excel
=ISTEXT(A3)
```

**Convert text and then test**

```excel
=ISNUMBER(VALUE(A3))
```

**Microsoft 365 spill of type flags**

```excel
=ISNUMBER(A2:A7)
```

**Turn text numbers into values**

```excel
=IF(ISTEXT(A2), VALUE(A2), A2)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=ISNUMBER(A2)
```

Excel uses the same ISNUMBER and ISTEXT formulas. Whole-column fills in Excel 365 spill from `=ISNUMBER(A2:A7)`; in Sheets you wrap the test in ARRAYFORMULA. Excel has no ISDATE; a date still passes ISNUMBER on both platforms because it is a serial number.

<!--SIBLING-->


## Common errors and how to fix them

- **SUM is 0 or too small even though the column looks numeric** — The values are text. ISTEXT is TRUE and ISNUMBER is FALSE, so SUM ignores them. **Fix:** Convert with VALUE, `--A2`, or the pattern on the [text to number](../text-to-number-excel/) page, then sum the converted column.
- **A date failed a "must be text" check, or a quantity passed a "must be a date" check** — Dates are numbers. ISNUMBER is TRUE for both a date and a plain amount; ISTEXT is FALSE for a real date. **Fix:** In Sheets use ISDATE when only a date should pass. In Excel test with DATEVALUE or compare the cell to a date, not with ISTEXT.
- **Both ISNUMBER and ISTEXT are FALSE on a cell that looks empty** — The cell is truly blank, or it holds a logical TRUE/FALSE (for example an unchecked checkbox in Sheets, which stores FALSE). **Fix:** Use [ISBLANK](../isblank-excel/) for an empty cell, and ISLOGICAL for TRUE/FALSE. A formula that returned `""` would have made ISTEXT TRUE.
- **#VALUE! after wrapping a test in VALUE** — VALUE was applied to text that is not a number, such as "hello" or a date in an unexpected locale format. **Fix:** Use `=IF(ISTEXT(A2), IFERROR(VALUE(A2), A2), A2)` so non-numeric text is left unchanged.

## FAQ

### Why is ISNUMBER false for "123"?

Because the value is text, even if it looks like a number. ISTEXT is TRUE in that case, as the worked example shows for A3. Convert it with VALUE or the double minus when you need a real number.

### Is a date a number or text?

A real date is a number (a serial). ISNUMBER is TRUE and ISTEXT is FALSE, which is why A6 returns TRUE for ISNUMBER. A date typed or imported as text, such as "2026-11-14", is text until you convert it with DATEVALUE or DATE.

### What do ISNUMBER and ISTEXT return for a blank, "", or TRUE?

A blank is FALSE for both. A formula that returned `""` is text, so ISTEXT is TRUE. Logical TRUE and FALSE are FALSE for both ISNUMBER and ISTEXT in Excel and Google Sheets; use ISLOGICAL to detect them.

### How do I flag a whole column at once?

In Microsoft 365, `=ISNUMBER(A2:A7)` or `=ISTEXT(A2:A7)` spills. In Google Sheets, use `=ARRAYFORMULA(IF(A2:A="", "", ISNUMBER(A2:A)))`, or the convert-and-keep pattern in the Sheets alternatives.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
