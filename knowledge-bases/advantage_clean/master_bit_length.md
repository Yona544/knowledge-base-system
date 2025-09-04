---
title: Master Bit Length
slug: master_bit_length
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_bit_length.htm
source: Advantage CHM
tags:
  - master
checksum: e25f5cde51e6170e9c966c85ae96e628c9433283
---

# Master Bit Length

BIT\_LENGTH()

BIT\_LENGTH()

Advantage Concepts

| BIT\_LENGTH()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the length of a character string in bits.

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

BIT\_LENGTH(<cString>) à nCount

Parameters

| <cString> | The character string to count. |

Return Value

The length of a character string in bits assuming 8 bits in a byte.

Remarks

The length includes trailing spaces. For Unicode fields, the length is the number of octets composing the string multiplied by 8.

Note Binary and image fields are not supported by this function.

See Also

[LEN()](master_len.md)
