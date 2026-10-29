---
title: How to Change Case with UPPER LOWER PROPER in Google Sheets
slug: change-case-google-sheets
date: '2026-10-29'
summary: UPPER converts text to all capitals, LOWER to all lowercase, and PROPER to
  title case (first letter of each word capitalised). Excel and Google Sheets share
  these three functions. Use them to normalise names, codes and labels before matching
  or display.
tags:
- Text formulas
- Google Sheets
keyword: change-case-google-sheets
niche: sheets-formulas
provider: structured
entry_id: change_case
platform: Google Sheets
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
- - trim-google-sheets
  - trim-excel
- - len-google-sheets
  - len-excel
- - substitute-google-sheets
  - substitute-excel
- - concatenate-google-sheets
  - concatenate-excel
sibling: change-case-excel
---
UPPER converts text to all capitals, LOWER to all lowercase, and PROPER to title case (first letter of each word capitalised). Excel and Google Sheets share these three functions. Use them to normalise names, codes and labels before matching or display.

## Quick answer

Use this formula in Google Sheets:

```excel
=PROPER(A2)
```

Same PROPER, UPPER and LOWER functions as Excel — title case, all caps, or all lowercase.

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

## Google Sheets-specific notes

Google Sheets implements UPPER, LOWER and PROPER with the same single-argument behaviour as Excel, including PROPER's habit of lowercasing the rest of each word. Fill a column with ARRAYFORMULA: `=ARRAYFORMULA(IF(A2:A="", "", PROPER(A2:A)))`. For more control — uppercase only the first character of the cell — use a LEFT/RIGHT mix: `=UPPER(LEFT(A2,1)) & LOWER(RIGHT(A2, LEN(A2)-1))`. REGEXREPLACE can force custom patterns, but PROPER remains the fast path for ordinary names. TRIM inside PROPER still helps when imports carry extra spaces. After conversion, paste as values if downstream sheets should not depend on live formulas.

**Whole column to title case**

```excel
=ARRAYFORMULA(IF(A2:A="", "", PROPER(A2:A)))
```

**Sentence case (first character only)**

```excel
=UPPER(LEFT(A2,1))&LOWER(RIGHT(A2,LEN(A2)-1))
```

**All uppercase for a column**

```excel
=ARRAYFORMULA(IF(A2:A="", "", UPPER(A2:A)))
```


## Excel version

The same formula works unchanged in Excel:

```excel
=PROPER(A2)
```

The three functions match Google Sheets. Sheets often wraps them in ARRAYFORMULA for a full column; Excel 365 can spill the same way without ARRAYFORMULA.

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
