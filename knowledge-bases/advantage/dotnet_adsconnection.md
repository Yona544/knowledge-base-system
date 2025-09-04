AdsConnection




Advantage Database Server 12  

AdsConnection

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConnection  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsConnection Advantage .NET Data Provider dotnet\_Adsconnection Advantage .NET Data Provider > AdsConnection Class > Overview / Dear Support Staff, |  |
| AdsConnection  Advantage .NET Data Provider |  |  |  |  |

Full name: Advantage.Data.Provider.AdsConnection

Implements: System.Data.IDbConnection

[Constructors](dotnet_adsconnection_constructors.htm)

[Properties](dotnet_adsconnection_properties.htm)

[Methods](dotnet_adsconnection_methods.htm)

[Events](dotnet_adsconnection_events.htm)

The AdsConnection class represents a single connection to Advantage Database Server or Advantage Local Server. It can be used for both [free connections](javascript:hhpopuplink.TextPopup(popid_272466414,FontFace,-1,-1,-1,-1)) and [data dictionary connections](master_advantage_data_dictionary.htm).

Example

The following C# code shows a simple example that creates a new AdsConnection object

AdsConnection conn = new AdsConnection( "data source=c:\\data;" +

"ServerType=remote|local; TableType=ADT" );

conn.Open();