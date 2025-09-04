---
title: Master Right
slug: master_right
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_right.htm
source: Advantage CHM
tags:
  - master
checksum: 68cc8ee4b58d6aaf487bf79dbade1e639abf35b8
---

# Master Right

RIGHT()

RIGHT()

Advantage Concepts

| RIGHT()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns a substring beginning with the rightmost character.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

RIGHT(<cString>, <nCount>) à cSubString

Parameters

<cString>  The character string from which to extract characters.

<nCount>  The number of characters to extract.

Return Values

RIGHT() returns the rightmost <nCount> characters of <cString>. If <nCount> is zero, RIGHT() returns a null string (""). If <nCount> is negative or larger than the length of the character string, RIGHT() returns <cString>. The maximum string size is 65,535 (64K) bytes.

Remarks

RIGHT() is a character function that extracts a substring beginning with the rightmost character in <cString>. It is the same as the character expression, SUBSTR(<cString>, <nCount>). For example, RIGHT("ABC", 1) is the same as SUBSTR("ABC", -1). RIGHT() is related to LEFT(), which extracts a substring beginning with the leftmost character in <cString>.

The RIGHT(), LEFT(), and SUBSTR() functions are often used with both the AT() and RAT() functions to locate either the first and/or the last position of a substring before extracting it.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[RTRIM()](master_rtrim.md)

[SUBSTR()](master_substr.md)
