---
title: Master Minute
slug: master_minute
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_minute.htm
source: Advantage CHM
tags:
  - master
checksum: fbaab539c7611b7df7d7441dd4c9d009c15518d6
---

# Master Minute

MINUTE()

MINUTE()

Advantage Concepts

| MINUTE()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the minute portion of a time or timestamp value.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

MINUTE( <tTime> ) à nMinute

Parameters

<tTime>  A time or timestamp value

Return Values

MINUTE() returns a number in the range of 0 to 59 as an integer numeric value.  If the time or timestamp argument is empty, MINUTE() returns zero.

Remarks

MINUTE() is a time conversion function used to return the minute portion of a time or timestamp value.

See Also

[YEAR()](master_year.md)

[QUARTER()](master_quarter.md)

[MONTH()](master_month.md)

[WEEK()](master_week.md)

[DAY()](master_day.md)

[HOUR()](master_hour.md)

[SECOND()](master_second.md)

[FRAC\_SECOND()](master_frac_second.md)

[EXTRACT()](master_extract.md)
