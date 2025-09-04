AdsConnection.Database




Advantage Database Server 12  

AdsConnection.Database

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConnection.Database  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsConnection.Database Advantage .NET Data Provider dotnet\_Adsconnection\_database Advantage .NET Data Provider > AdsConnection Class > AdsConnection Properties > AdsConnection.Database / Dear Support Staff, |  |
| AdsConnection.Database  Advantage .NET Data Provider |  |  |  |  |

Gets the name of the database that the connection object represents.

public string Database {get;}

Remarks

Gets the name of the database that the connection object represents. If the Initial Catalog property was provided in the [AdsConnection.ConnectionString](dotnet_adsconnection_connectionstring.htm), it will be returned. Otherwise, it will return the full connect path. An empty string is returned if no connection path information is available.