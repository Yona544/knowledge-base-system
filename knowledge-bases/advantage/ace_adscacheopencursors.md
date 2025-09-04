AdsCacheOpenCursors




Advantage Database Server 12  

AdsCacheOpenCursors

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCacheOpenCursors  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsCacheOpenCursors Advantage Client Engine ace\_Adscacheopencursors Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsCacheOpenCursors  Advantage Client Engine |  |  |  |  |

Provides caching of open cursors

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsCacheOpenCursors( UNSIGNED16 usOpen ) |

Parameters

|  |  |
| --- | --- |
| usOpen (I) | Number of cursors to cache. |

Remarks

AdsCacheOpenCursors allows cursor closes to be cached in order for subsequent SELECTS to occur faster. A call to [AdsCloseTable](ace_adsclosetable.htm) with the cursor cache greater than zero results in the cursor appearing closed to an application, but still open on the Advantage server. A subsequent [AdsExecuteSQL](ace_adsexecutesql.htm) or [AdsExecuteSQLDirect](ace_adsexecutesqldirect.htm) call will return very quickly because the server already has the cursor open. However, if the access rights for a statement handle on a cached cursor are different than those it was originally created with, the Advantage Client Engine will close the cursor and reopen it with the changed access rights.

This setting affects all base tables used in queries including queries that result in live (dynamic) cursors and static cursors. For example, the query "SELECT \* FROM table1 WHERE id=5" produces a live cursor. If cursor caching is turned on, then subsequent executions of queries that reference table1 will be faster because table1 will be held open on the server. A query such as "SELECT \* FROM table1, table2 WHERE table1.id=table2.id" produces a static cursor. With cursor caching turned on, both table1 and table2 will be held open by the server. The temporary (static) table produced by the query is not cached open; it is closed and deleted as soon as the cursor is closed.

AdsCacheOpenCursors is a global setting that affects the behavior of the entire application. The default number of open cursors that are cached is 25.

Normally, the cached cursors are only fully closed when the connections on which they are opened are disconnected. However, executing an SQL script, an SQL statement that begins with CREATE, DROP or ALTER, or an SQL statement terminated with a semicolon will force the application to close all cache closed cursors. If this is not the desired behavior, the ADS\_NOFLUSH escape clause may be used in the statement or script to instruct the Advantage Client Engine to not close the cache closed cursors. The escape clause must be supplied in the first comment in the statement before any other comments or statement text. Escape clauses supplied in other comments other than the very first one are ignored and treated as normal comments. For example, the following sequence will execute the "DROP TABLE" statement while retaining the existing cache closed cursors :

AdsPrepareSQL( hStmt, "/\* ADS\_NOFLUSH \*/ DROP TABLE table1;" );

AdsExecuteSQL( hStmt, NULL );

 

Note Cursor caching and table caching are separate. See [AdsCacheOpenTables](ace_adscacheopentables.htm) for details about caching open tables.

Example

[Click Here](ace_more_examples.htm#adscacheopencursorsexample)

See Also

[AdsCacheOpenTables](ace_adscacheopentables.htm)

[AdsCloseCachedTables](ace_adsclosecachedtables.htm)