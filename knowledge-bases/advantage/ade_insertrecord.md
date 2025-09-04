InsertRecord




Advantage Database Server 12  

TAdsTable/TAdsQuery.InsertRecord

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.InsertRecord  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.InsertRecord Advantage TDataSet Descendant ade\_Insertrecord Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.InsertRecord  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.htm) [TAdsQuery](ade_tadsquery.htm)

Appends a new, populated record to the dataset and posts it to the table.

Syntax

procedure InsertRecord(const Values: array of const);

Description

Call InsertRecord to create a new, empty record in the dataset, populate it with the field values in Values, and post the values to the table.

The newly appended record becomes the current record.

Note Due to the way Xbase works, the Insert is identical to an AppendRecord with DBF tables.