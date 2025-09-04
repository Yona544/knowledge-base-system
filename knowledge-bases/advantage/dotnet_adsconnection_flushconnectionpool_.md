AdsConnection.FlushConnectionPool()




Advantage Database Server 12  

AdsConnection.FlushConnectionPool()

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConnection.FlushConnectionPool()  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsConnection.FlushConnectionPool() Advantage .NET Data Provider dotnet\_Adsconnection\_flushconnectionpool\_ Advantage .NET Data Provider > AdsConnection Class > AdsConnection Methods > AdsConnection.FlushConnectionPool() / Dear Support Staff, |  |
| AdsConnection.FlushConnectionPool()  Advantage .NET Data Provider |  |  |  |  |

Closes all unused connections in all connection pools.

public void FlushConnectionPool();

Remarks

This method will close all unused connections in all connection pools. Note that the connection pool is application-wide, so this will close all unused connections in the application.

See Also

[AdsConnection.FlushConnectionPool( string )](dotnet_adsconnection_flushconnectionpool_string_.htm)