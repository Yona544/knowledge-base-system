IndexFiles




Advantage Database Server 12  

TAdsTable.IndexFiles

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.IndexFiles  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.IndexFiles Advantage TDataSet Descendant ade\_Indexfiles Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.IndexFiles  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.htm)

Specifies one or more ADI, CDX, IDX, or NTX index, depending on table type, to be opened with the table.

Syntax

property IndexFiles: TStringList;

Description

Use IndexFiles to specify index files to make available for the table. An index file can contain multiple index orders. Each index order in an index file becomes available as a selection for the IndexName property which specifies the actual index to use at any given time.

When index files are added to the list of available indexes, the table component opens them. Insertions and modifications made to the table are maintained in the index files. When files are removed from the list, the table component closes them and they are no longer maintained.

Note At design time, use the Object Inspector to add or remove index file names for the IndexFiles property. At runtime you can add index file names to the property through the Add method of the TStringList, or delete index file names through the Delete method of the TStringList.