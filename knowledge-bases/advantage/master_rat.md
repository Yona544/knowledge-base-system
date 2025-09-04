RAT()




Advantage Database Server 12  

RAT()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| RAT()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - RAT() Advantage Concepts master\_Rat Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| RAT()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the position of the last occurrence of a substring.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

RAT(<cSearch>, <cTarget>) à nPosition

Parameters

|  |  |
| --- | --- |
| <cSearch> | The character string to be located. |
| <cTarget> | The character string to be searched. |

Return Values

RAT() returns the position of <cSearch> within <cTarget> as an integer numeric value. If <cSearch> is not found, RAT() returns zero.

Remarks

RAT() is a character function that returns the position of the last occurrence of a character substring within another character string. It does this by searching the target string from the right. RAT() is like the AT() function, which returns the position of the first occurrence of a substring within another string. RAT() is also like the $ operator, which determines whether a substring is contained within a string.

Both the RAT() and AT() functions are used with SUBSTR(), LEFT(), and RIGHT() to extract substrings.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[AT()](master_at.htm)

[RIGHT()](master_right.htm)

[SUBSTR()](master_substr.htm)