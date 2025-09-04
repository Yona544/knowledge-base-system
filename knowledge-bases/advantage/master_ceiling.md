CEILING()




Advantage Database Server 12  

CEILING()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CEILING()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - CEILING() Advantage Concepts master\_ceiling Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| CEILING()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function to compute the integer ceiling of a number.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

CEILING( <nValue> ) à nInteger

Parameters

|  |  |
| --- | --- |
| <nValue> | Floating point value |

Return Value

The ceiling of <nValue>

Remarks

CEILING returns the smallest integer greater than or equal to <nValue>. In SQL usage, he return value is of the same data type as the input parameter.  In navigational usage, the result is a double floating point value.

See Also

[Math Functions](master_math_functions.htm)

[FLOOR()](master_floor.htm)