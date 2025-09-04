---
title: Master Ceiling
slug: master_ceiling
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_ceiling.htm
source: Advantage CHM
tags:
  - master
checksum: a8d7422276e9edb8fc42e71b940b719de4909942
---

# Master Ceiling

CEILING()

CEILING()

Advantage Concepts

| CEILING()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function to compute the integer ceiling of a number.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

CEILING( <nValue> ) à nInteger

Parameters

| <nValue> | Floating point value |

Return Value

The ceiling of <nValue>

Remarks

CEILING returns the smallest integer greater than or equal to <nValue>. In SQL usage, he return value is of the same data type as the input parameter.  In navigational usage, the result is a double floating point value.

See Also

[Math Functions](master_math_functions.md)

[FLOOR()](master_floor.md)
