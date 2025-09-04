ASCII()




Advantage Database Server 12  

ASCII()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ASCII()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - ASCII() Advantage Concepts Master\_ascii Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ASCII()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the ASCII code of a character value.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No (use [CHR](master_chr.htm)) |

Syntax

ASCII(<str>) à nCode

Parameters

<str>  A character string.

Return Values

ASCII() returns the ASCII code of the first character of the given string.

Remarks

ASCII() is a conversion function that converts a character to its ASCII code. It is the inverse of [CHAR()](master_char.htm).

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[CHAR](master_char.htm)