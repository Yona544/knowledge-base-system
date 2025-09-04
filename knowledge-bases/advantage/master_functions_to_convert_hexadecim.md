Functions to Convert Hexadecimal Values




Advantage Database Server 12  

Functions to Convert Hexadecimal Values

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Functions to Convert Hexadecimal Values  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Functions to Convert Hexadecimal Values Advantage SQL Engine master\_Functions\_to\_Convert\_Hexadecim Advantage SQL > SQL Functionality > Functions to Convert Hexadecimal Values / Dear Support Staff, |  |
| Functions to Convert Hexadecimal Values  Advantage SQL Engine |  |  |  |  |

The function CHAR2HEX can be used to convert character data containing hexadecimal characters to a binary value.  Two hexadecimal characters will be converted to one byte.  If the string contains an odd number of hexadecimal characters the value will be zero padded.  Spaces can be included in the string to improve readability, but will be ignored.  CHAR2HEX( 00 00 00 2A ) would be converted to a 4 byte value containing the decimal value 42.  CHAR2HEX( 00 00 00 2 ) would be converted to a 4 byte value containing the integer value 32.

The function HEX2CHAR converts a binary value to character value.  Each byte of the binary value is represented as two hexadecimal characters.   HEX2CHAR called with the binary value 0x002A would return the character value 00 00 00 2A.

See Also

[String Functions](master_string_functions.htm)

[Supported Scalar Functions](master_supported_scalar_functions.htm)

[Expression Engine](master_advantage_expression_engine.htm)

[SQL Literals](master_sql_literals.htm)