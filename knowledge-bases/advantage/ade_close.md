Close




Advantage Database Server 12  

TAdsQuery.Close

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsQuery.Close  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsQuery.Close Advantage TDataSet Descendant ade\_Close Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsQuery.Close  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.htm)

Closes the dataset.

Syntax

procedure Close;

Description

The close method changes the datasets active property to False. This method is identical to the Delphi TQuery method, except for performance reasons the tables involved in the query are cache-closed, and remain open on the server for the life of the query statement, or until the [AdsCloseSQLStatement](ade_adsclosesqlstatement.htm) method is called.

Note If the TAdsSettings.NumCachedCursors property is set to zero (not recommended), then cursors will not be cache-closed.

See Also

[NumCachedCursors](ade_numcachedcursors.htm)

[NumCachedTables](ade_numcachedtables.htm)

[CloseCachedTables](ade_closecachedtables.htm)