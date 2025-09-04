SIGN()




Advantage Database Server 12  

SIGN()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SIGN()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - SIGN() Advantage Concepts master\_sign Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| SIGN()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns an indicator of the sign of the parameter.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

SIGN( <nValue> ) à nSign

Parameters

|  |  |
| --- | --- |
| <nValue> | Value to test |

Return Value

-1, 0, or 1

Remarks

If <nValue> is less than zero, -1 is returned. If <nValue> equals zero, 0 is returned. If <nValue> is greater than zero, 1 is returned.

See Also

[Math Functions](master_math_functions.htm)