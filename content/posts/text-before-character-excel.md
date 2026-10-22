---
title: How to Extract Text Before a Character in Excel
slug: text-before-character-excel
date: '2026-10-22'
summary: 'Get everything before a character such as "@", "-" or a space: the username
  part of an email, a first name, or a product prefix. Excel 365 has TEXTBEFORE; LEFT
  with FIND works everywhere, and Google Sheets can use REGEXEXTRACT.'
tags:
- Text formulas
- Excel
keyword: text-before-character-excel
niche: sheets-formulas
provider: structured
entry_id: text-before-character
platform: Excel
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
- - text-after-character-excel
  - text-after-character-google-sheets
- - split-text-excel
  - split-text-google-sheets
- - trim-excel
  - trim-google-sheets
- - contains-text-excel
  - contains-text-google-sheets
sibling: text-before-character-google-sheets
---
Get everything before a character such as "@", "-" or a space: the username part of an email, a first name, or a product prefix. Excel 365 has TEXTBEFORE; LEFT with FIND works everywhere, and Google Sheets can use REGEXEXTRACT.

## Quick answer

Use this formula in Excel:

```excel
=TEXTBEFORE(A2, "@")
```

Syntax: `TEXTBEFORE(text, delimiter, [instance_num], [match_mode], [match_end], [if_not_found])`. Returns the text before the first "@".

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
=TEXTBEFORE(A2, "@")
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

## Excel-specific notes

TEXTBEFORE needs Microsoft 365, Excel 2024 or Excel for the web. Use a negative instance number to count from the end: `TEXTBEFORE(A2, ".", -1)` returns everything before the last dot. The if_not_found argument avoids #N/A when the character is missing. In any other version use LEFT with FIND; FIND returns the position of the character and LEFT takes everything before it.

**Any Excel version**

```excel
=LEFT(A2, FIND("@", A2)-1)
```

**Before the LAST occurrence (Microsoft 365)**

```excel
=TEXTBEFORE(A2, ".", -1)
```


## Google Sheets version

In Google Sheets, use:

```excel
=LEFT(A2, FIND("@", A2)-1)
```

Google Sheets has no TEXTBEFORE, so LEFT with FIND (or REGEXEXTRACT) is the way there.

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
