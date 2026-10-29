---
title: How to Count Characters with LEN in Google Sheets
slug: len-google-sheets
date: '2026-10-29'
summary: LEN returns the number of characters in a cell, including spaces and punctuation.
  Use it to enforce length limits, spot padded IDs, or build formulas that depend
  on text width. Excel and Google Sheets share the same LEN syntax; Sheets fills a
  whole column with ARRAYFORMULA, while Excel 365 can spill
tags:
- Text formulas
- Google Sheets
keyword: len-google-sheets
niche: sheets-formulas
provider: structured
entry_id: len
platform: Google Sheets
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
- - trim-google-sheets
  - trim-excel
- - left-right-mid-google-sheets
  - left-right-mid-excel
- - substitute-google-sheets
  - substitute-excel
- - concatenate-google-sheets
  - concatenate-excel
sibling: len-excel
---
LEN returns the number of characters in a cell, including spaces and punctuation. Use it to enforce length limits, spot padded IDs, or build formulas that depend on text width. Excel and Google Sheets share the same LEN syntax; Sheets fills a whole column with ARRAYFORMULA, while Excel 365 can spill LEN across a range.

## Quick answer

Use this formula in Google Sheets:

```excel
=LEN(A2)
```

Same LEN syntax in Google Sheets as in Excel — character count of A2, spaces included.

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

## Google Sheets-specific notes

LEN works the same way in Google Sheets, including spaces and punctuation. To fill an entire column at once use ARRAYFORMULA: `=ARRAYFORMULA(IF(A2:A="", "", LEN(A2:A)))`. Sheets has no separate LENB for everyday use; LEN already counts each Unicode character as one. Combine with TRIM when leading or trailing spaces should not count, and with SUBSTITUTE to count occurrences of a character. REGEXREPLACE can strip non-letters before LEN when you only want letter counts: `=LEN(REGEXREPLACE(A2, "[^A-Za-z]", ""))`. Blank cells return 0, same as Excel.

**Whole column of lengths**

```excel
=ARRAYFORMULA(IF(A2:A="", "", LEN(A2:A)))
```

**Length after trimming spaces**

```excel
=LEN(TRIM(A2))
```

**Count letters only with REGEXREPLACE**

```excel
=LEN(REGEXREPLACE(A2, "[^A-Za-z]", ""))
```


## Excel version

The same formula works unchanged in Excel:

```excel
=LEN(A2)
```

LEN itself is identical in Excel and Sheets. Sheets typically wraps it in ARRAYFORMULA for a whole column; Excel 365 can spill LEN over a range without ARRAYFORMULA.

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
