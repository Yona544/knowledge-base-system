AdsConnectionStringBuilder.ConnectionString




Advantage Database Server 12  

AdsConnectionStringBuilder.ConnectionString

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConnectionStringBuilder.ConnectionString  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsConnectionStringBuilder.ConnectionString Advantage .NET Data Provider dotnet\_Adsconnectionstringbuilder\_connectionstring Advantage .NET Data Provider > AdsConnectionStringBuilder Class > AdsConnectionStringBuilder Properties > AdsConnectionStringBuilder.ConnectionString / Dear Support Staff, |  |
| AdsConnectionStringBuilder.ConnectionString  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the connection string.

public string ConnectionString {get; set;}

Remarks

This property can be used to set or retrieve the full connection string. If the individual properties are set, then the full connection string can be retrieved with this property and assigned to an AdsConnection object.

Example

AdsConnectionStringBuilder builder =

new AdsConnectionStringBuilder();

 

builder.DataSource = @"c:\data";

builder.ServerType = "local";

 

AdsConnection conn = new AdsConnection();

conn.ConnectionString = builder.ConnectionString;

conn.Open();

See Also

[AdsConnection.ConnectionString](dotnet_adsconnection_connectionstring.htm)