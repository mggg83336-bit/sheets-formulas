---
title: How to Generate a Random Integer in Excel
slug: randbetween-excel
date: '2026-11-11'
summary: RANDBETWEEN returns a random whole number between two bounds, and both bounds
  are included. It is the usual tool for dice rolls, sample IDs, and test data in
  a fixed range. The function is volatile — a new integer appears on every recalculation
  — so freeze values you need to keep. Excel 365 can spil
tags:
- Financial & percentages
- Excel
keyword: randbetween-excel
niche: sheets-formulas
provider: structured
entry_id: randbetween
platform: Excel
category: financial
faq:
- q: Does RANDBETWEEN include both the bottom and the top?
  a: Yes. RANDBETWEEN(10, 20) can return 10 and can return 20. That is the same rule
    as INT(RAND()*(20-10+1))+10, which is why the +1 is required in the RAND form.
- q: How do I fill a column of random integers without dragging?
  a: In Excel 365 use =RANDARRAY(n, 1, bottom, top, TRUE). In Google Sheets RANDARRAY
    cannot take min, max, or integer; use =ARRAYFORMULA(INT(RANDARRAY(n, 1)*(top-bottom+1))+bottom)
    or ARRAYFORMULA with RANDBETWEEN. In older Excel, fill =RANDBETWEEN($E$2, $E$3)
    down.
- q: How do I get unique random integers?
  a: Do not filter duplicates after the fact and hope you still have enough rows.
    Build the list of allowed integers with SEQUENCE, shuffle it with RANDARRAY, and
    take as many as you need. That is sampling without replacement.
- q: Can I use this for lottery numbers or passwords?
  a: No. Spreadsheet random functions are fine for mock data and informal shuffles,
    not for security or a legally auditable draw. Generate those elsewhere and paste
    the results as values if you only need to display them.
related:
- - sequence-excel
  - sequence-google-sheets
- - unique-excel
  - unique-google-sheets
- - large-small-excel
  - large-small-google-sheets
- - rank-excel
  - rank-google-sheets
- - round-excel
  - round-google-sheets
sibling: randbetween-google-sheets
---
RANDBETWEEN returns a random whole number between two bounds, and both bounds are included. It is the usual tool for dice rolls, sample IDs, and test data in a fixed range. The function is volatile — a new integer appears on every recalculation — so freeze values you need to keep. Excel 365 can spill a block of integers with RANDARRAY; Google Sheets RANDARRAY cannot, and uses a different pattern.

## Quick answer

Use this formula in Excel:

```excel
=RANDBETWEEN(E2, E3)
```

Syntax: `RANDBETWEEN(bottom, top)` returns a random integer in that range, with both ends included. Here E2 is 10 and E3 is 20, so every draw is a whole number from 10 through 20. Non-integer bounds are truncated toward zero first. The result changes whenever the workbook recalculates.

## The problem

You need random integers from 10 to 20 inclusive: a few sample draws for a model, a check that both ends of the range are reachable, and a way to generate a whole column of draws without dragging the fill handle. You also want to know how to stop the numbers from changing every time the sheet recalculates.

## Worked example

Six already-drawn integers in column B stand in for a frozen RANDBETWEEN(10,20) sample, so the range checks can be recalculated. E4 and E5 are fixed stand-ins for a RAND() draw at the bottom and just below 1; the INT formulas show that both 10 and 20 are reachable. The live RANDBETWEEN in E12 changes on every recalc and is not machine-verified.

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Draw** | **Frozen sample** |  | **Item** | **Value** |
| 2 | 1 | 14 |  | Low | 10 |
| 3 | 2 | 10 |  | High | 20 |
| 4 | 3 | 17 |  | Stand-in at 0 | 0 |
| 5 | 4 | 11 |  | Stand-in near 1 | 0.999 |
| 6 | 5 | 20 |  | Integer at low bound | **10** |
| 7 | 6 | 15 |  | Integer at high bound | **20** |
| 8 |  |  |  | Min of sample | **10** |
| 9 |  |  |  | Max of sample | **20** |
| 10 |  |  |  | Rank of the 20 | **1** |
| 11 |  |  |  | Count inside 10–20 | **6** |
| 12 |  |  |  | Live RANDBETWEEN | **(changes on every recalc)** |

Formulas used in the example (results shown in **bold** in the table above):

**E6** — inclusive low bound from a 0 stand-in

```excel
=INT(E4*(E3-E2+1))+E2
```

Result: **10**

**E7** — inclusive high bound from a 0.999 stand-in

```excel
=INT(E5*(E3-E2+1))+E2
```

Result: **20**

**E8** — minimum of the frozen sample

```excel
=MIN(B2:B7)
```

Result: **10**

**E9** — maximum of the frozen sample

```excel
=MAX(B2:B7)
```

Result: **20**

**E10** — descending rank of the 20

```excel
=RANK(B6, B2:B7, 0)
```

Result: **1**

**E11** — how many frozen draws sit in 10–20

```excel
=COUNTIFS(B2:B7, ">="&E2, B2:B7, "<="&E3)
```

Result: **6**

**E12** — live random integer (volatile)

```excel
=RANDBETWEEN(E2, E3)
```

Result: **(changes on every recalc)**

<!--AD_IN_ARTICLE-->

## How the formula works

