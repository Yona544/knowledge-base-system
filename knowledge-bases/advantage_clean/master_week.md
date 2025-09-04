---
title: Master Week
slug: master_week
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_week.htm
source: Advantage CHM
tags:
  - master
checksum: 8b32929fd4391355af01efd036322eca2ff51382
---

# Master Week

WEEK()

WEEK()

Advantage Concepts

| WEEK()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the week number of a date value.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

WEEK(<dDate>) à nWeek

Parameters

<dDate>  A date or timestamp value

Return Values

WEEK() returns a number in the range of 1 to 53 as an integer numeric value.  If the date argument is empty, WEEK() returns zero.

Remarks

WEEK() is a date conversion function used to convert a date value to the week number and can be used in various date calculations.

See Also

[ISOWEEK()](master_isoweek.md)

[YEAR()](master_year.md)

[QUARTER()](master_quarter.md)

[MONTH()](master_month.md)

[DAY()](master_day.md)

[HOUR()](master_hour.md)

[MINUTE()](master_minute.md)

[SECOND()](master_second.md)

[FRAC\_SECOND()](master_frac_second.md)

[EXTRACT()](master_extract.md)
