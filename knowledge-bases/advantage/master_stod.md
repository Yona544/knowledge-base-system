STOD()




Advantage Database Server 12  

STOD()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| STOD()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - STOD() Advantage Concepts master\_Stod Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| STOD()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that converts a character string formatted as YYYYMMDD to a date value.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

STOD(<cDate>) -> dDate

Parameters

|  |  |
| --- | --- |
| <cDate> | A character string consisting of numbers representing the year, month, and day in the format YYYYMMDD. |

Return Values

STOD() returns a date value. If <cDate> is not a valid date, STOD() returns an empty date.

Remarks

STOD() is a character conversion function that converts a character string to a date. STOD() can be used whenever you need a literal date value. Some examples include:

|  |  |
| --- | --- |
| · | Specifying a literal date string in order to perform date arithmetic |

|  |  |
| --- | --- |
| · | Comparing the result of a date expression to a literal date string |

STOD() is the inverse of DTOS() which converts a date value to a character string in the format YYYYMMDD.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[DATE()](master_date.htm)

[DTOC()](master_dtoc.htm)

[DTOS()](master_dtos.htm)

[CTOD()](master_ctod.htm)

[CTOT()](master_ctot.htm)

[CTOTS()](master_ctots.htm)

[TSTOD()](master_tstod.htm)