CTOD()




Advantage Database Server 12  

CTOD()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CTOD()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - CTOD() Advantage Concepts master\_Ctod Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| CTOD()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that converts a date string to a date value.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

CTOD(<cDate>) à dDate

Parameters

|  |  |
| --- | --- |
| <cDate> | A character string consisting of numbers representing the month, day, and year separated by any character other than a number. The month, day, and year digits must be specified in accordance with the function to set the date format. |

Return Values

CTOD() returns a date value. If <cDate> is not a valid date, CTOD() returns an empty date.

Remarks

CTOD() is a character conversion function that converts a character string to a date. CTOD() is used whenever you need a literal date value. Some examples include:

|  |  |
| --- | --- |
| · | Specifying a literal date string in order to perform date arithmetic |

|  |  |
| --- | --- |
| · | Comparing the result of a date expression to a literal date string |

CTOD() is the inverse of DTOC() which converts a date value to a character string in the format specified by the function to set the date format. DTOS() also converts a date value to a character string in the form yyyymmdd.

Note Binary and image fields are not supported by this function. Memo fields are supported by the SQL version of the scalar.

See Also

[DATE()](master_date.htm)

[DTOC()](master_dtoc.htm)

[DTOS()](master_dtos.htm)

[CTOT()](master_ctot.htm)

[CTOTS()](master_ctots.htm)

[STOD()](master_stod.htm)

[STOTS()](master_stots.htm)

[TSTOD()](master_tstod.htm)

Advantage TDataSet Descendant

[TAdsSettings.DateFormat](ade_dateformat.htm)

Advantage Client Engine API

[AdsSetDateFormat](ace_adssetdateformat.htm)

[AdsSetEpoch](ace_adssetepoch.htm)