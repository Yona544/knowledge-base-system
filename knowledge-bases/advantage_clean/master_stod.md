---
title: Master Stod
slug: master_stod
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_stod.htm
source: Advantage CHM
tags:
  - master
checksum: d5bfa79dc2c09451d372b7400bd6e8c786e9b0cc
---

# Master Stod

STOD()

STOD()

Advantage Concepts

| STOD()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that converts a character string formatted as YYYYMMDD to a date value.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

STOD(<cDate>) -> dDate

Parameters

| <cDate> | A character string consisting of numbers representing the year, month, and day in the format YYYYMMDD. |

Return Values

STOD() returns a date value. If <cDate> is not a valid date, STOD() returns an empty date.

Remarks

STOD() is a character conversion function that converts a character string to a date. STOD() can be used whenever you need a literal date value. Some examples include:

- Specifying a literal date string in order to perform date arithmetic

- Comparing the result of a date expression to a literal date string

STOD() is the inverse of DTOS() which converts a date value to a character string in the format YYYYMMDD.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[DATE()](master_date.md)

[DTOC()](master_dtoc.md)

[DTOS()](master_dtos.md)

[CTOD()](master_ctod.md)

[CTOT()](master_ctot.md)

[CTOTS()](master_ctots.md)

[TSTOD()](master_tstod.md)
