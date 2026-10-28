---
title: How to Use the SUBSTITUTE Function in Excel
slug: substitute-excel
date: '2026-10-28'
summary: SUBSTITUTE replaces every occurrence of a text string with another, or only
  the N-th occurrence when you pass an instance number. It is the right tool when
  you know the text to find (a dash, a word, a typo) rather than a character position.
  Excel and Google Sheets share the same SUBSTITUTE syntax; S
tags:
- Text formulas
- Excel
keyword: substitute-excel
niche: sheets-formulas
provider: structured
entry_id: substitute
platform: Excel
category: text
faq:
- q: When should I use SUBSTITUTE instead of REPLACE?
  a: Use SUBSTITUTE when you know the text to find. Use REPLACE when you know the
    starting position and how many characters to overwrite.
- q: Is SUBSTITUTE case-sensitive?
  a: Yes. "SS" will not replace "ss". In Google Sheets, REGEXREPLACE with a case-insensitive
    flag (?i) can ignore case; in Excel, normalize with UPPER/LOWER first.
- q: Can I replace several different strings at once?
  a: Nest SUBSTITUTE calls, one per string. In Google Sheets, a single REGEXREPLACE
    with an alternation pattern can also cover several literals.
related:
- - replace-excel
  - replace-google-sheets
- - left-right-mid-excel
  - left-right-mid-google-sheets
- - trim-excel
  - trim-google-sheets
- - textsplit-excel
sibling: substitute-google-sheets
---
SUBSTITUTE replaces every occurrence of a text string with another, or only the N-th occurrence when you pass an instance number. It is the right tool when you know the text to find (a dash, a word, a typo) rather than a character position. Excel and Google Sheets share the same SUBSTITUTE syntax; Sheets also offers REGEXREPLACE for pattern-based swaps.

## Quick answer

Use this formula in Excel:

```excel
=SUBSTITUTE(A2, "-", "/")
```

Syntax: `SUBSTITUTE(text, old_text, new_text, [instance_num])`. Replace every "-" in A2 with "/". Omit instance_num to change all matches; pass 1, 2, … to change only that match.

## The problem

A column holds codes, names or phrases where one piece of text must change everywhere — turn dashes into slashes, fix a repeated typo, or swap only the first match — without touching surrounding characters the way a position-based REPLACE would.

## Worked example

Swap every dash for a slash, fix letters in a word, then change only the first match.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Text** | **Find** | **Replace with** | **All matches** | **First only** |
| 2 | SKU-1042-RED | - | / | **SKU/1042/RED** |  |
| 3 | banana | a | o | **bonono** |  |
| 4 | Miss Mississippi | ss | XX | **MiXX MiXXiXXippi** | **MiXX Mississippi** |

Formulas used in the example (results shown in **bold** in the table above):

**D2** — every dash becomes a slash

```excel
=SUBSTITUTE(A2, B2, C2)
```

Result: **SKU/1042/RED**

**D3** — every "a" becomes "o"

```excel
=SUBSTITUTE(A3, B3, C3)
```

Result: **bonono**

**D4** — every "ss" becomes "XX"

```excel
=SUBSTITUTE(A4, B4, C4)
```

Result: **MiXX MiXXiXXippi**

**E4** — only the first "ss"

```excel
=SUBSTITUTE(A4, B4, C4, 1)
```

Result: **MiXX Mississippi**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Type `=SUBSTITUTE(` and select the cell that holds the original text (A2).
2. Add the text to find in quotes (or a cell reference), a comma, then the replacement text.
3. Close the parenthesis and press Enter — every match is replaced.
4. To change only the N-th match, pass a fourth argument: `=SUBSTITUTE(A2, "ss", "XX", 1)`.
5. Nest another SUBSTITUTE when you need to swap more than one different string in the same cell.

## Excel-specific notes

SUBSTITUTE is available in every Excel version. Matching is case-sensitive: "SS" will not replace "ss". new_text may be empty (`""`) to delete old_text. Nest SUBSTITUTE calls to swap several different strings in one formula. For a character-position edit (overwrite 4 characters starting at position 5) use REPLACE instead. In Microsoft 365, TEXTBEFORE / TEXTAFTER / TEXTSPLIT often remove the need to strip delimiters by hand. After a mass replace, Copy > Paste Special > Values if you want to freeze the results.

**Replace only the first match**

```excel
=SUBSTITUTE(A2, "ss", "XX", 1)
```

**Delete every dash**

```excel
=SUBSTITUTE(A2, "-", "")
```

**Nested — swap two different strings**

```excel
=SUBSTITUTE(SUBSTITUTE(A2, "-", "/"), "_", "-")
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=SUBSTITUTE(A2, "-", "/")
```

Sheets matches Excel on SUBSTITUTE, adds ARRAYFORMULA for column fills, and uses REGEXREPLACE where Excel has no regex equivalent.

<!--SIBLING-->


## Common errors and how to fix them

- **Nothing changed** — old_text did not match exactly — wrong case, extra spaces, or a different dash character. **Fix:** Copy the exact characters from the source cell, or use TRIM / CLEAN first. Matching is case-sensitive.
- **Too many (or the wrong) matches changed** — instance_num was omitted, so every occurrence was replaced. **Fix:** Pass the occurrence number you want (1 = first, 2 = second, …), or nest SUBSTITUTE for a more specific swap.
- **#VALUE!** — instance_num is less than 1, or the formula references an error cell. **Fix:** Use a positive integer for instance_num, and wrap with IFERROR if the source may be blank or invalid.

## FAQ

### When should I use SUBSTITUTE instead of REPLACE?

Use SUBSTITUTE when you know the text to find. Use REPLACE when you know the starting position and how many characters to overwrite.

### Is SUBSTITUTE case-sensitive?

Yes. "SS" will not replace "ss". In Google Sheets, REGEXREPLACE with a case-insensitive flag `(?i)` can ignore case; in Excel, normalize with UPPER/LOWER first.

### Can I replace several different strings at once?

Nest SUBSTITUTE calls, one per string. In Google Sheets, a single REGEXREPLACE with an alternation pattern can also cover several literals.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
