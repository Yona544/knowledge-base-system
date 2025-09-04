BeginTransaction




Advantage Database Server 12  

TAdsConnection.BeginTransaction

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.BeginTransaction  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.BeginTransaction Advantage TDataSet Descendant ade\_Begintransaction Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.BeginTransaction  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Begins a transaction for the current connection.

Syntax

procedure BeginTransaction;

Description

Call this function to begin a transaction for the current connection. This function provides the ability to rollback or commit database updates, inserts, and deletes made during the transaction. Transactions can be nested by calling BeginTransaction inside of an existing transaction.

This method is ignored if the connection is using [Advantage Local Server](master_advantage_local_server.htm). See [Advantage Transaction Processing](master_transaction_processing_system.htm) for more information.

See Also

[Nesting Transactions](master_nesting_transactions.htm)

[Commit](ade_commit.htm)

[Rollback](ade_rollback.htm)