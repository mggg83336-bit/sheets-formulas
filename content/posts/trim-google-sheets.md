---
title: How to Remove Extra Spaces with TRIM in Google Sheets
slug: trim-google-sheets
date: '2026-11-02'
summary: TRIM removes leading and trailing spaces and reduces runs of spaces between
  words to a single space. It fixes failed lookups and duplicate-looking values. This
  guide also covers the non-breaking spaces that TRIM cannot remove on its own.
tags:
- Text formulas
- Google Sheets
keyword: trim-google-sheets
niche: sheets-formulas
provider: structured
entry_id: trim
platform: Google Sheets
category: text
faq:
- q: Does TRIM remove single spaces between words?
  a: No. It keeps one space between words and only removes extra ones.
- q: How do I remove all spaces?
  a: Use =SUBSTITUTE(A2, " ", "").
- q: Why does my lookup still fail after TRIM?
  a: 'Check whether one side is a number and the other text: TRIM always returns text,
    so a trimmed "102" will not match the number 102. Wrap it in VALUE, or compare
    with =ISNUMBER() on both sides to see which is which.'
related:
- - na-error-google-sheets
  - na-error-excel
- - text-before-character-google-sheets
  - text-before-character-excel
- - split-text-google-sheets
  - split-text-excel
- - leading-zeros-google-sheets
  - leading-zeros-excel
sibling: trim-excel
---
TRIM removes leading and trailing spaces and reduces runs of spaces between words to a single space. It fixes failed lookups and duplicate-looking values. This guide also covers the non-breaking spaces that TRIM cannot remove on its own.

## Quick answer

Use this formula in Google Sheets:

```excel
=TRIM(A2)
```

Same TRIM function in Google Sheets: it strips leading and trailing spaces and collapses repeated spaces between words to a single space, which fixes most failed lookup matches.

## The problem

Names imported from a CRM have random extra spaces, so "Ana Lopez" and " Ana  Lopez" are treated as different people and lookups fail.

## Worked example

The quotes show the hidden spaces in the raw values.

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **Raw name** | **Trimmed** | **Length before** | **Length after** |
| 2 | `"  Ana   Lopez "` | **Ana Lopez** | **14** | **9** |
| 3 | `" Ben Carter"` | **Ben Carter** | **11** | **10** |
| 4 | `"Chloe  Wong  "` | **Chloe Wong** | **13** | **10** |

Formulas used in the example (results shown in **bold** in the table above):

**B2 (filled to B4)** — filled down

```excel
=TRIM(A2)
```

Results: **Ana Lopez**, **Ben Carter**, **Chloe Wong**

**C2 (filled to C4)**

```excel
=LEN(A2)
```

Results: **14**, **11**, **13**

**D2 (filled to D4)**

```excel
=LEN(B2)
```

Results: **9**, **10**, **10**

<!--AD_IN_ARTICLE-->

## How the formula works

1. TRIM deletes every space before the first character and after the last one.
2. Runs of two or more spaces between words become one space.
3. LEN shows the effect: "  Ana   Lopez " has 14 characters, "Ana Lopez" has 9.
4. Use the trimmed column for lookups, or clean the lookup value inside the formula: `VLOOKUP(TRIM(F2), ...)`.

## Google Sheets-specific notes

Google Sheets has a menu shortcut that does not need a helper column: select the range and choose Data > Data cleanup > Trim whitespace. It edits the cells in place. For a formula that cleans a whole column at once, use `=ARRAYFORMULA(TRIM(A2:A))`. To strip every kind of whitespace, including non-breaking spaces and tabs, REGEXREPLACE works well: `=TRIM(REGEXREPLACE(A2, "\s+", " "))`. After cleaning, copy the results and use Paste special > Values only if you want to replace the original messy column.

**Whole column with one formula**

```excel
=ARRAYFORMULA(TRIM(A2:A))
```

**Collapse all whitespace characters**

```excel
=TRIM(REGEXREPLACE(A2, "\s+", " "))
```

**Also remove non-breaking spaces with CHAR**

```excel
=TRIM(SUBSTITUTE(A2, CHAR(160), " "))
```


## Excel version

The same formula works unchanged in Excel:

```excel
=TRIM(A2)
```

Excel uses the identical TRIM function.

<!--SIBLING-->


## Common errors and how to fix them

- **Spaces still there** — They are non-breaking spaces (CHAR(160)) from web data. **Fix:** SUBSTITUTE(A2, CHAR(160), " ") before TRIM.
- **Numbers become text** — TRIM always returns text, so trimmed numbers no longer add up. **Fix:** Wrap in VALUE, e.g. =VALUE(TRIM(A2)).
- **Line breaks remain** — TRIM does not remove line feeds (CHAR(10)). **Fix:** Use CLEAN, or SUBSTITUTE(A2, CHAR(10), " ").

## FAQ

### Does TRIM remove single spaces between words?

No. It keeps one space between words and only removes extra ones.

### How do I remove all spaces?

Use =SUBSTITUTE(A2, " ", "").

### Why does my lookup still fail after TRIM?

Check whether one side is a number and the other text: TRIM always returns text, so a trimmed "102" will not match the number 102. Wrap it in VALUE, or compare with =ISNUMBER() on both sides to see which is which.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
