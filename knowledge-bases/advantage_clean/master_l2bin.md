---
title: Master L2Bin
slug: master_l2bin
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_l2bin.htm
source: Advantage CHM
tags:
  - master
checksum: 7245b76b92397aa83a1b8939caeb5b53ec78946d
---

# Master L2Bin

L2BIN()

L2BIN()

Advantage Concepts

| L2BIN()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that converts a long integer numeric value to a character string formatted as a 32-bit binary integer.

| Supported in SQL: | No |
| Supported in Navigational: | Yes |

Syntax

L2BIN( <nLongInteger> ) --> cBinaryInteger

Parameters

| <nLongInteger> | A long integer numeric value to be converted. Decimal digits are truncated. |

Return Values

L2BIN() returns a four-byte character string containing a 32-bit binary integer.

Remarks

L2BIN() is a low-level file function that converts a long integer numeric value to a character string formatted as a 32-bit binary integerleast significant byte first.

See Also

[I2BIN()](master_i2bin.md)

[CHR()](master_chr.md)
