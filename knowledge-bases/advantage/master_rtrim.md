RTRIM()




Advantage Database Server 12  

RTRIM()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| RTRIM()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - RTRIM() Advantage Concepts master\_Rtrim Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| RTRIM()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that removes trailing spaces from a character string.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

RTRIM(<cString>) à cTrimString

Parameters

<cString>  The character string to be copied without trailing spaces.

Return Value

RTRIM() returns a copy of <cString> with the trailing spaces removed. If <cString> is a null string ("") or all spaces, RTRIM() returns a null string ("").

Remarks

RTRIM() is a character function that formats character strings. It is useful for deleting trailing spaces while concatenating strings. This is typically the case with database fields that are stored in fixed-width format. For example, use RTRIM() to concatenate first and last name fields to form a name string.

RTRIM() is related to LTRIM(), which removes leading spaces, and ALLTRIM(), which removes both leading and trailing spaces. The inverse of ALLTRIM(), LTRIM(), and RTRIM() are the PADC(), PADR(), and PADL() functions which center, right-justify, or left-justify character strings by padding them with fill characters.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[PAD()](master_pad.htm)

[SUBSTR()](master_substr.htm)

[TRIM()](master_trim.htm)

[ALLTRIM()](master_alltrim.htm)

[LTRIM()](master_ltrim.htm)