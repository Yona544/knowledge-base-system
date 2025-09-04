---
title: Master Truncate
slug: master_truncate
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_truncate.htm
source: Advantage CHM
tags:
  - master
checksum: 910abaccdfce0b8884f38f3e103a664c26a44f57
---

# Master Truncate

TRUNCATE()

TRUNCATE()

Advantage Concepts

| TRUNCATE()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that truncates a floating point value.

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

TRUNCATE( <nValue>, <iDecimals> ) à nResult

Parameters

| <nValue> | The floating point or numeric value to truncate |
| <iDecimals> | The desired number of decimal places. |

Return Value

<nValue> truncated as specified

Remarks

This function truncates <iDecimals> places to the right of the decimal point. If <iDecimals> is negative, <nValue> is truncated to ABS(<nDecimals>) places to the left of the decimal point.

See Also

[Math Functions](master_math_functions.md)
