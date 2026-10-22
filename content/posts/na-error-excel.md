---
title: 'How to Fix the #N/A Error in Excel'
slug: na-error-excel
date: '2026-10-22'
summary: '#N/A means "value not available": a lookup could not find what it was looking
  for. Most of the time the value is there, but it is stored differently, as text
  instead of a number or with an invisible space. This guide shows how to find the
  real cause and fix it, not just hide it.'
tags:
- Fixing formula errors
- Excel
keyword: na-error-excel
niche: sheets-formulas
provider: structured
entry_id: na-error
platform: Excel
category: errors
faq:
- q: Should I just wrap the formula in IFERROR?
  a: Only after you have confirmed the missing values are genuinely missing. Use IFNA
    rather than IFERROR so other problems still show.
- q: Why does
  a: Any
related:
- - vlookup-excel
  - vlookup-google-sheets
- - iferror-excel
  - iferror-google-sheets
- - trim-excel
  - trim-google-sheets
- - xlookup-excel
  - xlookup-google-sheets
- - index-match-excel
  - index-match-google-sheets
sibling: na-error-google-sheets
---
#N/A means "value not available": a lookup could not find what it was looking for. Most of the time the value is there, but it is stored differently, as text instead of a number or with an invisible space. This guide shows how to find the real cause and fix it, not just hide it.

## Quick answer

Use this formula in Excel:

```excel
=VLOOKUP(VALUE(TRIM(D2)), $A$2:$B$5, 2, FALSE)
```

TRIM removes stray spaces and VALUE turns the text "102" into the number 102, so it matches the numeric codes in column A.

## The problem

Your VLOOKUP returns #N/A for codes you can clearly see in the table. The lookup codes were pasted from an email or exported from another system.

## Worked example

The codes in column A are numbers. D2 is the text "102" and D3 is "104 " with a trailing space, so a plain VLOOKUP fails.

| | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 1 | **Code** | **Item** |  | **Lookup value** | **Plain VLOOKUP** | **Fixed** |
| 2 | 101 | Bolts |  | 102 | **#N/A** | **Nuts** |
| 3 | 102 | Nuts |  | `"104 "` | **#N/A** | **Screws** |
| 4 | 103 | Washers |  |  |  |  |
| 5 | 104 | Screws |  |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**E2 (filled to E3)** — plain lookup, filled down

```excel
=VLOOKUP(D2, $A$2:$B$5, 2, FALSE)
```

Results: **#N/A**, **#N/A**

**F2 (filled to F3)** — cleaned lookup value, filled down

```excel
=VLOOKUP(VALUE(TRIM(D2)), $A$2:$B$5, 2, FALSE)
```

Results: **Nuts**, **Screws**

<!--AD_IN_ARTICLE-->

## How the formula works

1. #N/A from VLOOKUP, XLOOKUP, MATCH or HLOOKUP means the exact value was not found in the lookup column.
2. Test the suspicion directly: `=D2=A3` returns FALSE even though both show 102, and `=ISTEXT(D2)` returns TRUE.
3. `TRIM(D2)` removes the trailing space from "104 ".
4. `VALUE(...)` converts the cleaned text into a real number that matches column A.
5. Once the data is fixed at the source, you can go back to the plain formula, and wrap it in IFNA only for values that are genuinely missing.

## Excel-specific notes

Excel marks numbers stored as text with a small green triangle; select the cells and choose "Convert to Number" to fix them permanently. Non-breaking spaces (character 160, common in data copied from web pages) are not removed by TRIM; use `SUBSTITUTE(D2, CHAR(160), "")` first. If the codes in the table are text and the lookup value is a number, convert the other way with `TEXT(D2, "0")` or `D2&""`.

**Handle non-breaking spaces from web data**

```excel
=VLOOKUP(VALUE(TRIM(SUBSTITUTE(D2, CHAR(160), ""))), $A$2:$B$5, 2, FALSE)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=VLOOKUP(VALUE(TRIM(D2)), $A$2:$B$5, 2, FALSE)
```

Google Sheets needs the same fix. Hover over the error to read the exact message.

<!--SIBLING-->


## Common errors and how to fix them

- **Number vs text** — One side is the number 102, the other the text "102". **Fix:** Convert one side with VALUE() or TEXT(), or convert the whole column.
- **Extra or invisible spaces** — Trailing spaces or non-breaking spaces from copied web data. **Fix:** Use TRIM, and SUBSTITUTE(..., CHAR(160), "") for non-breaking spaces.
- **Approximate match on unsorted data** — The last argument of VLOOKUP / MATCH was omitted. **Fix:** Use FALSE (VLOOKUP) or 0 (MATCH) for exact matches.
- **Lookup range does not include the value** — The table range stops before the last row, or the range shifted when copied because it was not locked. **Fix:** Lock the range with $ or use an Excel Table / open-ended range.

## FAQ

### Should I just wrap the formula in IFERROR?

Only after you have confirmed the missing values are genuinely missing. Use IFNA rather than IFERROR so other problems still show.

### Why does

Any

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
