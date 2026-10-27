---
title: XLOOKUP to Return Multiple Columns in Google Sheets
slug: xlookup-return-multiple-columns-google-sheets
date: '2026-10-27'
summary: 'One XLOOKUP can return several columns at once: give it a multi-column return
  range and the results spill across. This page shows how to return adjacent columns,
  columns in a different order, and a whole matching row.'
tags:
- Lookup & reference
- Google Sheets
keyword: xlookup-return-multiple-columns-google-sheets
niche: sheets-formulas
provider: structured
entry_id: xlookup-return-multiple-columns
platform: Google Sheets
category: lookup
faq:
- q: Can I copy a spilling XLOOKUP down a column?
  a: Yes, as long as each row has enough empty cells to its right. Lock the lookup
    and return ranges with $ so they do not shift.
- q: How do I return the columns in a different order?
  a: Wrap the return range in CHOOSECOLS (Excel 365 and Google Sheets), e.g. CHOOSECOLS(A2:D6,
    4, 1), or in Google Sheets use {D2:D6, A2:A6}.
related:
- - xlookup-google-sheets
  - xlookup-excel
- - vlookup-google-sheets
  - vlookup-excel
- - index-match-google-sheets
  - index-match-excel
- - lookup-multiple-values-google-sheets
  - lookup-multiple-values-excel
sibling: xlookup-return-multiple-columns-excel
---
One XLOOKUP can return several columns at once: give it a multi-column return range and the results spill across. This page shows how to return adjacent columns, columns in a different order, and a whole matching row.

## Quick answer

Use this formula in Google Sheets:

```excel
=XLOOKUP(F2, B2:B6, C2:D6)
```

Google Sheets spills the two returned values into G2 and H2 just like Excel.

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

## Google Sheets-specific notes

In Google Sheets you can also build the return range with curly braces, which is shorter and works in every version of Sheets: `{D2:D6, A2:A6}` puts Salary first and ID second. If a spilled result would overwrite existing data, Sheets shows #REF! with the message "Array result was not expanded because it would overwrite data", which is the Sheets equivalent of Excel's #SPILL!. CHOOSECOLS and HSTACK also exist in Sheets.

**Non-adjacent columns with curly braces**

```excel
=XLOOKUP(F2, B2:B6, {D2:D6, A2:A6})
```


## Excel version

The same formula works unchanged in Excel:

```excel
=XLOOKUP(F2, B2:B6, C2:D6)
```

Excel uses the same formula. Curly-brace arrays like {D2:D6, A2:A6} do not work in Excel, so use CHOOSECOLS or HSTACK there.

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
