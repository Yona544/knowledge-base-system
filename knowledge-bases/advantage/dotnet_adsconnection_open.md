AdsConnection.Open




Advantage Database Server 12  

AdsConnection.Open

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConnection.Open  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsConnection.Open Advantage .NET Data Provider dotnet\_Adsconnection\_open Advantage .NET Data Provider > AdsConnection Class > AdsConnection Methods > AdsConnection.Open / Dear Support Staff, |  |
| AdsConnection.Open  Advantage .NET Data Provider |  |  |  |  |

Opens a database connection with the property settings specified by the [ConnectionString](dotnet_adsconnection_connectionstring.htm).

public void Open();

Remarks

This method opens a connection to the database or retrieves an open connection from the [connection pool](dotnet_advantage_net_data_provider_and_connection_pooling.htm) (if pooling is enabled). Otherwise, it establishes a new connection. If pooling is on and the maximum pool size (property "Max Pool Size") is exceeded, an InvalidOperationException will be thrown.

See Also

[ConnectionString](dotnet_adsconnection_connectionstring.htm)

[Close](dotnet_adsconnection_close.htm)