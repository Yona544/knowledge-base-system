---
title: Master Dayofweek
slug: master_dayofweek
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_dayofweek.htm
source: Advantage CHM
tags:
  - master
checksum: 32724de5414f4fb57bcf6cf18555c930741f6a33
---

# Master Dayofweek

DAYOFWEEK()

DAYOFWEEK()

Advantage Concepts

| DAYOFWEEK()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the numeric day of a date value.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

DAYOFWEEK(<dDate>) à nDay

Parameters

<dDate>  A date value to convert.

Return Values

DAYOFWEEK() returns a number in the range of 1 to 7 as an integer numeric value.  If the date argument is empty, DAYOFWEEK() returns zero.

Remarks

DAYOFWEEK() is a date conversion function used to convert a date value to the numeric day of week value and can be used in various date calculations.

See Also

[DAYOFYEAR()](master_dayofyear.md)

[YEAR()](master_year.md)

[MONTH()](master_month.md)

[DAY()](master_day.md)

[WEEK()](master_week.md)

[QUARTER()](master_quarter.md)
