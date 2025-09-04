DAY()




Advantage Database Server 12  

DAY()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DAY()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - DAY() Advantage Concepts master\_Day Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| DAY()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the day of the month as a numeric value.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

DAY(<dDate>) à nDay

DAYOFMONTH( <dDate> ) à nDay       (SQL Only)

Parameters

<dDate>  A date or timestamp value.

Return Values

DAY() returns a number in the range of zero to 31 as an integer numeric value. If the month is February, leap years are considered. If the date argument is February 29 and the year is not a leap year, DAY() returns zero. If the date argument is empty, DAY() returns zero.

Remarks

DAY() is a date conversion function used to convert a date value to the day of a month and can be used in various date calculations.

See Also

[YEAR()](master_year.htm)

[QUARTER()](master_quarter.htm)

[MONTH()](master_month.htm)

[WEEK()](master_week.htm)

[HOUR()](master_hour.htm)

[MINUTE()](master_minute.htm)

[SECOND()](master_second.htm)

[FRAC\_SECOND()](master_frac_second.htm)

[EXTRACT()](master_extract.htm)