---
title: Master Dayname
slug: master_dayname
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_dayname.htm
source: Advantage CHM
tags:
  - master
checksum: a942a81fe23dd6acdbbeeda0e5d6ea3eadf31a84
---

# Master Dayname

DAYNAME()

DAYNAME()

Advantage Concepts

| DAYNAME()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the day name of a date value.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

DAYNAME(<dDate>) à cDayName

Parameters

<dDate>  A date value to convert.

Return Values

DAYNAME() returns the string name for the day of week of the date value. If the date argument is empty, DAYNAME() returns an empty string.

Remarks

DAYNAME() is a date conversion function used to return the day of week name of the date value.

See Also

[MONTHNAME()](master_monthname.md)

[DAY()](master_day.md)
