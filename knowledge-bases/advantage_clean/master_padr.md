---
title: Master Padr
slug: master_padr
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_padr.htm
source: Advantage CHM
tags:
  - master
checksum: 30584a9978343e60a07edd54bae6ca0575eba146
---

# Master Padr

PADR()

PADR()

Advantage Concepts

| PADR()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that pads character, date, and numeric values with a fill character.

| Supported in SQL: | No |
| Supported in Navigational: | Yes |

Syntax

PADR(<exp>, <nLength>, [<cFillChar>]) à cPaddedString

Parameters

| <exp> | A character, numeric, or date value to be padded with a fill character. |
| <nLength> | The length of the character string to be returned. |
| <cFillChar> | The character with which to pad <exp>. If not specified, the default is a space character. |

Return Values

PADR() returns the result of <exp> as a character string padded with <cFillChar> to a total length of <nLength>.

Remarks

PADR() is a character function that pads character, date, and numeric values with a fill character to create a new character string of a specified length. PADR() adds fill characters on the right side. If the length of <exp> exceeds <nLength>, all of the PAD() functions truncate cPaddedString to <nLength>.

PADR() is the inverse of the ALLTRIM(), RTRIM(), and LTRIM() functions which trim leading and trailing space from character strings.

Note Advantage Expression Engine functions can be used in expressions such as record filter expressions and index expressions. This function is not supported within SQL statements.

Note Memo, binary, and image fields are not supported in this Advantage Expression Engine function. If memo, binary, or image fields are used with this expression engine function, the Advantage Expression Engine will be unable to evaluate the expression.

See Also

[RTRIM()](master_rtrim.md)
