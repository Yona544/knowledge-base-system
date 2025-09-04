---
title: Master Day
slug: master_day
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_day.htm
source: Advantage CHM
tags:
  - master
checksum: 0998906297678079ed58757f2f9860bb9b18b489
---

# Master Day

DAY()

DAY()

Advantage Concepts

| DAY()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the day of the month as a numeric value.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

DAY(<dDate>) à nDay

DAYOFMONTH( <dDate> ) à nDay       (SQL Only)

Parameters

<dDate>  A date or timestamp value.

Return Values

DAY() returns a number in the range of zero to 31 as an integer numeric value. If the month is February, leap years are considered. If the date argument is February 29 and the year is not a leap year, DAY() returns zero. If the date argument is empty, DAY() returns zero.

Remarks

DAY() is a date conversion function used to convert a date value to the day of a month and can be used in various date calculations.

See Also

[YEAR()](master_year.md)

[QUARTER()](master_quarter.md)

[MONTH()](master_month.md)

[WEEK()](master_week.md)

[HOUR()](master_hour.md)

[MINUTE()](master_minute.md)

[SECOND()](master_second.md)

[FRAC\_SECOND()](master_frac_second.md)

[EXTRACT()](master_extract.md)
