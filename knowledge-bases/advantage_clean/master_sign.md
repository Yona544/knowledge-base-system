---
title: Master Sign
slug: master_sign
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sign.htm
source: Advantage CHM
tags:
  - master
checksum: d66bfbc785ca04ac03cb2f57be68556ac3f095fb
---

# Master Sign

SIGN()

SIGN()

Advantage Concepts

| SIGN()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns an indicator of the sign of the parameter.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

SIGN( <nValue> ) à nSign

Parameters

| <nValue> | Value to test |

Return Value

-1, 0, or 1

Remarks

If <nValue> is less than zero, -1 is returned. If <nValue> equals zero, 0 is returned. If <nValue> is greater than zero, 1 is returned.

See Also

[Math Functions](master_math_functions.md)
