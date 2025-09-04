---
title: Master Reverse
slug: master_reverse
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_reverse.htm
source: Advantage CHM
tags:
  - master
checksum: 336a3db58bd792f176bb1b56cf7dfe3b60f0130c
---

# Master Reverse

REVERSE()

REVERSE()

Advantage Concepts

| REVERSE()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that reverses the order of characters in a string.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

REVERSE(<cString>) -> cReverseString

Parameters

<cString>  A character string to be converted to reverse order.

Returns Values

REVERSE() returns a copy of <cString> with all characters in the string put in reverse order.

Remarks

REVERSE() is a character function that reverses all characters in a string. For example, REVERSE( "abcdef" ) would return the string "fedcba".

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[RAT()](master_rat.md)
