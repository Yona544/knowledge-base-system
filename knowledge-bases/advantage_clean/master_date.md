---
title: Master Date
slug: master_date
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_date.htm
source: Advantage CHM
tags:
  - master
checksum: c75971e8d561700996155acf6e36992f9b98627f
---

# Master Date

DATE()

DATE(), CURDATE()

Advantage Concepts

| DATE(), CURDATE()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the system date as a date value.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

DATE() à dSystem

CURDATE() à dSystem           (SQL Only)

CURRENT\_DATE() à dSystem       (SQL Only)

 

Return Values

DATE() returns the system date as a date value.

Remarks

DATE() is a date function that provides a means of initializing memory variables to the current date, comparing other date values to the current date, and performing date arithmetic relative to the current date.

The display format for dates is controlled by the function to set the date format. The default format is mm/dd/yy in navigational usage.  In SQL usage, the standard format is yyyy-mm-dd.

See Also

[CTOD()](master_ctod.md)

[DTOC()](master_dtoc.md)

[DTOS()](master_dtos.md)

[NOW()](master_now.md)

[STOD()](master_stod.md)

[STOTS()](master_stots.md)

[TSTOD()](master_tstod.md)

Advantage TDataSet Descendant

[TAdsSettings.DateFormat](ade_dateformat.md)

Advantage Client Engine API

[AdsSetDateFormat](ace_adssetdateformat.md)
