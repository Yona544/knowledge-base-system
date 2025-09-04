master\_substring




Advantage Database Server 12  

SUBSTRING()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SUBSTRING()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - SUBSTRING() Advantage Concepts Master\_substring Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| SUBSTRING()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that extracts a substring from a character string.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No. See [SUBSTR()](master_substr.htm) |

Syntax

SUBSTRING(<cString>, <nStart>, <nCount>) à cSubstring

Parameters

|  |  |
| --- | --- |
| <cString> | The character string from which to extract a substring. |
| <nStart> | The starting position in <cString>. The value must be > 0. |
| <nCount> | The number of characters to be extracted. If omitted, the substring begins at <nStart> and continues to the end of the string. If <nCount> is greater than the number of characters from <nStart> to the end of <cString>, the excess numbers are ignored. |

Return Values

SUBSTRING() returns a character string.

Remarks

SUBSTRING() is a character function that extracts a substring from another character string. It is related to the LEFT() and RIGHT() functions which extract substrings beginning with leftmost and rightmost characters in <cString>, respectively.

Note Binary and image fields are not supported by this function.

See Also

[RAT()](master_rat.htm)

[LEFT()](master_left.htm)

[RIGHT()](master_right.htm)

[STR()](master_str.htm)