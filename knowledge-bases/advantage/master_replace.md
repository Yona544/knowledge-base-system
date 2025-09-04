REPLACE()




Advantage Database Server 12  

REPLACE()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| REPLACE()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - REPLACE() Advantage Concepts master\_replace Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| REPLACE()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that replaces substrings in one string with another.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

REPLACE( <cTarget>, <cSearch>, <cReplace> ) à cResult

Parameters

|  |  |
| --- | --- |
| <cTarget> | The string to be searched |
| <cSearch> | The substring to search for |
| <cReplace> | The replacement string. |

Return Value

A copy of <cTarget> where all instances of the substring <cSearch> have been replaced with <cReplace>

Remarks

This function replaces all occurrences of <cSearch> in <cTarget> with <cReplace>.

Example

 

SELECT REPLACE( 'abcdefabc', 'abc', '12345' ) FROM system.iota;   // returns 12345def12345

See Also

[AT()](master_at.htm)

[SUBSTR()](master_substr.htm)