---
title: How to Extract Text After a Character in Excel
slug: text-after-character-excel
date: '2026-10-22'
summary: Return everything after the first or the last occurrence of a character,
  for example the size code at the end of a SKU or the domain of an email address.
  Covers TEXTAFTER (Excel 365), MID with FIND (all versions) and REGEXEXTRACT (Google
  Sheets).
tags:
- Text formulas
- Excel
keyword: text-after-character-excel
niche: sheets-formulas
provider: structured
entry_id: text-after-character
platform: Excel
category: text
faq:
- q: How do I get the domain from an email address?
  a: Use the text after "@", e.g. =MID(A2, FIND("@", A2)+1, LEN(A2)) or =TEXTAFTER(A2,
    "@").
- q: How do I get the text after the second dash?
  a: In Excel 365 use =TEXTAFTER(A2, "-", 2). In other versions, nest FIND, e.g. =MID(A2,
    FIND("-", A2, FIND("-", A2)+1)+1, LEN(A2)).
related:
- - text-before-character-excel
  - text-before-character-google-sheets
- - split-text-excel
  - split-text-google-sheets
- - trim-excel
  - trim-google-sheets
- - textjoin-excel
  - textjoin-google-sheets
sibling: text-after-character-google-sheets
---
Return everything after the first or the last occurrence of a character, for example the size code at the end of a SKU or the domain of an email address. Covers TEXTAFTER (Excel 365), MID with FIND (all versions) and REGEXEXTRACT (Google Sheets).

## Quick answer

Use this formula in Excel:

```excel
=TEXTAFTER(A2, "-")
```

Returns the text after the first "-". Use -1 as the third argument to start from the last dash instead.

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
=TEXTAFTER(A2, "-")
```

Results: **RED-XL**, **BLUE-M**, **GREEN-S**

**C2 (filled to C4)** — Excel 365, filled down

```excel
=TEXTAFTER(A2, "-", -1)
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

## Excel-specific notes

TEXTAFTER is available in Microsoft 365, Excel 2024 and Excel for the web. In older versions use MID with FIND for the first occurrence. For the last occurrence, the RIGHT/SUBSTITUTE/REPT trick works in every version: it pads every dash with 100 spaces, takes the last 100 characters and trims them, leaving the final part.

**After the LAST dash (Microsoft 365)**

```excel
=TEXTAFTER(A2, "-", -1)
```

**After the first dash, any version**

```excel
=MID(A2, FIND("-", A2)+1, LEN(A2))
```

**After the last dash, any version**

```excel
=TRIM(RIGHT(SUBSTITUTE(A2, "-", REPT(" ", 100)), 100))
```


## Google Sheets version

In Google Sheets, use:

```excel
=MID(A2, FIND("-", A2)+1, LEN(A2))
```

Google Sheets has no TEXTAFTER; use MID/FIND or REGEXEXTRACT there.

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
