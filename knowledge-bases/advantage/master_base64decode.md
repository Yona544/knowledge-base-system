BASE64DECODE




Advantage Database Server 12  

BASE64DECODE()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| BASE64DECODE()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - BASE64DECODE() Advantage Concepts master\_Base64Decode Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| BASE64DECODE()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that converts a Base64 encoded value to the original value.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

BASE64DECODE(<cBase64>) à bValue

Parameters

<cBase64>   The Base64 value to decode

Return Values

BASE64DECODE() returns a a binary value with the bytes representing the original encoded value.

Remarks

BASE64DECODE converts a string representation of a Base64 value into the original value and returns it as binary data. If the original value is a string, then the result value can be cast to the appropriate type (e.g., SQL\_VARCHAR or SQL\_WVARCHAR).

See Also

[Miscellaneous Functions](master_miscellaneous_functions.htm)

[BASE64ENCODE](master_base64encode.htm)