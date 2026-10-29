---
title: How to Change Case with UPPER LOWER PROPER in Excel
slug: change-case-excel
date: '2026-10-29'
summary: UPPER converts text to all capitals, LOWER to all lowercase, and PROPER to
  title case (first letter of each word capitalised). Excel and Google Sheets share
  these three functions. Use them to normalise names, codes and labels before matching
  or display.
tags:
- Text formulas
- Excel
keyword: change-case-excel
niche: sheets-formulas
provider: structured
entry_id: change_case
platform: Excel
category: text
faq:
- q: What is the difference between PROPER and UPPER?
  a: UPPER makes every letter capital. PROPER capitalises the first letter of each
    word and forces the rest to lowercase. LOWER forces everything to lowercase.
- q: Does PROPER work with accented characters?
  a: Yes in modern Excel and Google Sheets — accented letters are cased correctly
    in most locales. Always spot-check uncommon scripts.
- q: Can I change case without a formula?
  a: In Excel, flash fill or Power Query can rewrite case. In Sheets, extensions exist,
    but UPPER/LOWER/PROPER remain the reliable built-in approach.
related:
- - trim-excel
  - trim-google-sheets
- - len-excel
  - len-google-sheets
- - substitute-excel
  - substitute-google-sheets
- - concatenate-excel
  - concatenate-google-sheets
sibling: change-case-google-sheets
---
UPPER converts text to all capitals, LOWER to all lowercase, and PROPER to title case (first letter of each word capitalised). Excel and Google Sheets share these three functions. Use them to normalise names, codes and labels before matching or display.

## Quick answer

Use this formula in Excel:

```excel
=PROPER(A2)
```

`PROPER(A2)` capitalises the first letter of each word and lowercases the rest. Swap in `UPPER(A2)` for all caps or `LOWER(A2)` for all lowercase.

## The problem

Imported names and codes arrive in mixed or inconsistent casing — `john SMITH`, `hola` — and you need predictable UPPER, lower or Title Case without retyping.

## Worked example

Turn mixed text into UPPER, lower and Proper forms.

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **Text** | **UPPER** | **LOWER** | **PROPER** |
| 2 | hello WORLD | **HELLO WORLD** | **hello world** | **Hello World** |
| 3 | john smith |  |  | **John Smith** |
| 4 | `"  maria  "` |  |  | **Maria** |

Formulas used in the example (results shown in **bold** in the table above):

**B2** — all caps

```excel
=UPPER(A2)
```

Result: **HELLO WORLD**

**C2** — all lowercase

```excel
=LOWER(A2)
```

Result: **hello world**

**D2** — title case

```excel
=PROPER(A2)
```

Result: **Hello World**

**D3** — proper name

```excel
=PROPER(A3)
```

Result: **John Smith**

**D4** — proper after trim

```excel
=PROPER(TRIM(A4))
```

Result: **Maria**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Pick the case you need — UPPER, LOWER or PROPER.
2. In the result cell type `=PROPER(A2)` (or UPPER / LOWER) and press Enter.
3. Fill or spill down the column for every row to normalise.
4. Optional: wrap with TRIM, e.g. `=PROPER(TRIM(A2))`, when spaces are messy.
5. Paste Special > Values over the source column if you want to keep only the converted text.

## Excel-specific notes

UPPER, LOWER and PROPER exist in every Excel version and take a single text argument. PROPER treats any non-letter as a word break, so `o'brien` becomes `O'Brien`, but `mcdonald` becomes `Mcdonald` — it will not preserve internal capitals in brand names. For those, keep a correction list or edit manually after PROPER. Numbers and punctuation pass through unchanged. In Microsoft 365 you can spill `=UPPER(A2:A100)`. After converting a column, Copy > Paste Special > Values if you want to replace the originals. Combine with TRIM to clean spaces in the same step: `=PROPER(TRIM(A2))`.

**All uppercase**

```excel
=UPPER(A2)
```

**All lowercase**

```excel
=LOWER(A2)
```

**Title case after trimming**

```excel
=PROPER(TRIM(A2))
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=PROPER(A2)
```

Sheets matches Excel on UPPER / LOWER / PROPER and commonly uses ARRAYFORMULA for column fills. Sentence-case patterns with LEFT/RIGHT/LEN work on both platforms.

<!--SIBLING-->


## Common errors and how to fix them

- **Brand names lose internal capitals** — PROPER lowercases every letter after the first in each word (`iPhone` → `Iphone`). **Fix:** Keep an exceptions list, fix those rows manually, or avoid PROPER for product codes that need exact casing.
- **Leading spaces remain after PROPER** — PROPER does not remove spaces; it only changes case. **Fix:** Use `=PROPER(TRIM(A2))` so spacing and case are fixed together.
- **Formula shows the function name as text** — The cell was formatted as Text before the formula was entered, or an extra space preceded the equals sign. **Fix:** Set the format to General, re-enter the formula starting with `=`.

## FAQ

### What is the difference between PROPER and UPPER?

UPPER makes every letter capital. PROPER capitalises the first letter of each word and forces the rest to lowercase. LOWER forces everything to lowercase.

### Does PROPER work with accented characters?

Yes in modern Excel and Google Sheets — accented letters are cased correctly in most locales. Always spot-check uncommon scripts.

### Can I change case without a formula?

In Excel, flash fill or Power Query can rewrite case. In Sheets, extensions exist, but UPPER/LOWER/PROPER remain the reliable built-in approach.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
