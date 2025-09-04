---
title: Master Now Utc
slug: master_now_utc
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_now_utc.htm
source: Advantage CHM
tags:
  - master
checksum: 3f31b0cb6fa3023875e48180b95e94fb0f475301
---

# Master Now Utc

NOW\_UTC()

NOW\_UTC()

Advantage Concepts

| NOW\_UTC()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the current system date and time as a timestamp value.

| Supported in SQL: | No (use CURRENT\_TIMESTAMP\_UTC) |
| Supported in Navigational: | Yes |

Syntax

NOW\_UTC() -> Timestamp

Return Values

NOW\_UTC() returns the current UTC (GMT) date and time as a timestamp value.

Remarks

NOW\_UTC() is a datetime function that provides a means of initializing memory variables to the current UTC Timestamp and comparing other Timestamp values to the current Timestamp.

See Also

[NOW()](master_now.md)

[TODAY()](master_today.md)

[TIME()](master_time.md)

[STOTS()](master_stots.md)
