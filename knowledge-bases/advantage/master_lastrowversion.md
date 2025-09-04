LASTROWVERSION()




Advantage Database Server 12  

LASTROWVERSION()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| LASTROWVERSION()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - LASTROWVERSION() Advantage Concepts master\_lastrowversion Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| LASTROWVERSION()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that retrieves the ROWVERSION of the most recent table update.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

LASTROWVERSION() à iRowversion

Parameters

|  |  |
| --- | --- |
| None |  |

Return Value

A ROWVERSION value (a 64-bit integer).

Remarks

Returns the ROWVERSION from the most recent update of a table having a ROWVERSION field for the current statement handle.

See Also

[LASTAUTOINC()](master_lastautoinc.htm)

[LASTROWID()](master_lastrowid.htm)