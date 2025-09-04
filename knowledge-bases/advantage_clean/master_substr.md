---
title: Master Substr
slug: master_substr
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_substr.htm
source: Advantage CHM
tags:
  - master
checksum: f2c9b246dbf5178fc575a539df1aa991277db894
---

# Master Substr

SUBSTR()

SUBSTR()

Advantage Concepts

| SUBSTR()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that extracts a substring from a character string.

| Supported in SQL: | No.  See [SUBSTRING()](master_substring.md) |
| Supported in Navigational: | Yes |

Syntax

SUBSTR(<cString>, <nStart>, [<nCount>]) à cSubstring

Parameters

| <cString> | The character string from which to extract a substring. It can be up to 65,535 (64K) bytes, the maximum character string size. |
| <nStart> | The starting position in <cString>. If <nStart> is positive, it is relative to the leftmost character in <cString>. If <nStart> is negative, it is relative to the rightmost character in the <cString>. |
| <nCount> | The number of characters to be extracted. If omitted, the substring begins at <nStart> and continues to the end of the string. If <nCount> is greater than the number of characters from <nStart> to the end of <cString>, the excess numbers are ignored. |

Return Values

SUBSTR() returns a character string.

Remarks

SUBSTR() is a character function that extracts a substring from another character string. SUBSTR() is related to the LEFT() and RIGHT() functions which extract substrings beginning with leftmost and rightmost characters in <cString>, respectively.

The SUBSTR(), RIGHT(), and LEFT() functions are often used with both the AT() and RAT() functions to locate either the first and/or the last position of a substring before extracting it. They are also used to display or print only a portion of a character string.

Note Memo, binary, and image fields are not supported in this Advantage Expression Engine function. If memo, binary, or image fields are used with this expression engine function, the Advantage Expression Engine will be unable to evaluate the expression.

See Also

[RAT()](master_rat.md)

[LEFT()](master_left.md)

[RIGHT()](master_right.md)

[STR()](master_str.md)
