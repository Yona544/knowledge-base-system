---
title: Master Current Timestamp
slug: master_current_timestamp
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_current_timestamp.htm
source: Advantage CHM
tags:
  - master
checksum: 89f3a07e3963ed5348132f4ffc45b080d7c627b5
---

# Master Current Timestamp

CURRENT\_TIMESTAMP()

CURRENT\_TIMESTAMP()

Advantage Concepts

| CURRENT\_TIMESTAMP()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns a timestamp value for the current local time.

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

CURRENT\_TIMESTAMP([ <nPrecision> ]) à timestamp

Parameters

| <nPrecision> | Optional parameter to specify the precision of the fractional portion of seconds returned.  <nPrecision> can be a value from 0 to 3. |

Return Value

A timestamp representing the local time.

See Also

[NOW()](master_now.md)

[CURRENT\_TIMESTAMP\_UTC()](master_current_timestamp_utc.md)

[Date/Time Functions](master_date_time_functions.md)
