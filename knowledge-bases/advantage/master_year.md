YEAR()




Advantage Database Server 12  

YEAR()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| YEAR()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - YEAR() Advantage Concepts master\_Year Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| YEAR()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that converts a date value to the year as a numeric value.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

YEAR(<dDate>) à nYear

Parameters

<dDate> The date or timestamp value

Return Values

YEAR() returns the year of the specified date value including the century digits as a four-digit numeric value. The value returned is not affected by the current date format. Specifying a null date from a DBF table (CTOD("")) returns zero. Specifying a null date from an ADT table returns NULL.

Remarks

YEAR() is a date conversion function that converts a date value to a numeric year value. Use it in calculations for documents such as periodic reports.

YEAR() is a member of a group of functions that return components of a date value as numeric values. The group includes DAY() and MONTH() which return the day and month values as numeric values.

See Also

[QUARTER()](master_quarter.htm)

[MONTH()](master_month.htm)

[WEEK()](master_week.htm)

[DAY()](master_day.htm)

[HOUR()](master_hour.htm)

[MINUTE()](master_minute.htm)

[SECOND()](master_second.htm)

[FRAC\_SECOND()](master_frac_second.htm)

[EXTRACT()](master_extract.htm)