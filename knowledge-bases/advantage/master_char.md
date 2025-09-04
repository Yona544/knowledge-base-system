CHAR()




Advantage Database Server 12  

CHAR()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CHAR()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - CHAR() Advantage Concepts Master\_char Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| CHAR()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that converts an ASCII code to a character value.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No (use [CHR](master_chr.htm)) |

Syntax

CHAR(<nCode>) à cChar

Parameters

<nCode>  An ASCII code in the range of zero to 255.

Return Values

CHAR() returns a single character value whose ASCII code is specified by <nCode>.

Remarks

CHAR() is a numeric conversion function that converts an ASCII code to a character. It is the inverse of ASCII().

See Also

[ASCII](master_ascii.htm)