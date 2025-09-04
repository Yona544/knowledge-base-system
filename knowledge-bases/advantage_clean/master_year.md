---
title: Master Year
slug: master_year
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_year.htm
source: Advantage CHM
tags:
  - master
checksum: dec0b48a57efa12deec9dbb6d26aa8fbc93c87f0
---

# Master Year

YEAR()

YEAR()

Advantage Concepts

| YEAR()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that converts a date value to the year as a numeric value.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

YEAR(<dDate>) à nYear

Parameters

<dDate> The date or timestamp value

Return Values

YEAR() returns the year of the specified date value including the century digits as a four-digit numeric value. The value returned is not affected by the current date format. Specifying a null date from a DBF table (CTOD("")) returns zero. Specifying a null date from an ADT table returns NULL.

Remarks

YEAR() is a date conversion function that converts a date value to a numeric year value. Use it in calculations for documents such as periodic reports.

YEAR() is a member of a group of functions that return components of a date value as numeric values. The group includes DAY() and MONTH() which return the day and month values as numeric values.

See Also

[QUARTER()](master_quarter.md)

[MONTH()](master_month.md)

[WEEK()](master_week.md)

[DAY()](master_day.md)

[HOUR()](master_hour.md)

[MINUTE()](master_minute.md)

[SECOND()](master_second.md)

[FRAC\_SECOND()](master_frac_second.md)

[EXTRACT()](master_extract.md)
