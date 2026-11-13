---
title: How to Use ISBLANK to Check for Empty Cells in Google Sheets
slug: isblank-google-sheets
date: '2026-11-13'
summary: 'ISBLANK returns TRUE when a cell has nothing in it, and FALSE when it holds
  a value, a space, or a formula — including a formula that looks empty because it
  returned an empty string (""). That last case is the usual gotcha: a cell that displays
  as blank is not always blank. Use ISBLANK to flag missi'
tags:
- Logic & error handling
- Google Sheets
keyword: isblank-google-sheets
niche: sheets-formulas
provider: structured
entry_id: isblank
platform: Google Sheets
category: logic
faq:
- q: Why is ISBLANK false when the cell looks empty?
  a: Because a formula such as ="" still lives in the cell. ISBLANK is TRUE only when
    there is nothing there at all. Use A2="" or LEN(A2)=0 if you want both a true
    blank and an empty string to count as empty, as the worked example shows for C2.
- q: Should I use ISBLANK or A2=""?
  a: Use ISBLANK when you specifically need a truly empty cell, for example before
    writing into it or when a formula should not be treated as blank. Use A2="" (or
    IF with that test) when a formula that hides its result should be treated the
    same as a missing value.
- q: Does ISBLANK treat a zero or a space as blank?
  a: No. 0 is a number, so ISBLANK is FALSE. A space or a non-breaking space is text,
    so ISBLANK is also FALSE. TRIM the cell, or test LEN(TRIM(A2))=0, if imported
    data may contain padding.
- q: How do I check a whole column at once?
  a: In Microsoft 365, =ISBLANK(B2:B5) spills. In Google Sheets, use =ARRAYFORMULA(ISBLANK(B2:B5)),
    or wrap the IF label pattern shown in the Sheets alternatives. Bound the range
    so unused rows are not all flagged as blank.
related:
- - if-google-sheets
  - if-excel
- - iferror-google-sheets
  - iferror-excel
- - if-and-or-google-sheets
  - if-and-or-excel
- - countif-google-sheets
  - countif-excel
- - trim-google-sheets
  - trim-excel
sibling: isblank-excel
---
ISBLANK returns TRUE when a cell has nothing in it, and FALSE when it holds a value, a space, or a formula — including a formula that looks empty because it returned an empty string (""). That last case is the usual gotcha: a cell that displays as blank is not always blank. Use ISBLANK to flag missing inputs, to skip empty rows in IF, or to guard a lookup. To treat both truly empty cells and "" as empty, test `A2=""` or `LEN(A2)=0` instead. The function is the same in Excel and Google Sheets; Sheets typically wraps it in ARRAYFORMULA to check a whole column.

## Quick answer

Use this formula in Google Sheets:

```excel
=ISBLANK(B3)
```

Identical syntax in Google Sheets: `ISBLANK(value)` is TRUE when B3 has nothing in it, and FALSE when the cell holds a value or a formula, including `=""`.

## The problem

You have a contact list and need to flag rows with a missing email, show a clear "Missing email" label, and understand why a cell that looks empty (because a formula returned "") still fails an ISBLANK test.

## Worked example

Four contacts. Ben has no email. C2 holds a formula that returns an empty string, so the cell looks blank. D2 tests whether Ben's email is truly empty, D3 tests Ann's email, D4 turns a missing email into a label, and D5 shows that ISBLANK is FALSE for the empty-string formula in C2.

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **Name** | **Email** | **Hidden** | **Result** |
| 2 | Ann | ann@ex.com | **** | **TRUE** |
| 3 | Ben |  |  | **FALSE** |
| 4 | Cara | cara@ex.com |  | **Missing email** |
| 5 | Dan | dan@ex.com |  | **FALSE** |

Formulas used in the example (results shown in **bold** in the table above):

**C2** — a formula that displays as blank

```excel
=""
```

Result: *(blank)*

**D2** — Ben's email is empty

```excel
=ISBLANK(B3)
```

Result: **TRUE**

**D3** — Ann's email is not empty

```excel
=ISBLANK(B2)
```

Result: **FALSE**

**D4** — label a missing email

```excel
=IF(ISBLANK(B3), "Missing email", B3)
```

Result: **Missing email**

**D5** — ISBLANK is FALSE for a formula that returned ""

```excel
=ISBLANK(C2)
```

Result: **FALSE**

<!--AD_IN_ARTICLE-->

## How the formula works

1. B3, Ben's email, has nothing in it. `=ISBLANK(B3)` returns TRUE. `=ISBLANK(B2)` on Ann's email returns FALSE, because the cell holds text.
2. `=IF(ISBLANK(B3), "Missing email", B3)` turns that test into a label and returns Missing email. The same pattern works to skip a calculation: `=IF(ISBLANK(B3), "", some_formula)`.
3. C2 holds `=""`, a formula that displays as empty. `=ISBLANK(C2)` is FALSE, because the cell is not empty — it contains a formula. This is the gotcha that catches most people.
4. To treat both a true blank and `""` as empty, test `=IF(B3="", "Missing email", B3)` or `=LEN(B3)=0`. COUNTBLANK also counts `""` as blank, which is why a count of "empty-looking" cells is often better done with COUNTBLANK than with ISBLANK.
5. Combine ISBLANK with [IF](../if-google-sheets/) to branch on a missing input, or with [IFERROR](../iferror-google-sheets/) when you need to handle a lookup error as well. A cell that contains only a space is not blank; [TRIM](../trim-google-sheets/) it first if an import added padding.

