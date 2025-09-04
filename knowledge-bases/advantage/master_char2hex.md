CHAR2HEX()




Advantage Database Server 12  

CHAR2HEX()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CHAR2HEX()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - CHAR2HEX() Advantage Concepts Master\_CHAR2HEX Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| CHAR2HEX()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that converts a character string to a binary value.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

CHAR2HEX(<cHexadecimal>) à bBinary

Parameters

|  |  |
| --- | --- |
| <cHexadecimal> | A character string consisting of hexadecimal characters or spaces.  Hexadecimal characters are the digits 0-9 and the uppercase and lowercase letters A-F.  Spaces in the string will be ignored. If an odd number of hexadecimal characters is specified the binary value will be zero padded. |

Return Values

CHAR2HEX() returns a binary value. If <cHexadecimal> is not a valid hexadecimal string, an error will be returned.

Remarks

CHAR2HEX() is a character conversion function that converts a character string to a binary value. CHAR2HEX() is used whenever you need a literal binary value. CHAR2HEX() is the inverse of HEX2CHAR() which converts a binary value to a character string.

The binary result can be stored in fields with a raw or binary data type.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[Functions to Convert Hexadecimal Values](master_functions_to_convert_hexadecim.htm)

[String Functions](master_string_functions.htm)

[HEX2CHAR()](master_hex2char.htm)