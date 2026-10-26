---
title: How to Extract Text After a Character in Google Sheets
slug: text-after-character-google-sheets
date: '2026-10-26'
summary: Return everything after the first or the last occurrence of a character,
  for example the size code at the end of a SKU or the domain of an email address.
  Covers TEXTAFTER (Excel 365), MID with FIND (all versions) and REGEXEXTRACT (Google
  Sheets).
tags:
- Text formulas
- Google Sheets
keyword: text-after-character-google-sheets
niche: sheets-formulas
provider: structured
entry_id: text-after-character
platform: Google Sheets
category: text
faq:
- q: How do I get the domain from an email address?
  a: Use the text after "@", e.g. =MID(A2, FIND("@", A2)+1, LEN(A2)) or =TEXTAFTER(A2,
    "@").
- q: How do I get the text after the second dash?
  a: In Excel 365 use =TEXTAFTER(A2, "-", 2). In other versions, nest FIND, e.g. =MID(A2,
    FIND("-", A2, FIND("-", A2)+1)+1, LEN(A2)).
related:
- - text-before-character-google-sheets
  - text-before-character-excel
- - split-text-google-sheets
  - split-text-excel
- - trim-google-sheets
  - trim-excel
- - textjoin-google-sheets
  - textjoin-excel
sibling: text-after-character-excel
---
Return everything after the first or the last occurrence of a character, for example the size code at the end of a SKU or the domain of an email address. Covers TEXTAFTER (Excel 365), MID with FIND (all versions) and REGEXEXTRACT (Google Sheets).

## Quick answer

Use this formula in Google Sheets:

```excel
=MID(A2, FIND("-", A2)+1, LEN(A2))
```

FIND locates the first dash; MID returns everything from the next character on.

## The problem

Product codes look like SKU-RED-XL. You need the part after the first dash (RED-XL) and, separately, just the size after the last dash (XL).

## Worked example

Four ways to split the SKU.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **SKU** | **TEXTAFTER first** | **TEXTAFTER last** | **MID + FIND** | **RIGHT + SUBSTITUTE** |
| 2 | SKU-RED-XL | **RED-XL** | **XL** | **RED-XL** | **XL** |
| 3 | SKU-BLUE-M | **BLUE-M** | **M** | **BLUE-M** | **M** |
| 4 | SKU-GREEN-S | **GREEN-S** | **S** | **GREEN-S** | **S** |

Formulas used in the example (results shown in **bold** in the table above):

**B2 (filled to B4)** — Excel 365, filled down

```excel
=REGEXEXTRACT(A2, "-(.*)")
```

Results: **RED-XL**, **BLUE-M**, **GREEN-S**

**C2 (filled to C4)** — Excel 365, filled down

```excel
=REGEXEXTRACT(A2, "[^-]+$")
```

Results: **XL**, **M**, **S**

**D2 (filled to D4)** — after first dash, any version

```excel
=MID(A2, FIND("-", A2)+1, LEN(A2))
```

Results: **RED-XL**, **BLUE-M**, **GREEN-S**

**E2 (filled to E4)** — after last dash, any version

```excel
=TRIM(RIGHT(SUBSTITUTE(A2, "-", REPT(" ", 100)), 100))
```

Results: **XL**, **M**, **S**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `FIND("-", A2)` returns 4, the position of the first dash in SKU-RED-XL.
2. `MID(A2, 5, LEN(A2))` starts at the character after the dash and takes up to the full length, which simply means "to the end".
3. For the last part, SUBSTITUTE turns each dash into 100 spaces; RIGHT(..., 100) grabs the final block, which contains only spaces and "XL".
4. TRIM removes the spaces, leaving XL.

## Google Sheets-specific notes

Google Sheets has no TEXTAFTER. Besides MID with FIND, REGEXEXTRACT handles both cases neatly: `-(.*)` captures everything after the first dash, and `[^-]+$` matches the last group of characters that contains no dash, i.e. everything after the final dash. A third option for the last part is `=INDEX(SPLIT(A2, "-"), COUNTA(SPLIT(A2, "-")))`.

**After the first dash with REGEXEXTRACT**

```excel
=REGEXEXTRACT(A2, "-(.*)")
```

**After the last dash with REGEXEXTRACT**

```excel
=REGEXEXTRACT(A2, "[^-]+$")
```


## Excel version

In Excel, use:

```excel
=TEXTAFTER(A2, "-")
```

Excel 365 has TEXTAFTER (use -1 for the last occurrence). Google Sheets does not.

<!--SIBLING-->


## Common errors and how to fix them

- **#VALUE!** — The character does not occur in the cell. **Fix:** Wrap in IFERROR(..., A2) to return the original text, or use TEXTAFTER's if_not_found argument.
- **Returns the wrong segment** — FIND always finds the first occurrence. **Fix:** Use TEXTAFTER with -1, the RIGHT/SUBSTITUTE trick, or "[^-]+$" in Google Sheets.
- **Part longer than 100 characters is cut off** — The REPT(" ", 100) padding is too short. **Fix:** Use a larger number such as 500 in both places.

## FAQ

### How do I get the domain from an email address?

Use the text after "@", e.g. =MID(A2, FIND("@", A2)+1, LEN(A2)) or =TEXTAFTER(A2, "@").

### How do I get the text after the second dash?

In Excel 365 use =TEXTAFTER(A2, "-", 2). In other versions, nest FIND, e.g. =MID(A2, FIND("-", A2, FIND("-", A2)+1)+1, LEN(A2)).

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
