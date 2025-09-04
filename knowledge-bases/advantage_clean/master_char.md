---
title: Master Char
slug: master_char
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_char.htm
source: Advantage CHM
tags:
  - master
checksum: 7509d5ddf9554e0912b7001aa0333430a42950d7
---

# Master Char

CHAR()

CHAR()

Advantage Concepts

| CHAR()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that converts an ASCII code to a character value.

| Supported in SQL: | Yes |
| Supported in Navigational: | No (use [CHR](master_chr.md)) |

Syntax

CHAR(<nCode>) à cChar

Parameters

<nCode>  An ASCII code in the range of zero to 255.

Return Values

CHAR() returns a single character value whose ASCII code is specified by <nCode>.

Remarks

CHAR() is a numeric conversion function that converts an ASCII code to a character. It is the inverse of ASCII().

See Also

[ASCII](master_ascii.md)
