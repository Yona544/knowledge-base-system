EXTRACT()




Advantage Database Server 12  

EXTRACT()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| EXTRACT()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - EXTRACT() Advantage Concepts master\_extract Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| EXTRACT()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that retrieves one part of a timestamp value.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

EXTRACT( time-value FROM <timestamp> ) à nValue

Parameters

|  |  |
| --- | --- |
| time-value | Specifies the desired portion of the timestamp. It can be YEAR, MONTH, DAY, HOUR, MINUTE, SECOND, or FRAC\_SECOND. |
| <timestamp> | The timestamp value to extract the value from. |

Return Value

An integer value representing the specified portion of the timestamp.

Remarks

Extract year, month, day, hour, minute, or second from TIMESTAMP.

See Also

[CREATETIMESTAMP()](master_createtimestamp.htm)