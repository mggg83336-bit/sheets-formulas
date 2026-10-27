---
title: How to Use LEFT, RIGHT and MID in Excel
slug: left-right-mid-excel
date: '2026-10-27'
summary: LEFT, RIGHT and MID pull a fixed number of characters from the start, end
  or middle of a text string. Combined with FIND or LEN they also extract variable
  pieces such as everything before a dash. The same three functions work in Excel
  and Google Sheets; Sheets users also have REGEXEXTRACT for patter
tags:
- Text formulas
- Excel
keyword: left-right-mid-excel
niche: sheets-formulas
provider: structured
entry_id: left_right_mid
platform: Excel
category: text
faq:
- q: What is the difference between LEFT / RIGHT / MID and TEXTBEFORE / TEXTAFTER?
  a: LEFT / RIGHT / MID cut by character count (or with FIND for a marker). TEXTBEFORE
    / TEXTAFTER (Excel 365) cut by a delimiter string directly and support instance
    numbers and case options.
- q: How do I extract text between two dashes?
  a: 'Excel: =MID(A2, FIND("-",A2)+1, FIND("-",A2, FIND("-",A2)+1)-FIND("-",A2)-1).
    Google Sheets can use =REGEXEXTRACT(A2, "-([^-]+)-").'
- q: Do LEFT, RIGHT and MID work the same in Google Sheets?
  a: Yes — same argument order and results. Use ARRAYFORMULA to apply them to a whole
    column, and REGEXEXTRACT when a regular expression is clearer than FIND + MID.
related:
- - text-before-character-excel
  - text-before-character-google-sheets
- - text-after-character-excel
  - text-after-character-google-sheets
- - split-text-excel
  - split-text-google-sheets
- - trim-excel
  - trim-google-sheets
sibling: left-right-mid-google-sheets
---
LEFT, RIGHT and MID pull a fixed number of characters from the start, end or middle of a text string. Combined with FIND or LEN they also extract variable pieces such as everything before a dash. The same three functions work in Excel and Google Sheets; Sheets users also have REGEXEXTRACT for pattern-based pulls.

## Quick answer

Use this formula in Excel:

```excel
=LEFT(A2, 3)
```

Syntax: `LEFT(text, [num_chars])`, `RIGHT(text, [num_chars])`, `MID(text, start_num, num_chars)`. LEFT returns the first 3 characters of A2.

## The problem

Codes, phone numbers or full names sit in one column, and you need a prefix, a suffix or the middle segment in its own cell — for example the first three letters of a name, the last four digits of a phone number, or the characters between two dashes.

## Worked example

Pull a prefix, a suffix and a middle segment; then everything before a dash.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Value** | **Left 3** | **Right 4** | **Mid 5** | **Before dash** |
| 2 | Ana Lopez | **Ana** | **opez** | **Lopez** |  |
| 3 | SKU-1042-RED | **SKU** | **-RED** |  | **SKU** |
| 4 | (555) 123-4567 | **(55** | **4567** |  | **4567** |

Formulas used in the example (results shown in **bold** in the table above):

**B2 (filled to B4)** — first 3 characters, filled down

```excel
=LEFT(A2, 3)
```

Results: **Ana**, **SKU**, **(55**

**C2 (filled to C4)** — last 4 characters, filled down

```excel
=RIGHT(A2, 4)
```

Results: **opez**, **-RED**, **4567**

**D2** — 5 characters starting at position 5

```excel
=MID(A2, 5, 5)
```

Result: **Lopez**

**E3** — everything before the first dash

```excel
=LEFT(A3, FIND("-", A3)-1)
```

Result: **SKU**

**E4** — last 4 digits via RIGHT (phone)

```excel
=RIGHT(A4, 4)
```

Result: **4567**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Decide whether you need characters from the start (LEFT), the end (RIGHT) or a position in the middle (MID).
2. For LEFT / RIGHT, pass the cell and the number of characters, e.g. `=LEFT(A2, 3)` or `=RIGHT(A2, 4)`.
3. For MID, pass start position and length: `=MID(A2, 5, 5)` returns five characters beginning at character 5.
4. When the cut point depends on a marker, nest FIND: `=LEFT(A2, FIND("-", A2)-1)` stops just before the first dash.
5. Fill the formula down the column, or in Google Sheets wrap it in ARRAYFORMULA to fill every row at once.

## Excel-specific notes

LEFT / RIGHT / MID are available in every Excel version. `num_chars` is optional for LEFT and RIGHT (default 1). MID always needs a start position (1 = first character) and a length. To take everything before a marker use `LEFT(A2, FIND("-", A2)-1)`; everything after the first marker is `MID(A2, FIND("-", A2)+1, LEN(A2))` or, in Microsoft 365, TEXTAFTER. LEN counts characters so you can compute dynamic lengths. These functions treat numbers as text automatically; if you need a real number wrap the result in VALUE. For pattern-based extracts in Microsoft 365, TEXTBEFORE / TEXTAFTER / TEXTSPLIT are often clearer.

**Last 4 characters**

```excel
=RIGHT(A2, 4)
```

**Characters 5 to 9 (start at 5, length 5)**

```excel
=MID(A2, 5, 5)
```

**Everything before the first dash**

```excel
=LEFT(A2, FIND("-", A2)-1)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=LEFT(A2, 3)
```

Sheets matches Excel on LEFT / RIGHT / MID, adds ARRAYFORMULA for whole-column fills, and uses REGEXEXTRACT where Excel 365 would use TEXTBEFORE / TEXTAFTER.

<!--SIBLING-->


## Common errors and how to fix them

- **#VALUE!** — FIND did not find the marker, so `FIND(...)-1` became invalid, or num_chars was negative. **Fix:** Wrap with IFERROR, or check the marker exists first: `=IF(ISNUMBER(FIND("-",A2)), LEFT(A2, FIND("-",A2)-1), A2)`.
- **Result looks truncated or includes an extra character** — Off-by-one in the length or start position (forgetting that FIND returns the marker's position). **Fix:** Subtract 1 from FIND when using LEFT; add 1 when using MID/RIGHT to start after the marker. Test on one row first.
- **Leading zeros disappear** — The extracted piece looks like a number and the cell is formatted as General. **Fix:** Format the result column as Text, or keep it as text with `="" & LEFT(A2, 3)`.

## FAQ

### What is the difference between LEFT / RIGHT / MID and TEXTBEFORE / TEXTAFTER?

LEFT / RIGHT / MID cut by character count (or with FIND for a marker). TEXTBEFORE / TEXTAFTER (Excel 365) cut by a delimiter string directly and support instance numbers and case options.

### How do I extract text between two dashes?

Excel: `=MID(A2, FIND("-",A2)+1, FIND("-",A2, FIND("-",A2)+1)-FIND("-",A2)-1)`. Google Sheets can use `=REGEXEXTRACT(A2, "-([^-]+)-")`.

### Do LEFT, RIGHT and MID work the same in Google Sheets?

Yes — same argument order and results. Use ARRAYFORMULA to apply them to a whole column, and REGEXEXTRACT when a regular expression is clearer than FIND + MID.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
