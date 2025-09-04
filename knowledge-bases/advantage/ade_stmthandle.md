StmtHandle




Advantage Database Server 12  

TAdsStoredProc.StmtHandle

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsStoredProc.StmtHandle  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsStoredProc.StmtHandle Advantage TDataSet Descendant ade\_Stmthandle Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsStoredProc.StmtHandle  Advantage TDataSet Descendant |  |  |  |  |

[TAdsStoredProc](ade_tadsstoredproc.htm)

Advantage Client Engine (ACE) statement handle for the stored procedure.

Syntax

property StmtHandle: ADSHANDLE;

Description

Retrieve StmtHandle if an application makes a direct call to the Advantage Client Engine, bypassing the methods of TAdsStoredProc. Some API calls require a statement handle as a parameter. Under all other circumstances an application does not need to access this property.