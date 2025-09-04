---
title: Master Extract
slug: master_extract
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_extract.htm
source: Advantage CHM
tags:
  - master
checksum: 892c9454fe699a4c0e759bbc801d6ea9636ea10d
---

# Master Extract

EXTRACT()

EXTRACT()

Advantage Concepts

| EXTRACT()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that retrieves one part of a timestamp value.

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

EXTRACT( time-value FROM <timestamp> ) à nValue

Parameters

| time-value | Specifies the desired portion of the timestamp. It can be YEAR, MONTH, DAY, HOUR, MINUTE, SECOND, or FRAC\_SECOND. |
| <timestamp> | The timestamp value to extract the value from. |

Return Value

An integer value representing the specified portion of the timestamp.

Remarks

Extract year, month, day, hour, minute, or second from TIMESTAMP.

See Also

[CREATETIMESTAMP()](master_createtimestamp.md)
