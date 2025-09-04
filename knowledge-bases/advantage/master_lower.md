LOWER()




Advantage Database Server 12  

LOWER()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| LOWER()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - LOWER() Advantage Concepts master\_Lower Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| LOWER()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that converts uppercase characters to lowercase.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

LOWER(<cString>) à cLowerString

LCASE(<cString>) à cLowerString     SQL Only

Parameters

<cString>  A character string to be converted to lowercase.

Returns Values

LOWER() returns a copy of <cString> with all alphabetic characters converted to lowercase. All other characters remain the same as in the original string.

Remarks

LOWER() is a character function that converts uppercase and mixed case strings to lowercase. It is related to UPPER() which converts lowercase and mixed case strings to uppercase.

LOWER() can be used to normalize strings for case-independent comparison or indexing purposes.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[UPPER()](master_upper.htm)