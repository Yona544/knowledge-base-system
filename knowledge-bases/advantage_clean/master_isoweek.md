---
title: Master Isoweek
slug: master_isoweek
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_isoweek.htm
source: Advantage CHM
tags:
  - master
checksum: 04e7b6ef2c8147391559d5b8b6176b7bafdd4a7f
---

# Master Isoweek

ISOWEEK()

ISOWEEK()

Advantage Concepts

| ISOWEEK()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the ISO 8601 week number of a date value.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

ISOWEEK(<dDate>) à nISOWeek

Parameters

<dDate>  The date value to be converted.

Return Values

ISOWEEK() returns a number in the range of 1 to 53 as an integer numeric value.  If the date value is empty, ISOWEEK() returns zero.

Remarks

ISOWEEK() is a date conversion function used to return the ISO 8601 week number of a date value.

See Also

[DAY()](master_day.md)

[MONTH()](master_month.md)

[QUARTER()](master_quarter.md)

[WEEK()](master_week.md)

[YEAR()](master_year.md)
