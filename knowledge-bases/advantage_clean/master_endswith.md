---
title: Master Endswith
slug: master_endswith
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_endswith.htm
source: Advantage CHM
tags:
  - master
checksum: 3c01751caf732c8f52918703f7d5c8cc46e77f0c
---

# Master Endswith

ENDSWITH()

ENDSWITH()

Advantage Concepts

| ENDSWITH()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that determines if one string ends with another.

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

ENDSWITH( <cStr1>, <cStr2> ) à bResult

Parameters

| <cStr1> | The string to be searched |
| <cStr2> | The string to search for at the end of <cStr1> |

Return Value

A boolean value

Remarks

Returns True if str1 ends with str2, and False otherwise.

See Also

[RAT()](master_rat.md)

[STARTSWITH()](master_startswith.md)
