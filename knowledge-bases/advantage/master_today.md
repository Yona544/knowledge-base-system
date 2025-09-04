TODAY()




Advantage Database Server 12  

TODAY()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TODAY()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - TODAY() Advantage Concepts master\_Today Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TODAY()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the system date as a date value.

|  |  |
| --- | --- |
| Supported in SQL: | No.  See [DATE()](master_date.htm) |
| Supported in Navigational: | Yes |

Syntax

Today() à dSystemDate

Remarks

Today() provides a means of retrieving the current date within the expression, comparing other date values to the current date, and performing date arithmetic relative to the current date.

The display format for dates is controlled by the current date format setting. The default format is mm/dd/yy.

Note Today() is the same as the Date() function in CA-Clipper, but DATE is a reserved word in CA-Visual Objects.

Note Advantage Expression Engine functions can be used in expressions such as record filter expressions and index expressions. They are not necessarily scalars supported within SQL statements. For a list of supported SQL scalar functions, see [Supported Scalar Functions](master_supported_scalar_functions.htm).

Example

These examples show Today() used in various ways:

? Today()         // 09/19/93

? Today() + 30    // 10/19/93

? Today() - 30    // 08/20/93

See Also

[CTOD()](master_ctod.htm)

[DTOC()](master_dtoc.htm)

[DTOS()](master_dtos.htm)

[DATE()](master_date.htm)

Advantage TDataSet Descendant

[TAdsSettings.DateFormat](ade_dateformat.htm)

Advantage Client Engine API

[AdsSetDateFormat](ace_adssetdateformat.htm)