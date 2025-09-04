---
title: Master Startswith
slug: master_startswith
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_startswith.htm
source: Advantage CHM
tags:
  - master
checksum: eb33f739b723ca42e8d5a15f742abdf67b132922
---

# Master Startswith

STARTSWITH()

STARTSWITH()

Advantage Concepts

| STARTSWITH()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that determines if one string begins with another.

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

STARTSWITH( <cStr1>, <cStr2> ) à bResult

Parameters

| <cStr1> | The string to be searched |
| <cStr2> | The string to search for at the beginning of <cStr1> |

Return Value

A boolean value

Remarks

Returns True if str1 starts with str2, and False otherwise.

See Also

[AT()](master_at.md)

[ENDSWITH()](master_endswith.md)
