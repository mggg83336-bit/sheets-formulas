---
title: How to Count Blank Cells with COUNTBLANK in Google Sheets
slug: countblank-google-sheets
date: '2026-11-14'
summary: COUNTBLANK counts cells that are truly empty and cells that only look empty
  because a formula returned an empty string (""). It does not count a space, a zero,
  text, a date, or TRUE/FALSE — those are values, even when the cell looks sparse.
  That makes COUNTBLANK the opposite of [ISBLANK](../{isblank
tags:
- Conditional sums & counts
- Google Sheets
keyword: countblank-google-sheets
niche: sheets-formulas
provider: structured
entry_id: countblank
platform: Google Sheets
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
- - counta-google-sheets
  - counta-excel
- - isblank-google-sheets
  - isblank-excel
- - countif-google-sheets
  - countif-excel
- - countifs-google-sheets
  - countifs-excel
- - if-google-sheets
  - if-excel
sibling: countblank-excel
---
COUNTBLANK counts cells that are truly empty and cells that only look empty because a formula returned an empty string (""). It does not count a space, a zero, text, a date, or TRUE/FALSE — those are values, even when the cell looks sparse. That makes COUNTBLANK the opposite of [ISBLANK](../isblank-google-sheets/) on `""` (ISBLANK is FALSE for a hidden formula) and a counterpart to [COUNTA](../counta-google-sheets/), which counts `""` as filled. Use it to find missing replies, incomplete rows, or how many cells in a range still need input. The function is the same in Excel and Google Sheets; the Sheets trap is an open-ended range such as B2:B, which counts every unused row to the bottom of the sheet.

## Quick answer

Use this formula in Google Sheets:

```excel
=COUNTBLANK(B2:B6)
```

Identical syntax in Google Sheets: `COUNTBLANK(range)` counts truly empty replies and cells that hold `""`. On this list that is Tuesday and Thursday, so the result is 2.

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

## Google Sheets-specific notes

Sheets COUNTBLANK matches Excel for true blanks, for `""`, and for the space gotcha: a cell that contains only a space is not blank. The usual Sheets habit of writing open-ended ranges is dangerous here. `=COUNTBLANK(B2:B)` adds every unused row from the last reply to the bottom of the sheet, so a five-row list can return a count in the hundreds or thousands. Always bound the range (`B2:B6`), or count blanks only on rows that already have an entry in another column, for example `=ARRAYFORMULA(SUM(N((A2:A6<>"")*(B2:B6=""))))` to count missing replies on named rows. An unchecked checkbox stores FALSE, not a blank, so COUNTBLANK will not see it as missing; test `=COUNTIF(B2:B6, FALSE)` instead. To flag each blank reply in a helper column, use `=ARRAYFORMULA(IF(A2:A="", "", IF(B2:B="", "Missing", "")))`. If the file must open in Excel, keep the bounded `=COUNTBLANK(B2:B6)` and skip ARRAYFORMULA.

**Missing replies only on rows that have a day name**

```excel
=ARRAYFORMULA(SUM(N((A2:A6<>"")*(B2:B6=""))))
```

**Flag each blank reply**

```excel
=ARRAYFORMULA(IF(A2:A="", "", IF(B2:B="", "Missing", "")))
```

**Same count with COUNTIF**

```excel
=COUNTIF(B2:B6, "")
```

**How many replies were actually filled, including ""**

```excel
=COUNTA(B2:B6)
```


## Excel version

The same formula works unchanged in Excel:

```excel
=COUNTBLANK(B2:B6)
```

Google Sheets uses the same COUNTBLANK rule, including `""` and excluding spaces. The important Sheets difference is range style: `=COUNTBLANK(B2:B)` on an open column counts every unused row to the bottom of the sheet, so you must bound the range or count blanks only on rows that already have a key value.

<!--SIBLING-->


## Common errors and how to fix them

- **COUNTBLANK is huge, often in the hundreds or thousands** — The range is open-ended (B:B or B2:B) and every unused row under the data is genuinely blank. **Fix:** Bound the range to the data (B2:B6), or count blanks only on rows that already have a value in another column.
- **COUNTBLANK and ISBLANK disagree on the same cell** — The cell contains a formula that returned `""`. COUNTBLANK counts it as blank; ISBLANK does not. **Fix:** Use COUNTBLANK (or `B5=""`) when a hidden formula should count as empty. Use ISBLANK when you need the cell to be truly empty.
- **A cell that looks empty was not counted** — The cell holds a space, a non-breaking space, an apostrophe, a zero, or the text "NULL" from an export. **Fix:** Inspect the formula bar. Use `=LEN(C2)` to confirm a space, then TRIM the column, or count with `=COUNTIF(C2:C6, "")` only after cleaning.
- **#VALUE! or a count of 0 when you expected blanks** — COUNTBLANK was given several loose arguments, or the range pointed at the wrong column. **Fix:** COUNTBLANK takes one range only. Recheck the address, and use COUNTA or COUNTIF if you meant to count filled cells or a specific label.

## FAQ

### Does COUNTBLANK count a formula that returns ""?

Yes. That is the main difference from [ISBLANK](../isblank-google-sheets/), which is FALSE for the same cell. In the worked example Thursday is included in COUNTBLANK and excluded from ISBLANK.

### What is the difference between COUNTBLANK and COUNTA?

COUNTA counts filled cells and treats `""` as filled. COUNTBLANK counts empty-looking cells and treats `""` as empty. On the reply column they sum to 6, not 5, because B5 is counted by both. A range of five cells can therefore fail a "COUNTA + COUNTBLANK = ROWS" sanity check when `""` is present.

### Does a zero or a space count as blank?

No. 0 is a number, and a space is text. COUNTBLANK skips both. TRIM the cell, or test `LEN(TRIM(A2))=0`, if imported data may contain padding.

### Can I use COUNTBLANK on a whole column in Google Sheets?

Avoid it. `=COUNTBLANK(B2:B)` counts every unused row to the bottom of the sheet. Bound the range, or use an ARRAYFORMULA that tests blanks only on rows that already have a key value, as in the Sheets alternatives.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
