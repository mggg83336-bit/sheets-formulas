---
title: XLOOKUP to Return Multiple Columns in Excel
slug: xlookup-return-multiple-columns-excel
date: '2026-10-22'
summary: 'One XLOOKUP can return several columns at once: give it a multi-column return
  range and the results spill across. This page shows how to return adjacent columns,
  columns in a different order, and a whole matching row.'
tags:
- Lookup & reference
- Excel
keyword: xlookup-return-multiple-columns-excel
niche: sheets-formulas
provider: structured
entry_id: xlookup-return-multiple-columns
platform: Excel
category: lookup
faq:
- q: Can I copy a spilling XLOOKUP down a column?
  a: Yes, as long as each row has enough empty cells to its right. Lock the lookup
    and return ranges with $ so they do not shift.
- q: How do I return the columns in a different order?
  a: Wrap the return range in CHOOSECOLS (Excel 365 and Google Sheets), e.g. CHOOSECOLS(A2:D6,
    4, 1), or in Google Sheets use {D2:D6, A2:A6}.
related:
- - xlookup-excel
  - xlookup-google-sheets
- - vlookup-excel
  - vlookup-google-sheets
- - index-match-excel
  - index-match-google-sheets
- - lookup-multiple-values-excel
  - lookup-multiple-values-google-sheets
sibling: xlookup-return-multiple-columns-google-sheets
---
One XLOOKUP can return several columns at once: give it a multi-column return range and the results spill across. This page shows how to return adjacent columns, columns in a different order, and a whole matching row.

## Quick answer

Use this formula in Excel:

```excel
=XLOOKUP(F2, B2:B6, C2:D6)
```

The return array C2:D6 is two columns wide, so the result spills into G2 and H2.

## The problem

For a given employee you want the department and the salary next to each other. Writing one lookup per column works, but it is slower to maintain and easy to get out of sync.

## Worked example

Type a name in F2; the department and salary spill into G2:H2.

| | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| 1 | **Employee ID** | **Name** | **Department** | **Salary** |  | **Name** | **Department** | **Salary** |
| 2 | E-1001 | Ana Lopez | Sales | 58000 |  | Chloe Wong | **Finance** | **66000** |
| 3 | E-1002 | Ben Carter | IT | 72000 |  |  |  |  |
| 4 | E-1003 | Chloe Wong | Finance | 66000 |  |  |  |  |
| 5 | E-1004 | David Kim | IT | 69500 |  |  |  |  |
| 6 | E-1005 | Emma Novak | Marketing | 61000 |  |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**G2** — one formula, two results (spills into H2)

```excel
=XLOOKUP(F2, B2:B6, C2:D6)
```

Results: **Finance**, **66000**

<!--AD_IN_ARTICLE-->

## How the formula works

1. XLOOKUP finds the position of F2 in B2:B6 (Chloe Wong is the 3rd item).
2. It returns the 3rd row of the return range. Because C2:D6 has two columns, that row contains two values.
3. The two values spill into G2 and H2. Only G2 contains the formula; H2 shows the spilled result.
4. To return the full record, use A2:D6 as the return range and leave four empty cells to the right.

## Excel-specific notes

Spilled results need empty cells to the right; if anything is in the way, Excel shows #SPILL!. To return columns that are not next to each other, or in a different order, build the return array with CHOOSECOLS or HSTACK (Microsoft 365 and Excel 2024). When you copy the formula down, lock the ranges with $ so every row looks at the same table.

**Non-adjacent columns in any order (salary, then ID)**

```excel
=XLOOKUP(F2, B2:B6, CHOOSECOLS(A2:D6, 4, 1))
```

**The same with HSTACK**

```excel
=XLOOKUP(F2, B2:B6, HSTACK(D2:D6, A2:A6))
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=XLOOKUP(F2, B2:B6, C2:D6)
```

Google Sheets uses the same formula. A blocked spill shows #REF! instead of #SPILL!, and you can also build the return range with curly braces such as {D2:D6, A2:A6}.

<!--SIBLING-->


## Common errors and how to fix them

- **#SPILL! (Excel) / #REF! (Google Sheets)** — A cell in the spill area is not empty. **Fix:** Clear the cells to the right of the formula, including cells that contain only a space.
- **#VALUE!** — The return range has a different number of rows than the lookup range. **Fix:** Make the lookup range and the return range start and end on the same rows.
- **Only one value appears** — The formula is in an old Excel version or inside a table column that cannot spill (Excel tables do not allow spilled formulas). **Fix:** Move the formula outside the Excel Table, or use one XLOOKUP per column.

## FAQ

### Can I copy a spilling XLOOKUP down a column?

Yes, as long as each row has enough empty cells to its right. Lock the lookup and return ranges with $ so they do not shift.

### How do I return the columns in a different order?

Wrap the return range in CHOOSECOLS (Excel 365 and Google Sheets), e.g. CHOOSECOLS(A2:D6, 4, 1), or in Google Sheets use {D2:D6, A2:A6}.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
