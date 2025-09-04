LASTAUTOINC()




Advantage Database Server 12  

LASTAUTOINC()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| LASTAUTOINC()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - LASTAUTOINC() Advantage Concepts master\_lastautoinc Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| LASTAUTOINC()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that retrieves the last autoinc value generated.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

LASTAUTOINC( CONNECTION | STATEMENT ) à nAutoinc

Parameters

|  |  |
| --- | --- |
| CONNECTION | Indicates that the last autoinc value generated for the current connection will be returned. |
| STATEMENT | Indicates that the last autoinc value generated on the current SQL statement handle will be returned. |

Return Value

The last generated autoinc value as specified by the parameter.

Remarks

LASTAUTOINC returns the last used autoinc value from an insert or append statement. If no autoinc value has been updated yet, a NULL value is returned.

Note Triggers that operate on tables with autoinc fields may affect the last autoinc value. SQL script triggers run on their own SQL statement. Therefore, calling LASTAUTOINC( STATEMENT ) inside an SQL script trigger would return the lastautoinc value used by the trigger's SQL statement, not the original SQL statement which caused the trigger to fire. To obtain the original SQL statement's lastautoinc value, use LASTAUTOINC( CONNECTION ) instead.

Example

 

SELECT LASTAUTOINC( STATEMENT ) FROM system.iota;

See Also

[LASTROWID()](master_rowid.htm)

[LASTROWVERSION()](master_lastrowversion.htm)