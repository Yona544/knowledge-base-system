AdsConnection.ServerType




Advantage Database Server 12  

AdsConnection.ServerType

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConnection.ServerType  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsConnection.ServerType Advantage .NET Data Provider dotnet\_Adsconnection\_servertype Advantage .NET Data Provider > AdsConnection Class > AdsConnection Properties > AdsConnection.ServerType / Dear Support Staff, |  |
| AdsConnection.ServerType  Advantage .NET Data Provider |  |  |  |  |

Returns the type of Advantage Database Server a connection uses.

public string ServerType{ get; }

Remarks

ServerType returns the type of connection being used as a string. Values returned include:

|  |  |
| --- | --- |
| "REMOTE" | The Advantage Database Server for Windows or the Advantage Database Server for Linux is in use. |
| "LOCAL" | The Advantage Local Server is being used by this connection. |
| "AIS" | The connection is using an Advantage Internet Server. |

It is possible to have connections to each type of Advantage server in one application. If the connection is not open, ServerType will return a string based on the ServerType value in the ConnectionString.

See Also

[ConnectionString](dotnet_adsconnection_connectionstring.htm)