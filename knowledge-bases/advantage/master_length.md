LENGTH()




Advantage Database Server 12  

LENGTH()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| LENGTH()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - LENGTH() Advantage Concepts Master\_length Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| LENGTH()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the length of a character string excluding trailing spaces.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

LENGTH(<cString>) à nCount

Parameters

|  |  |
| --- | --- |
| <cString> | The character string to count. |

Return Values

LENGTH() returns the length of a character string as an integer numeric value.

Remarks

LENGTH() returns the length of a character string excluding trailing spaces.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[LTRIM()](master_ltrim.htm)

[RTRIM()](master_rtrim.htm)

[LEN()](master_len.htm)