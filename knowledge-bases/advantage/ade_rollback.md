Rollback




Advantage Database Server 12  

TAdsConnection.Rollback

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.Rollback  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.Rollback Advantage TDataSet Descendant ade\_Rollback Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.Rollback  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Aborts all of the database updates, inserts, and deletes sent to the server since the transaction began.

Syntax

procedure Rollback;

procedure Rollback( strSavepoint: string );

 

Description

Call this function to abort the database updates, inserts, and deletes made during the transaction. If a savepoint is specified, the transaction is rolled back to that savepiont. When using [nested transactions](master_nesting_transactions.htm), calling Rollback without a savepoint name rolls back all work to the outermost begin transaction operation and ends the transaction.

This method is ignored if the connection is using Advantage Local Server. See [Advantage Transaction Processing](master_transaction_processing_system.htm) for more information.

See Also

[BeginTransaction](ade_begintransaction.htm)

[Commit](ade_commit.htm)

[CreateSavepoint](ade_createsavepoint.htm)