## Google Sheets-specific notes

Sheets ISBLANK matches Excel for true blanks, for values, and for the empty-string gotcha: a formula that returns `""` is not blank. The usual Sheets pattern is to wrap the test in ARRAYFORMULA and guard the column, for example `=ARRAYFORMULA(IF(A2:A="", "", IF(ISBLANK(B2:B), "Missing email", B2:B)))`, which labels only the rows that have a name and a truly empty email. When you also want to catch emails hidden by `""`, test `B2:B=""` inside ARRAYFORMULA instead of ISBLANK. COUNTBLANK in Sheets, as in Excel, counts both empty cells and `""`, so it is the better function when you want a single count of "looks empty" cells. Open-ended ranges such as B2:B are legal, but an unbounded ISBLANK will flag every unused row to the bottom of the sheet; cap the range or blank-check the name column first. IF, IFS, and IFERROR combine with ISBLANK the same way they do in Excel. If the file must open in older Excel, keep the single-cell form `=ISBLANK(B3)` or `=IF(ISBLANK(B3), "Missing email", B3)` and skip ARRAYFORMULA.

**Whole column of missing-email labels**

```excel
=ARRAYFORMULA(IF(A2:A="", "", IF(ISBLANK(B2:B), "Missing email", B2:B)))
```

**Treat both a blank and "" as empty, whole column**

```excel
=ARRAYFORMULA(IF(A2:A="", "", IF(B2:B="", "Missing email", B2:B)))
```

**Label a missing email**

```excel
=IF(ISBLANK(B3), "Missing email", B3)
```

**Count empty-looking cells, including ""**

```excel
=COUNTBLANK(B2:B5)
```


## Excel version

The same formula works unchanged in Excel:

```excel
=ISBLANK(B3)
```

Google Sheets uses the same ISBLANK rule, including FALSE for a formula that returns "". To check a whole column from one cell, wrap ISBLANK in ARRAYFORMULA; Excel 365 can spill from `ISBLANK(B2:B5)` instead.

<!--SIBLING-->


## Common errors and how to fix them

- **ISBLANK returns FALSE on a cell that looks empty** — The cell contains a formula that returned `""`, a space, a non-breaking space, or an apostrophe. ISBLANK tests the cell, not what it displays. **Fix:** Use `B3=""` or `LEN(TRIM(B3))=0` when you want to treat those as empty. Clear the cell completely if you truly need ISBLANK to be TRUE.
- **A whole-column ISBLANK flags hundreds of unused rows** — The range is open-ended (B:B or B2:B) and every unused row under the data is genuinely blank. **Fix:** Bound the range (B2:B5) or blank-check a column that is only filled on real rows, for example `=IF(A2="", "", ISBLANK(B2))`.
- **COUNTBLANK and ISBLANK disagree on the same column** — COUNTBLANK counts formulas that return `""` as blank; ISBLANK does not. The two functions are answering slightly different questions. **Fix:** Use ISBLANK when you need to know whether a cell is truly empty. Use COUNTBLANK, or `B3=""`, when a hidden formula should count as empty.
- **#NAME?** — The function was misspelled (IS_BLANK, ISTBLANK) or the workbook's list separator / language name is different. **Fix:** In English Excel and Google Sheets the name is `ISBLANK`. Check the formula for a typo and that you are not in a locale that uses a translated function name without the English alias.

## FAQ

### Why is ISBLANK false when the cell looks empty?

Because a formula such as `=""` still lives in the cell. ISBLANK is TRUE only when there is nothing there at all. Use `A2=""` or `LEN(A2)=0` if you want both a true blank and an empty string to count as empty, as the worked example shows for C2.

### Should I use ISBLANK or A2=""?

Use ISBLANK when you specifically need a truly empty cell, for example before writing into it or when a formula should not be treated as blank. Use `A2=""` (or [IF](../if-google-sheets/) with that test) when a formula that hides its result should be treated the same as a missing value.

### Does ISBLANK treat a zero or a space as blank?

No. 0 is a number, so ISBLANK is FALSE. A space or a non-breaking space is text, so ISBLANK is also FALSE. TRIM the cell, or test `LEN(TRIM(A2))=0`, if imported data may contain padding.

### How do I check a whole column at once?

In Microsoft 365, `=ISBLANK(B2:B5)` spills. In Google Sheets, use `=ARRAYFORMULA(ISBLANK(B2:B5))`, or wrap the IF label pattern shown in the Sheets alternatives. Bound the range so unused rows are not all flagged as blank.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
