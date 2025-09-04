INLIST()




Advantage Database Server 12  

INLIST()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| INLIST()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - INLIST() Advantage Concepts master\_Inlist Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| INLIST()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function to determine if one expression matches another expression in a set of expressions.

|  |  |
| --- | --- |
| Supported in SQL: | No |
| Supported in Navigational: | Yes |

Syntax

INLIST(<Expression>, <Expression2>, [ Expression3,]) à lFound

Parameters

<Expression>  Expression to search for in the set of expressions.

<Expression2> The first of up to 25 expressions to be searched.

Return Values

Logical or NULL

Remarks

Returns true if the expression is found in the list. False if the expression is not found in the set and NULL if the expression was not found and one or more values in the expression set was NULL.

See Also