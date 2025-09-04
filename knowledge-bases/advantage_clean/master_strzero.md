---
title: Master Strzero
slug: master_strzero
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_strzero.htm
source: Advantage CHM
tags:
  - master
checksum: f66378b929e7e23ce7669cfb9eecf9134b9ed7a4
---

# Master Strzero

STRZERO()

STRZERO()

Advantage Concepts

| STRZERO()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that converts a numeric expression to a string and pads it with leading zeroes instead of blanks.

| Supported in SQL: | Yes (the 3 parameter version is supported in SQL) |
| Supported in Navigational: | Yes |

Syntax

StrZero(<nNumber>,[<nLength>],[<nDecimals>]) à cString

Parameters

| <nNumber> | The numeric expression to convert to a string. |
| <nLength> | The length of the string to return, including zeroes, decimal digits, decimal point, and sign. |
| <nDecimals> | The number of decimal places in the return value. |

Return Values

A string.

Remarks

STRZERO() is useful in displaying numbers, creating codes such as part numbers from numeric values, and creating order keys that combine numeric and character data. STRZERO() is similar to the STR() function except that the padding character is zero instead of a blank. For more information, see the [STR()](master_str.md) function.

Example

This example uses StrZero() to convert a 3-digit number to a 5-character string:

? StrZero(987, 5, 0)    // "00987"

See Also

[PAD()](master_pad.md)

[STR()](master_str.md)

[VAL()](master_val.md)
