AdsTransaction.Connection




Advantage Database Server 12  

AdsTransaction.Connection

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsTransaction.Connection  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsTransaction.Connection Advantage .NET Data Provider dotnet\_Adstransaction\_connection Advantage .NET Data Provider > AdsTransaction Class > AdsTransaction Properties > AdsTransaction.Connection / Dear Support Staff, |  |
| AdsTransaction.Connection  Advantage .NET Data Provider |  |  |  |  |

Retrieves the AdsConnection associated with the transaction.

public AdsConnection Connection {get;}

Remarks

The Advantage .NET Data Provider stores a reference to the AdsConnection object that began the transaction in the AdsTransaction object. This property can be used by an application to retrieve that connection. This may be useful for applications that have multiple connections active at a time.

See Also

[AdsConnection](dotnet_adsconnection.htm)