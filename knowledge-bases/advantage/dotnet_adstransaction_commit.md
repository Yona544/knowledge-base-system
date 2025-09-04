AdsTransaction.Commit




Advantage Database Server 12  

AdsTransaction.Commit

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsTransaction.Commit  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsTransaction.Commit Advantage .NET Data Provider dotnet\_Adstransaction\_commit Advantage .NET Data Provider > AdsTransaction Class > AdsTransaction Methods > AdsTransaction.Commit / Dear Support Staff, |  |
| AdsTransaction.Commit  Advantage .NET Data Provider |  |  |  |  |

Commits the database transaction.

public void Commit();

Remarks

If the transaction is still active, this will commit the transaction running on the associated [AdsConnection](dotnet_adsconnection.htm). If the transaction has already been committed or rolled back, this will throw an InvalidOperationException.

If a connections has [nested transactions](master_nesting_transactions.htm), the nesting level will be decremented, but the work will not be committed. When used in nested transactions, commits of the inner transactions do not commit the data or release locks. Only committing the outer most transaction will commit the work and end the transaction.

See Also

[AdsTransaction.Rollback](dotnet_adstransaction_rollback.htm)