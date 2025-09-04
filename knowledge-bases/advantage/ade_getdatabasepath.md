GetDatabasePath




Advantage Database Server 12  

TAdsDataSet.GetDatabasePath

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDataSet.GetDatabasePath  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDataSet.GetDatabasePath Advantage TDataSet Descendant ade\_Getdatabasepath Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDataSet.GetDatabasePath  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.htm) [TAdsQuery](ade_tadsquery.htm) [TAdsStoredProc](ade_tadsstoredproc.htm)

Retrieves the path the TAdsDataSet instance is using.

Syntax

function GetDatabasePath : String;

Description

GetDatabasePath will return the path the TAdsDataSet instance is using, regardless of what method has been used to assign the databasename property.

If the TAdsDataSet instance is using an alias, the alias path will be returned. If the TAdsDataSet is using a simple path in the databasename property, that path will be returned. If the TAdsDataSet instance is using a TAdsConnection, the TAdsConnection path will be returned, etc.

See Also

[DatabaseName](ade_databasename.htm)