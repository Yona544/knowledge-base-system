---
title: Master Ascii
slug: master_ascii
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_ascii.htm
source: Advantage CHM
tags:
  - master
checksum: 97107ade15c250c4a1fcbd811990768c52bfaf50
---

# Master Ascii

ASCII()

ASCII()

Advantage Concepts

| ASCII()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the ASCII code of a character value.

| Supported in SQL: | Yes |
| Supported in Navigational: | No (use [CHR](master_chr.md)) |

Syntax

ASCII(<str>) à nCode

Parameters

<str>  A character string.

Return Values

ASCII() returns the ASCII code of the first character of the given string.

Remarks

ASCII() is a conversion function that converts a character to its ASCII code. It is the inverse of [CHAR()](master_char.md).

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[CHAR](master_char.md)
