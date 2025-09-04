REPEAT()




Advantage Database Server 12  

REPEAT()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| REPEAT()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - REPEAT() Advantage Concepts Master\_repeat Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| REPEAT()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns a string with given characters duplicated 1 or more times.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

REPEAT(<cString>, <nCnt>) à cRepeatedString

Parameters

<cString> The character string to repeat.

<nCnt> The number of times to duplicate <cString>.

Return Values

REPEAT() returns a string consisting of <cString> repeated <nCnt> times.

Remarks

<nCnt> must be greater or equal to zero. If nCnt is zero, an empty string is returned.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[SPACE()](master_space.htm)