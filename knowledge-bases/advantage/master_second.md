SECOND()




Advantage Database Server 12  

SECOND()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SECOND()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - SECOND() Advantage Concepts Master\_SECOND Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| SECOND()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the second portion of a time or timestamp value.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

SECOND( <tTime> ) à nSecond

Parameters

<tTime>  A time or timestamp value

Return Values

SECOND() returns a number in the range of 0 to 59 as an integer numeric value.  If the time or timestamp argument is empty, SECOND() returns zero.

Remarks

SECOND() is a time conversion function used to return the second portion of a time or timestamp value.

See Also

[YEAR()](master_year.htm)

[QUARTER()](master_quarter.htm)

[MONTH()](master_month.htm)

[WEEK()](master_week.htm)

[DAY()](master_day.htm)

[HOUR()](master_hour.htm)

[MINUTE()](master_minute.htm)

[FRAC\_SECOND()](master_frac_second.htm)

[EXTRACT()](master_extract.htm)