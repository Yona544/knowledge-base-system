DAYOFWEEK()




Advantage Database Server 12  

DAYOFWEEK()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DAYOFWEEK()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - DAYOFWEEK() Advantage Concepts Master\_DAYOFWEEK Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| DAYOFWEEK()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the numeric day of a date value.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

DAYOFWEEK(<dDate>) à nDay

Parameters

<dDate>  A date value to convert.

Return Values

DAYOFWEEK() returns a number in the range of 1 to 7 as an integer numeric value.  If the date argument is empty, DAYOFWEEK() returns zero.

Remarks

DAYOFWEEK() is a date conversion function used to convert a date value to the numeric day of week value and can be used in various date calculations.

See Also

[DAYOFYEAR()](master_dayofyear.htm)

[YEAR()](master_year.htm)

[MONTH()](master_month.htm)

[DAY()](master_day.htm)

[WEEK()](master_week.htm)

[QUARTER()](master_quarter.htm)