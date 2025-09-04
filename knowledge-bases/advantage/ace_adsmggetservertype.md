AdsMgGetServerType




Advantage Database Server 12  

AdsMgGetServerType

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsMgGetServerType  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsMgGetServerType Advantage Client Engine ace\_Adsmggetservertype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsMgGetServerType  Advantage Client Engine |  |  |  |  |

Returns the Advantage server type of the current management API connection

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsMgGetServerType ( ADSHANDLE hMgmtConnect,  UNSIGNED16 \*pusServerType ); |

Parameters

|  |  |
| --- | --- |
| hMgmtConnect (I) | Management API connection handle. |
| pusServerType (O) | Advantage server type of the current management API connection. |

Remarks

AdsMgGetServerType returns the Advantage server type of the current management connection.

If connected to the Advantage Database Server for Windows, ADS\_MGMT\_NT\_SERVER or ADS\_MGMT\_NT\_SERVER\_64\_BIT is returned.

If connected to the Advantage Local Server, ADS\_MGMT\_LOCAL\_SERVER is returned.

If connected to the Advantage Database Server for Linux, ADS\_MGMT\_LINUX\_SERVER or ADS\_MGMT\_LINUX\_SERVER\_64\_BIT is returned.

Example

[Click Here](ace_advantage_management_api_examples.htm#adsmggetservertype_example)

See Also

[AdsMgConnect](ace_adsmgconnect.htm)

[AdsGetConnectionType](ace_adsgetconnectiontype.htm)