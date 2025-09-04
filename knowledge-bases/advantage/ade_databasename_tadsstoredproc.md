DatabaseName




Advantage Database Server 12  

TAdsStoredProc.DatabaseName

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsStoredProc.DatabaseName  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsStoredProc.DatabaseName Advantage TDataSet Descendant ade\_Databasename\_tadsstoredproc Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsStoredProc.DatabaseName  Advantage TDataSet Descendant |  |  |  |  |

[TAdsStoredProc](ade_tadsstoredproc.htm)

Specifies the name of the TAdsConnection component to associate with this TAdsStoredProc component.

Syntax

property DatabaseName: string;

Description

Use DatabaseName to specify the TAdsConnection component to associate with this TAdsStoredProc component. TAdsStoredProc components can not directly access Advantage alias names or connection paths, they must reference a TAdsConnection component. All Advantage Database Dictionary access is accomplished through a TAdsConnection component. See [Accessing an Advantage Data Dictionary](master_accessing_an_advantage_data_dictionary_with_the_advantage_tdataset_descendant.htm) for more information.

See Also

[GetDatabasePath](ade_getdatabasepath.htm)