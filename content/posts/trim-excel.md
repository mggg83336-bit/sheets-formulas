---
title: How to Remove Extra Spaces with TRIM in Excel
slug: trim-excel
date: '2026-10-22'
summary: TRIM removes leading and trailing spaces and reduces runs of spaces between
  words to a single space. It fixes failed lookups and duplicate-looking values. This
  guide also covers the non-breaking spaces that TRIM cannot remove on its own.
tags:
- Text formulas
- Excel
keyword: trim-excel
niche: sheets-formulas
provider: structured
entry_id: trim
platform: Excel
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
- - na-error-excel
  - na-error-google-sheets
- - text-before-character-excel
  - text-before-character-google-sheets
- - split-text-excel
  - split-text-google-sheets
- - leading-zeros-excel
  - leading-zeros-google-sheets
sibling: trim-google-sheets
---
TRIM removes leading and trailing spaces and reduces runs of spaces between words to a single space. It fixes failed lookups and duplicate-looking values. This guide also covers the non-breaking spaces that TRIM cannot remove on its own.

## Quick answer

Use this formula in Excel:

```excel
=TRIM(A2)
```

Removes spaces at the start and end and leaves single spaces between words.

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

## Excel-specific notes

Excel's TRIM only removes the normal space character (code 32). Text copied from web pages often contains non-breaking spaces (code 160), which look identical but survive TRIM; replace them first with SUBSTITUTE. CLEAN removes non-printing control characters such as line feeds from older systems. After cleaning, use Copy > Paste Special > Values to replace the original column if you no longer need the formula.

**Also remove non-breaking spaces and control characters**

```excel
=TRIM(CLEAN(SUBSTITUTE(A2, CHAR(160), " ")))
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=TRIM(A2)
```

Google Sheets uses the same TRIM function and also offers Data > Data cleanup > Trim whitespace.

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
