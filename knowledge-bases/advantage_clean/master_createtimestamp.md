---
title: Master Createtimestamp
slug: master_createtimestamp
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_createtimestamp.htm
source: Advantage CHM
tags:
  - master
checksum: 7f5e498461eb9aba9dd677e9dd31f816170c89ab
---

# Master Createtimestamp

CREATETIMESTAMP()

CREATETIMESTAMP()

Advantage Concepts

| CREATETIMESTAMP()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function to create a timestamp literal from the given integer parameter values.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

CREATETIMESTAMP( <nYear>, <nMonth>, <nDay>, <nHour>, <nMinute>, <nSecond>, <nMillisecond> ) à timestamp

Parameters

| <nValue> | The components of the timestamp can be expression values with constants or based on field values. |

Return Value

A timestamp value

See Also

[STOTS()](master_stots.md)

[EXTRACT()](master_extract.md)
