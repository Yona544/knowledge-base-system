AdsConnection.CloseCachedTables




Advantage Database Server 12  

AdsConnection.CloseCachedTables

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConnection.CloseCachedTables  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsConnection.CloseCachedTables Advantage .NET Data Provider dotnet\_Adsconnection\_closecachedtables Advantage .NET Data Provider > AdsConnection Class > AdsConnection Methods > AdsConnection.CloseCachedTables / Dear Support Staff, |  |
| AdsConnection.CloseCachedTables  Advantage .NET Data Provider |  |  |  |  |

Closes all cached tables on an open connection.

public void CloseCachedTables();

Remarks

CloseCachedTables can be used to close all cached tables on a given connection. All cached closed tables on the client will be closed, as well as all cache closed tables on the server that might have been used when executing SQL statements.

This API can be useful if you know another application (or some other instance of the same application) will require exclusive access to a table that has been used by the existing application, or if you want tables used by some server-side functionality (like an extended procedure, or a trigger) to be available for exclusive use by the client at some later time.

Note The AdsConnection must be open when calling CloseCachedTables.

 

Note Closing an AdsConnection may not actually close the connection to the server due to connection pooling, so cached tables may still be open. For details on connection pooling, see [Advantage .NET Data Provider and Connection Pooling.](dotnet_advantage_net_data_provider_and_connection_pooling.htm)

See Also

[ConnectionString](dotnet_adsconnection_connectionstring.htm)