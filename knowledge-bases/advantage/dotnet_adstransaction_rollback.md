AdsTransaction.Rollback




Advantage Database Server 12  

AdsTransaction.Rollback

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsTransaction.Rollback  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsTransaction.Rollback Advantage .NET Data Provider dotnet\_Adstransaction\_rollback Advantage .NET Data Provider > AdsTransaction Class > AdsTransaction Methods > AdsTransaction.Rollback / Dear Support Staff, |  |
| AdsTransaction.Rollback  Advantage .NET Data Provider |  |  |  |  |

Rolls back the database transaction.

public void Rollback();

public void Rollback( string strSavepoint);

Remarks

If the transaction is still active, this will roll back the transaction running on the associated [AdsConnection](dotnet_adsconnection.htm). If the transaction has already been committed or rolled back, this will throw an InvalidOperationException. If a savepoint is specified the transaction will be rolled back to the savepoint.

When using [nested transactions](master_nesting_transactions.htm), calling Rollback without a savepoint name rolls back all work to the outermost begin transaction operation and ends the transaction.

See Also

[AdsTransaction.Commit](dotnet_adstransaction_commit.htm)

[AdsTransaction.CreateSavepoint](dotnet_adstransaction_createsavepoint.htm)