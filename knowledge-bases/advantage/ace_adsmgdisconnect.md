AdsMgDisconnect




Advantage Database Server 12  

AdsMgDisconnect

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsMgDisconnect  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsMgDisconnect Advantage Client Engine ace\_Adsmgdisconnect Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsMgDisconnect  Advantage Client Engine |  |  |  |  |

Disconnects the management API connection from the given server

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsMgDisconnect (ADSHANDLE hMgmtConnect); |

Parameters

|  |  |
| --- | --- |
| hMgmtConnect (I) | Handle of management API connection. |

Remarks

AdsMgDisconnect currently is stubbed to call [AdsDisconnect](ace_adsdisconnect.htm). It is recommended you use AdsMgDisconnect to disconnect the management API connection. A future release of the Advantage Client Engine may not support using a standard connection handle in place of a management API connection handle.

In a future release, AdsMgDisconnect may be used to disconnect the management API from the specified server.

Example

[Click Here](ace_advantage_management_api_examples.htm#adsmgdisconnect_example)

See Also

[AdsMgConnect](ace_adsmgconnect.htm)

[AdsMgDisconnect](ace_adsmgdisconnect.htm)

[AdsConnect](ace_adsconnect.htm)