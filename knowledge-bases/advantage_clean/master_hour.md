---
title: Master Hour
slug: master_hour
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_hour.htm
source: Advantage CHM
tags:
  - master
checksum: 452ebb3127da2ded23433cb0f5b598e1ca62be94
---

# Master Hour

HOUR()

HOUR()

Advantage Concepts

| HOUR()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the hour portion of a time or timestamp value.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

HOUR( <tTime> ) à nHour

Parameters

<tTime>  A time or timestamp value

Return Values

HOUR() returns a number in the range of 0 to 23 as an integer numeric value.  If the time or timestamp argument is empty, HOUR() returns zero.

Remarks

HOUR() is a time conversion function used to return the hour portion of a time or timestamp value.

See Also

[YEAR()](master_year.md)

[QUARTER()](master_quarter.md)

[MONTH()](master_month.md)

[WEEK()](master_week.md)

[DAY()](master_day.md)

[MINUTE()](master_minute.md)

[SECOND()](master_second.md)

[FRAC\_SECOND()](master_frac_second.md)

[EXTRACT()](master_extract.md)
