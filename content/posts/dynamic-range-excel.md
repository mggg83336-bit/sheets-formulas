---
title: How to Create a Dynamic Named Range in Excel
slug: dynamic-range-excel
date: '2026-11-12'
summary: A dynamic named range expands as you add rows, so SUM, charts, data-validation
  lists and lookups keep working without edits. In Excel the durable options are an
  Excel Table or a non-volatile INDEX range; OFFSET plus COUNTA still works but recalculates
  often. In Google Sheets the idiomatic approach i
tags:
- Lookup & reference
- Excel
keyword: dynamic-range-excel
niche: sheets-formulas
provider: structured
entry_id: dynamic-range
platform: Excel
category: lookup
faq:
- q: Should I use an Excel Table or a named formula?
  a: Use a Table when the data is a proper list with headers and you work mainly in
    Excel — structured references such as Table1[Qty] expand automatically and are
    not volatile. Use a named INDEX (or OFFSET) range when you need a name for data
    validation, a chart in an older workbook, or a single column that is not part
    of a table.
- q: How do I do this in Google Sheets?
  a: Data > Named ranges, name the range, and set the address to B2:B (or A2:B for
    two columns). That open-ended form is the Sheets equivalent of an auto-expanding
    range. Use FILTER when you must skip blanks or a trailing total. Sheets has no
    Excel Tables.
- q: Can a drop-down use a dynamic named range?
  a: Yes. In Excel, point Data Validation at =Qty (the name must be workbook-scoped).
    In Google Sheets, point the validation list at the named range, or at a helper
    column filled by FILTER. If the drop-down does not grow, the name is still a fixed
    address — redefine it as shown in the steps.
- q: OFFSET or INDEX, which should I store in Name Manager?
  a: INDEX. It returns the same growing range and does not recalculate on every unrelated
    change. Keep OFFSET for cases where the start cell itself moves. INDIRECT can
    also build an address from text, but it is volatile too and is the wrong tool
    for a simple growing list.
related:
- - offset-excel
  - offset-google-sheets
- - indirect-excel
  - indirect-google-sheets
- - last-value-excel
  - last-value-google-sheets
- - filter-excel
  - filter-google-sheets
- - unique-excel
  - unique-google-sheets
sibling: dynamic-range-google-sheets
---
A dynamic named range expands as you add rows, so SUM, charts, data-validation lists and lookups keep working without edits. In Excel the durable options are an Excel Table or a non-volatile INDEX range; OFFSET plus COUNTA still works but recalculates often. In Google Sheets the idiomatic approach is an open-ended named range such as B2:B, with FILTER as a formula-only alternative.

## Quick answer

Use this formula in Excel:

```excel
=SUM(B2:INDEX(B2:B10, COUNTA(B2:B10)))
```

`INDEX(B2:B10, COUNTA(B2:B10))` returns the last filled cell in the quantity column. Joining it to B2 with a colon builds a range that ends at that cell, and SUM adds 10 + 8 + 15 + 6 = 39. Put the same formula (with a taller ceiling such as B2:B1000) in Formulas > Name Manager as the definition of a name like `Qty`, then write `=SUM(Qty)` anywhere in the workbook.

## The problem

You keep a product list that gains a new row every week. A total, a drop-down, and a chart should all follow the list automatically. You do not want to edit the named range — or every formula that uses it — each time someone types a new product.

## Worked example

Four products in A2:B5, with room to type more rows underneath. D2 sums the quantities with OFFSET, D3 counts the product names, D4 uses the non-volatile INDEX form of the same sum, and D5 returns the last product name.

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **Product** | **Qty** |  | **Result** |
| 2 | Apples | 10 |  | **39** |
| 3 | Bananas | 8 |  | **4** |
| 4 | Cherries | 15 |  | **39** |
| 5 | Dates | 6 |  | **Dates** |

Formulas used in the example (results shown in **bold** in the table above):

**D2** — sum of Qty with OFFSET and COUNTA

```excel
=SUM(OFFSET(B2, 0, 0, COUNTA(B2:B10), 1))
```

Result: **39**

**D3** — count of product names in the dynamic range

```excel
=COUNTA(OFFSET(A2, 0, 0, COUNTA(A2:A10), 1))
```

Result: **4**

**D4** — same sum with a non-volatile INDEX range

```excel
=SUM(B2:INDEX(B2:B10, COUNTA(B2:B10)))
```

Result: **39**

**D5** — last product name in the growing list

```excel
=INDEX(A2:A10, COUNTA(A2:A10))
```

