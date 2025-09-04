REVERSE()




Advantage Database Server 12  

REVERSE()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| REVERSE()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - REVERSE() Advantage Concepts master\_Reverse Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| REVERSE()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that reverses the order of characters in a string.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

REVERSE(<cString>) -> cReverseString

Parameters

<cString>  A character string to be converted to reverse order.

Returns Values

REVERSE() returns a copy of <cString> with all characters in the string put in reverse order.

Remarks

REVERSE() is a character function that reverses all characters in a string. For example, REVERSE( "abcdef" ) would return the string "fedcba".

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[RAT()](master_rat.htm)