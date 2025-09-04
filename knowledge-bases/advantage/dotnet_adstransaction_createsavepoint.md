AdsTransaction.CreateSavepoint




Advantage Database Server 12  

AdsTransaction.CreateSavepoint

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsTransaction.CreateSavepoint  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsTransaction.CreateSavepoint Advantage .NET Data Provider dotnet\_Adstransaction\_createsavepoint Advantage .NET Data Provider > AdsTransaction Class > AdsTransaction Methods > AdsTransaction.CreateSavepoint / Dear Support Staff, |  |
| AdsTransaction.CreateSavepoint  Advantage .NET Data Provider |  |  |  |  |

Creates a savepoint in the current transaction.

public void CreateSavepoint( string strSavepoint);

Remarks

This function creates a savepoint in the transaction associated with the AdsConnection. If the transaction has already been committed or rolled back, this will throw an InvalidOperationException.

See Also

[AdsTransaction.Commit](dotnet_adstransaction_commit.htm)

[AdsTransaction.Rollback](dotnet_adstransaction_rollback.htm)