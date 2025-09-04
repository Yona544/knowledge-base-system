Exclusive




Advantage Database Server 12  

TAdsTable.Exclusive

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.Exclusive  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.Exclusive Advantage TDataSet Descendant ade\_Exclusive Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.Exclusive  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.htm)

Enables an application to gain sole access to a DBF table or Advantage proprietary ADT table.

Syntax

property Exclusive: Boolean;

Description

Use Exclusive to prevent other applications from accessing a DBF or ADT table while this application is using it. Before opening the table, set Exclusive to True.

When Exclusive is True, then when the application successfully opens the table, no other application can access it. If the table for which the application has requested exclusive access is already in use by another application, an exception is raised. To handle such exceptions, write an exception handler.

Note The table cannot be opened in the IDE during design time with Exclusive set to True and have the application run with the table open. The solution will be to set the Active property of the table to False and open the table in the application startup.