---
title: How to Use TEXTJOIN in Excel
slug: textjoin-excel
date: '2026-10-22'
summary: TEXTJOIN combines text from many cells with a delimiter of your choice and
  can skip empty cells automatically. It is the modern replacement for chains of &
  or CONCATENATE. This page includes a conditional join, listing only the names that
  meet a condition, in one cell.
tags:
- Text formulas
- Excel
keyword: textjoin-excel
niche: sheets-formulas
provider: structured
entry_id: textjoin
platform: Excel
category: text
faq:
- q: What is the difference between TEXTJOIN, CONCAT and CONCATENATE?
  a: TEXTJOIN adds a delimiter and can skip blanks. CONCAT joins ranges without a
    delimiter. CONCATENATE only accepts individual cells.
- q: How do I join with a line break?
  a: Use CHAR(10) as the delimiter and enable Wrap Text on the cell.
related:
- - lookup-multiple-values-excel
  - lookup-multiple-values-google-sheets
- - split-text-excel
  - split-text-google-sheets
- - count-unique-excel
  - count-unique-google-sheets
- - trim-excel
  - trim-google-sheets
sibling: textjoin-google-sheets
---
TEXTJOIN combines text from many cells with a delimiter of your choice and can skip empty cells automatically. It is the modern replacement for chains of & or CONCATENATE. This page includes a conditional join, listing only the names that meet a condition, in one cell.

## Quick answer

Use this formula in Excel:

```excel
=TEXTJOIN(", ", TRUE, B2:B7)
```

Syntax: `TEXTJOIN(delimiter, ignore_empty, text1, [text2], ...)`. Join B2:B7 with ", ", skipping empty cells because the second argument is TRUE.

## The problem

You need a comma-separated list of team members in one cell, both for everyone and for one team only, for example to paste into an email or a report header.

## Worked example

Join all members, then only the Red team.

| | A | B | C | D |
|---|---|---|---|---|
| 1 | **Team** | **Member** |  | **List** |
| 2 | Red | Ana |  | **Ana, Ben, Chloe, Dev, Eva, Finn** |
| 3 | Blue | Ben |  | **Ana, Chloe, Eva** |
| 4 | Red | Chloe |  |  |
| 5 | Green | Dev |  |  |
| 6 | Red | Eva |  |  |
| 7 | Blue | Finn |  |  |

Formulas used in the example (results shown in **bold** in the table above):

**D2** — everyone

```excel
=TEXTJOIN(", ", TRUE, B2:B7)
```

Result: **Ana, Ben, Chloe, Dev, Eva, Finn**

**D3** — Red team only

```excel
=TEXTJOIN(", ", TRUE, FILTER(B2:B7, A2:A7="Red"))
```

Result: **Ana, Chloe, Eva**

<!--AD_IN_ARTICLE-->

## How the formula works

1. The delimiter `", "` is placed between items (not after the last one).
2. `TRUE` skips empty cells so you never get ", ," gaps. Use FALSE to keep a placeholder for blanks.
3. `B2:B7` can be any mix of ranges and single values, e.g. `TEXTJOIN(" ", TRUE, A2, B2, C2)`.
4. In the conditional version, FILTER first reduces the list to the Red rows and TEXTJOIN joins only those.

## Excel-specific notes

TEXTJOIN is available in Excel 2019, 2021, 2024 and Microsoft 365. In Excel 2016 and older you have to chain cells with & or use CONCATENATE, neither of which can skip blanks. For a conditional list in Microsoft 365, feed FILTER into TEXTJOIN. In Excel 2019, which has TEXTJOIN but not FILTER, use `IF(A2:A7="Red", B2:B7, "")` as the text argument and confirm with Ctrl+Shift+Enter. A single cell holds at most 32,767 characters.

**Excel 2019 conditional join (array formula)**

```excel
=TEXTJOIN(", ", TRUE, IF(A2:A7="Red", B2:B7, ""))
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=TEXTJOIN(", ", TRUE, B2:B7)
```

Google Sheets uses the same syntax and also has JOIN, which does not skip blanks.

<!--SIBLING-->


## Common errors and how to fix them

- **#NAME?** — Excel 2016 or older does not have TEXTJOIN. **Fix:** Use & or CONCATENATE, or open the file in Excel 2019+ / Microsoft 365.
- **#VALUE!** — The result is longer than 32,767 characters. **Fix:** Join fewer cells or split the output across cells.
- **Numbers lose their formatting** — TEXTJOIN uses the raw value, so 0.5 stays 0.5 even if the cell shows 50%. **Fix:** Format inside the join, e.g. TEXT(C2:C7, "0%").

## FAQ

### What is the difference between TEXTJOIN, CONCAT and CONCATENATE?

TEXTJOIN adds a delimiter and can skip blanks. CONCAT joins ranges without a delimiter. CONCATENATE only accepts individual cells.

### How do I join with a line break?

Use CHAR(10) as the delimiter and enable Wrap Text on the cell.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
