AdsConnection.IsDictionaryConn




Advantage Database Server 12  

AdsConnection.IsDictionaryConn

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConnection.IsDictionaryConn  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsConnection.IsDictionaryConn Advantage .NET Data Provider dotnet\_Adsconnection\_isdictionaryconn Advantage .NET Data Provider > AdsConnection Class > AdsConnection Properties > AdsConnection.IsDictionaryConn / Dear Support Staff, |  |
| AdsConnection.IsDictionaryConn  Advantage .NET Data Provider |  |  |  |  |

Returns whether an open connection is an Advantage Data Dictionary connection.

public bool IsDictionaryConn{ get; }

Remarks

IsDictionaryConn checks an open connection and returns true if the connection is a data dictionary connection (connection types ADS\_DATABASE\_CONNECTION or ADS\_SYS\_ADMIN\_CONNECTION). Otherwise false is returned.

Note If the connection is not open, calling IsDictionaryConn will cause an exception.