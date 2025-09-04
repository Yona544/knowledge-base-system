DATE()




Advantage Database Server 12  

DATE(), CURDATE()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DATE(), CURDATE()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - DATE(), CURDATE() Advantage Concepts master\_Date Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| DATE(), CURDATE()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the system date as a date value.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

DATE() à dSystem

CURDATE() à dSystem           (SQL Only)

CURRENT\_DATE() à dSystem       (SQL Only)

 

Return Values

DATE() returns the system date as a date value.

Remarks

DATE() is a date function that provides a means of initializing memory variables to the current date, comparing other date values to the current date, and performing date arithmetic relative to the current date.

The display format for dates is controlled by the function to set the date format. The default format is mm/dd/yy in navigational usage.  In SQL usage, the standard format is yyyy-mm-dd.

See Also

[CTOD()](master_ctod.htm)

[DTOC()](master_dtoc.htm)

[DTOS()](master_dtos.htm)

[NOW()](master_now.htm)

[STOD()](master_stod.htm)

[STOTS()](master_stots.htm)

[TSTOD()](master_tstod.htm)

Advantage TDataSet Descendant

[TAdsSettings.DateFormat](ade_dateformat.htm)

Advantage Client Engine API

[AdsSetDateFormat](ace_adssetdateformat.htm)