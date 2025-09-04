BeforeRollback




Advantage Database Server 12  

TAdsConnection.BeforeRollback

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.BeforeRollback  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.BeforeRollback Advantage TDataSet Descendant ade\_Beforerollback Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.BeforeRollback  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

BeforeRollback occurs before an application makes a request to rollback modifications to the current transaction.

Syntax

type TNotifyEvent = procedure of object;

 

property BeforeRollback: TNotifyEvent;

Description

Write a BeforeRollback event handler to take specific action before an application rolls back changes to the current transaction.