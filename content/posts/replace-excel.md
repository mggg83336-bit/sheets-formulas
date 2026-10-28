---
title: How to Use the REPLACE Function in Excel
slug: replace-excel
date: '2026-10-28'
summary: REPLACE overwrites a fixed number of characters starting at a known position.
  It is the position-based counterpart to SUBSTITUTE (which finds text by content).
  The same REPLACE function works in Excel and Google Sheets; Sheets users often reach
  for REGEXREPLACE when the cut point is a pattern rather
tags:
- Text formulas
- Excel
keyword: replace-excel
niche: sheets-formulas
provider: structured
entry_id: replace_fn
platform: Excel
category: text
faq:
- q: What is the difference between REPLACE and SUBSTITUTE?
  a: REPLACE overwrites by start position and length. SUBSTITUTE finds old_text by
    content and can limit the change to the N-th match.
- q: Can REPLACE insert text without deleting anything?
  a: 'Yes — set num_chars to 0: =REPLACE(A2, 5, 0, "-") inserts a dash before the
    old 5th character.'
- q: Does REPLACE work the same in Google Sheets?
  a: Yes for the four-argument form. Use ARRAYFORMULA for whole-column edits, and
    REGEXREPLACE when a pattern is clearer than a start index.
related:
- - substitute-excel
  - substitute-google-sheets
- - left-right-mid-excel
  - left-right-mid-google-sheets
- - trim-excel
  - trim-google-sheets
- - text-before-character-excel
  - text-before-character-google-sheets
sibling: replace-google-sheets
---
REPLACE overwrites a fixed number of characters starting at a known position. It is the position-based counterpart to SUBSTITUTE (which finds text by content). The same REPLACE function works in Excel and Google Sheets; Sheets users often reach for REGEXREPLACE when the cut point is a pattern rather than a character index.

## Quick answer

Use this formula in Excel:

```excel
=REPLACE(A2, 5, 4, "9999")
```

Syntax: `REPLACE(old_text, start_num, num_chars, new_text)`. Starting at character 5 of A2, overwrite 4 characters with "9999".

## The problem

You need to overwrite part of a code, mask the middle of a phone number, or insert new text at a character position — jobs where counting from the left is clearer than searching for a substring.

## Worked example

Overwrite a product code segment, shorten a string mid-way, then mask part of a phone number.

| | A | B | C |
|---|---|---|---|
| 1 | **Value** | **Replaced** |  |
| 2 | SKU-1042-RED | **SKU-9999-RED** |  |
| 3 | ABCDE | **AXYE** |  |
| 4 | (555) 123-4567 | **(***) 123-4567** | **(555) ***-****** |

Formulas used in the example (results shown in **bold** in the table above):

**B2** — overwrite 4 characters starting at position 5

```excel
=REPLACE(A2, 5, 4, "9999")
```

Result: **SKU-9999-RED**

**B3** — overwrite 3 characters starting at position 2 with "XY"

```excel
=REPLACE(A3, 2, 3, "XY")
```

Result: **AXYE**

**B4** — mask the area code digits

```excel
=REPLACE(A4, 2, 3, "***")
```

Result: **(***) 123-4567**

**C4** — mask the local number after the area code

```excel
=REPLACE(A4, 7, 8, "***-****")
```

Result: **(555) ***-******

<!--AD_IN_ARTICLE-->

## How the formula works

1. Decide the 1-based start position and how many characters to overwrite.
2. Type `=REPLACE(A2, start, length, "new text")` — e.g. `=REPLACE(A2, 5, 4, "9999")`.
3. Press Enter and check that the characters before start_num stayed the same.
4. Use num_chars 0 when you only want to insert text at that position.
5. Fill down the column, or in Google Sheets wrap REPLACE in ARRAYFORMULA for every row at once.

## Excel-specific notes

REPLACE is in every Excel version. start_num is 1-based (1 = first character). num_chars may be 0, which inserts new_text without deleting anything. new_text may be longer or shorter than num_chars — the rest of the string shifts accordingly. REPLACE is not the same as Find & Replace on the ribbon (that searches by content). For content-based swaps use SUBSTITUTE. To overwrite from the right, combine with LEN: `=REPLACE(A2, LEN(A2)-3, 4, "XXXX")` masks the last four characters. Microsoft 365 also has TEXTAFTER / TEXTBEFORE when a delimiter marks the cut instead of a position.

**Insert without deleting (num_chars = 0)**

```excel
=REPLACE(A2, 5, 0, "-")
```

**Mask the last 4 characters**

```excel
=REPLACE(A2, LEN(A2)-3, 4, "XXXX")
```

**Mask digits inside a phone number**

```excel
=REPLACE(A2, 2, 3, "***")
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=REPLACE(A2, 5, 4, "9999")
```

Sheets matches Excel on REPLACE, adds ARRAYFORMULA for column fills, and uses REGEXREPLACE when a regular expression marks the edit better than a start index.

<!--SIBLING-->


## Common errors and how to fix them

- **Wrong characters overwritten** — Off-by-one in start_num (forgetting it is 1-based), or counting visible punctuation differently from the real string. **Fix:** Test LEN and MID on the same cell first to confirm positions, then adjust start_num.
- **#VALUE!** — start_num or num_chars is less than 0, or the source value is an error. **Fix:** Use start_num ≥ 1 and num_chars ≥ 0. Wrap with IFERROR when the source may be blank.
- **Confused with Find & Replace or SUBSTITUTE** — REPLACE edits by position; ribbon Find & Replace and SUBSTITUTE edit by matching text. **Fix:** Switch to SUBSTITUTE when you know the text to find rather than its character index.

## FAQ

### What is the difference between REPLACE and SUBSTITUTE?

REPLACE overwrites by start position and length. SUBSTITUTE finds old_text by content and can limit the change to the N-th match.

### Can REPLACE insert text without deleting anything?

Yes — set num_chars to 0: `=REPLACE(A2, 5, 0, "-")` inserts a dash before the old 5th character.

### Does REPLACE work the same in Google Sheets?

Yes for the four-argument form. Use ARRAYFORMULA for whole-column edits, and REGEXREPLACE when a pattern is clearer than a start index.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
