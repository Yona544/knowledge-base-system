AdsConnection.ServerName




Advantage Database Server 12  

AdsConnection.ServerName

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConnection.ServerName  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsConnection.ServerName Advantage .NET Data Provider dotnet\_Adsconnection\_servername Advantage .NET Data Provider > AdsConnection Class > AdsConnection Properties > AdsConnection.ServerName / Dear Support Staff, |  |
| AdsConnection.ServerName  Advantage .NET Data Provider |  |  |  |  |

Gets the server name.

public string ServerName {get;}

Remarks

Retrieves the server name associated with a connection. ServerName returns the name of the server on which the connected Advantage server is loaded. The server name will not include any volume or share information. If accessing data on a local drive and using Advantage Local Server, the drive letter is returned.