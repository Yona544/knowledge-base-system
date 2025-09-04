---
title: Master Length
slug: master_length
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_length.htm
source: Advantage CHM
tags:
  - master
checksum: 4a756df6c857765283733695e60323e68343535d
---

# Master Length

LENGTH()

LENGTH()

Advantage Concepts

| LENGTH()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the length of a character string excluding trailing spaces.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

LENGTH(<cString>) à nCount

Parameters

| <cString> | The character string to count. |

Return Values

LENGTH() returns the length of a character string as an integer numeric value.

Remarks

LENGTH() returns the length of a character string excluding trailing spaces.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[LTRIM()](master_ltrim.md)

[RTRIM()](master_rtrim.md)

[LEN()](master_len.md)
