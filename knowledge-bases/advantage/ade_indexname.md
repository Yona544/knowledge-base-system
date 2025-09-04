IndexName




Advantage Database Server 12  

TAdsQuery.IndexName

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsQuery.IndexName  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsQuery.IndexName Advantage TDataSet Descendant ade\_Indexname Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsQuery.IndexName  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.htm)

With Advantage TDataSet, the IndexName property may be used with TAdsQuery exactly as it is used with TAdsTable. If these properties are left blank, the rowset is ordered as defined by the ORDER BY clause of the SQL statement. However, if other indexes are available, one can be selected as the sequence in which the rows are presented.

If the cursor is a live cursor, any index on the original table is available. If the cursor is static, no indexes exist. In either case, you may use the [AdsCreateIndex](ade_adscreateindex.htm) method to create new index orders.