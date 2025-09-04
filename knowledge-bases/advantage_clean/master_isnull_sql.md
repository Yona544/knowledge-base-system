---
title: Master Isnull Sql
slug: master_isnull_sql
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_isnull_sql.htm
source: Advantage CHM
tags:
  - master
checksum: 8aefb697bcfac2d14ccc8967bc62c777bb47fc99
---

# Master Isnull Sql

ISNULL() SQL

ISNULL()

Advantage Concepts

| ISNULL()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns a given value or an alternative if the first is null.

| Supported in SQL: | Yes |
| Supported in Navigational: | No (See remarks) |

Syntax

ISNULL( <expr>, <value> ) à result

Parameters

| <expr> | An expression or value |
| <value> | The alternate value to return if <expr> is null |

Return Value

This returns either <expr> or <value>

Remarks

The SQL version of ISNULL is functionally the same as [IFNULL()](master_ifnull.md).  There is a navigational scalar named [ISNULL()](master_isnull.md), but it has different functionality.

See Also

[COALESCE()](master_coalesce.md)

[IFNULL()](master_ifnull.md)
