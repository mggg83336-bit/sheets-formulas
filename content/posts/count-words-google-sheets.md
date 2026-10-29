---
title: How to Count Words in a Cell in Google Sheets
slug: count-words-google-sheets
date: '2026-10-29'
summary: Excel has no built-in WORDCOUNT. The classic approach subtracts the length
  without spaces from the trimmed length, then adds one. Google Sheets can use the
  same math, or SPLIT the cell on spaces and COUNTA the pieces. Both handle blank
  cells when you guard with TRIM.
tags:
- Text formulas
- Google Sheets
keyword: count-words-google-sheets
niche: sheets-formulas
provider: structured
entry_id: count_words
platform: Google Sheets
category: text
faq:
- q: Is there a WORDCOUNT function?
  a: Not in Excel. Google Sheets has no dedicated WORDCOUNT either — use SPLIT + COUNTA
    or the LEN − SUBSTITUTE formula. Some add-ins expose word count, but the formulas
    here need nothing extra.
- q: Do hyphenated words count as one or two?
  a: As one, because the separator is a space. well-known is a single word to these
    formulas. Split on "-" only if you intentionally want hyphen pieces.
- q: Can I count words in a whole range?
  a: Sum per-row counts, e.g. fill the formula in B2:B100 then =SUM(B2:B100). Joining
    the range into one cell first is usually harder to audit.
related:
- - len-google-sheets
  - len-excel
- - trim-google-sheets
  - trim-excel
- - textsplit-excel
- - substitute-google-sheets
  - substitute-excel
sibling: count-words-excel
---
Excel has no built-in WORDCOUNT. The classic approach subtracts the length without spaces from the trimmed length, then adds one. Google Sheets can use the same math, or SPLIT the cell on spaces and COUNTA the pieces. Both handle blank cells when you guard with TRIM.

## Quick answer

Use this formula in Google Sheets:

```excel
=IF(TRIM(A2)="",0,COUNTA(SPLIT(TRIM(A2)," ")))
```

TRIM the cell, SPLIT on spaces into separate pieces, then COUNTA those pieces. Blank cells return 0 via the IF guard.

## The problem

A notes or title column needs a word count per cell — for limits, summaries or QA — and counting manually does not scale.

## Worked example

Count words in phrases, a single word, padded text, and a blank cell.

| | A | B |
|---|---|---|
| 1 | **Text** | **Words** |
| 2 | one two three | **3** |
| 3 | single | **1** |
| 4 | `"  spaced out  "` | **2** |
| 5 |  | **0** |

Formulas used in the example (results shown in **bold** in the table above):

**B2** — three words

```excel
=IF(TRIM(A2)="",0,LEN(TRIM(A2))-LEN(SUBSTITUTE(TRIM(A2)," ",""))+1)
```

Result: **3**

**B3** — one word

```excel
=IF(TRIM(A3)="",0,LEN(TRIM(A3))-LEN(SUBSTITUTE(TRIM(A3)," ",""))+1)
```

Result: **1**

**B4** — trimmed spaced out — two words

```excel
=IF(TRIM(A4)="",0,LEN(TRIM(A4))-LEN(SUBSTITUTE(TRIM(A4)," ",""))+1)
```

Result: **2**

**B5** — blank is zero

```excel
=IF(TRIM(A5)="",0,LEN(TRIM(A5))-LEN(SUBSTITUTE(TRIM(A5)," ",""))+1)
```

Result: **0**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Prefer a clean source column — TRIM the text or paste values without odd spacing.
2. Enter `=IF(TRIM(A2)="",0,LEN(TRIM(A2))-LEN(SUBSTITUTE(TRIM(A2)," ",""))+1)` in Excel (or Sheets).
3. In Google Sheets you can instead use `=IF(TRIM(A2)="",0,COUNTA(SPLIT(TRIM(A2)," ")))`.
4. Fill the formula down. Spot-check rows that had double spaces or punctuation.
5. Optional: collapse repeated spaces with SUBSTITUTE or REGEXREPLACE before counting.

## Google Sheets-specific notes

SPLIT + COUNTA is the natural Google Sheets word count and matches the Excel LEN trick on clean single-spaced text. SPLIT treats each delimiter break as a piece, so repeated spaces can create empty pieces — TRIM the input, and consider `=COUNTA(SPLIT(REGEXREPLACE(TRIM(A2), "\s+"," ")," "))` to collapse whitespace first. ARRAYFORMULA can drive a column: `=ARRAYFORMULA(IF(TRIM(A2:A)="",0,COUNTA(SPLIT(TRIM(A2:A)," "))))` does not expand SPLIT row-by-row the way you might expect, so many Sheets users fill the LEN − SUBSTITUTE formula down instead, or use a per-row MAP/LAMBDA in newer Sheets. The LEN − SUBSTITUTE formula from the Excel side works unchanged in Sheets when you want identical logic on both platforms.

**Same LEN formula as Excel**

```excel
=IF(TRIM(A2)="",0,LEN(TRIM(A2))-LEN(SUBSTITUTE(TRIM(A2)," ",""))+1)
```

**Collapse whitespace then SPLIT**

```excel
=IF(TRIM(A2)="",0,COUNTA(SPLIT(REGEXREPLACE(TRIM(A2),"\s+"," ")," ")))
```

**Character count instead**

```excel
=LEN(TRIM(A2))
```


## Excel version

In Excel, use:

```excel
=IF(TRIM(A2)="",0,LEN(TRIM(A2))-LEN(SUBSTITUTE(TRIM(A2)," ",""))+1)
```

Excel typically uses the LEN − SUBSTITUTE pattern or Excel 365 TEXTSPLIT. Google Sheets can use the same math, or SPLIT + COUNTA, which is often shorter.

<!--SIBLING-->


## Common errors and how to fix them

- **Count is higher than the words you see** — Repeated internal spaces create extra "gaps" in the LEN − SUBSTITUTE method, or SPLIT produced empty pieces. **Fix:** Collapse spaces first (`SUBSTITUTE` repeatedly, or `REGEXREPLACE` in Sheets), then recount.
- **Blank cell shows 1** — The IF(TRIM=…) guard was omitted, so LEN of "" − LEN of "" + 1 equals 1. **Fix:** Always wrap with `IF(TRIM(A2)="",0, …)` so empty and all-space cells return 0.
- **#NAME? with TEXTSPLIT** — TEXTSPLIT needs Microsoft 365 or Excel 2021+. **Fix:** Use the LEN − SUBSTITUTE formula on this page; it works in older Excel.

## FAQ

### Is there a WORDCOUNT function?

Not in Excel. Google Sheets has no dedicated WORDCOUNT either — use SPLIT + COUNTA or the LEN − SUBSTITUTE formula. Some add-ins expose word count, but the formulas here need nothing extra.

### Do hyphenated words count as one or two?

As one, because the separator is a space. `well-known` is a single word to these formulas. Split on `"-"` only if you intentionally want hyphen pieces.

### Can I count words in a whole range?

Sum per-row counts, e.g. fill the formula in B2:B100 then `=SUM(B2:B100)`. Joining the range into one cell first is usually harder to audit.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
