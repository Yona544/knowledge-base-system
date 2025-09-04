IFNULL()




Advantage Database Server 12  

IFNULL()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IFNULL()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - IFNULL() Advantage Concepts master\_ifnull Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| IFNULL()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns a given value or an alternative if the first is null.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

IFNULL( <expr>, <value> ) à result

Parameters

|  |  |
| --- | --- |
| <expr> | An expression or value |
| <value> | The alternate value to return if <expr> is null |

Return Value

This returns either <expr> or <value>

Remarks

If <expr> is NULL, then <value> is returned. Otherwise <expr> is returned.

See Also

[COALESCE()](master_coalesce.htm)