---
title: How to Use IFERROR (and IFNA) in Excel
slug: iferror-excel
date: '2026-10-22'
summary: 'IFERROR replaces any error result (#DIV/0!, #N/A, #VALUE! and so on) with
  a value you choose. IFNA only catches #N/A, which makes it safer for lookups. This
  page shows when to use each and why wrapping everything in IFERROR can hide real
  problems.'
tags:
- Logic & error handling
- Excel
keyword: iferror-excel
niche: sheets-formulas
provider: structured
entry_id: iferror
platform: Excel
category: logic
faq:
- q: What is the difference between IFERROR and IFNA?
  a: IFERROR catches all error types. IFNA catches only
- q: Can IFERROR return a blank cell?
  a: It can return an empty string with "" (both apps). In Google Sheets you can also
    omit the second argument.
- q: Should a lookup use IFERROR or XLOOKUP if_not_found?
  a: 'Prefer XLOOKUP''s if_not_found argument, or IFNA, for a missing key. Both replace
    only the not-found result. IFERROR also hides #REF! and #NAME?, so a broken range
    can look like a blank cell. if_not_found does not turn a found-but-empty cell
    into a blank; that cell still comes back as 0.'
related:
- - na-error-excel
  - na-error-google-sheets
- - xlookup-excel
  - xlookup-google-sheets
- - vlookup-excel
  - vlookup-google-sheets
- - div0-error-excel
  - div0-error-google-sheets
- - value-error-excel
  - value-error-google-sheets
sibling: iferror-google-sheets
---
IFERROR replaces any error result (#DIV/0!, #N/A, #VALUE! and so on) with a value you choose. IFNA only catches #N/A, which makes it safer for lookups. This page shows when to use each and why wrapping everything in IFERROR can hide real problems.

## Quick answer

Use this formula in Excel:

```excel
=IFERROR(B2/C2, "n/a")
```

Syntax: `IFERROR(value, value_if_error)`. If B2/C2 is an error, show "n/a", otherwise show the result of the division.

<!--CTA_PROMINENT-->

## XLOOKUP if_not_found instead of IFERROR

For a lookup, the modern replacement for IFERROR is XLOOKUP's `if_not_found` argument. It substitutes a value only when the key is missing. Every other error still shows:

```excel
=XLOOKUP(F2, $A$2:$A$6, $C$2:$C$6, "")
```

`""` returns a blank cell for a missing key. `"Not found"` returns words. This does not turn a found-but-empty cell into a blank. That cell still comes back as 0. To blank empty cells and keep a real 0, blank the return range, as shown on the [XLOOKUP](../xlookup-excel/) page.

IFNA around VLOOKUP is the same idea when you cannot use XLOOKUP:

```excel
=IFNA(VLOOKUP(F2, $A$2:$D$6, 3, FALSE), "")
```

IFERROR around that VLOOKUP would also hide #REF! and #NAME?. Prefer IFNA or `if_not_found` so a broken range stays visible. The usual reasons for the #N/A you are replacing are listed under [the #N/A error](../na-error-excel/), including a lookup aimed at [another sheet](../vlookup-another-sheet-excel/).

## The problem

A price-per-unit column shows #DIV/0! whenever units are 0 or blank, and a lookup shows #N/A for products that are not in the list. Both make the report look broken.

## Worked example

Price per unit with missing units, and a lookup for a product that does not exist.

| | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 1 | **Product** | **Revenue** | **Units** | **Per unit** |  | **Lookup** |
| 2 | Mouse | 1250 | 50 | **25** |  | **Not listed** |
| 3 | Hub | 0 | 0 | **n/a** |  |  |
| 4 | Stand | 960 | 24 | **40** |  |  |
| 5 | Lamp | 555 |  | **n/a** |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**D2 (filled to D5)** — filled down to D5

```excel
=IFERROR(B2/C2, "n/a")
```

Results: **25**, **n/a**, **40**, **n/a**

**F2** — IFNA around a lookup for "Webcam"

```excel
=IFNA(VLOOKUP("Webcam", A2:C5, 2, FALSE), "Not listed")
```

Result: **Not listed**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `B2/C2` is calculated first. For Hub (0 units) and Lamp (blank units) it returns #DIV/0!.
2. IFERROR checks whether that result is any kind of error. If it is, the second argument ("n/a") is shown instead.
3. For valid rows the original result passes through unchanged: 1250/50 = 25, 960/24 = 40.
4. IFNA works the same way but only reacts to

## Excel-specific notes

IFERROR catches every error type, including ones caused by typos (#NAME?) or broken references (#REF!), so a mistake in your formula can turn into a quiet "n/a" that nobody notices. Prefer IFNA around lookups, which only hides "not found", and test for the specific condition where you can (`=IF(C2=0, "n/a", B2/C2)`). IFNA is available from Excel 2013.

**Test the cause instead of hiding all errors**

```excel
=IF(C2=0, "n/a", B2/C2)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=IFERROR(B2/C2, "n/a")
```

Google Sheets uses the same functions; there the second IFERROR argument is optional (a blank is returned on error).

<!--SIBLING-->


## Common errors and how to fix them

- **Real mistakes hidden** — IFERROR also hides **Fix:** Use IFNA for lookups and a specific IF test for division.
- **Totals ignore hidden problems** — Returning 0 or "" from IFERROR makes rows silently drop out of sums and averages. **Fix:** Return a visible marker such as "check" during development, and only switch to "" once the data is clean.
- **#NAME? on IFNA** — Excel 2010 or older does not have IFNA. **Fix:** Use IF(ISNA(formula), "Not listed", formula), or upgrade.

<!--CTA_AFTER_ERRORS-->

## FAQ

### What is the difference between IFERROR and IFNA?

IFERROR catches all error types. IFNA catches only

### Can IFERROR return a blank cell?

It can return an empty string with "" (both apps). In Google Sheets you can also omit the second argument.

### Should a lookup use IFERROR or XLOOKUP if_not_found?

Prefer XLOOKUP's if_not_found argument, or IFNA, for a missing key. Both replace only the not-found result. IFERROR also hides #REF! and #NAME?, so a broken range can look like a blank cell. if_not_found does not turn a found-but-empty cell into a blank; that cell still comes back as 0.

## Related formulas

<!--RELATED-->
