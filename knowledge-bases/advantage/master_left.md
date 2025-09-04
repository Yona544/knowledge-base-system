LEFT()




Advantage Database Server 12  

LEFT()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| LEFT()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - LEFT() Advantage Concepts master\_Left Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| LEFT()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that extracts a substring beginning with the first character in a string.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

LEFT(<cString>, <nCount>) à cSubString

Parameters

|  |  |
| --- | --- |
| <cString> | A character string from which to extract characters. The maximum size of <cString> is 65,535 (64K) bytes. |
| <nCount> | The number of characters to extract. |

Return Values

LEFT() returns the leftmost <nCount> characters of <cString> as a character string. If <nCount> is negative or zero, LEFT() returns a null string (""). If <nCount> is larger than the length of the character string, LEFT() returns the entire string.

Remarks

LEFT() is a character function that returns a substring of a specified character string. It is the same as SUBSTR(<cString>, 1, <nCount>). LEFT() is also like RIGHT(), which returns a substring beginning with the last character in a string.

LEFT(), RIGHT(), and SUBSTR() are often used with both the AT() and RAT() functions to locate the first and/or the last position of a substring before extracting it.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[AT()](master_at.htm)

[LTRIM()](master_ltrim.htm)

[RAT()](master_rat.htm)

[RTRIM()](master_rtrim.htm)

[SUBSTR()](master_substr.htm)

[RIGHT()](master_right.htm)