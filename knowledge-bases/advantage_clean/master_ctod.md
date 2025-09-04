---
title: Master Ctod
slug: master_ctod
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_ctod.htm
source: Advantage CHM
tags:
  - master
checksum: 7c58ce8d229dcec94cefed243d64043cda8b8437
---

# Master Ctod

CTOD()

CTOD()

Advantage Concepts

| CTOD()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that converts a date string to a date value.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

CTOD(<cDate>) à dDate

Parameters

| <cDate> | A character string consisting of numbers representing the month, day, and year separated by any character other than a number. The month, day, and year digits must be specified in accordance with the function to set the date format. |

Return Values

CTOD() returns a date value. If <cDate> is not a valid date, CTOD() returns an empty date.

Remarks

CTOD() is a character conversion function that converts a character string to a date. CTOD() is used whenever you need a literal date value. Some examples include:

- Specifying a literal date string in order to perform date arithmetic

- Comparing the result of a date expression to a literal date string

CTOD() is the inverse of DTOC() which converts a date value to a character string in the format specified by the function to set the date format. DTOS() also converts a date value to a character string in the form yyyymmdd.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[DATE()](master_date.md)

[DTOC()](master_dtoc.md)

[DTOS()](master_dtos.md)

[CTOT()](master_ctot.md)

[CTOTS()](master_ctots.md)

[STOD()](master_stod.md)

[STOTS()](master_stots.md)

[TSTOD()](master_tstod.md)

Advantage TDataSet Descendant

[TAdsSettings.DateFormat](ade_dateformat.md)

Advantage Client Engine API

[AdsSetDateFormat](ace_adssetdateformat.md)

[AdsSetEpoch](ace_adssetepoch.md)
