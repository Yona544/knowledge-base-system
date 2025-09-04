AdsCloseTable




Advantage Database Server 12  

AdsCloseTable

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCloseTable  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsCloseTable Advantage Client Engine ace\_Adsclosetable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsCloseTable  Advantage Client Engine |  |  |  |  |

Closes the given table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsCloseTable (ADSHANDLE hTable); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor to close. |

Remarks

AdsCloseTable is used to close an open table and any associated index or memo files. Any locks held on the table are released, and changes are flushed when a table is closed. If the close is cached, however, changes are flushed and implicit locks are released. Explicit locks remain if any are held when the table was closed.

The Advantage Client Engine will NOT disconnect from the server when the last table is closed. Settings specified by [AdsCacheOpenTables](ace_adscacheopentables.htm) will be obeyed.

When using SQL cursors the table handle parameter can be replaced with a cursor handle. In this situation AdsCloseTable will close the cursor and all of its associated memory. After closing a cursor the cursor handle can then be reused in a new call to either AdsExecuteSQL or AdsExecuteSQLDirect.

Note This function is legal in a transaction, but its behavior varies. If the table, memo, and indexes associated with the table were never modified, then the files will be closed. If they were modified in any way, then the files will be cached closed. The file will not actually be closed until the transaction is committed or rolled back.

Example

[Click Here](ace_examples.htm#adsclosetableexample)

See Also

[AdsOpenTable](ace_adsopentable.htm)

[AdsDisconnect](ace_adsdisconnect.htm)

[AdsCloseAllTables](ace_adsclosealltables.htm)

[AdsCacheOpenTables](ace_adscacheopentables.htm)

[AdsExecuteSQL](ace_adsexecutesql.htm)

[AdsExecuteSQLDirect](ace_adsexecutesqldirect.htm)

[AdsCloseCachedTables](ace_adsclosecachedtables.htm)