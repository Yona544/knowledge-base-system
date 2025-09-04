---
title: Master Dtoc
slug: master_dtoc
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_dtoc.htm
source: Advantage CHM
tags:
  - master
checksum: ee43e48945f8384c27028e97e84f9461191b589a
---

# Master Dtoc

DTOC()

DTOC()

Advantage Concepts

| DTOC()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that converts a date value to a character string.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

DTOC(<dDate>, [<nFormat>]) à cDate

Parameters

<dDate>  The date value to convert.

<nFormat> When this optional value is 1 the date format used is yyyymmdd.

Return Values

DTOC() returns a character string representation of a date value. The return value is formatted in the current date format. The default format is mm/dd/yyyy.A null date from a DBF table returns a string of spaces equal in length to the current date format. The function returns NULL if the parameter is a null date in an ADT table.

Remarks

If you are indexing a date in combination with a character string, use DTOS() instead of DTOC() to convert the date value to a character string.

See Also

[CTOD()](master_ctod.md)

[DATE()](master_date.md)

[DTOS()](master_dtos.md)

[STOD()](master_stod.md)

[TTOC()](master_ttoc.md)

[STOTS()](master_stots.md)

Advantage TDataSet Descendant

[TAdsSettings.DateFormat](ade_dateformat.md)

Advantage Client Engine API

[AdsSetDateFormat](ace_adssetdateformat.md)
