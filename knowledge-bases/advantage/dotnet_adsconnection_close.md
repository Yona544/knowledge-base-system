AdsConnection.Close




Advantage Database Server 12  

AdsConnection.Close

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConnection.Close  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsConnection.Close Advantage .NET Data Provider dotnet\_Adsconnection\_close Advantage .NET Data Provider > AdsConnection Class > AdsConnection Methods > AdsConnection.Close / Dear Support Staff, |  |
| AdsConnection.Close  Advantage .NET Data Provider |  |  |  |  |

Closes the connection to the database.

public void Close();

Remarks

The Close method rolls back any pending transactions. It then returns the connection to the [connection pool](dotnet_advantage_net_data_provider_and_connection_pooling.htm), or closes the connection if connection pooling is disabled (pooling=false).

An application can call Close more than one time. No exception is generated.

See Also

[AdsConnection.Open](dotnet_adsconnection_open.htm)

[AdsConnection.ConnectionString](dotnet_adsconnection_connectionstring.htm)