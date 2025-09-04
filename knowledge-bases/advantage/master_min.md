MIN()




Advantage Database Server 12  

MIN()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| MIN()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - MIN() Advantage Concepts master\_Min Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| MIN()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the smaller of two numeric or date values.

|  |  |
| --- | --- |
| Supported in SQL: | No (name conflicts with [MIN aggregate](master_supported_aggregate_column_functions.htm)) |
| Supported in Navigational: | Yes |

Syntax

MIN( <nExp1>, <nExp2> ) --> nSmaller

MIN( <dExp1>, <dExp2> ) --> dSmaller

Parameters

|  |  |
| --- | --- |
| <nExp1> and <nExp2> | The numeric values to be compared. |
| <dExp1> and <dExp2> | The date values to be compared. |

Return Values

MIN() returns the smaller of the two arguments. The value returned is the same data type as the arguments.

Remarks

MIN() is a numeric and date function that ensures the value of an expression is smaller than a specified minimum. The inverse of MIN() is MAX() which returns the greater of two numeric or date values.

Note Advantage Expression Engine functions can be used in expressions such as record filter expressions and index expressions. The name of this scalar conflicts with the SQL MAX aggregate function and so cannot be used in SQL statements.

See Also

[MAX()](master_max.htm)