---
title: Master Tstod
slug: master_tstod
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_tstod.htm
source: Advantage CHM
tags:
  - master
checksum: 2b2921fe9e431d35fcc3d31a285dc2c26b252113
---

# Master Tstod

TSTOD()

TSTOD()

Advantage Concepts

| TSTOD()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that converts a timestamp value to a date value.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

TSTOD(<TimeStamp>) -> dDate

Parameters

| <TimeStamp> | The timestamp value to convert. |

Return Values

TSTOD() returns the date portion of a timestamp value. The function returns a NULL value if the given parameter is NULL.

See Also

[CTOD()](master_ctod.md)

[CTOTS()](master_ctots.md)

[DATE()](master_date.md)

[STOD()](master_stod.md)

[STOTS()](master_stots.md)
