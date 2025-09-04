---
title: Master Min
slug: master_min
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_min.htm
source: Advantage CHM
tags:
  - master
checksum: 010b27441bc5f9bd7e3952f72d129d0b1d063b62
---

# Master Min

MIN()

MIN()

Advantage Concepts

| MIN()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the smaller of two numeric or date values.

| Supported in SQL: | No (name conflicts with [MIN aggregate](master_supported_aggregate_column_functions.md)) |
| Supported in Navigational: | Yes |

Syntax

MIN( <nExp1>, <nExp2> ) --> nSmaller

MIN( <dExp1>, <dExp2> ) --> dSmaller

Parameters

| <nExp1> and <nExp2> | The numeric values to be compared. |
| <dExp1> and <dExp2> | The date values to be compared. |

Return Values

MIN() returns the smaller of the two arguments. The value returned is the same data type as the arguments.

Remarks

MIN() is a numeric and date function that ensures the value of an expression is smaller than a specified minimum. The inverse of MIN() is MAX() which returns the greater of two numeric or date values.

Note Advantage Expression Engine functions can be used in expressions such as record filter expressions and index expressions. The name of this scalar conflicts with the SQL MAX aggregate function and so cannot be used in SQL statements.

See Also

[MAX()](master_max.md)
