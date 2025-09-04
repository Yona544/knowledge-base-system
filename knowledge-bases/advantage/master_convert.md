CONVERT()




Advantage Database Server 12  

CONVERT()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CONVERT()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - CONVERT() Advantage Concepts master\_convert Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| CONVERT()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that converts a value from one type to another.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

CONVERT( <expr>, data-type ) à result

Parameters

|  |  |
| --- | --- |
| <expr> | The value to convert |
| data-type | SQL\_BINARY, SQL\_VARBINARY, SQL\_BIT (logical), SQL\_LONGVARCHAR, SQL\_VARCHAR, SQL\_CHAR, SQL\_WLONGVARCHAR, SQL\_WVARCHAR, SQL\_WCHAR, SQL\_DATE, SQL\_DOUBLE, SQL\_INTEGER, SQL\_NUMERIC, SQL\_TIME, SQL\_TIMESTAMP, or SQL\_MONEY. |

Return Value

This function returns <expr> convert to a value of the specified data type.

See Also

[CAST()](master_cast.htm)

[STR()](master_str.htm)

[VAL()](master_val.htm)