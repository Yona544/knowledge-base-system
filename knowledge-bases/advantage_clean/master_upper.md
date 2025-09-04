---
title: Master Upper
slug: master_upper
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_upper.htm
source: Advantage CHM
tags:
  - master
checksum: 33d465532b96bbdca02ebffcda2b6ae1ca58c69c
---

# Master Upper

UPPER()

UPPER()

Advantage Concepts

| UPPER()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that converts lowercase characters to uppercase.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

UPPER(<cString>) à cUpperString

UCASE(<cString>) à cLowerString     SQL Only

Parameters

<cString>  The character string to be converted.

Return Values

UPPER() returns a copy of <cString> with all alphabetical characters converted to uppercase. All other characters remain the same as in the original string.

Remarks

UPPER() is a character function that converts lowercase and mixed case strings to uppercase. It is related to LOWER() which converts uppercase and mixed case strings to lowercase.

UPPER() can be used to normalize strings for case-independent comparison or indexing purposes.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[LOWER()](master_lower.md)
