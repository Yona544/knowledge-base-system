AdsFindConnection25




Advantage Database Server 12  

AdsFindConnection25

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsFindConnection25  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsFindConnection25 Advantage Client Engine ace\_Adsfindconnection25 Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsFindConnection25  Advantage Client Engine |  |  |  |  |

Finds a connection handle associated with the full path name.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsFindConnection25 (UNSIGNED8 \*pucFullPath,  ADSHANDLE \*phConnect); |

Parameters

|  |  |
| --- | --- |
| pucFullPath (I) | Full path name. |
| phConnect (O) | Return the connection handle if connection found. |

Remarks

AdsFindConnection25 is similar to [AdsFindConnection](ace_adsfindconnection.htm). It will find the connection handle related to a server. The connection handle will be returned only if the path supplied is identical to a path used when creating a previous Advantage server connection. The connection handle can be used in calls to [AdsOpenTable](ace_adsopentable.htm) , [AdsCreateTable](ace_adscreatetable.htm) , and the transaction functions such as [AdsBeginTransaction](ace_adsbegintransaction.htm).

Example

[Click Here](ace_examples.htm#adsfindconnection25_example)

See Also

[AdsConnect](ace_adsconnect.htm)

[AdsDisconnect](ace_adsdisconnect.htm)

[AdsFindConnection](ace_adsfindconnection.htm)

[AdsOpenTable](ace_adsopentable.htm)