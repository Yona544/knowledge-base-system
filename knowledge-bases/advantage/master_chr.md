CHR()




Advantage Database Server 12  

CHR()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CHR()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - CHR() Advantage Concepts master\_Chr Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| CHR()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that converts an ASCII code to a character value.

|  |  |
| --- | --- |
| Supported in SQL: | No (use [CHAR](master_char.htm)) |
| Supported in Navigational: | Yes |

Syntax

CHR(<nCode>) à cChar

Parameters

<nCode>  An ASCII code in the range of zero to 255.

Return Values

CHR() returns a single character value whose ASCII code is specified by <nCode>.

Remarks

CHR() is a numeric conversion function that converts an ASCII code to a character. It is the inverse of [ASCII()](master_ascii.htm).

Note CHR(0) has a length of one (1) and is treated like any other character.

See Also

[ASCII](master_ascii.htm)