---
title: Master Left
slug: master_left
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_left.htm
source: Advantage CHM
tags:
  - master
checksum: 0954f48434fa648257d3a905f22e0545150ce90d
---

# Master Left

LEFT()

LEFT()

Advantage Concepts

| LEFT()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that extracts a substring beginning with the first character in a string.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

LEFT(<cString>, <nCount>) à cSubString

Parameters

| <cString> | A character string from which to extract characters. The maximum size of <cString> is 65,535 (64K) bytes. |
| <nCount> | The number of characters to extract. |

Return Values

LEFT() returns the leftmost <nCount> characters of <cString> as a character string. If <nCount> is negative or zero, LEFT() returns a null string (""). If <nCount> is larger than the length of the character string, LEFT() returns the entire string.

Remarks

LEFT() is a character function that returns a substring of a specified character string. It is the same as SUBSTR(<cString>, 1, <nCount>). LEFT() is also like RIGHT(), which returns a substring beginning with the last character in a string.

LEFT(), RIGHT(), and SUBSTR() are often used with both the AT() and RAT() functions to locate the first and/or the last position of a substring before extracting it.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[AT()](master_at.md)

[LTRIM()](master_ltrim.md)

[RAT()](master_rat.md)

[RTRIM()](master_rtrim.md)

[SUBSTR()](master_substr.md)

[RIGHT()](master_right.md)
