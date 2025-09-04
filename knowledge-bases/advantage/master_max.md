MAX()




Advantage Database Server 12  

MAX()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| MAX()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - MAX() Advantage Concepts master\_Max Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| MAX()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the larger of two numeric or date values.

|  |  |
| --- | --- |
| Supported in SQL: | No (name conflicts with [MAX aggregate](master_supported_aggregate_column_functions.htm)) |
| Supported in Navigational: | Yes |

Syntax

MAX( <nExp1>, <nExp2> ) -> nLarger

MAX( <dExp1>, <dExp2> ) -> dLarger

Parameters

|  |  |
| --- | --- |
| <nExp1> and <nExp2> | The numeric values to be compared. |
| <dExp1> and <dExp2> | The date values to be compared. |

Return Values

MAX() returns the larger of the two arguments. The value returned is the same data type as the arguments.

Remarks

MAX() is a numeric and date function that ensures the value of an expression is larger than a specified minimum. The inverse of MAX() is MIN() which returns the lesser of two numeric or date values.

Note Advantage Expression Engine functions can be used in expressions such as record filter expressions and index expressions. The name of this scalar conflicts with the SQL MAX aggregate function and so cannot be used in SQL statements.

See Also

[MIN()](master_min.htm)