---
title: Master Max
slug: master_max
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_max.htm
source: Advantage CHM
tags:
  - master
checksum: 23018d911f756779ece2d82eba1aa3c4595fb24e
---

# Master Max

MAX()

MAX()

Advantage Concepts

| MAX()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the larger of two numeric or date values.

| Supported in SQL: | No (name conflicts with [MAX aggregate](master_supported_aggregate_column_functions.md)) |
| Supported in Navigational: | Yes |

Syntax

MAX( <nExp1>, <nExp2> ) -> nLarger

MAX( <dExp1>, <dExp2> ) -> dLarger

Parameters

| <nExp1> and <nExp2> | The numeric values to be compared. |
| <dExp1> and <dExp2> | The date values to be compared. |

Return Values

MAX() returns the larger of the two arguments. The value returned is the same data type as the arguments.

Remarks

MAX() is a numeric and date function that ensures the value of an expression is larger than a specified minimum. The inverse of MAX() is MIN() which returns the lesser of two numeric or date values.

Note Advantage Expression Engine functions can be used in expressions such as record filter expressions and index expressions. The name of this scalar conflicts with the SQL MAX aggregate function and so cannot be used in SQL statements.

See Also

[MIN()](master_min.md)
