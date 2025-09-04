MONTH()




Advantage Database Server 12  

MONTH()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| MONTH()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - MONTH() Advantage Concepts master\_Month Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| MONTH()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that converts a date value to the number of the month.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

MONTH(<dDate>) à nMonth

Parameters

<dDate>  The date or timestamp value

Return Values

MONTH() returns an integer numeric value in the range of zero to 12. Specifying a null date from a DBF table (CTOD("")) returns zero. Specifying a null date from an ADT table returns NULL.

Remarks

MONTH() is a date conversion function that is useful when you require a numeric month value during calculations for such things as periodic reports. MONTH() is a member of a group of functions that return components of a date value as numeric values. The group includes DAY() and YEAR() to return the day and year values as numerics.

See Also

[YEAR()](master_year.htm)

[QUARTER()](master_quarter.htm)

[WEEK()](master_week.htm)

[DAY()](master_day.htm)

[HOUR()](master_hour.htm)

[MINUTE()](master_minute.htm)

[SECOND()](master_second.htm)

[FRAC\_SECOND()](master_frac_second.htm)

[EXTRACT()](master_extract.htm)