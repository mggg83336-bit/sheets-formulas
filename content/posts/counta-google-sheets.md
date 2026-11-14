---
title: How to Count Non-Blank Cells with COUNTA in Google Sheets
slug: counta-google-sheets
date: '2026-11-14'
summary: 'COUNTA counts every cell that is not empty: text, numbers, dates, TRUE or
  FALSE, error values, and even a formula that looks blank because it returned an
  empty string (""). That last case is the usual surprise. COUNT, by contrast, counts
  only numbers (including dates). Use COUNTA when you need how m'
tags:
- Conditional sums & counts
- Google Sheets
keyword: counta-google-sheets
niche: sheets-formulas
provider: structured
entry_id: counta
platform: Google Sheets
category: conditional
faq:
- q: What is the difference between COUNTA and COUNT?
  a: COUNT counts only numbers (and dates, which are numbers). COUNTA counts every
    non-empty cell — text, numbers, booleans, errors, and formulas that return "".
    In the worked example both return 4 on the Score column, but only COUNTA sees
    the comments.
- q: Does COUNTA count a formula that returns ""?
  a: Yes. The cell is not empty; it contains a formula. ISBLANK is also FALSE for
    that cell. Use SUMPRODUCT(--(A2:A6<>"")) or COUNTBLANK when you want "" treated
    as empty.
- q: Does a zero or a space count?
  a: Yes. 0 is a number, and a space is text, so both increment COUNTA. A space does
    not increment COUNT. TRIM imported data if padding should not count as filled.
- q: How do I count non-blank cells in a filtered list or a whole column?
  a: In Excel, =SUBTOTAL(3, B2:B6) ignores rows hidden by a filter. In Google Sheets,
    =COUNTA(B2:B) on an open-ended range is safe because unused rows are empty; do
    not switch that pattern to COUNTBLANK, which would count every unused row.
related:
- - countblank-google-sheets
  - countblank-excel
- - countif-google-sheets
  - countif-excel
- - countifs-google-sheets
  - countifs-excel
- - count-unique-google-sheets
  - count-unique-excel
- - isblank-google-sheets
  - isblank-excel
sibling: counta-excel
---
COUNTA counts every cell that is not empty: text, numbers, dates, TRUE or FALSE, error values, and even a formula that looks blank because it returned an empty string (""). That last case is the usual surprise. COUNT, by contrast, counts only numbers (including dates). Use COUNTA when you need how many cells in a list actually have something in them — filled names, submitted replies, or a column that mixes text and numbers. To treat "" as empty, count with `SUMPRODUCT(--(A2:A6<>""))` or `COUNTIF(A2:A6,"<>")` instead. The function is the same in Excel and Google Sheets; Excel can limit the count to visible rows with SUBTOTAL, and Sheets must not confuse COUNTA with an unchecked checkbox, which stores FALSE and therefore counts as filled.

## Quick answer

Use this formula in Google Sheets:

```excel
=COUNTA(B2:B6)
```

Identical syntax in Google Sheets: `COUNTA(value1, [value2], ...)` counts the non-empty scores in B2:B6 and returns 4, including Cara's 0 and skipping Ben's blank cell.

## The problem

You have a short score list with a missing score, a genuine zero, and a comment hidden by a formula that returns "". You want the number of names entered, the number of scores that were actually recorded (including zero), and you need to understand why COUNTA still counts that hidden comment.

## Worked example

Five people with scores and comments. Ben has no score. Cara's score is 0, which still counts. C5 holds a formula that returns an empty string, so the comment looks blank but COUNTA still includes it. D2 counts names, D3 counts scores with COUNTA, D4 counts scores with COUNT, D5 counts comments, and D6 shows that COUNT ignores the text comments entirely.

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **Name** | **Score** | **Comment** | **Result** |
| 2 | Ann | 85 | good | **5** |
| 3 | Ben |  |  | **4** |
| 4 | Cara | 0 |  | **4** |
| 5 | Dan | 90 | **** | **2** |
| 6 | Eve | 70 |  | **0** |

Formulas used in the example (results shown in **bold** in the table above):

**C5** — a comment formula that displays as blank

```excel
=""
```

Result: *(blank)*

**D2** — how many names were entered

```excel
=COUNTA(A2:A6)
```

Result: **5**

**D3** — how many scores were recorded, including zero

```excel
=COUNTA(B2:B6)
```

Result: **4**

**D4** — COUNT on the same scores, numbers only

```excel
=COUNT(B2:B6)
```

Result: **4**

**D5** — comments including the hidden ""

```excel
=COUNTA(C2:C6)
```

Result: **2**

**D6** — COUNT ignores text comments

```excel
=COUNT(C2:C6)
```

