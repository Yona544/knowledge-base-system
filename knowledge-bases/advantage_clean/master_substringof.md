---
title: Master Substringof
slug: master_substringof
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_substringof.htm
source: Advantage CHM
tags:
  - master
checksum: 617034b742f23f3bb9eeafdf3edbb987ec9db582
---

# Master Substringof

SUBSTRINGOF()

SUBSTRINGOF()

Advantage Concepts

| SUBSTRINGOF()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that searches a string for a substring.

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

SUBSTRINGOF( <cSearch>, <cTarget> ) à SyntaxRetPH

Parameters

| <cSearch> | The string to search for |
| <cTarget> | The string to be searched |

Return Value

A boolean value indicating if the substring was found

Remarks

Returns True if str1 is a substring str2, and False otherwise.

See Also

[AT()](master_at.md)

[POSITION()](master_position.md)
