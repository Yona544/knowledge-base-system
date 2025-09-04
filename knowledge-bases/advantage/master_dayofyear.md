DAYOFYEAR()




Advantage Database Server 12  

DAYOFYEAR()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DAYOFYEAR()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - DAYOFYEAR() Advantage Concepts Master\_DAYOFYEAR Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| DAYOFYEAR()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the day of the year of a date value.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

DAYOFYEAR(<dDate>) à nDay

Parameters

<dDate>  A date value to convert.

Return Values

DAYOFYEAR() returns a number in the range of 1 to 366 as an integer numeric value.  If the date argument is empty, DAYOFYEAR() returns zero.

Remarks

DAYOFYEAR() is a date conversion function used to convert a date value to the day of year.

See Also

[DAYOFWEEK()](master_dayofweek.htm)

[DAY()](master_day.htm)

[MONTH()](master_month.htm)

[QUARTER()](master_quarter.htm)

[YEAR()](master_year.htm)