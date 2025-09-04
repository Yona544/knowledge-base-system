---
title: Master I2Bin
slug: master_i2bin
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_i2bin.htm
source: Advantage CHM
tags:
  - master
checksum: 021a95a9e92abc64ff8051fbebc4538732c125e0
---

# Master I2Bin

I2BIN()

I2BIN()

Advantage Concepts

| I2BIN()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that converts an integer numeric value to a character string formatted as a binary integer.

| Supported in SQL: | No |
| Supported in Navigational: | Yes |

Syntax

I2BIN( <nInteger> ) à cBinaryInteger

Parameters

| <nInteger> | An integer numeric value to be converted. Decimal digits are truncated. |

Return Values

I2BIN() returns a two-byte character string containing a 16-bit binary integer.

Remarks

I2BIN() is a low-level file function that converts an integer numeric value to a character string formatted as a binary integerleast significant byte first.

See Also

[CHR()](master_chr.md)

[L2BIN()](master_l2bin.md)
