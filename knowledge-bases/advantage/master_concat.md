CONCAT()




Advantage Database Server 12  

CONCAT()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CONCAT()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - CONCAT() Advantage Concepts Master\_concat Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| CONCAT()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that concatenates two strings together.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

CONCAT( <cString1>, <cString2> ) -> <cString>

 

Parameters

|  |  |
| --- | --- |
| <cString1>, <cString2> | The two strings to be concatenated. |

Return Values

CONCAT returns a string consisting of the concatenation of the two input strings.

Remarks

The result is the same as using the + operator on the two strings.

Note Binary and image fields are not supported by this function.