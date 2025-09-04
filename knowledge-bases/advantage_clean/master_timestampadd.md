---
title: Master Timestampadd
slug: master_timestampadd
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_timestampadd.htm
source: Advantage CHM
tags:
  - master
checksum: dea02c13141f6c8f643d0939d09ace3b05f37bf9
---

# Master Timestampadd

TIMESTAMPADD()

TIMESTAMPADD()

Advantage Concepts

| TIMESTAMPADD()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that adds an interval to a timestamp value.

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

TIMESTAMPADD( interval, <nValue>, <timestamp> ) à timestamp

Parameters

| interval | SQL\_TSI\_FRAC\_SECOND, SQL\_TSI\_SECOND, SQL\_TSI\_MINUTE, SQL\_TSI\_HOUR, SQL\_TSI\_DAY, SQL\_TSI\_WEEK, SQL\_TSI\_MONTH, SQL\_TSI\_QUARTER, SQL\_TSI\_YEAR |
| <nValue> | The value to add to <timestamp> |
| <timestamp> | The original timestamp to add to |

Return Value

<timestamp> plus <nValue> intervals

See Also

[TIMESTAMPDIFF()](master_timestampdiff.md)
