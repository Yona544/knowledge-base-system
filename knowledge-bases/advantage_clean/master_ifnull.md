---
title: Master Ifnull
slug: master_ifnull
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_ifnull.htm
source: Advantage CHM
tags:
  - master
checksum: a9829d065ba5f4f8dc2d172032b5dd65c3911046
---

# Master Ifnull

IFNULL()

IFNULL()

Advantage Concepts

| IFNULL()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns a given value or an alternative if the first is null.

| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

IFNULL( <expr>, <value> ) à result

Parameters

| <expr> | An expression or value |
| <value> | The alternate value to return if <expr> is null |

Return Value

This returns either <expr> or <value>

Remarks

If <expr> is NULL, then <value> is returned. Otherwise <expr> is returned.

See Also

[COALESCE()](master_coalesce.md)
