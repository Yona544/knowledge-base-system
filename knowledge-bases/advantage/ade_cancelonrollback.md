CancelOnRollback




Advantage Database Server 12  

TAdsConnection.CancelOnRollback

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.CancelOnRollback  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.CancelOnRollback Advantage TDataSet Descendant ade\_Cancelonrollback Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.CancelOnRollback  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Controls dataset behavior when a [Rollback](ade_rollback.htm) operation is performed.

Syntax

property CancelOnRollback : boolean;

Description

CancelOnRollback is TRUE by default. This property controls the behavior of the Rollback method. If TRUE, when a Rollback is performed all datasets attached to the connection will cancel any pending updates and return to a browse state. If FALSE, the transaction will be rolled back, but datasets attached to the connection will remain in the state they were in before the rollback operation.

See Also

[BeginTransaction](ade_begintransaction.htm)

[Rollback](ade_rollback.htm)