AdsFactory.CreateConnection




Advantage Database Server 12  

AdsFactory.CreateConnection

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsFactory.CreateConnection  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsFactory.CreateConnection Advantage .NET Data Provider dotnet\_Adsfactory\_createconnection Advantage .NET Data Provider > AdsFactory Class > AdsFactory Methods > AdsFactory.CreateConnection / Dear Support Staff, |  |
| AdsFactory.CreateConnection  Advantage .NET Data Provider |  |  |  |  |

Returns an AdsConnection object as a strongly typed DbConnection instance.

public DbConnection CreateConnection();

Example

AdsFactory adsFact = AdsFactory.Instance;

DbConnection adsConn = adsFact.CreateConnection();

See Also

[AdsConnection](dotnet_adsconnection.htm)