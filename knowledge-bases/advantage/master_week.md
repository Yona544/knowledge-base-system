WEEK()




Advantage Database Server 12  

WEEK()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| WEEK()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - WEEK() Advantage Concepts Master\_week Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| WEEK()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the week number of a date value.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

WEEK(<dDate>) à nWeek

Parameters

<dDate>  A date or timestamp value

Return Values

WEEK() returns a number in the range of 1 to 53 as an integer numeric value.  If the date argument is empty, WEEK() returns zero.

Remarks

WEEK() is a date conversion function used to convert a date value to the week number and can be used in various date calculations.

See Also

[ISOWEEK()](master_isoweek.htm)

[YEAR()](master_year.htm)

[QUARTER()](master_quarter.htm)

[MONTH()](master_month.htm)

[DAY()](master_day.htm)

[HOUR()](master_hour.htm)

[MINUTE()](master_minute.htm)

[SECOND()](master_second.htm)

[FRAC\_SECOND()](master_frac_second.htm)

[EXTRACT()](master_extract.htm)