---
title: Master Month
slug: master_month
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_month.htm
source: Advantage CHM
tags:
  - master
checksum: 0704586a2aeac9182bc1428ce8b24fb651f44e80
---

# Master Month

MONTH()

MONTH()

Advantage Concepts

| MONTH()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that converts a date value to the number of the month.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

MONTH(<dDate>) à nMonth

Parameters

<dDate>  The date or timestamp value

Return Values

MONTH() returns an integer numeric value in the range of zero to 12. Specifying a null date from a DBF table (CTOD("")) returns zero. Specifying a null date from an ADT table returns NULL.

Remarks

MONTH() is a date conversion function that is useful when you require a numeric month value during calculations for such things as periodic reports. MONTH() is a member of a group of functions that return components of a date value as numeric values. The group includes DAY() and YEAR() to return the day and year values as numerics.

See Also

[YEAR()](master_year.md)

[QUARTER()](master_quarter.md)

[WEEK()](master_week.md)

[DAY()](master_day.md)

[HOUR()](master_hour.md)

[MINUTE()](master_minute.md)

[SECOND()](master_second.md)

[FRAC\_SECOND()](master_frac_second.md)

[EXTRACT()](master_extract.md)
