---
title: Master If
slug: master_if
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_if.htm
source: Advantage CHM
tags:
  - master
checksum: c32ed2c1ecbcb8abcc1726253cf10e0a61f46ca3
---

# Master If

IF()

IF()

Advantage Concepts

| IF()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the result of an expression based on a condition.

| Supported in SQL: | No   see [IIF()](master_iif.md) |
| Supported in Navigational: | Yes |

Syntax

IF(<lCondition>, <expTrue>, <expFalse>) à Value

Parameters

| <lCondition> | A logical expression to be evaluated. |
| <expTrue> | The value, a condition-expression, of any data type, returned if <lCondition> is true (.T.). |
| <expFalse> | The value, of any date type, returned if <lCondition> is false (.F.). This argument does not need to be the same data type as <expTrue>. |

Return Values

IF() returns the evaluation of <expTrue> if <lCondition> evaluates to true (.T.) and <expFalse> if it evaluates to false (.F.). The value returned is the data type of the valid condition-expression.

Remarks

IF() is a logical conversion function. It provides a mechanism to evaluate a condition within an expression. With this ability, you can convert a logical expression to another data type.

Note Advantage Expression Engine functions can be used in expressions such as record filter expressions and index expressions. They are not necessarily scalars supported within SQL statements. For a list of supported SQL scalar functions, see [Supported Scalar Functions](master_supported_scalar_functions.md).

Note Memo, binary, and image fields are not supported in this Advantage Expression Engine function. If memo, binary, or image fields are used with this expression engine function, the Advantage Expression Engine will be unable to evaluate the expression.

See Also

[IIF()](master_iif.md)
