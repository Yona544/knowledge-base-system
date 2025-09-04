OCTET\_LENGTH()




Advantage Database Server 12  

OCTET\_LENGTH()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| OCTET\_LENGTH()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - OCTET\_LENGTH() Advantage Concepts master\_octet\_length Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| OCTET\_LENGTH()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the length of a string in octets (i.e., bytes).

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

OCTET\_LENGTH( <cStr> ) à nOctets

Parameters

|  |  |
| --- | --- |
| <cStr> | An ANSI or Unicode string |

Return Value

The number of bytes of the given string

Remarks

This value is useful for finding the number of bytes needed to store a Unicode string.

See Also

[CHAR\_LENGTH()](master_char_length.htm)

[LEN()](master_len.htm)