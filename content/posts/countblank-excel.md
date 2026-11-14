---
title: How to Count Blank Cells with COUNTBLANK in Excel
slug: countblank-excel
date: '2026-11-14'
summary: COUNTBLANK counts cells that are truly empty and cells that only look empty
  because a formula returned an empty string (""). It does not count a space, a zero,
  text, a date, or TRUE/FALSE — those are values, even when the cell looks sparse.
  That makes COUNTBLANK the opposite of [ISBLANK](../{isblank
tags:
- Conditional sums & counts
- Excel
keyword: countblank-excel
niche: sheets-formulas
provider: structured
entry_id: countblank
platform: Excel
category: conditional
faq:
- q: Does COUNTBLANK count a formula that returns ""?
  a: Yes. That is the main difference from ISBLANK, which is FALSE for the same cell.
    In the worked example Thursday is included in COUNTBLANK and excluded from ISBLANK.
- q: What is the difference between COUNTBLANK and COUNTA?
  a: COUNTA counts filled cells and treats "" as filled. COUNTBLANK counts empty-looking
    cells and treats "" as empty. On the reply column they sum to 6, not 5, because
    B5 is counted by both. A range of five cells can therefore fail a "COUNTA + COUNTBLANK
    = ROWS" sanity check when "" is present.
- q: Does a zero or a space count as blank?
  a: No. 0 is a number, and a space is text. COUNTBLANK skips both. TRIM the cell,
    or test LEN(TRIM(A2))=0, if imported data may contain padding.
- q: Can I use COUNTBLANK on a whole column in Google Sheets?
  a: Avoid it. =COUNTBLANK(B2:B) counts every unused row to the bottom of the sheet.
    Bound the range, or use an ARRAYFORMULA that tests blanks only on rows that already
    have a key value, as in the Sheets alternatives.
related:
- - counta-excel
  - counta-google-sheets
- - isblank-excel
  - isblank-google-sheets
- - countif-excel
  - countif-google-sheets
- - countifs-excel
  - countifs-google-sheets
- - if-excel
  - if-google-sheets
sibling: countblank-google-sheets
---
COUNTBLANK counts cells that are truly empty and cells that only look empty because a formula returned an empty string (""). It does not count a space, a zero, text, a date, or TRUE/FALSE — those are values, even when the cell looks sparse. That makes COUNTBLANK the opposite of [ISBLANK](../isblank-excel/) on `""` (ISBLANK is FALSE for a hidden formula) and a counterpart to [COUNTA](../counta-excel/), which counts `""` as filled. Use it to find missing replies, incomplete rows, or how many cells in a range still need input. The function is the same in Excel and Google Sheets; the Sheets trap is an open-ended range such as B2:B, which counts every unused row to the bottom of the sheet.

## Quick answer

Use this formula in Excel:

```excel
=COUNTBLANK(B2:B6)
```

Syntax: `COUNTBLANK(range)`. `=COUNTBLANK(B2:B6)` counts the reply cells that are empty or that contain `""`. Tuesday is a true blank and Thursday's formula returned `""`, so the result is 2. Monday, Wednesday and Friday have text and are not counted.

## The problem

You have a five-day reply list. Tuesday was never filled in, Thursday is hidden by a formula that returns "", and one note cell holds only a space. You want a count of replies that are still missing, and you need to see why COUNTBLANK and ISBLANK disagree on Thursday, and why the space is not treated as blank.

## Worked example

Five weekdays of replies. Tuesday was never filled in. B5 holds a formula that returns "", so Thursday looks blank. C2 holds a single space. D2 counts blank replies with COUNTBLANK, D3 counts filled replies with COUNTA, D4 and D5 compare ISBLANK on Tuesday versus Thursday, and D6 shows that COUNTBLANK does not treat the space in C2 as blank.

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **Day** | **Reply** | **Note** | **Result** |
| 2 | Mon | TRUE | `" "` | **2** |
| 3 | Tue |  |  | **4** |
| 4 | Wed | FALSE |  | **TRUE** |
| 5 | Thu | **** |  | **FALSE** |
| 6 | Fri | TRUE |  | **4** |

Formulas used in the example (results shown in **bold** in the table above):

**B5** — a reply formula that displays as blank

```excel
=""
```

Result: *(blank)*

**D2** — blank replies, including ""

```excel
=COUNTBLANK(B2:B6)
```

Result: **2**

**D3** — filled replies, including ""

```excel
=COUNTA(B2:B6)
```

Result: **4**

**D4** — Tuesday is truly empty

```excel
=ISBLANK(B3)
```

Result: **TRUE**

**D5** — Thursday's "" is not ISBLANK

```excel
=ISBLANK(B5)
```

Result: **FALSE**

**D6** — a space is not a blank

```excel
=COUNTBLANK(C2:C6)
```

Result: **4**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Click the result cell and type `=COUNTBLANK(`.
2. Select the range of cells that should be filled, for example B2:B6, and close the parenthesis. Press Enter.
3. `=COUNTBLANK(B2:B6)` returns 2: Tuesday is a true blank, and Thursday's formula returned `""`. Monday, Wednesday and Friday have text and are not counted.
4. `=COUNTA(B2:B6)` returns 4 on the same range, because COUNTA includes the hidden `""` in B5. The two functions disagree by one whenever a formula has hidden its result. `=ISBLANK(B3)` is TRUE, but `=ISBLANK(B5)` is FALSE for the same reason.
5. C2 holds a single space. `=COUNTBLANK(C2:C6)` returns 4, not 5: the space is text, so it is not blank, and the other four Note cells are empty. TRIM imported notes if padding should not hide a missing value. Always bound the range; a whole-column COUNTBLANK will count every unused row below the data.

## Excel-specific notes

COUNTBLANK is available in every Excel version and takes a single range (it does not accept a list of separate areas the way COUNTA does). It counts both truly empty cells and formulas that return `""`, which is why it often matches what you see on the screen better than ISBLANK. A cell that contains only a space, a non-breaking space, or an apostrophe is not blank — COUNTBLANK skips it and COUNTA includes it; TRIM the column first if an import added padding. Zero is a number, so a recorded 0 is not blank. Error values are not blank either. `=COUNTIF(B2:B6, "")` and `=SUMPRODUCT(--(B2:B6=""))` return the same count as COUNTBLANK, including `""`. There is no SUBTOTAL function number for COUNTBLANK, so a filtered list needs a helper column or `=SUMPRODUCT((B2:B6="")*(SUBTOTAL(3, OFFSET(B2, ROW(B2:B6)-ROW(B2), 0))))` when you must ignore hidden rows; for a simple visible non-blank count, SUBTOTAL 3 (COUNTA) is usually easier. Bound the range to the data. `COUNTBLANK(B:B)` counts every unused cell in the column, which is almost never the number you want. Use [COUNTA](../counta-excel/) when you want filled cells, and [COUNTIF](../countif-excel/) when the missing value should match a specific label rather than a blank.

**Same count with COUNTIF**

```excel
=COUNTIF(B2:B6, "")
```

**Same count with SUMPRODUCT**

```excel
=SUMPRODUCT(--(B2:B6=""))
```

**How many replies were actually filled, including ""**

```excel
=COUNTA(B2:B6)
```

**Truly empty only (ISBLANK)**

```excel
=ISBLANK(B3)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=COUNTBLANK(B2:B6)
```

Excel uses the same COUNTBLANK formula on a bounded range. Excel does not use ARRAYFORMULA; it fills a flag column down, or uses COUNTIF / SUMPRODUCT for the same count. Never copy a Sheets open range such as B2:B into COUNTBLANK, on either platform, unless you really want unused rows included.

<!--SIBLING-->


## Common errors and how to fix them

- **COUNTBLANK is huge, often in the hundreds or thousands** — The range is open-ended (B:B or B2:B) and every unused row under the data is genuinely blank. **Fix:** Bound the range to the data (B2:B6), or count blanks only on rows that already have a value in another column.
- **COUNTBLANK and ISBLANK disagree on the same cell** — The cell contains a formula that returned `""`. COUNTBLANK counts it as blank; ISBLANK does not. **Fix:** Use COUNTBLANK (or `B5=""`) when a hidden formula should count as empty. Use ISBLANK when you need the cell to be truly empty.
- **A cell that looks empty was not counted** — The cell holds a space, a non-breaking space, an apostrophe, a zero, or the text "NULL" from an export. **Fix:** Inspect the formula bar. Use `=LEN(C2)` to confirm a space, then TRIM the column, or count with `=COUNTIF(C2:C6, "")` only after cleaning.
- **#VALUE! or a count of 0 when you expected blanks** — COUNTBLANK was given several loose arguments, or the range pointed at the wrong column. **Fix:** COUNTBLANK takes one range only. Recheck the address, and use COUNTA or COUNTIF if you meant to count filled cells or a specific label.

## FAQ

### Does COUNTBLANK count a formula that returns ""?

Yes. That is the main difference from [ISBLANK](../isblank-excel/), which is FALSE for the same cell. In the worked example Thursday is included in COUNTBLANK and excluded from ISBLANK.

### What is the difference between COUNTBLANK and COUNTA?

COUNTA counts filled cells and treats `""` as filled. COUNTBLANK counts empty-looking cells and treats `""` as empty. On the reply column they sum to 6, not 5, because B5 is counted by both. A range of five cells can therefore fail a "COUNTA + COUNTBLANK = ROWS" sanity check when `""` is present.

### Does a zero or a space count as blank?

No. 0 is a number, and a space is text. COUNTBLANK skips both. TRIM the cell, or test `LEN(TRIM(A2))=0`, if imported data may contain padding.

### Can I use COUNTBLANK on a whole column in Google Sheets?

Avoid it. `=COUNTBLANK(B2:B)` counts every unused row to the bottom of the sheet. Bound the range, or use an ARRAYFORMULA that tests blanks only on rows that already have a key value, as in the Sheets alternatives.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
