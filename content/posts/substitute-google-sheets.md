---
title: How to Use the SUBSTITUTE Function in Google Sheets
slug: substitute-google-sheets
date: '2026-10-28'
summary: SUBSTITUTE replaces every occurrence of a text string with another, or only
  the N-th occurrence when you pass an instance number. It is the right tool when
  you know the text to find (a dash, a word, a typo) rather than a character position.
  Excel and Google Sheets share the same SUBSTITUTE syntax; S
tags:
- Text formulas
- Google Sheets
keyword: substitute-google-sheets
niche: sheets-formulas
provider: structured
entry_id: substitute
platform: Google Sheets
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
- - replace-google-sheets
  - replace-excel
- - left-right-mid-google-sheets
  - left-right-mid-excel
- - trim-google-sheets
  - trim-excel
- - textsplit-excel
sibling: substitute-excel
---
SUBSTITUTE replaces every occurrence of a text string with another, or only the N-th occurrence when you pass an instance number. It is the right tool when you know the text to find (a dash, a word, a typo) rather than a character position. Excel and Google Sheets share the same SUBSTITUTE syntax; Sheets also offers REGEXREPLACE for pattern-based swaps.

## Quick answer

Use this formula in Google Sheets:

```excel
=SUBSTITUTE(A2, "-", "/")
```

Same SUBSTITUTE syntax in Google Sheets as in Excel.

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

## Google Sheets-specific notes

SUBSTITUTE works the same way in Google Sheets, including the optional instance_num argument and case-sensitive matching. To fill a whole column at once wrap it in ARRAYFORMULA, e.g. `=ARRAYFORMULA(IF(A2:A="", "", SUBSTITUTE(A2:A, "-", "/")))`. For pattern-based swaps — digits, optional spaces, word boundaries — use REGEXREPLACE instead: `=REGEXREPLACE(A2, "\s+", " ")` collapses runs of whitespace, and `=REGEXREPLACE(A2, "[^0-9]", "")` strips non-digits. REGEXREPLACE has no instance_num; craft the pattern (or use SUBSTITUTE) when you need only the N-th match. Nested SUBSTITUTE still works when you are swapping fixed literal strings.

**Whole column with ARRAYFORMULA**

```excel
=ARRAYFORMULA(IF(A2:A="", "", SUBSTITUTE(A2:A, "-", "/")))
```

**Collapse repeated spaces with REGEXREPLACE**

```excel
=REGEXREPLACE(A2, "\s+", " ")
```

**Strip every non-digit with REGEXREPLACE**

```excel
=REGEXREPLACE(A2, "[^0-9]", "")
```


## Excel version

The same formula works unchanged in Excel:

```excel
=SUBSTITUTE(A2, "-", "/")
```

Excel and Sheets share SUBSTITUTE. Sheets adds REGEXREPLACE for regular-expression replacements; Excel has no built-in regex function.

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
