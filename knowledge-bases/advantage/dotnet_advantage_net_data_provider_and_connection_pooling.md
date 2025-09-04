Advantage .NET Data Provider and Connection Pooling




Advantage Database Server 12  

Advantage .NET Data Provider and Connection Pooling

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage .NET Data Provider and Connection Pooling  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - Advantage .NET Data Provider and Connection Pooling Advantage .NET Data Provider dotnet\_Advantage\_net\_data\_provider\_and\_connection\_pooling Advantage .NET Data Provider > Developing .NET Applications > Advantage .NET Data Provider and Connection Pooling / Dear Support Staff, |  |
| Advantage .NET Data Provider and Connection Pooling  Advantage .NET Data Provider |  |  |  |  |

By default, the Advantage .NET Data Provider supports connection pooling. This can be controlled through the pooling property in [AdsConnection.ConnectionString](dotnet_adsconnection_connectionstring.htm). Connection pooling can provide better performance in situations where an application must connect, perform some sequence of actions, and then disconnect on a repeated basis. The common example of this is a web application.

With connection pooling turned on (pooling=true), the Advantage .NET Data Provider will get a free connection from the pool if one is available. It maintains a separate pool for each unique connection string used by the application. If no free connection is available, Advantage .NET Data Provider will create a new connection. When connections are released ([AdsConnection.Close](dotnet_adsconnection_close.htm)), they are returned to the connection pool.

With connection pooling turned off (pooling=false), each connect ([AdsConnection.Open](dotnet_adsconnection_open.htm)) and disconnect ([AdsConnection.Close](dotnet_adsconnection_close.htm)) request results in acquiring and releasing a physical connection to Advantage Database Server or Advantage Local Server.

If it is necessary to physically release all free connections to the server, your application can call [AdsConnection.FlushConnectionPool()](dotnet_adsconnection_flushconnectionpool_.htm).

You can control the size of pools and lifetime of individual connections through other [AdsConnection.ConnectionString](dotnet_adsconnection_connectionstring.htm) properties. The property "Max Pool Size" controls the upper limit for individual pools for a given connection string. The property "Min Pool Size" specifies a lower limit for the pool; the first connection for a given pool will cause the Advantage .NET Data Provider to acquire the minimum number of physical connections. The property "Connection Lifetime" controls the amount of time a free connection is allowed to remain open.