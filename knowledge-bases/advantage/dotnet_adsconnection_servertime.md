AdsConnection.ServerTime




Advantage Database Server 12  

AdsConnection.ServerTime

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConnection.ServerTime  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsConnection.ServerTime Advantage .NET Data Provider dotnet\_Adsconnection\_servertime Advantage .NET Data Provider > AdsConnection Class > AdsConnection Properties > AdsConnection.ServerTime / Dear Support Staff, |  |
| AdsConnection.ServerTime  Advantage .NET Data Provider |  |  |  |  |

Gets the current server time on an open connection.

public DateTime ServerTime {get;}

Remarks

Retrieves the current time and date from the server via the Advantage Database Server. ServerTime is useful if the Advantage client application is running at a site that is in a different time zone than where the data is located and is being accessed by the Advantage Database Server. When Advantage is used in a WAN environment or is being used with the Advantage Internet Server, the Advantage client and Advantage server will often be located in different time zones. This API allows time, date, and timestamp fields to be populated with a consistent date and time, that is, the date and time of the server location.

Note The AdsConnection must be open when getting ServerTime.