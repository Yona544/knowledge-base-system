---
title: Master Len
slug: master_len
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_len.htm
source: Advantage CHM
tags:
  - master
checksum: 410f98965b97e426116ed2ca9d6735a01c2b7ce6
---

# Master Len

LEN()

LEN()

Advantage Concepts

| LEN()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the length of a character string including trailing spaces.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

LEN(<cString>) à nCount

Parameters

| <cString> | The character string to count. |

Return Values

LEN() returns the length of a character string as an integer numeric value.

Remarks

LEN() returns the length of a character string including trailing spaces.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[LTRIM()](master_ltrim.md)

[RTRIM()](master_rtrim.md)

[LENGTH()](master_length.md)
