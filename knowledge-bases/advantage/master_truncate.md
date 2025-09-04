TRUNCATE()




Advantage Database Server 12  

TRUNCATE()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TRUNCATE()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - TRUNCATE() Advantage Concepts master\_truncate Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TRUNCATE()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that truncates a floating point value.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

TRUNCATE( <nValue>, <iDecimals> ) à nResult

Parameters

|  |  |
| --- | --- |
| <nValue> | The floating point or numeric value to truncate |
| <iDecimals> | The desired number of decimal places. |

Return Value

<nValue> truncated as specified

Remarks

This function truncates <iDecimals> places to the right of the decimal point. If <iDecimals> is negative, <nValue> is truncated to ABS(<nDecimals>) places to the left of the decimal point.

See Also

[Math Functions](master_math_functions.htm)