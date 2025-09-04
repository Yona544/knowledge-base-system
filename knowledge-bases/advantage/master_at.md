AT()




Advantage Database Server 12  

AT()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AT()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - AT() Advantage Concepts master\_At Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AT()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the position of a substring within a character string.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

AT(<cSearch>, <cTarget> [,<nStart>]) à nPosition

LOCATE(<cSearch>, <cTarget> [,<nStart>]) à nPosition   SQL Only

Parameters

<cSearch>  The character substring to be searched for.

<cTarget>  The character string to be searched.

<nStart>  Optional position in cTarget to start searching from.

Return Values

AT() returns the position of the first instance of <cSearch> within <cTarget> as an integer numeric value. If <cSearch> is not found, AT() returns zero.

Remarks

AT() is a character function used to determine the position of the first occurrence of a character substring within another string. To find the last instance of a substring within a string, use RAT().

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[RAT()](master_rat.htm)

[SUBSTR()](master_substr.htm)