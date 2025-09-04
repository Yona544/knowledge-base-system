SUBSTRINGOF()




Advantage Database Server 12  

SUBSTRINGOF()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SUBSTRINGOF()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - SUBSTRINGOF() Advantage Concepts master\_substringof Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| SUBSTRINGOF()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that searches a string for a substring.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

SUBSTRINGOF( <cSearch>, <cTarget> ) à SyntaxRetPH

Parameters

|  |  |
| --- | --- |
| <cSearch> | The string to search for |
| <cTarget> | The string to be searched |

Return Value

A boolean value indicating if the substring was found

Remarks

Returns True if str1 is a substring str2, and False otherwise.

See Also

[AT()](master_at.htm)

[POSITION()](master_position.htm)