1. Set the bounds in E2 and E3 (here 10 and 20). `=RANDBETWEEN(E2, E3)` then returns a whole number in that closed interval.
2. The inclusive rewrite is `=INT(RAND()*(top-bottom+1))+bottom`. With a stand-in of 0, `=INT(E4*(E3-E2+1))+E2` equals 10. With 0.999, the same formula equals 20. A stand-in of 1 would overshoot, which is why RAND itself never returns 1.
3. Column B is a frozen sample, as if six RANDBETWEEN results had already been pasted as values. MIN is 10, MAX is 20, every draw falls inside the bounds (COUNTIFS = 6), and the 20 ranks first.
4. To keep a live draw, copy it and paste values. Leaving RANDBETWEEN in the cell means the number will change the next time the workbook calculates.
5. For a list of integers that must not repeat, shuffle `SEQUENCE(E3-E2+1, 1, E2)` with RANDARRAY rather than calling RANDBETWEEN once per row. Duplicates are expected when you draw with replacement.

## Excel-specific notes

RANDBETWEEN has been built into Excel since Excel 2007 (older versions needed the Analysis ToolPak). It is volatile: any edit, opening the file, or pressing F9 draws a new integer, which will silently rewrite a posted sample, an assigned ID, or a “random” prize if you leave the live formula in place. When a draw must stay put, copy the cells and use Paste Special > Values. Both bounds are inclusive, which is why the classic rewrite `=INT(RAND()*(top-bottom+1))+bottom` adds 1 inside the parentheses — without it the top integer would almost never appear. Duplicates are allowed; this is sampling with replacement. For a set of unique integers, shuffle a SEQUENCE of the range with SORTBY and RANDARRAY, then TAKE as many as you need, instead of calling RANDBETWEEN in a loop and hoping. In Microsoft 365 / Excel 2021 you can spill a column of integers directly with `=RANDARRAY(6, 1, E2, E3, TRUE)`; that function is not in Excel 2019 or earlier, where you fill `=RANDBETWEEN($E$2, $E$3)` down. Do not use either function as a source of cryptographic or audit-grade randomness, and never let a live random formula sit in a cell that is later treated as a permanent invoice or employee number. `#NUM!` means bottom is greater than top after any truncation.

**Spill six random integers (Excel 365 / 2021)**

```excel
=RANDARRAY(6, 1, E2, E3, TRUE)
```

**Classic RAND rewrite (inclusive)**

```excel
=INT(RAND()*(E3-E2+1))+E2
```

**Unique shuffle of every integer in the range**

```excel
=SORTBY(SEQUENCE(E3-E2+1, 1, E2), RANDARRAY(E3-E2+1))
```

**Fill-down form with locked bounds**

```excel
=RANDBETWEEN($E$2, $E$3)
```


## Google Sheets version

The same formula works unchanged in Google Sheets:

```excel
=RANDBETWEEN(E2, E3)
```

Excel 365 can spill integers with RANDARRAY(rows, columns, min, max, TRUE). Sheets RANDARRAY cannot take those extra arguments; use the INT or ARRAYFORMULA forms above. Excel has no ARRAYFORMULA and no open-ended A2:A range.

<!--SIBLING-->


## Common errors and how to fix them

- **#NUM!** — Bottom is greater than top, or became greater after Excel truncated a non-integer bound toward zero. **Fix:** Swap the bounds or correct them, e.g. `=RANDBETWEEN(10, 20)` not `=RANDBETWEEN(20, 10)`.
- **The numbers keep changing** — RANDBETWEEN is volatile and recalculates on every workbook change (and typically when the file is reopened). **Fix:** Copy the results and use Paste Special > Values when the draws need to stay fixed.
- **The top value never appears, or a value one past the top does** — The RAND rewrite omitted the `+1`, or someone used a scale that can reach 1 (`INT(RAND()*10)+1` is 1–10; `INT(RAND()*10)` is 0–9). **Fix:** Use `=INT(RAND()*(top-bottom+1))+bottom`, or just call RANDBETWEEN, which already includes both ends.
- **Repeated integers in a “unique” sample** — RANDBETWEEN (and RANDARRAY with integer TRUE) samples with replacement, so duplicates are normal. **Fix:** Shuffle a SEQUENCE of the range (SORTBY or SORT with RANDARRAY) and take the first n values.

## FAQ

### Does RANDBETWEEN include both the bottom and the top?

Yes. RANDBETWEEN(10, 20) can return 10 and can return 20. That is the same rule as INT(RAND()*(20-10+1))+10, which is why the +1 is required in the RAND form.

### How do I fill a column of random integers without dragging?

In Excel 365 use `=RANDARRAY(n, 1, bottom, top, TRUE)`. In Google Sheets RANDARRAY cannot take min, max, or integer; use `=ARRAYFORMULA(INT(RANDARRAY(n, 1)*(top-bottom+1))+bottom)` or ARRAYFORMULA with RANDBETWEEN. In older Excel, fill `=RANDBETWEEN($E$2, $E$3)` down.

### How do I get unique random integers?

Do not filter duplicates after the fact and hope you still have enough rows. Build the list of allowed integers with SEQUENCE, shuffle it with RANDARRAY, and take as many as you need. That is sampling without replacement.

### Can I use this for lottery numbers or passwords?

No. Spreadsheet random functions are fine for mock data and informal shuffles, not for security or a legally auditable draw. Generate those elsewhere and paste the results as values if you only need to display them.

## Related formulas

<!--RELATED-->

<!--PRODUCT_BOX-->
