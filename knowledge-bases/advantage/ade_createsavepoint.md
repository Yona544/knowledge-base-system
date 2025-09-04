CreateSavepoint




Advantage Database Server 12  

TAdsConnection.CreateSavepoint

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.CreateSavepoint  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.CreateSavepoint Advantage TDataSet Descendant ade\_Createsavepoint Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.CreateSavepoint  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Creates a savepoint in the current transactions.

Syntax

procedure CreateSavepoint( strSavepoint: string );

Description

Call this function to create a savepoint inside the current transaction. This method is ignored if the connection is using Advantage Local Server. See [Advantage Transaction Processing](master_advantage_transaction_processing_system_overview.htm) for more information.

See Also

[BeginTransaction](ade_begintransaction.htm)

[Commit](ade_commit.htm)

[Rollback](ade_rollback.htm)