---
title: 'How to Fix the #VALUE! Error in Excel'
slug: value-error-excel
date: '2026-10-22'
summary: '#VALUE! means a formula received the wrong type of value, usually text where
  it expected a number. This guide shows the common causes (units typed into number
  cells, dates stored as text, mismatched ranges) and the formulas that clean the
  data.'
tags:
- Fixing formula errors
- Excel
keyword: value-error-excel
niche: sheets-formulas
provider: structured
entry_id: value-error
platform: Excel
category: errors
faq:
- q: Why does =A1+A2 give
  a: The + operator must convert every input to a number and fails on text. SUM simply
    ignores text cells, which avoids the error but can give a wrong total.
- q: How do I find which cell causes
  a: Use Formulas > Evaluate Formula in Excel, or hover over the error in Google Sheets
    to read the message, then check each referenced cell with ISNUMBER.
related:
- - iferror-excel
  - iferror-google-sheets
- - div0-error-excel
  - div0-error-google-sheets
- - na-error-excel
  - na-error-google-sheets
- - trim-excel
  - trim-google-sheets
sibling: value-error-google-sheets
---
#VALUE! means a formula received the wrong type of value, usually text where it expected a number. This guide shows the common causes (units typed into number cells, dates stored as text, mismatched ranges) and the formulas that clean the data.

## Quick answer

Use this formula in Excel:

```excel
=VALUE(SUBSTITUTE(B2, " USD", ""))*C2
```

SUBSTITUTE strips the " USD" suffix and VALUE converts the remaining text to a number, so the multiplication works for every row.

## The problem

A line-total column multiplies price by quantity, but one price was typed as "4 USD", so the total shows #VALUE!.

## Worked example

One price was typed with a currency suffix.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Item** | **Price** | **Qty** | **Total** | **Fixed total** |
| 2 | Pen | 1.5 | 10 | **15** | **15** |
| 3 | Pad | 4 USD | 5 | **#VALUE!** | **20** |
| 4 | Clip | 0.25 | 40 | **10** | **10** |

Formulas used in the example (results shown in **bold** in the table above):

**D2 (filled to D4)** — plain multiplication, filled down

```excel
=B2*C2
```

Results: **15**, **#VALUE!**, **10**

**E2 (filled to E4)** — cleaned, filled down

```excel
=VALUE(SUBSTITUTE(B2, " USD", ""))*C2
```

Results: **15**, **20**, **10**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `B3*C3` fails because "4 USD" is text that cannot be converted to a number.
2. `SUBSTITUTE(B3, " USD", "")` returns the text "4".
3. `VALUE("4")` returns the number 4, so the multiplication gives 20.
4. For rows that were already numbers, SUBSTITUTE returns the number as text (e.g. "1.5") and VALUE converts it back, so the formula is safe for the whole column.

## Excel-specific notes

Excel automatically converts text that looks like a number ("4.20") in arithmetic, but not text with letters or symbols such as "4 USD" or "N/A". Click the error indicator next to the cell and choose "Show Calculation Steps" to see which part fails. Also watch out for functions like SUM, which skip text instead of failing: `=SUM(B2:B4)` silently ignores "4 USD", which is worse than an error because the total is just wrong.

**Check which cells are not numbers**

```excel
=ISNUMBER(B2)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=VALUE(SUBSTITUTE(B2, " USD", ""))*C2
```

The same fix works in Google Sheets. Hover over the error for an explanation, and REGEXEXTRACT can pull out numbers from messy text.

<!--SIBLING-->


## Common errors and how to fix them

- **Text in a number column** — Units, currency codes, "N/A" or a space typed into a cell used in arithmetic. **Fix:** Clean the cells, or strip the text with SUBSTITUTE / REGEXEXTRACT and VALUE.
- **Dates stored as text** — Imported dates such as "2026.03.15" are not recognized, so date math fails. **Fix:** Convert with DATEVALUE or DATE(LEFT(...), MID(...), RIGHT(...)).
- **Ranges of different sizes** — Array calculations like SUMPRODUCT(A2:A10, B2:B11) need same-size ranges. **Fix:** Make every range cover the same rows.

## FAQ

### Why does =A1+A2 give

The + operator must convert every input to a number and fails on text. SUM simply ignores text cells, which avoids the error but can give a wrong total.

### How do I find which cell causes

Use Formulas > Evaluate Formula in Excel, or hover over the error in Google Sheets to read the message, then check each referenced cell with ISNUMBER.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
