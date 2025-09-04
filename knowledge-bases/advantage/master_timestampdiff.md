TIMESTAMPDIFF()




Advantage Database Server 12  

TIMESTAMPDIFF()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TIMESTAMPDIFF()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - TIMESTAMPDIFF() Advantage Concepts master\_timestampdiff Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TIMESTAMPDIFF()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that finds the number of specified intervals between two timestamp values.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

TIMESTAMPDIFF( interval, <timestamp1>, <timestamp2> ) à nValue

Parameters

|  |  |
| --- | --- |
| interval | SQL\_TSI\_FRAC\_SECOND, SQL\_TSI\_SECOND, SQL\_TSI\_MINUTE, SQL\_TSI\_HOUR, SQL\_TSI\_DAY, SQL\_TSI\_WEEK, SQL\_TSI\_MONTH, SQL\_TSI\_QUARTER, SQL\_TSI\_YEAR |
| <timestamp1> | The starting timestamp value |
| <timestamp> | The original timestamp to add to |

Return Value

Number of intervals from <timestamp2> - <timestamp1>

Remarks

Returns number of integer intervals based on subtracting <timestamp1> from <timestamp2>.

See Also

[TIMESTAMPADD()](master_timestampadd.htm)