Result: **Dates**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Type the list with a header in row 1 and a contiguous block of data from row 2 down. In the example, four products sit in A2:B5; A6:A10 and B6:B10 are empty on purpose so the range still has room to grow.
2. `COUNTA(B2:B10)` returns 4, the number of filled quantities. `=SUM(OFFSET(B2, 0, 0, COUNTA(B2:B10), 1))` turns that count into a height, so the range is B2:B5 and the sum is 10 + 8 + 15 + 6 = 39.
3. The same idea on the name column, `=COUNTA(OFFSET(A2, 0, 0, COUNTA(A2:A10), 1))`, returns 4. When you later type Elderberry in A6, both COUNTA results become 5 and the sum range grows on its own.
4. The INDEX form is the one to store in Excel’s Name Manager: `=SUM(B2:INDEX(B2:B10, COUNTA(B2:B10)))` also returns 39, but it is not volatile. Raise the ceiling to B2:B1000 in a real workbook. `=INDEX(A2:A10, COUNTA(A2:A10))` returns Dates, the last name in the list.
5. To turn the formula into a name in Excel, open Formulas > Name Manager, add `Qty`, and paste `=Sheet1!$B$2:INDEX(Sheet1!$B$2:$B$1000, COUNTA(Sheet1!$B$2:$B$1000))`. In Google Sheets, open Data > Named ranges and point `Qty` at `B2:B`. After that, `=SUM(Qty)` works in both. In Excel, converting the list to a Table is often simpler still.

## Excel-specific notes

The preferred Excel approach, when you can use it, is an Excel Table. Select the list, choose Insert > Table, and refer to the column with a structured reference (`=SUM(Table1[Qty])`). The table — and any chart or validation list that uses it — grows when you type in the next row, and the reference is not volatile. When you need a named range rather than a table (for example a single-column list used by data validation in an older workbook), define it with INDEX as above, or with `=OFFSET(Sheet1!$B$2,0,0,COUNTA(Sheet1!$B$2:$B$1000),1)`. OFFSET is easier to read for some people but is volatile; INDEX is the better default. In Name Manager, decide whether the name is workbook-scoped or worksheet-scoped, and always lock the anchors with `$` so the definition does not shift when you click around. COUNTA must count only data cells: if you write COUNTA($B:$B) and B1 is the header “Qty”, the height is one too tall. Blank cells in the middle of the list also throw the count off — keep the list contiguous. Microsoft 365 can additionally spill a clean list with FILTER (`=FILTER(A2:B10, A2:A10<>"")`) and feed that to a function or a chart, which avoids a named range altogether.

**OFFSET definition for a named range (volatile)**

```excel
=SUM(OFFSET(B2, 0, 0, COUNTA(B2:B10), 1))
```

**Excel Table structured reference**

```excel
=SUM(Table1[Qty])
```

**Spill only the filled rows (Microsoft 365)**

```excel
=FILTER(A2:B10, A2:A10<>"")
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=SUM(B2:INDEX(B2:B10, COUNTA(B2:B10)))
```

Excel cannot use B2:B as a native open-ended range and instead uses an Excel Table or an INDEX/OFFSET named range. Structured references such as Table1[Qty] are Excel-only.

<!--SIBLING-->


## Common errors and how to fix them

- **The total is one row too large, or includes the header** — COUNTA was applied to the whole column (`B:B`) and counted the header, or a total already sitting under the list. **Fix:** Count only the data (`COUNTA(B2:B1000)`), keep totals off to the side, and in Sheets avoid an open-ended `B2:B` if something sits below the list.
- **The range stops too early or skips new rows** — A blank cell in the middle of the list makes COUNTA smaller than the last row number, so INDEX or OFFSET ends before the real last item. **Fix:** Keep the list contiguous. If gaps are unavoidable, FILTER on `<>""` instead of COUNTA.
- **#NAME? or the name does not update** — The named range was defined as a fixed address (B2:B5) rather than a formula or an open-ended range, or the sheet name in the definition no longer matches. **Fix:** Redefine it with INDEX, OFFSET, an Excel Table, or (in Sheets) `B2:B`. Check the sheet name and the `$` anchors in Name Manager.
- **The workbook became slow** — The name uses OFFSET (volatile) and is referenced many times, or COUNTA is running over an entire column on every recalc. **Fix:** Switch the definition to INDEX with a bounded ceiling (B2:B1000), or use an Excel Table. In Sheets, prefer `B2:B` or FILTER.

## FAQ

### Should I use an Excel Table or a named formula?

Use a Table when the data is a proper list with headers and you work mainly in Excel — structured references such as `Table1[Qty]` expand automatically and are not volatile. Use a named INDEX (or OFFSET) range when you need a name for data validation, a chart in an older workbook, or a single column that is not part of a table.

### How do I do this in Google Sheets?

Data > Named ranges, name the range, and set the address to `B2:B` (or `A2:B` for two columns). That open-ended form is the Sheets equivalent of an auto-expanding range. Use FILTER when you must skip blanks or a trailing total. Sheets has no Excel Tables.

### Can a drop-down use a dynamic named range?

Yes. In Excel, point Data Validation at `=Qty` (the name must be workbook-scoped). In Google Sheets, point the validation list at the named range, or at a helper column filled by FILTER. If the drop-down does not grow, the name is still a fixed address — redefine it as shown in the steps.

### OFFSET or INDEX, which should I store in Name Manager?

INDEX. It returns the same growing range and does not recalculate on every unrelated change. Keep [OFFSET](../offset-excel/) for cases where the start cell itself moves. [INDIRECT](../indirect-excel/) can also build an address from text, but it is volatile too and is the wrong tool for a simple growing list.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
