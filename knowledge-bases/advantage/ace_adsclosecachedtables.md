AdsCloseCachedTables




Advantage Database Server 12  

AdsCloseCachedTables

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCloseCachedTables  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsCloseCachedTables Advantage Client Engine ace\_Adsclosecachedtables Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsCloseCachedTables  Advantage Client Engine |  |  |  |  |

Close all cached tables on the given connection

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsCloseCachedTables( ADSHANDLE hConnection ) |

Parameters

|  |  |
| --- | --- |
| hConnection (I) | Handle of the connection to close all cached tables on. |

Remarks

AdsCloseCachedTables can be used to close all cached tables on a given connection. All cached closed tables on the client will be closed, as well as all cache closed tables on the server that might have been used when executing SQL statements.

This API can be useful if you know another application (or some other instance of the same application) will require exclusive access to a table that has been used by the existing application, or if you want tables used by some server-side functionality (like an extended procedure, or a trigger) to be available for exclusive use by the client at some later time.

See Also

[AdsCacheOpenTables](ace_adscacheopentables.htm)

[AdsCacheOpenCursors](ace_adscacheopencursors.htm)

[AdsCloseSQLStatement](ace_adsclosesqlstatement.htm)