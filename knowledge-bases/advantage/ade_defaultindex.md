DefaultIndex




Advantage Database Server 12  

DefaultIndex

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DefaultIndex  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - DefaultIndex Advantage TDataSet Descendant ade\_Defaultindex Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| DefaultIndex  Advantage TDataSet Descendant |  |  |  |  |

The data dictionary can store a default index for each table. The default index does not have to be the primary key, it can be any existing index. When new table objects are created (in Delphi, OLE DB, etc.) they will automatically be configured to use the default index from the data dictionary. If the default index is changed in the dictionary at a later time, all tables will automatically begin using the new default index.

For optimized performance, the default index is initially not set to reduce unneccessary index page reads.