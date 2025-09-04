AdsZapTable




Advantage Database Server 12  

TAdsTable.AdsZapTable

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsZapTable  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsZapTable Advantage TDataSet Descendant ade\_Adszaptable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsZapTable  Advantage TDataSet Descendant |  |  |  |  |

Removes all records from the table and rebuilds indexes associated with the table.

Syntax

procedure AdsZapTable;

Description

AdsZapTable will remove all records from the table; then the Advantage Client Engine will reindex the table. The indexes must be opened during the empty or they will become invalid. This operation requires exclusive access to the table, which is specified during the open.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsZapTable;

See Also

[AdsPackTable](ade_adspacktable.htm)