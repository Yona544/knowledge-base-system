LASTROWID()




Advantage Database Server 12  

LASTROWID()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| LASTROWID()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - LASTROWID() Advantage Concepts master\_lastrowid Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| LASTROWID()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that retrieves the ROWID of the last row inserted into the table.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

LASTROWID() à cRowid

Parameters

|  |  |
| --- | --- |
| None |  |

Return Value

A [ROWID](master_rowid.htm) value

Remarks

Returns the ROWID of the last row inserted into the table. This value can be used to identify a newly inserted row without prior knowledge of that row's key value, and without requiring the table to have an autoinc column.

See Also

[LASTAUTOINC()](master_lastautoinc.htm)

[LASTROWVERSION()](master_lastrowversion.htm)