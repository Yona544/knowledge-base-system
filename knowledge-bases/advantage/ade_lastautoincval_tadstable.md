LastAutoincVal




Advantage Database Server 12  

TAdsTable.LastAutoincVal

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.LastAutoincVal  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.LastAutoincVal Advantage TDataSet Descendant ade\_Lastautoincval\_tadstable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.LastAutoincVal  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.htm)

Indicates the last AutoIncrement field value that was inserted into the table.

Syntax

property LastAutoincVal : Integer;

Description

Use LastAutoincVal after a record has been appended to the table. If the table contains an AutoIncrement field, this property will store the last value inserted into that field. If the table does not contain an AutoIncrement field, or no record has been inserted, then this property will be set to 0. The LastAutoincVal property is read-only.

With TAdsQuery the LastAutoincVal is available immediately after execution of the INSERT statement.

Note This behavior differs from [TAdsQuery.LastAutoincVal](ade_lastautoincval_tadsquery.htm).

 

Note The autoinc value returned is client-specific, and because of concurrent database access, is not guaranteed to be the absolute last autoinc value in the table.