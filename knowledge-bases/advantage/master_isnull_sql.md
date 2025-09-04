ISNULL() SQL




Advantage Database Server 12  

ISNULL()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ISNULL()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - ISNULL() Advantage Concepts master\_isnull\_sql Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ISNULL()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns a given value or an alternative if the first is null.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No (See remarks) |

Syntax

ISNULL( <expr>, <value> ) à result

Parameters

|  |  |
| --- | --- |
| <expr> | An expression or value |
| <value> | The alternate value to return if <expr> is null |

Return Value

This returns either <expr> or <value>

Remarks

The SQL version of ISNULL is functionally the same as [IFNULL()](master_ifnull.htm).  There is a navigational scalar named [ISNULL()](master_isnull.htm), but it has different functionality.

See Also

[COALESCE()](master_coalesce.htm)

[IFNULL()](master_ifnull.htm)