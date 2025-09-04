NumCachedCursors




Advantage Database Server 12  

TAdsSettings.NumCachedCursors

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsSettings.NumCachedCursors  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsSettings.NumCachedCursors Advantage TDataSet Descendant ade\_Numcachedcursors Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsSettings.NumCachedCursors  Advantage TDataSet Descendant |  |  |  |  |

[TAdsSettings](ade_tadssettings_7.htm)

Provides caching of open cursors.

Syntax

property NumCachedCursors: ShortInteger;

Description

Advantage allows cursor closes to be cached in order for subsequent SELECTS to occur more quickly. A call to TAdsQuery.Close with the cursor cache greater than zero results in the cursor appearing closed to an application, but still open on the Advantage server. A subsequent TAdsQuery.Open or TAdsQuery.Exec call will return very quickly because the server already has the cursor open. However, if the access rights for a statement handle on a cached cursor are different than those it was originally created with, the Advantage Client Engine will close the cursor and reopen it with the changed access rights.

This setting affects all base tables used in queries including queries that result in live (dynamic) cursors and static cursors. For example, the query "SELECT \* FROM table1 WHERE id=5" produces a live cursor. If cursor caching is turned on, then subsequent executions of queries that reference table1 will be faster because table1 will be held open on the server. A query such as "SELECT \* FROM table1, table2 WHERE table1.id=table2.id" produces a static cursor. With cursor caching turned on, both table1 and table2 will be held open by the server. The temporary (static) table produced by the query is not cached open; it is closed and deleted as soon as the cursor is closed.

TAdsSettings.NumCachedCursors is a global setting that affects the behavior of the entire application. The default number of open cursors that are cached is 25.

Note Cursor caching and table caching are separate. See [TAdsSettings.NumCachedTables](ade_numcachedtables.htm) for details about caching open tables.

See Also

[NumCachedTables](ade_numcachedtables.htm)

[AdsCloseSQLStatement](ade_adsclosesqlstatement.htm)

[CloseCachedTables](ade_closecachedtables.htm)