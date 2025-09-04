AdsDisconnect




Advantage Database Server 12  

AdsDisconnect

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDisconnect  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDisconnect Advantage Client Engine ace\_Adsdisconnect Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDisconnect  Advantage Client Engine |  |  |  |  |

Disconnects the connection associated with the given connection handle

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsDisconnect (ADSHANDLE hConnect); |

Parameters

|  |  |
| --- | --- |
| hConnect (I) | Handle of server to disconnect. |

Remarks

AdsDisconnect is used to disconnect a connection from the specified server. If tables are currently opened, all data is flushed, locks are released, and open tables are closed before the disconnect occurs.

If zero is passed as the connection handle, all connections on the server associated with the user will be disconnected.

If AdsDisconnect is called on a connection with a transaction active, the transaction will be rolled back.

Example

[Click Here](ace_examples.htm#adsdisconnectexample)

See Also

[AdsConnect](ace_adsconnect.htm)

[AdsOpenTable](ace_adsopentable.htm)