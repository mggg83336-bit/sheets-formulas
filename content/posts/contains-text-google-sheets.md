---
title: How to Check if a Cell Contains Text in Google Sheets
slug: contains-text-google-sheets
date: '2026-10-27'
summary: Test whether a cell contains a word or a substring anywhere inside it, return
  Yes/No or a custom result, and count matching cells. Covers ISNUMBER with SEARCH
  (case-insensitive), FIND (case-sensitive), COUNTIF with wildcards and REGEXMATCH
  in Google Sheets.
tags:
- Text formulas
- Google Sheets
keyword: contains-text-google-sheets
niche: sheets-formulas
provider: structured
entry_id: contains-text
platform: Google Sheets
category: text
faq:
- q: How do I sum values where the description contains a word?
  a: Use SUMIF with wildcards, e.g. =SUMIF(A2:A5, "*mouse*", B2:B5).
- q: How do I highlight cells that contain a word?
  a: 'Use conditional formatting with a formula rule: =ISNUMBER(SEARCH("mouse", $A2)).'
related:
- - countif-google-sheets
  - countif-excel
- - text-before-character-google-sheets
  - text-before-character-excel
- - sumif-google-sheets
  - sumif-excel
- - trim-google-sheets
  - trim-excel
sibling: contains-text-excel
---
Test whether a cell contains a word or a substring anywhere inside it, return Yes/No or a custom result, and count matching cells. Covers ISNUMBER with SEARCH (case-insensitive), FIND (case-sensitive), COUNTIF with wildcards and REGEXMATCH in Google Sheets.

## Quick answer

Use this formula in Google Sheets:

```excel
=ISNUMBER(SEARCH("mouse", A2))
```

Same formula in Google Sheets.

## The problem

You want to flag every product whose description mentions "mouse", regardless of where the word appears or how it is capitalised.

## Worked example

Which descriptions mention "mouse"?

| | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 1 | **Description** | **Contains** | **Yes or No** | **Case-sensitive** |  | **Count** |
| 2 | Wireless Mouse - Black | **TRUE** | **Yes** | **FALSE** |  | **2** |
| 3 | USB-C Hub (7-in-1) | **FALSE** | **No** | **FALSE** |  |  |
| 4 | Mouse Pad XL | **TRUE** | **Yes** | **FALSE** |  |  |
| 5 | Laptop Stand | **FALSE** | **No** | **FALSE** |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**B2 (filled to B5)** — filled down

```excel
=REGEXMATCH(A2, "(?i)mouse")
```

Results: **TRUE**, **FALSE**, **TRUE**, **FALSE**

**C2 (filled to C5)** — filled down

```excel
=IF(ISNUMBER(SEARCH("mouse", A2)), "Yes", "No")
```

Results: **Yes**, **No**, **Yes**, **No**

**D2 (filled to D5)** — FIND is case-sensitive, so lowercase "mouse" is not found

```excel
=ISNUMBER(FIND("mouse", A2))
```

Results: **FALSE**, **FALSE**, **FALSE**, **FALSE**

**F2** — how many cells contain the word

```excel
=COUNTIF(A2:A5, "*mouse*")
```

Result: **2**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `SEARCH("mouse", A2)` returns 10 for "Wireless Mouse - Black" (the position where the word starts) and #VALUE! when the word is not there.
2. `ISNUMBER(...)` converts a position into TRUE and the error into FALSE.
3. Wrap it in IF to show any text you like instead of TRUE/FALSE.
4. COUNTIF with `"*mouse*"` counts cells that contain the word anywhere; the asterisks match any characters before and after.

## Google Sheets-specific notes

Google Sheets also offers REGEXMATCH, which returns TRUE/FALSE directly. Add (?i) at the start of the pattern for a case-insensitive match: `=REGEXMATCH(A2, "(?i)mouse")`. Regular expressions make "any of several words" and whole-word matching easy, for example `=REGEXMATCH(A2, "(?i)\b(mouse|keyboard)\b")`. REGEXMATCH needs text input, so use A2&"" if the cell may contain a number.

**Case-insensitive REGEXMATCH**

```excel
=REGEXMATCH(A2, "(?i)mouse")
```

**Whole words, several options**

```excel
=REGEXMATCH(A2, "(?i)\b(mouse|keyboard)\b")
```


## Excel version

The same formula works unchanged in Excel:

```excel
=ISNUMBER(SEARCH("mouse", A2))
```

Excel uses the same ISNUMBER(SEARCH()) formula. REGEXTEST is available only in recent Microsoft 365 builds.

<!--SIBLING-->


## Common errors and how to fix them

- **Always FALSE** — Using =A2="mouse" checks for an exact full-cell match, or FIND was used with the wrong case. **Fix:** Use ISNUMBER(SEARCH(...)).
- **#VALUE! instead of FALSE** — SEARCH was used without ISNUMBER. **Fix:** Wrap SEARCH in ISNUMBER or IFERROR.
- **Unexpected matches** — The search term is part of a longer word. **Fix:** Search for " pad " with spaces, or use whole-word regular expressions in Google Sheets.

## FAQ

### How do I sum values where the description contains a word?

Use SUMIF with wildcards, e.g. =SUMIF(A2:A5, "*mouse*", B2:B5).

### How do I highlight cells that contain a word?

Use conditional formatting with a formula rule: =ISNUMBER(SEARCH("mouse", $A2)).

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
