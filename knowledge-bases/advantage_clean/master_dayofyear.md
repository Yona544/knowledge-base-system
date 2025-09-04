---
title: Master Dayofyear
slug: master_dayofyear
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_dayofyear.htm
source: Advantage CHM
tags:
  - master
checksum: 3af827bb3d081477623f54c110652a9429eb4c9f
---

# Master Dayofyear

DAYOFYEAR()

DAYOFYEAR()

Advantage Concepts

| DAYOFYEAR()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the day of the year of a date value.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

DAYOFYEAR(<dDate>) à nDay

Parameters

<dDate>  A date value to convert.

Return Values

DAYOFYEAR() returns a number in the range of 1 to 366 as an integer numeric value.  If the date argument is empty, DAYOFYEAR() returns zero.

Remarks

DAYOFYEAR() is a date conversion function used to convert a date value to the day of year.

See Also

[DAYOFWEEK()](master_dayofweek.md)

[DAY()](master_day.md)

[MONTH()](master_month.md)

[QUARTER()](master_quarter.md)

[YEAR()](master_year.md)
