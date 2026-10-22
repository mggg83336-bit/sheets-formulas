---
title: How to Check if a Cell Contains Text in Excel
slug: contains-text-excel
date: '2026-10-22'
summary: Test whether a cell contains a word or a substring anywhere inside it, return
  Yes/No or a custom result, and count matching cells. Covers ISNUMBER with SEARCH
  (case-insensitive), FIND (case-sensitive), COUNTIF with wildcards and REGEXMATCH
  in Google Sheets.
tags:
- Text formulas
- Excel
keyword: contains-text-excel
niche: sheets-formulas
provider: structured
entry_id: contains-text
platform: Excel
category: text
faq:
- q: How do I sum values where the description contains a word?
  a: Use SUMIF with wildcards, e.g. =SUMIF(A2:A5, "*mouse*", B2:B5).
- q: How do I highlight cells that contain a word?
  a: 'Use conditional formatting with a formula rule: =ISNUMBER(SEARCH("mouse", $A2)).'
related:
- - countif-excel
  - countif-google-sheets
- - text-before-character-excel
  - text-before-character-google-sheets
- - sumif-excel
  - sumif-google-sheets
- - trim-excel
  - trim-google-sheets
sibling: contains-text-google-sheets
---
Test whether a cell contains a word or a substring anywhere inside it, return Yes/No or a custom result, and count matching cells. Covers ISNUMBER with SEARCH (case-insensitive), FIND (case-sensitive), COUNTIF with wildcards and REGEXMATCH in Google Sheets.

## Quick answer

Use this formula in Excel:

```excel
=ISNUMBER(SEARCH("mouse", A2))
```

SEARCH returns the position of "mouse" (any case) or #VALUE! if it is missing. ISNUMBER turns that into TRUE or FALSE.

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
=ISNUMBER(SEARCH("mouse", A2))
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

## Excel-specific notes

`A2="mouse"` only checks whether the whole cell equals the word, which is a common mistake. SEARCH is case-insensitive and supports wildcards; FIND is case-sensitive and does not. To check for any of several words, pass an array and add the results: `=SUM(--ISNUMBER(SEARCH({"mouse","keyboard"}, A2)))>0`. Note that searching for short words also matches inside longer ones ("pad" matches "iPad"); include spaces or punctuation in the search term if that matters.

**Any of several words**

```excel
=SUM(--ISNUMBER(SEARCH({"mouse","keyboard"}, A2)))>0
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=ISNUMBER(SEARCH("mouse", A2))
```

The same formula works in Google Sheets, where REGEXMATCH(A2, "(?i)mouse") is a shorter alternative.

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
