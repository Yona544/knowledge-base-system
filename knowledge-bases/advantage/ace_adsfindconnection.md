AdsFindConnection




Advantage Database Server 12  

AdsFindConnection

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsFindConnection  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsFindConnection Advantage Client Engine ace\_Adsfindconnection Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsFindConnection  Advantage Client Engine |  |  |  |  |

Finds a connection handle associated with the server name

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsFindConnection (UNSIGNED8 \*pucServerName,  ADSHANDLE \*phConnect); |

Parameters

|  |  |
| --- | --- |
| pucServerName (I) | Server name. |
| phConnect (O) | Return the connection handle if connection found. |

Remarks

AdsFindConnection will find the connection handle related to a server. The connection handle can be used in calls to [AdsOpenTable](ace_adsopentable.htm) , [AdsCreateTable](ace_adscreatetable.htm) , and the transaction functions such as [AdsBeginTransaction](ace_adsbegintransaction.htm).

Example

[Click Here](ace_examples.htm#adsfindconnection_example)

See Also

[AdsConnect](ace_adsconnect.htm)

[AdsDisconnect](ace_adsdisconnect.htm)

[AdsOpenTable](ace_adsopentable.htm)

[AdsFindConnection25](ace_adsfindconnection25.htm)