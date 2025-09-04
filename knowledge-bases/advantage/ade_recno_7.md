RecNo




Advantage Database Server 12  

TAdsTable.RecNo

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.RecNo  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.RecNo Advantage TDataSet Descendant ade\_Recno\_7 Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.RecNo  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.htm)

Indicates the current record in the dataset.

Syntax

property RecNo: Longint;

Description

Examine RecNo to determine the record number of the current record in the dataset. Applications might use this property with RecordCount to iterate through all the records in a dataset, though typically record iteration is handled with calls to First, Last, MoveBy, Next, and Prior.

Note By default RecNo will not return the sequential (logical) record number if an index or filter is set. This can be turned on using the [Sequenced](ade_sequenced.htm) property.

 

Note Records deleted inside of a transaction that has not yet been committed will still be included in a record count.

See Also

[SequencedLevel](ade_sequencedlevel.htm)