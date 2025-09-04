---
title: Master Quarter
slug: master_quarter
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_quarter.htm
source: Advantage CHM
tags:
  - master
checksum: 3a96643c824791c9149a62b90e812b219b0b44e3
---

# Master Quarter

QUARTER()

QUARTER()

Advantage Concepts

| QUARTER()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the quarter of a date value.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

QUARTER(<dDate>) à nQuarter

Parameters

<dDate>  A date or timestamp value

Return Values

QUARTER() returns a number in the range of 1 to 4 as an integer numeric value. If the date argument is empty, QUARTER() returns zero.

Remarks

QUARTER() is a date conversion function used to convert a date value to the quarter number.

See Also

[YEAR()](master_year.md)

[MONTH()](master_month.md)

[WEEK()](master_week.md)

[DAY()](master_day.md)

[HOUR()](master_hour.md)

[MINUTE()](master_minute.md)

[SECOND()](master_second.md)

[FRAC\_SECOND()](master_frac_second.md)

[EXTRACT()](master_extract.md)
