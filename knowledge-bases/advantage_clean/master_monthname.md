---
title: Master Monthname
slug: master_monthname
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_monthname.htm
source: Advantage CHM
tags:
  - master
checksum: 0c47ec3fad1f8d837291ca9a7d7d79890a918746
---

# Master Monthname

MONTHNAME()

MONTHNAME()

Advantage Concepts

| MONTHNAME()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the month name of a date value.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

MONTHNAME(<dDate>) à cMonthName

Parameters

<dDate>  The date value to be converted.

Return Values

MONTHNAME() returns the string name for the month of the date value.  If the date value is empty, MONTHNAME() returns an empty string.

Remarks

MONTHNAME() is a date conversion function used to return the month name of a date value.

See Also

[DAYNAME()](master_dayname.md)

[MONTH()](master_month.md)
