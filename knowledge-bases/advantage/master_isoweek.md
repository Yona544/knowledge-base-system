ISOWEEK()




Advantage Database Server 12  

ISOWEEK()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ISOWEEK()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - ISOWEEK() Advantage Concepts Master\_ISOWEEK Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ISOWEEK()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the ISO 8601 week number of a date value.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

ISOWEEK(<dDate>) à nISOWeek

Parameters

<dDate>  The date value to be converted.

Return Values

ISOWEEK() returns a number in the range of 1 to 53 as an integer numeric value.  If the date value is empty, ISOWEEK() returns zero.

Remarks

ISOWEEK() is a date conversion function used to return the ISO 8601 week number of a date value.

See Also

[DAY()](master_day.htm)

[MONTH()](master_month.htm)

[QUARTER()](master_quarter.htm)

[WEEK()](master_week.htm)

[YEAR()](master_year.htm)