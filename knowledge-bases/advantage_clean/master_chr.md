---
title: Master Chr
slug: master_chr
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_chr.htm
source: Advantage CHM
tags:
  - master
checksum: 8d84d082b4b43c041782c423255d834673d6117b
---

# Master Chr

CHR()

CHR()

Advantage Concepts

| CHR()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that converts an ASCII code to a character value.

| Supported in SQL: | No (use [CHAR](master_char.md)) |
| Supported in Navigational: | Yes |

Syntax

CHR(<nCode>) à cChar

Parameters

<nCode>  An ASCII code in the range of zero to 255.

Return Values

CHR() returns a single character value whose ASCII code is specified by <nCode>.

Remarks

CHR() is a numeric conversion function that converts an ASCII code to a character. It is the inverse of [ASCII()](master_ascii.md).

Note CHR(0) has a length of one (1) and is treated like any other character.

See Also

[ASCII](master_ascii.md)
