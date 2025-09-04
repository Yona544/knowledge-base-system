TIMESTAMPADD()




Advantage Database Server 12  

TIMESTAMPADD()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TIMESTAMPADD()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - TIMESTAMPADD() Advantage Concepts master\_timestampadd Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TIMESTAMPADD()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that adds an interval to a timestamp value.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

TIMESTAMPADD( interval, <nValue>, <timestamp> ) à timestamp

Parameters

|  |  |
| --- | --- |
| interval | SQL\_TSI\_FRAC\_SECOND, SQL\_TSI\_SECOND, SQL\_TSI\_MINUTE, SQL\_TSI\_HOUR, SQL\_TSI\_DAY, SQL\_TSI\_WEEK, SQL\_TSI\_MONTH, SQL\_TSI\_QUARTER, SQL\_TSI\_YEAR |
| <nValue> | The value to add to <timestamp> |
| <timestamp> | The original timestamp to add to |

Return Value

<timestamp> plus <nValue> intervals

See Also

[TIMESTAMPDIFF()](master_timestampdiff.htm)