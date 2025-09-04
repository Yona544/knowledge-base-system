---
title: Master Second
slug: master_second
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_second.htm
source: Advantage CHM
tags:
  - master
checksum: 4c237e4d302508ecbe17a819680f83580172bc6c
---

# Master Second

SECOND()

SECOND()

Advantage Concepts

| SECOND()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the second portion of a time or timestamp value.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

SECOND( <tTime> ) à nSecond

Parameters

<tTime>  A time or timestamp value

Return Values

SECOND() returns a number in the range of 0 to 59 as an integer numeric value.  If the time or timestamp argument is empty, SECOND() returns zero.

Remarks

SECOND() is a time conversion function used to return the second portion of a time or timestamp value.

See Also

[YEAR()](master_year.md)

[QUARTER()](master_quarter.md)

[MONTH()](master_month.md)

[WEEK()](master_week.md)

[DAY()](master_day.md)

[HOUR()](master_hour.md)

[MINUTE()](master_minute.md)

[FRAC\_SECOND()](master_frac_second.md)

[EXTRACT()](master_extract.md)
