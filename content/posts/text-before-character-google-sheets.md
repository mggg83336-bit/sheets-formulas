---
title: How to Extract Text Before a Character in Google Sheets
slug: text-before-character-google-sheets
date: '2026-10-26'
summary: 'Get everything before a character such as "@", "-" or a space: the username
  part of an email, a first name, or a product prefix. Excel 365 has TEXTBEFORE; LEFT
  with FIND works everywhere, and Google Sheets can use REGEXEXTRACT.'
tags:
- Text formulas
- Google Sheets
keyword: text-before-character-google-sheets
niche: sheets-formulas
provider: structured
entry_id: text-before-character
platform: Google Sheets
category: text
faq:
- q: Is FIND case-sensitive?
  a: Yes. Use SEARCH for a case-insensitive position; it also supports wildcards.
- q: How do I get the first word of a cell?
  a: Use a space as the character, =LEFT(A2, FIND(" ", A2&" ")-1). Adding a space
    to A2 avoids an error for single words.
- q: How do I get the text before a space, comma or line break?
  a: 'Replace "@" with the character you need: " " for a space, "," for a comma, or
    CHAR(10) for a line break inside the cell, e.g. =LEFT(A2, FIND(CHAR(10), A2)-1).'
related:
- - text-after-character-google-sheets
  - text-after-character-excel
- - split-text-google-sheets
  - split-text-excel
- - trim-google-sheets
  - trim-excel
- - contains-text-google-sheets
  - contains-text-excel
sibling: text-before-character-excel
---
Get everything before a character such as "@", "-" or a space: the username part of an email, a first name, or a product prefix. Excel 365 has TEXTBEFORE; LEFT with FIND works everywhere, and Google Sheets can use REGEXEXTRACT.

## Quick answer

Use this formula in Google Sheets:

```excel
=LEFT(A2, FIND("@", A2)-1)
```

FIND returns the position of "@"; LEFT takes all characters before it.

## The problem

You have a column of email addresses and need the part before the @ sign in a separate column.

## Worked example

Extract the username before the @.

| | A | B | C |
|---|---|---|---|
| 1 | **Email** | **TEXTBEFORE** | **LEFT + FIND** |
| 2 | ana.lopez@acme.com | **ana.lopez** | **ana.lopez** |
| 3 | ben@globex.io | **ben** | **ben** |
| 4 | chloe.wong@initech.co | **chloe.wong** | **chloe.wong** |

Formulas used in the example (results shown in **bold** in the table above):

**B2 (filled to B4)** — Excel 365, filled down

```excel
=REGEXEXTRACT(A2, "^[^@]+")
```

Results: **ana.lopez**, **ben**, **chloe.wong**

**C2 (filled to C4)** — works everywhere, filled down

```excel
=LEFT(A2, FIND("@", A2)-1)
```

Results: **ana.lopez**, **ben**, **chloe.wong**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `FIND("@", A2)` returns the position of the @ sign: 10 in ana.lopez@acme.com.
2. `-1` excludes the @ itself, so LEFT takes 9 characters.
3. `LEFT(A2, 9)` returns ana.lopez.
4. TEXTBEFORE does the same in one step and can count occurrences from either end.

## Google Sheets-specific notes

Google Sheets does not have TEXTBEFORE; typing it returns #NAME?. LEFT with FIND is the standard replacement. REGEXEXTRACT is the more flexible Sheets option: `^[^@]+` means "from the start, every character that is not @". Regular expressions also make it easy to take the text before the last occurrence: `=REGEXEXTRACT(A2, "(.*)\.")` is greedy and stops at the final dot. Note that REGEXEXTRACT only works on text, so convert numbers with A2&"".

**REGEXEXTRACT version**

```excel
=REGEXEXTRACT(A2, "^[^@]+")
```

**Before the last dot**

```excel
=REGEXEXTRACT(A2, "(.*)\.")
```


## Excel version

In Excel, use:

```excel
=TEXTBEFORE(A2, "@")
```

TEXTBEFORE exists only in Excel (Microsoft 365 / 2024); Google Sheets does not have it.

<!--SIBLING-->


## Common errors and how to fix them

- **#VALUE!** — FIND did not find the character in that cell (e.g. an empty cell or a value without @). **Fix:** Wrap in IFERROR, or in Excel 365 use if_not_found: =TEXTBEFORE(A2, "@", , , , "").
- **#NAME? in Google Sheets** — TEXTBEFORE is an Excel-only function. **Fix:** Use LEFT/FIND or REGEXEXTRACT.
- **Wrong part when the character is not unique** — FIND returns the first occurrence. **Fix:** Use TEXTBEFORE with -1 (Excel 365) or a greedy regular expression (Google Sheets) for the last occurrence.

## FAQ

### Is FIND case-sensitive?

Yes. Use SEARCH for a case-insensitive position; it also supports wildcards.

### How do I get the first word of a cell?

Use a space as the character, =LEFT(A2, FIND(" ", A2&" ")-1). Adding a space to A2 avoids an error for single words.

### How do I get the text before a space, comma or line break?

Replace "@" with the character you need: " " for a space, "," for a comma, or CHAR(10) for a line break inside the cell, e.g. =LEFT(A2, FIND(CHAR(10), A2)-1).

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
