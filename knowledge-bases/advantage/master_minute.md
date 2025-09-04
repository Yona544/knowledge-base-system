MINUTE()




Advantage Database Server 12  

MINUTE()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| MINUTE()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - MINUTE() Advantage Concepts Master\_MINUTE Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| MINUTE()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the minute portion of a time or timestamp value.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

MINUTE( <tTime> ) à nMinute

Parameters

<tTime>  A time or timestamp value

Return Values

MINUTE() returns a number in the range of 0 to 59 as an integer numeric value.  If the time or timestamp argument is empty, MINUTE() returns zero.

Remarks

MINUTE() is a time conversion function used to return the minute portion of a time or timestamp value.

See Also

[YEAR()](master_year.htm)

[QUARTER()](master_quarter.htm)

[MONTH()](master_month.htm)

[WEEK()](master_week.htm)

[DAY()](master_day.htm)

[HOUR()](master_hour.htm)

[SECOND()](master_second.htm)

[FRAC\_SECOND()](master_frac_second.htm)

[EXTRACT()](master_extract.htm)