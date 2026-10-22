---
title: How to Use XLOOKUP in Excel
slug: xlookup-excel
date: '2026-10-22'
summary: 'XLOOKUP searches one range and returns the matching item from another range.
  It replaces VLOOKUP, HLOOKUP and most INDEX MATCH formulas: it can look left, defaults
  to an exact match, and has a built-in "not found" message. Here is the syntax, a
  worked example and the optional arguments you will actu'
tags:
- Lookup & reference
- Excel
keyword: xlookup-excel
niche: sheets-formulas
provider: structured
entry_id: xlookup
platform: Excel
category: lookup
faq:
- q: Is XLOOKUP better than VLOOKUP?
  a: In most cases yes. It can return columns to the left, defaults to an exact match,
    does not break when columns are inserted, and can return several columns at once.
    VLOOKUP is only better for compatibility with old Excel versions.
- q: Can XLOOKUP return more than one column?
  a: Yes. Give it a multi-column return range such as C2:D6 and the result spills
    into adjacent cells.
- q: Does Google Sheets have XLOOKUP?
  a: Yes. Google Sheets has had XLOOKUP since 2022 with the same arguments as Excel.
related:
- - vlookup-excel
  - vlookup-google-sheets
- - xlookup-return-multiple-columns-excel
  - xlookup-return-multiple-columns-google-sheets
- - index-match-excel
  - index-match-google-sheets
- - vlookup-multiple-criteria-excel
  - vlookup-multiple-criteria-google-sheets
- - last-value-excel
  - last-value-google-sheets
sibling: xlookup-google-sheets
---
XLOOKUP searches one range and returns the matching item from another range. It replaces VLOOKUP, HLOOKUP and most INDEX MATCH formulas: it can look left, defaults to an exact match, and has a built-in "not found" message. Here is the syntax, a worked example and the optional arguments you will actually use.

## Quick answer

Use this formula in Excel:

```excel
=XLOOKUP(F2, B2:B6, A2:A6, "Not found")
```

Syntax: `XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])`. Find F2 in B2:B6 and return the item in the same position of A2:A6.

## The problem

You have an employee table and want to type a name and get the employee ID. The ID column is to the left of the name column, so VLOOKUP cannot do it without rearranging the data.

## Worked example

Look up the employee ID (column A) for the name typed in column F.

| | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| 1 | **Employee ID** | **Name** | **Department** | **Salary** |  | **Name** | **Employee ID** |
| 2 | E-1001 | Ana Lopez | Sales | 58000 |  | David Kim | **E-1004** |
| 3 | E-1002 | Ben Carter | IT | 72000 |  | Zoe Hart | **Not found** |
| 4 | E-1003 | Chloe Wong | Finance | 66000 |  |  |  |
| 5 | E-1004 | David Kim | IT | 69500 |  |  |  |
| 6 | E-1005 | Emma Novak | Marketing | 61000 |  |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**G2** — ID for David Kim (a column to the left)

```excel
=XLOOKUP(F2, B2:B6, A2:A6, "Not found")
```

Result: **E-1004**

**G3** — a name that is not in the list

```excel
=XLOOKUP(F3, B2:B6, A2:A6, "Not found")
```

Result: **Not found**

<!--AD_IN_ARTICLE-->

## How the formula works

1. `F2` is the value to search for.
2. `B2:B6` is where to search. Unlike VLOOKUP, this can be any column, it does not have to be the first one.
3. `A2:A6` is what to return. It must have the same number of rows as the search range; here it is to the left, which VLOOKUP cannot do.
4. `"Not found"` is returned instead of #N/A when there is no match.
5. Match mode and search mode are optional. Leaving them out gives an exact match searched from top to bottom, which is what you want most of the time.

## Excel-specific notes

XLOOKUP is available in Microsoft 365, Excel 2021, Excel 2024 and Excel for the web. In Excel 2019 and older it returns #NAME?, so use INDEX MATCH if the file is shared with people on older versions. Useful options: match_mode 2 enables wildcards (* and ?), match_mode -1 returns the next smaller item, and search_mode -1 searches from the last row up, which gives you the most recent entry when a value appears more than once.

**Most recent match (search from the bottom)**

```excel
=XLOOKUP(F2, B2:B6, D2:D6, "Not found", 0, -1)
```

**Wildcard match (name starts with the text in F2)**

```excel
=XLOOKUP(F2&"*", B2:B6, A2:A6, "Not found", 2)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=XLOOKUP(F2, B2:B6, A2:A6, "Not found")
```

Google Sheets supports XLOOKUP with the same argument order, so this formula works unchanged there.

<!--SIBLING-->


## Common errors and how to fix them

- **#NAME?** — Your Excel version does not have XLOOKUP (Excel 2019 or older), or the function name is misspelled. **Fix:** Use INDEX MATCH instead, or open the file in Microsoft 365 / Excel for the web.
- **#VALUE!** — The lookup array and return array have different sizes, for example B2:B6 and A2:A7. **Fix:** Make both ranges cover exactly the same rows.
- **#N/A** — No match and no if_not_found argument, often due to stray spaces or numbers stored as text. **Fix:** Add a fourth argument such as "Not found", and clean the data with TRIM or VALUE.

## FAQ

### Is XLOOKUP better than VLOOKUP?

In most cases yes. It can return columns to the left, defaults to an exact match, does not break when columns are inserted, and can return several columns at once. VLOOKUP is only better for compatibility with old Excel versions.

### Can XLOOKUP return more than one column?

Yes. Give it a multi-column return range such as C2:D6 and the result spills into adjacent cells.

### Does Google Sheets have XLOOKUP?

Yes. Google Sheets has had XLOOKUP since 2022 with the same arguments as Excel.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
