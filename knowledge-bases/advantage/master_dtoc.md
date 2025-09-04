DTOC()




Advantage Database Server 12  

DTOC()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DTOC()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - DTOC() Advantage Concepts master\_Dtoc Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| DTOC()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that converts a date value to a character string.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

DTOC(<dDate>, [<nFormat>]) à cDate

Parameters

<dDate>  The date value to convert.

<nFormat> When this optional value is 1 the date format used is yyyymmdd.

Return Values

DTOC() returns a character string representation of a date value. The return value is formatted in the current date format. The default format is mm/dd/yyyy.A null date from a DBF table returns a string of spaces equal in length to the current date format. The function returns NULL if the parameter is a null date in an ADT table.

Remarks

If you are indexing a date in combination with a character string, use DTOS() instead of DTOC() to convert the date value to a character string.

See Also

[CTOD()](master_ctod.htm)

[DATE()](master_date.htm)

[DTOS()](master_dtos.htm)

[STOD()](master_stod.htm)

[TTOC()](master_ttoc.htm)

[STOTS()](master_stots.htm)

Advantage TDataSet Descendant

[TAdsSettings.DateFormat](ade_dateformat.htm)

Advantage Client Engine API

[AdsSetDateFormat](ace_adssetdateformat.htm)