FLOOR()




Advantage Database Server 12  

FLOOR()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| FLOOR()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - FLOOR() Advantage Concepts master\_floor Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| FLOOR()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function to compute the integer floor of a number.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

FLOOR( <nValue> ) à nInteger

Parameters

|  |  |
| --- | --- |
| <nValue> | Floating point value |

Return Value

The floor of <nValue>

Remarks

FLOOR returns the largest integer less than or equal to <nValue>. In SQL usage, he return value is of the same data type as the input parameter.  In navigational usage, the result is a double floating point value.

See Also

[Math Functions](master_math_functions.htm)

[CEILING()](master_ceiling.htm)