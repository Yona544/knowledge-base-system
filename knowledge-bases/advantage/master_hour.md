HOUR()




Advantage Database Server 12  

HOUR()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| HOUR()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - HOUR() Advantage Concepts Master\_HOUR Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| HOUR()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the hour portion of a time or timestamp value.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

HOUR( <tTime> ) à nHour

Parameters

<tTime>  A time or timestamp value

Return Values

HOUR() returns a number in the range of 0 to 23 as an integer numeric value.  If the time or timestamp argument is empty, HOUR() returns zero.

Remarks

HOUR() is a time conversion function used to return the hour portion of a time or timestamp value.

See Also

[YEAR()](master_year.htm)

[QUARTER()](master_quarter.htm)

[MONTH()](master_month.htm)

[WEEK()](master_week.htm)

[DAY()](master_day.htm)

[MINUTE()](master_minute.htm)

[SECOND()](master_second.htm)

[FRAC\_SECOND()](master_frac_second.htm)

[EXTRACT()](master_extract.htm)