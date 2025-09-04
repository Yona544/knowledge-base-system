SYS()




Advantage Database Server 12  

SYS()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SYS()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - SYS() Advantage Concepts master\_Sys Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| SYS()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that provides compatibility with Microsoft Visual Foxpro.

|  |  |
| --- | --- |
| Supported in SQL: | No |
| Supported in Navigational: | Yes |

Syntax

SYS(<nNumber>, <Value> ) à cNumber

Parameters

<nNumber> The system function to perform, currently only function 11 is supported.

<Value> An argument to the function.

Return Values

SYS( 11 ) returns the Julian day of a date value as a character string.

Remarks

SYS( 11 ) converts a date value to a Julian date and returns the value as a string.

Note Binary, memo, and image fields are not supported by this function.