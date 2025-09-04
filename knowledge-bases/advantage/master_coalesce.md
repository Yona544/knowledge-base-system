COALESCE()




Advantage Database Server 12  

COALESCE()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| COALESCE()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - COALESCE() Advantage Concepts master\_coalesce Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| COALESCE()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the first non-NULL expression result in a list of values.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

COALESCE( <expr1>, ... <exprn> ) à expr

Parameters

|  |  |
| --- | --- |
| <exprn> | An expression or value |

Return Value

COALESCE returns the first value of <expr1> ... <exprn> that is non-null.

Remarks

All expressions must be of the same type or be implicitly convertible to the same type. No parameters or BLOBs are allowed as an expression type. If all the expressions evaluate to NULL, COALESCE returns a NULL value.

See Also

[IIF()](master_iif.htm)