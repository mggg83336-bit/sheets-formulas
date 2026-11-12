---
title: How to Use the OFFSET Function in Google Sheets
slug: offset-google-sheets
date: '2026-11-12'
summary: OFFSET starts at a cell or range and returns another range a given number
  of rows and columns away, optionally with a new height and width. It is the classic
  way to build a moving or growing range for SUM, AVERAGE, or a chart. The function
  is volatile, so a non-volatile INDEX range or an Excel Table
tags:
- Lookup & reference
- Google Sheets
keyword: offset-google-sheets
niche: sheets-formulas
provider: structured
entry_id: offset
platform: Google Sheets
category: lookup
faq:
- q: When should I use OFFSET instead of INDEX?
  a: Use OFFSET when the starting cell itself moves — for example “two rows below
    this label” or “a block that starts n columns to the right.” If the start is fixed
    and only the length of the list changes, B2:INDEX(B2:B100, COUNTA(B2:B100)) does
    the same job and is not volatile. In Microsoft 365, TAKE is often clearer still.
- q: Does OFFSET work the same in Google Sheets?
  a: The five arguments are the same. The usual Sheets alternative for a growing column
    is an open-ended range (B2:B) or FILTER, which Excel does not treat the same way.
    TAKE is Excel-only; INDEX works in both.
- q: Can I use OFFSET in a named range?
  a: Yes. In Excel open Formulas > Name Manager and set the refers-to formula to =OFFSET(Sheet1!$B$2,0,0,COUNTA(Sheet1!$B$2:$B$100),1).
    In Google Sheets use Data > Named ranges, or point the name at B2:B and skip OFFSET.
    See dynamic named range for the full walkthrough.
- q: Why is OFFSET called volatile?
  a: A volatile function recalculates whenever anything in the workbook changes, even
    if its inputs did not. A few OFFSET formulas are fine; a sheet of them, each wrapping
    COUNTA on a large column, is a common reason a model feels sluggish.
related:
- - indirect-google-sheets
  - indirect-excel
- - last-value-google-sheets
  - last-value-excel
- - index-match-google-sheets
  - index-match-excel
- - filter-google-sheets
  - filter-excel
- - dynamic-range-google-sheets
  - dynamic-range-excel
sibling: offset-excel
---
OFFSET starts at a cell or range and returns another range a given number of rows and columns away, optionally with a new height and width. It is the classic way to build a moving or growing range for SUM, AVERAGE, or a chart. The function is volatile, so a non-volatile INDEX range or an Excel Table is often a better long-term choice. Google Sheets uses the same syntax and also offers open-ended ranges and FILTER.

## Quick answer

Use this formula in Google Sheets:

```excel
=OFFSET(A2, 2, 0)
```

Same syntax in Google Sheets: `OFFSET(cell_reference, offset_rows, offset_columns, [height], [width])`. From A2, two rows down and no column shift returns East. Height and width, when given, must be positive.

## The problem

You have a growing list of regional sales and want one formula that can return a cell a few rows down, a block of the first few months, or a range that expands as new rows are typed — without editing the formula each time the list gets longer.

## Worked example

Five regional sales in A2:C6. E2 returns the region two rows below the first name, E3 a single sale, E4 the sum of the first four sales, E5 the average of every filled sale, and E6 a three-row block that starts one row down.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Region** | **Sales** | **Month** |  | **Result** |
| 2 | North | 120 | Jan |  | **East** |
| 3 | South | 85 | Feb |  | **95** |
| 4 | East | 140 | Mar |  | **440** |
| 5 | West | 95 | Apr |  | **110** |
| 6 | North | 110 | May |  | **320** |

Formulas used in the example (results shown in **bold** in the table above):

**E2** — region two rows down from A2

```excel
=OFFSET(A2, 2, 0)
```

Result: **East**

**E3** — sales three rows down from B2

```excel
=OFFSET(B2, 3, 0)
```

Result: **95**

**E4** — sum of the first four sales

```excel
=SUM(OFFSET(B2, 0, 0, 4, 1))
```

Result: **440**

**E5** — average of every filled sale (COUNTA sets the height)

```excel
=AVERAGE(OFFSET(B2, 0, 0, COUNTA(B2:B6), 1))
```

Result: **110**

**E6** — sum of a 3-row block starting one row down

```excel
=SUM(OFFSET(A2, 1, 1, 3, 1))
```

