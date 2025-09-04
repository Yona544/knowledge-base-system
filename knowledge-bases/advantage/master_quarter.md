QUARTER()




Advantage Database Server 12  

QUARTER()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| QUARTER()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - QUARTER() Advantage Concepts Master\_QUARTER Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| QUARTER()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the quarter of a date value.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

QUARTER(<dDate>) à nQuarter

Parameters

<dDate>  A date or timestamp value

Return Values

QUARTER() returns a number in the range of 1 to 4 as an integer numeric value. If the date argument is empty, QUARTER() returns zero.

Remarks

QUARTER() is a date conversion function used to convert a date value to the quarter number.

See Also

[YEAR()](master_year.htm)

[MONTH()](master_month.htm)

[WEEK()](master_week.htm)

[DAY()](master_day.htm)

[HOUR()](master_hour.htm)

[MINUTE()](master_minute.htm)

[SECOND()](master_second.htm)

[FRAC\_SECOND()](master_frac_second.htm)

[EXTRACT()](master_extract.htm)