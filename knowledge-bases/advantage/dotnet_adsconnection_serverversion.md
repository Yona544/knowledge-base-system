AdsConnection.ServerVersion




Advantage Database Server 12  

AdsConnection.ServerVersion

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConnection.ServerVersion  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsConnection.ServerVersion Advantage .NET Data Provider dotnet\_Adsconnection\_serverversion Advantage .NET Data Provider > AdsConnection Class > AdsConnection Properties > AdsConnection.ServerVersion / Dear Support Staff, |  |
| AdsConnection.ServerVersion  Advantage .NET Data Provider |  |  |  |  |

Retrieves the version of the Advantage Database Server to which the object is connected.

public string ServerVersion {get;}

Remarks

This property retrieves a string that represents the version of the Advantage server to which the connection is made. The connection must be open in order to retrieve the property. The first time the property is retrieved, it results in a call to the server.