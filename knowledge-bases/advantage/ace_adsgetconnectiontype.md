AdsGetConnectionType




Advantage Database Server 12  

AdsGetConnectionType

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetConnectionType  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetConnectionType Advantage Client Engine ace\_Adsgetconnectiontype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetConnectionType  Advantage Client Engine |  |  |  |  |

Returns the type of Advantage Database Server a connection uses.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetConnectionType (ADSHANDLE hConnect,  UNSIGNED16 \*pusConnectType); |

Parameters

|  |  |
| --- | --- |
| hConnect (I) | Connection handle |
| pucConnectType (O) | Type of Advantage Server that connection uses, either ADS\_REMOTE\_SERVER, ADS\_AIS\_SERVER, or ADS\_LOCAL\_SERVER |

Remarks

If AdsGetConnectionType returns ADS\_AIS\_SERVER, the connection is using an Advantage Internet Server.

A return value of ADS\_REMOTE\_SERVER indicates the Advantage Database Server for Windows or the Advantage Database Server for Linux is in use.

ADS\_LOCAL\_SERVER indicates the [Advantage Local Server](master_advantage_local_server.htm) is being used by this connection. It is possible to have connections to each type of Advantage server in one application.

Example

None.

See Also

[AdsConnect](ace_adsconnect.htm)

[AdsGetTableConnection](ace_adsgettableconnection.htm)

[AdsIsServerLoaded](ace_adsisserverloaded.htm)