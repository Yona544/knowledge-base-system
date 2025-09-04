---
title: Master Rtrim
slug: master_rtrim
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_rtrim.htm
source: Advantage CHM
tags:
  - master
checksum: cc723d7cd6f8eb90cabf1aff9fb61ced76c30509
---

# Master Rtrim

RTRIM()

RTRIM()

Advantage Concepts

| RTRIM()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that removes trailing spaces from a character string.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

RTRIM(<cString>) à cTrimString

Parameters

<cString>  The character string to be copied without trailing spaces.

Return Value

RTRIM() returns a copy of <cString> with the trailing spaces removed. If <cString> is a null string ("") or all spaces, RTRIM() returns a null string ("").

Remarks

RTRIM() is a character function that formats character strings. It is useful for deleting trailing spaces while concatenating strings. This is typically the case with database fields that are stored in fixed-width format. For example, use RTRIM() to concatenate first and last name fields to form a name string.

RTRIM() is related to LTRIM(), which removes leading spaces, and ALLTRIM(), which removes both leading and trailing spaces. The inverse of ALLTRIM(), LTRIM(), and RTRIM() are the PADC(), PADR(), and PADL() functions which center, right-justify, or left-justify character strings by padding them with fill characters.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[PAD()](master_pad.md)

[SUBSTR()](master_substr.md)

[TRIM()](master_trim.md)

[ALLTRIM()](master_alltrim.md)

[LTRIM()](master_ltrim.md)
