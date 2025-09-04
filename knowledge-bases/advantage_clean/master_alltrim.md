---
title: Master Alltrim
slug: master_alltrim
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_alltrim.htm
source: Advantage CHM
tags:
  - master
checksum: 979c13436eb988ad358cedfa1e003d8148ba1d11
---

# Master Alltrim

ALLTRIM()

ALLTRIM()

Advantage Concepts

| ALLTRIM()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that removes leading and trailing spaces from a character string.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

ALLTRIM(<cString>) à cTrimString

Parameters

<cString>  The character expression to be trimmed.

Return Values

Returns a character string with leading and trailing spaces removed.

Remarks

ALLTRIM() is a character function that removes both leading and trailing spaces from a string. It is related to LTRIM() and RTRIM() which remove leading and trailing spaces, respectively. The inverse of ALLTRIM(), LTRIM(), and RTRIM() are the PADC(), PADL(), and PADR() functions which center, left-justify, or right-justify character strings by padding them with fill characters.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[LTRIM()](master_ltrim.md)

[PAD()](master_pad.md)

[RTRIM()](master_rtrim.md)

[TRIM()](master_trim.md)
