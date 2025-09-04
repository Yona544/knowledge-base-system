DAYNAME()




Advantage Database Server 12  

DAYNAME()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DAYNAME()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - DAYNAME() Advantage Concepts Master\_DAYNAME Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| DAYNAME()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the day name of a date value.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

DAYNAME(<dDate>) à cDayName

Parameters

<dDate>  A date value to convert.

Return Values

DAYNAME() returns the string name for the day of week of the date value. If the date argument is empty, DAYNAME() returns an empty string.

Remarks

DAYNAME() is a date conversion function used to return the day of week name of the date value.

See Also

[MONTHNAME()](master_monthname.htm)

[DAY()](master_day.htm)