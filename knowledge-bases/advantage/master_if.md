IF()




Advantage Database Server 12  

IF()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IF()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - IF() Advantage Concepts master\_If Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| IF()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the result of an expression based on a condition.

|  |  |
| --- | --- |
| Supported in SQL: | No   see [IIF()](master_iif.htm) |
| Supported in Navigational: | Yes |

Syntax

IF(<lCondition>, <expTrue>, <expFalse>) à Value

Parameters

|  |  |
| --- | --- |
| <lCondition> | A logical expression to be evaluated. |
| <expTrue> | The value, a condition-expression, of any data type, returned if <lCondition> is true (.T.). |
| <expFalse> | The value, of any date type, returned if <lCondition> is false (.F.). This argument does not need to be the same data type as <expTrue>. |

Return Values

IF() returns the evaluation of <expTrue> if <lCondition> evaluates to true (.T.) and <expFalse> if it evaluates to false (.F.). The value returned is the data type of the valid condition-expression.

Remarks

IF() is a logical conversion function. It provides a mechanism to evaluate a condition within an expression. With this ability, you can convert a logical expression to another data type.

Note Advantage Expression Engine functions can be used in expressions such as record filter expressions and index expressions. They are not necessarily scalars supported within SQL statements. For a list of supported SQL scalar functions, see [Supported Scalar Functions](master_supported_scalar_functions.htm).

Note Memo, binary, and image fields are not supported in this Advantage Expression Engine function. If memo, binary, or image fields are used with this expression engine function, the Advantage Expression Engine will be unable to evaluate the expression.

See Also

[IIF()](master_iif.htm)