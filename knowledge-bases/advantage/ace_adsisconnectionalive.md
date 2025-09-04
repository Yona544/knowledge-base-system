AdsIsConnectionAlive




Advantage Database Server 12  

AdsIsConnectionAlive

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsIsConnectionAlive  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsIsConnectionAlive Advantage Client Engine ace\_Adsisconnectionalive Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsIsConnectionAlive  Advantage Client Engine |  |  |  |  |

Returns a flag that indicates if the given connection to Advantage Database Server is still active.

Syntax

UNSIGNED32 AdsIsConnectionAlive ( ADSHANDLE hConnect,

UNSIGNED16 \*pbConnectionIsAlive );

Parameters

|  |  |
| --- | --- |
| hConnect (I) | Connection handle to check. |
| pbConnectionIsAlive (O) | A non-zero value (1) indicates that the connection to the server is still active. A value of zero indicates that the connection has been lost or that the server itself is no longer responding. |

Remarks

AdsIsConnectionAlive can be used by an application to test if a given connection to Advantage Database Server is still usable. If a call to this API returns zero in the pbConnectionIsAlive output parameter, it indicates that the connection has been lost. Reasons for a lost connection include network failure, server failure, Advantage Database Server failure, or cluster node failover. If an application needs to stay connected at all times, it can use this API to test a connection. If the connection is lost, a possible course of action is to close all objects (tables, cursors, SQL statements, and the connection itself) and attempt to reconnect to the server, which may succeed if the server was stopped momentarily or if it is part of a cluster and was moved to another node by the cluster manager.

See Also

[AdsDisconnect](ace_adsdisconnect.htm)

[AdsConnect60](ace_adsconnect60.htm)

[AdsGetLastError](ace_adsgetlasterror.htm)