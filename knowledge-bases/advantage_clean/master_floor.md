---
title: Master Floor
slug: master_floor
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_floor.htm
source: Advantage CHM
tags:
  - master
checksum: fed62475e239d3f4dbba6a19f15a7f173071feed
---

# Master Floor

FLOOR()

FLOOR()

Advantage Concepts

| FLOOR()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function to compute the integer floor of a number.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

FLOOR( <nValue> ) à nInteger

Parameters

| <nValue> | Floating point value |

Return Value

The floor of <nValue>

Remarks

FLOOR returns the largest integer less than or equal to <nValue>. In SQL usage, he return value is of the same data type as the input parameter.  In navigational usage, the result is a double floating point value.

See Also

[Math Functions](master_math_functions.md)

[CEILING()](master_ceiling.md)
