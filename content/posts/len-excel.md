---
title: How to Count Characters with LEN in Excel
slug: len-excel
date: '2026-10-29'
summary: LEN returns the number of characters in a cell, including spaces and punctuation.
  Use it to enforce length limits, spot padded IDs, or build formulas that depend
  on text width. Excel and Google Sheets share the same LEN syntax; Sheets fills a
  whole column with ARRAYFORMULA, while Excel 365 can spill
tags:
- Text formulas
- Excel
keyword: len-excel
niche: sheets-formulas
provider: structured
entry_id: len
platform: Excel
category: text
faq:
- q: Does LEN count spaces?
  a: Yes. Every space, tab-like character stored as a space, and punctuation mark
    counts as one character. Use TRIM first when you want the visible-word length
    only.
- q: How do I count characters across many rows at once?
  a: In Excel 365 enter =LEN(A2:A100) and let it spill. In Google Sheets use =ARRAYFORMULA(LEN(A2:A100)).
    Older Excel — fill the formula down.
- q: How do I count only digits or only letters?
  a: 'Excel 365: walk characters with MID + SEQUENCE, or strip unwanted ones then
    LEN. Sheets: =LEN(REGEXREPLACE(A2,"[^0-9]","")) for digits, or [^A-Za-z] for letters.'
related:
- - trim-excel
  - trim-google-sheets
- - left-right-mid-excel
  - left-right-mid-google-sheets
- - substitute-excel
  - substitute-google-sheets
- - concatenate-excel
  - concatenate-google-sheets
sibling: len-google-sheets
---
LEN returns the number of characters in a cell, including spaces and punctuation. Use it to enforce length limits, spot padded IDs, or build formulas that depend on text width. Excel and Google Sheets share the same LEN syntax; Sheets fills a whole column with ARRAYFORMULA, while Excel 365 can spill LEN across a range.

## Quick answer

Use this formula in Excel:

```excel
=LEN(A2)
```

Syntax: `LEN(text)`. Returns the character count of A2, counting every letter, digit, space and symbol. An empty cell returns 0.

## The problem

You need to know how long each value is — character limits for imports, codes that must be exactly N digits, or helper math that subtracts spaces — without counting by hand.

## Worked example

Measure raw length, trimmed length, and how many times a letter appears.

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **Text** | **Length** | **Trimmed length** | **Count of a** |
| 2 | Hello | **5** |  |  |
| 3 | `"  ab  "` | **6** | **2** |  |
| 4 | banana |  |  | **3** |
| 5 |  | **0** |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**B2** — characters in Hello

```excel
=LEN(A2)
```

Result: **5**

**B3** — spaces count too

```excel
=LEN(A3)
```

Result: **6**

**C3** — length after TRIM

```excel
=LEN(TRIM(A3))
```

Result: **2**

**D4** — how many times a appears

```excel
=LEN(A4)-LEN(SUBSTITUTE(A4,"a",""))
```

Result: **3**

**B5** — empty cell is zero

```excel
=LEN(A5)
```

Result: **0**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Click the result cell and type `=LEN(`.
2. Select the cell whose characters you want to count (A2) and close the parenthesis.
3. Press Enter — the number of characters, including spaces, appears.
4. Wrap with TRIM when leading or trailing spaces should be ignored: `=LEN(TRIM(A2))`.
5. Fill or spill the formula down the column for every row you need to measure.

## Excel-specific notes

LEN is available in every Excel version. It counts spaces, so `"  ab  "` is length 6, not 2 — wrap with TRIM first when you only want visible characters: `=LEN(TRIM(A2))`. LENB counts bytes in double-byte character sets (mostly relevant for East Asian locales); for ordinary English text LEN and LENB match. In Microsoft 365 you can spill lengths for a column with `=LEN(A2:A10)`. Pair LEN with SUBSTITUTE to count specific characters, e.g. `=LEN(A2)-LEN(SUBSTITUTE(A2,"a",""))` for how many times "a" appears. Empty strings and blank cells both return 0.

**Length after trimming spaces**

```excel
=LEN(TRIM(A2))
```

**Count how many times a letter appears**

```excel
=LEN(A2)-LEN(SUBSTITUTE(A2,"a",""))
```

**Spill lengths for a range (Excel 365)**

```excel
=LEN(A2:A10)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=LEN(A2)
```

Sheets matches Excel on LEN, adds ARRAYFORMULA for column fills, and can pair LEN with REGEXREPLACE when you need letter-only or digit-only counts.

<!--SIBLING-->


## Common errors and how to fix them

- **Length looks too high** — Invisible leading or trailing spaces, or a non-breaking space from a paste, are being counted. **Fix:** Use `=LEN(TRIM(A2))`, or CLEAN + TRIM for paste junk. Check the cell with ISTEXT if a number was stored as text with padding.
- **Result is 0 for a cell that looks filled** — The cell holds a formula that returned "" , or only spaces that TRIM would remove. **Fix:** Inspect the formula bar. Use `=LEN(A2)>0` to test for any characters, including spaces.
- **Wrong count for accented or CJK characters** — Confusing LEN (characters) with LENB (bytes) in older double-byte Excel modes. **Fix:** Prefer LEN for character counts. LENB is only needed for byte-oriented legacy workflows.

## FAQ

### Does LEN count spaces?

Yes. Every space, tab-like character stored as a space, and punctuation mark counts as one character. Use TRIM first when you want the visible-word length only.

### How do I count characters across many rows at once?

In Excel 365 enter `=LEN(A2:A100)` and let it spill. In Google Sheets use `=ARRAYFORMULA(LEN(A2:A100))`. Older Excel — fill the formula down.

### How do I count only digits or only letters?

Excel 365: walk characters with MID + SEQUENCE, or strip unwanted ones then LEN. Sheets: `=LEN(REGEXREPLACE(A2,"[^0-9]",""))` for digits, or `[^A-Za-z]` for letters.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
