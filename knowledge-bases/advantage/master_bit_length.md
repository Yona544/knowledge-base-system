BIT\_LENGTH()




Advantage Database Server 12  

BIT\_LENGTH()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| BIT\_LENGTH()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - BIT\_LENGTH() Advantage Concepts Master\_bit\_length Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| BIT\_LENGTH()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the length of a character string in bits.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

BIT\_LENGTH(<cString>) à nCount

Parameters

|  |  |
| --- | --- |
| <cString> | The character string to count. |

Return Value

The length of a character string in bits assuming 8 bits in a byte.

Remarks

The length includes trailing spaces. For Unicode fields, the length is the number of octets composing the string multiplied by 8.

Note Binary and image fields are not supported by this function.

See Also

[LEN()](master_len.htm)