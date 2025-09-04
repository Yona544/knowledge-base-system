ALLTRIM()




Advantage Database Server 12  

ALLTRIM()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ALLTRIM()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - ALLTRIM() Advantage Concepts master\_Alltrim Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ALLTRIM()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that removes leading and trailing spaces from a character string.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

ALLTRIM(<cString>) à cTrimString

Parameters

<cString>  The character expression to be trimmed.

Return Values

Returns a character string with leading and trailing spaces removed.

Remarks

ALLTRIM() is a character function that removes both leading and trailing spaces from a string. It is related to LTRIM() and RTRIM() which remove leading and trailing spaces, respectively. The inverse of ALLTRIM(), LTRIM(), and RTRIM() are the PADC(), PADL(), and PADR() functions which center, left-justify, or right-justify character strings by padding them with fill characters.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[LTRIM()](master_ltrim.htm)

[PAD()](master_pad.htm)

[RTRIM()](master_rtrim.htm)

[TRIM()](master_trim.htm)