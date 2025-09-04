---
title: Master Ltrim
slug: master_ltrim
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_ltrim.htm
source: Advantage CHM
tags:
  - master
checksum: 0556e38c09acda47ecf9010712710833e4039540
---

# Master Ltrim

LTRIM()

LTRIM()

Advantage Concepts

| LTRIM()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that removes leading spaces from a character string.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

LTRIM(<cString>) à cTrimString

Parameters

<cString> The character string to copy without leading spaces.

Return Values

LTRIM() returns a copy of <cString> with the leading spaces removed. If <cString> is a null string ("") or all spaces, LTRIM() returns a null ("").

Remarks

LTRIM() is a character function that formats character strings with leading spaces. These can be, for example, numbers converted to character strings using STR().

LTRIM() is related to RTRIM(), which removes trailing spaces, and ALLTRIM(), which removes both leading and trailing spaces. The inverse of ALLTRIM(), LTRIM(), and RTRIM() are the PADC(), PADR(), and PADL() functions which center, right-justify, or left-justify character strings by padding them with fill characters.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[ALLTRIM()](master_alltrim.md)

[PAD()](master_pad.md)

[RTRIM()](master_rtrim.md)

[STR()](master_str.md)

[SUBSTR()](master_substr.md)

[TRIM()](master_trim.md)
