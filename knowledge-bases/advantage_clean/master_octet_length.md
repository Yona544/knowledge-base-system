---
title: Master Octet Length
slug: master_octet_length
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_octet_length.htm
source: Advantage CHM
tags:
  - master
checksum: 506fc59596992da9b2df8d62544c7fdaf7102b0a
---

# Master Octet Length

OCTET\_LENGTH()

OCTET\_LENGTH()

Advantage Concepts

| OCTET\_LENGTH()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the length of a string in octets (i.e., bytes).

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

OCTET\_LENGTH( <cStr> ) à nOctets

Parameters

| <cStr> | An ANSI or Unicode string |

Return Value

The number of bytes of the given string

Remarks

This value is useful for finding the number of bytes needed to store a Unicode string.

See Also

[CHAR\_LENGTH()](master_char_length.md)

[LEN()](master_len.md)
