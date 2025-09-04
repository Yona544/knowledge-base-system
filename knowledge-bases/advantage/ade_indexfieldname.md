IndexFieldName




Advantage Database Server 12  

TAdsQuery.IndexFieldName

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsQuery.IndexFieldName  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsQuery.IndexFieldName Advantage TDataSet Descendant ade\_Indexfieldname Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsQuery.IndexFieldName  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.htm)

With Advantage TDataSet, the IndexFieldName property may be used with TAdsQuery exactly as it is used with TAdsTable. If these properties are left blank, the rowset is ordered as defined by the ORDER BY clause of the SQL statement. However, if other indexes are available, one can be selected as the sequence in which the rows are presented.

If the cursor is a live cursor, any index on the original table is available. If the cursor is a static cursor, the availability of indexes is not guaranteed. When generating static cursors, Advantage may optimize the cursor generation in a variety of ways. Often the SteamlineSQL engine can order a query without using an index. If this is the case, and you have set the IndexFieldName property, an exception will be generated.

In either case, you may use the [AdsCreateIndex](ade_adscreateindex.htm) method to create new index orders.