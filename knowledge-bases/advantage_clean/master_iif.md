---
title: Master Iif
slug: master_iif
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_iif.htm
source: Advantage CHM
tags:
  - master
checksum: eb1fdee57a4fa4e2789bb81c8ba0c4e1be87c131
---

# Master Iif

IIF()

IIF()

Advantage Concepts

| IIF()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the result of an expression based on a condition.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

[I]IF(<lCondition>, <expTrue>, <expFalse>) à Value

Parameters

| <lCondition> | A logical expression to be evaluated. |
| <expTrue> | The value, a condition-expression, of any data type, returned if <lCondition> is true (.T.). |
| <expFalse> | The value, of any date type, returned if <lCondition> is false (.F.). This argument does not need to be the same data type as <expTrue>. |

Return Values

IIF() returns the evaluation of <expTrue> if <lCondition> evaluates to true (.T.) and <expFalse> if it evaluates to false (.F.). The value returned is the data type of the valid condition-expression.

Remarks

IIF() is a logical conversion function. It provides a mechanism to evaluate a condition within an expression. With this ability you can convert a logical expression to another data type.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[IF()](master_if.md)

[IIF() SQL Details](master_iif_sql.md)
