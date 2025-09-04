---
title: Master At
slug: master_at
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_at.htm
source: Advantage CHM
tags:
  - master
checksum: 4c1a765327e6103270850282e32003082c6db74c
---

# Master At

AT()

AT()

Advantage Concepts

| AT()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the position of a substring within a character string.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

AT(<cSearch>, <cTarget> [,<nStart>]) à nPosition

LOCATE(<cSearch>, <cTarget> [,<nStart>]) à nPosition   SQL Only

Parameters

<cSearch>  The character substring to be searched for.

<cTarget>  The character string to be searched.

<nStart>  Optional position in cTarget to start searching from.

Return Values

AT() returns the position of the first instance of <cSearch> within <cTarget> as an integer numeric value. If <cSearch> is not found, AT() returns zero.

Remarks

AT() is a character function used to determine the position of the first occurrence of a character substring within another string. To find the last instance of a substring within a string, use RAT().

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[RAT()](master_rat.md)

[SUBSTR()](master_substr.md)
