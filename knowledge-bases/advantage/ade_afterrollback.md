AfterRollback




Advantage Database Server 12  

TAdsConnection.AfterRollback

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.AfterRollback  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.AfterRollback Advantage TDataSet Descendant ade\_Afterrollback Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.AfterRollback  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

AfterRollback occurs after an application completes a request to rollback modifications to the current transaction.

Syntax

type TNotifyEvent = procedure of object;

 

property AfterRollback: TNotifyEvent;

Description

Write an AfterRollback event handler to take specific action after an application rolls back changes to the current transaction.