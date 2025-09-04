HEX2CHAR




Advantage Database Server 12  

HEX2CHAR()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| HEX2CHAR()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - HEX2CHAR() Advantage Concepts Master\_HEX2CHAR Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| HEX2CHAR()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that converts a binary value to a character string.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

HEX2CHAR(<bBinary>) à cHexadecimal

Parameters

<bBinary>       The binary value to convert.

Return Values

HEX2CHAR() returns a binary value. If <cHexadecimal> is not a valid hexadecimal string, an error will be returned.

Remarks

HEX2CHAR() returns a character string representation of a binary value. Each byte of the binary value is represented as two hexadecimal characters.  Hexadecimal characters are the digits 0-9 and the uppercase letters A-F.

HEX2CHAR() is the inverse CHAR2HEX() of which converts a character string to a binary value.

The binary input can come from a field with a raw data type. Note variable length fields like binary fields are not supported by the Advantage Expression Engine.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[Functions to Convert Hexadecimal Values](master_functions_to_convert_hexadecim.htm)

[String Functions](master_string_functions.htm)

[CHAR2HEX()](master_char2hex.htm)