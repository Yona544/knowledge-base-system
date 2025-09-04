LEN()




Advantage Database Server 12  

LEN()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| LEN()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - LEN() Advantage Concepts master\_Len Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| LEN()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the length of a character string including trailing spaces.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

LEN(<cString>) à nCount

Parameters

|  |  |
| --- | --- |
| <cString> | The character string to count. |

Return Values

LEN() returns the length of a character string as an integer numeric value.

Remarks

LEN() returns the length of a character string including trailing spaces.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[LTRIM()](master_ltrim.htm)

[RTRIM()](master_rtrim.htm)

[LENGTH()](master_length.htm)