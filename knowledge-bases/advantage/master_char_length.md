CHAR\_LENGTH()




Advantage Database Server 12  

CHAR\_LENGTH()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CHAR\_LENGTH()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - CHAR\_LENGTH() Advantage Concepts Master\_char\_length Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| CHAR\_LENGTH()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the length of a character string in specified units.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

CHAR\_LENGTH(<cString> [USING <unit>) à nCount

CHARACTER\_LENGTH(<cString> [USING <unit>) à nCount

 

Parameters

|  |  |
| --- | --- |
| <cString> | The character string to count. |
| <unit> | Optional unit type. Valid values are CHARACTERS, OCTETS, or CODE\_POINTS. |

Return Value

The length of a character string in the specified units.

Remarks

The length includes trailing spaces. This function can be useful for Unicode strings because of the ability to choose the units. If there is no unit specification, the default is CHARACTERS which is the number of character for non-Unicode string input or number of code units (UTF16 characters) for Unicode string input. For non-Unicode string input, the result is the same regardless of the units. For Unicode string input, if the unit is OCTETS, the function returns the length of the string in number of bytes. If the unit is CODE\_POINTS, the function returns the number of code points (the number of Unicode characters) in the string.  If one or more Unicode characters in the string takes up two code units (two UTF16 characters), then the result when specifying CODE\_POINTS as the unit will be less than the result when specifying CHARACTERS.

Note Binary and image fields are not supported by this function.

See Also

[LEN()](master_len.htm)

[OCTET\_LENGTH()](master_octet_length.htm)