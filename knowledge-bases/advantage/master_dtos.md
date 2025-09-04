DTOS()




Advantage Database Server 12  

DTOS()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DTOS()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - DTOS() Advantage Concepts master\_Dtos Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| DTOS()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that converts a date value to a character string formatted as yyyymmdd.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

DTOS(<dDate>) à cDate

Parameters

<dDate>  The date value to convert.

Return Values

DTOS() returns a character string eight characters long in the format yyyymmdd. When <dDate> is a null date from a DBF table (CTOD("")), DTOS() returns a string of eight spaces. The return value is not affected by the current date format. The function returns NULL if the parameter is a null date in an ADT table.

Remarks

DTOS() is a date conversion function that is used when creating index expressions consisting of a date value and a character expression. DTOS() converts a date value to a character string that can be concatenated to any other character expression. The return value is structured to preserve date order (year, month, and day).

See Also

[CTOD()](master_ctod.htm)

[DATE()](master_date.htm)

[DTOC()](master_dtoc.htm)

[STOD()](master_stod.htm)

[STOTS()](master_stots.htm)