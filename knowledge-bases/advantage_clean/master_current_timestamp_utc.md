---
title: Master Current Timestamp Utc
slug: master_current_timestamp_utc
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_current_timestamp_utc.htm
source: Advantage CHM
tags:
  - master
checksum: a36747f0237dfae35277e49a4519d6c3768eab71
---

# Master Current Timestamp Utc

CURRENT\_TIMESTAMP\_UTC()

CURRENT\_TIMESTAMP\_UTC()

Advantage Concepts

| CURRENT\_TIMESTAMP\_UTC()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the timestamp for the current UTC (GMT) time.

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

CURRENT\_TIMESTAMP\_UTC([ <nPrecision> ]) à timestamp

Parameters

| <nPrecision> | Optional parameter to specify the precision of the fractional portion of seconds returned.  <nPrecision> can be a value from 0 to 3. |

Return Value

A timestamp representing the current UTC time.

See Also

[CURRENT\_TIMESTAMP()](master_current_timestamp.md)

[Date/Time Functions](master_date_time_functions.md)
