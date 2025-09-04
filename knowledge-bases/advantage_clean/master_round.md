---
title: Master Round
slug: master_round
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_round.htm
source: Advantage CHM
tags:
  - master
checksum: 5494ce94586568dfda0436b62c2c031c87d4c1bc
---

# Master Round

ROUND()

ROUND()

Advantage Concepts

| ROUND()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns a numeric value rounded to a specified number of digits.

| Supported in SQL: | Yes (See note below) |
| Supported in Navigational: | Yes (See note below) |

Syntax

ROUND(<nNumber>, <nDecimals>) à nRounded

Parameters

<nNumber>  The numeric value to be rounded.

<nDecimals>  Defines the number of decimal places to retain. Specifying a negative <nDecimals> value rounds whole number digits.

Return Values

ROUND() returns a numeric value.

Remarks

ROUND() is a numeric function that rounds <nNumber> to the number of places specified by <nDecimals>. Specifying a zero or negative value for <nDecimals> allows rounding of whole numbers. A negative <nDecimals> indicates the number of digits to the left of the decimal point to round. Digits between five and nine (inclusive) are rounded up. Digits below five are rounded down.

Note Even though a version of this scalar exists for both SQL and navigational usage, the use of it in an SQL statement will result in a static cursor.

See Also

[STR()](master_str.md)

[VAL()](master_val.md)
