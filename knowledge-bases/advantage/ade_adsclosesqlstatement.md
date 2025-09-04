AdsCloseSQLStatement




Advantage Database Server 12  

TAdsQuery.AdsCloseSQLStatement

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsQuery.AdsCloseSQLStatement  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsQuery.AdsCloseSQLStatement Advantage TDataSet Descendant ade\_Adsclosesqlstatement Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsQuery.AdsCloseSQLStatement  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.htm)

Completely closes all files associated with any TAdsQuery instance.

Syntax

procedure TAdsQuery.AdsCloseSQLStatement();

Description

When an SQL statement is executed, the Advantage Client Engine and the Advantage Database Server open any tables and indexes necessary to produce the rowset. Even if the TAdsQuery.Close method is called, these files remain opened for performance reasons. After the Close method is called, the CloseSQLStatement method will close all files and destroy all pertinent information within the Advantage Database Server and the Advantage Client Engine.

Note The [TAdsSettings.NumCachedCursors](ade_numcachedcursors.htm) property must be set to zero in conjunction with the AdsCloseSQLStatement. Use these functions only when necessary due to performance loss. To close all cached tables without modifying NumCachedCursors, see the [TAdsConnection.CloseCachedTables](ade_closecachedtables.htm) method.