Result: **320**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `=OFFSET(A2, 2, 0)` starts at North in A2, moves down two rows, and returns East from A4. Changing the 2 to 3 would return West.
2. `=OFFSET(B2, 3, 0)` does the same move in the Sales column and returns 95, the West figure in B5.
3. Height and width turn OFFSET into a range. `=SUM(OFFSET(B2, 0, 0, 4, 1))` starts at B2, stays four rows tall and one column wide (B2:B5), and adds 120 + 85 + 140 + 95 = 440.
4. `COUNTA` can supply that height so the range grows with the list. `=AVERAGE(OFFSET(B2, 0, 0, COUNTA(B2:B6), 1))` sees five filled sales and returns 110, the average of 120, 85, 140, 95 and 110.
5. The last example moves and resizes at once: `=SUM(OFFSET(A2, 1, 1, 3, 1))` starts one row down and one column right of A2 (that is B3), then takes three rows (B3:B5) and adds 85 + 140 + 95 = 320.
6. When you only need a growing list and care about speed, prefer `=SUM(B2:INDEX(B2:B6, COUNTA(B2:B6)))` or, in Excel, an Excel Table. Keep OFFSET for a start point or size that really does change by a calculated row or column offset.

## Google Sheets-specific notes

OFFSET behaviour matches Excel for the five arguments, including negative row and column shifts and the `#REF!` you get when the result would fall off the sheet. The practical difference is how Sheets grows a list. Open-ended ranges such as `B2:B` already expand as you add rows, so `=SUM(B2:B)` or a named range pointed at `B2:B` often replaces an OFFSET+COUNTA construction — watch for a total or note sitting at the bottom of the column, which an open-ended range would include. FILTER is the usual Sheets-native alternative when you want every filled sale (`=SUM(FILTER(B2:B, B2:B<>""))`) and is easier to read than OFFSET. INDIRECT can also build a height from COUNTA, but it is volatile too. OFFSET itself remains volatile, so a dashboard with many OFFSET named ranges will recalc often; INDEX (`=SUM(B2:INDEX(B2:B, COUNTA(B2:B)))`) is the cheaper equivalent. TAKE does not exist in Google Sheets; CHOOSEROWS plus SEQUENCE can pick the first n rows if you need that shape. If Excel collaborators will open the file, stay with closed ranges and skip FILTER-only or B2:B-only formulas.

**Open-ended sum that grows with the column**

```excel
=SUM(B2:B)
```

**Growing list with FILTER**

```excel
=SUM(FILTER(B2:B, B2:B<>""))
```

**Growing list with INDEX (non-volatile)**

```excel
=SUM(B2:INDEX(B2:B, COUNTA(B2:B)))
```

**First four sales, as a range inside SUM**

```excel
=SUM(OFFSET(B2, 0, 0, 4, 1))
```


## Excel version

The same formula works unchanged in Excel:

```excel
=OFFSET(A2, 2, 0)
```

Google Sheets uses the same OFFSET syntax. It also allows open-ended ranges such as B2:B, and FILTER is often a clearer replacement than OFFSET for a growing list. TAKE is not available in Sheets.

<!--SIBLING-->


## Common errors and how to fix them

- **#REF!** — The shift would land above row 1 or left of column A, or height or width was 0 or omitted in a context that cannot accept it. **Fix:** Keep `rows` and `cols` small enough that the result stays on the sheet. Use a positive height and width when you want a multi-cell range.
- **The sum is too large, too small, or includes a header** — COUNTA counted a column header, a trailing total, or skipped blanks in the middle, so the height does not match the real list. **Fix:** Count only the data cells (for example COUNTA(B2:B100), not COUNTA(B:B) when B1 is a header) and do not leave blank rows in the middle of the list.
- **The workbook became slow** — OFFSET is volatile, so every OFFSET named range recalculates on every change. **Fix:** Switch to an INDEX-ended range or an Excel Table wherever the start cell is fixed and only the length changes.
- **The formula returns a single number when you expected a range** — OFFSET was not wrapped in SUM, AVERAGE, or another function, and the cell shows only the first value of the range. **Fix:** Wrap the OFFSET call in the function that should aggregate it, or use it as the source of a named range or chart series.

## FAQ

### When should I use OFFSET instead of INDEX?

Use OFFSET when the starting cell itself moves — for example “two rows below this label” or “a block that starts n columns to the right.” If the start is fixed and only the length of the list changes, `B2:INDEX(B2:B100, COUNTA(B2:B100))` does the same job and is not volatile. In Microsoft 365, TAKE is often clearer still.

### Does OFFSET work the same in Google Sheets?

The five arguments are the same. The usual Sheets alternative for a growing column is an open-ended range (`B2:B`) or FILTER, which Excel does not treat the same way. TAKE is Excel-only; INDEX works in both.

### Can I use OFFSET in a named range?

Yes. In Excel open Formulas > Name Manager and set the refers-to formula to `=OFFSET(Sheet1!$B$2,0,0,COUNTA(Sheet1!$B$2:$B$100),1)`. In Google Sheets use Data > Named ranges, or point the name at `B2:B` and skip OFFSET. See [dynamic named range](../dynamic-range-google-sheets/) for the full walkthrough.

### Why is OFFSET called volatile?

A volatile function recalculates whenever anything in the workbook changes, even if its inputs did not. A few OFFSET formulas are fine; a sheet of them, each wrapping COUNTA on a large column, is a common reason a model feels sluggish.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