Result: **0**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Click the result cell and type `=COUNTA(`.
2. Select the range you want to count, for example B2:B6, and close the parenthesis. Press Enter.
3. `=COUNTA(B2:B6)` returns 4. Ben's score is skipped because the cell is empty; Cara's 0 is counted because zero is a value.
4. `=COUNTA(C2:C6)` returns 2: Ann's "good" and the formula in C5 that returned `""`. The hidden comment is the gotcha — the cell looks empty, but COUNTA still counts it.
5. `=COUNT(B2:B6)` also returns 4 here, because every filled score is numeric, but `=COUNT(C2:C6)` returns 0, because COUNT ignores text. Use COUNT when you only want numbers; use COUNTA when any filled cell should count. To treat `""` as empty, use `=SUMPRODUCT(--(C2:C6<>""))` instead.

## Google Sheets-specific notes

Sheets COUNTA matches Excel for text, numbers, dates, errors, zero, and the empty-string gotcha: a formula that returns `""` is counted. An open-ended range such as `=COUNTA(B2:B)` is the usual Sheets pattern and is safe here, because unused rows at the bottom are empty and do not increment the count — the opposite of COUNTBLANK, which would add every unused row. A Sheets checkbox stores TRUE or FALSE, never a blank, so COUNTA on a checkbox column equals the number of rows, not the number of ticks; count checks with `=COUNTIF(B2:B, TRUE)` instead. To count non-blank cells in each row of a block, use `=BYROW(B2:D, LAMBDA(r, COUNTA(r)))`, or an ARRAYFORMULA of `(B2:B<>"")+(C2:C<>"")` when you also want `""` treated as empty. FILTER plus COUNTA is handy when only some rows should be included, for example `=COUNTA(FILTER(B2:B6, A2:A6<>""))`. If the file must open in Excel, keep the bounded form `=COUNTA(B2:B6)` and skip BYROW and checkbox assumptions.

**Whole column, unused rows are safely ignored**

```excel
=COUNTA(B2:B)
```

**Count checked checkboxes only**

```excel
=COUNTIF(B2:B6, TRUE)
```

**Non-blank count for each row**

```excel
=BYROW(B2:D6, LAMBDA(r, COUNTA(r)))
```

**Count numbers only**

```excel
=COUNT(B2:B6)
```


## Excel version

The same formula works unchanged in Excel:

```excel
=COUNTA(B2:B6)
```

Google Sheets uses the same COUNTA rule, including counting `""` and 0. Sheets has no SUBTOTAL-style visible-row count in everyday use; it typically uses open-ended ranges such as B2:B (safe for COUNTA, because unused rows are empty) and must treat an unchecked checkbox as FALSE, which COUNTA counts as filled.

<!--SIBLING-->


## Common errors and how to fix them

- **COUNTA is one too high on a column that looks partly empty** — A formula that returned `""`, a space, a non-breaking space, or an apostrophe still lives in the cell. COUNTA counts those as filled. **Fix:** Clear the cells completely, TRIM padding, or count with `=SUMPRODUCT(--(A2:A6<>""))` when a hidden formula should not count.
- **A recorded 0 was left out of a manual tally but COUNTA includes it** — Zero is a number, not a blank. COUNTA and COUNT both include it. **Fix:** This is correct. To count scores above zero, use [COUNTIF](../countif-google-sheets/) with `">0"` rather than COUNTA.
- **The count includes the header or hundreds of extra rows** — The range is a whole column (B:B) or starts on the header row. **Fix:** Bound the range to the data (B2:B6), or use an Excel Table column such as `Table1[Score]`.
- **Filtered-out rows are still in the total** — COUNTA always counts hidden and filtered rows. **Fix:** In Excel use `=SUBTOTAL(3, B2:B6)` or `=AGGREGATE(3, 5, B2:B6)`. In Sheets, filter first with FILTER and then COUNTA the result.

## FAQ

### What is the difference between COUNTA and COUNT?

COUNT counts only numbers (and dates, which are numbers). COUNTA counts every non-empty cell — text, numbers, booleans, errors, and formulas that return `""`. In the worked example both return 4 on the Score column, but only COUNTA sees the comments.

### Does COUNTA count a formula that returns ""?

Yes. The cell is not empty; it contains a formula. [ISBLANK](../isblank-google-sheets/) is also FALSE for that cell. Use `SUMPRODUCT(--(A2:A6<>""))` or [COUNTBLANK](../countblank-google-sheets/) when you want `""` treated as empty.

### Does a zero or a space count?

Yes. 0 is a number, and a space is text, so both increment COUNTA. A space does not increment COUNT. TRIM imported data if padding should not count as filled.

### How do I count non-blank cells in a filtered list or a whole column?

In Excel, `=SUBTOTAL(3, B2:B6)` ignores rows hidden by a filter. In Google Sheets, `=COUNTA(B2:B)` on an open-ended range is safe because unused rows are empty; do not switch that pattern to COUNTBLANK, which would count every unused row.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
