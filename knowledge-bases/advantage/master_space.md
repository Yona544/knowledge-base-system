SPACE()




Advantage Database Server 12  

SPACE()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SPACE()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - SPACE() Advantage Concepts master\_Space Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| SPACE()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns a string of spaces.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

SPACE(<nCount>) à cSpaces

Parameters

<nCount> The number of spaces to be returned, up to a maximum of 65,535 (64K) in navigational usage and up to 1024 in SQL usage.

Return Values

SPACE() returns a character string. If <nCount> is zero, SPACE() returns an empty string ("").

Remarks

SPACE() is a character function that returns a specified number of spaces. SPACE() can pad strings with leading or trailing spaces.

See Also

[PAD()](master_pad.htm)

[REPEAT()](master_repeat.htm)