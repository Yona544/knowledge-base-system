AdsIsServerLoaded




Advantage Database Server 12  

AdsIsServerLoaded

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsIsServerLoaded  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsIsServerLoaded Advantage Client Engine ace\_Adsisserverloaded Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsIsServerLoaded  Advantage Client Engine |  |  |  |  |

Determines if an Advantage server is available

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsIsServerLoaded (UNSIGNED8 \*pucLocation,  UNSIGNED16 \*usServerType); |

Parameters

|  |  |
| --- | --- |
| pucLocation (I) | Null terminated string containing drive letter or server name to check. If the application uses a server name as the parameter, it must include the share or volume name as well. For example, use "\\server\share" or "\\server\vol:". |
| usServerType (O) | This will be set to the server type if an Advantage server is available to access data at the specified location. The server types are ADS\_REMOTE\_SERVER and ADS\_LOCAL\_SERVER. If no Advantage server is available, usServerType will be set to 0. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_NO\_DRIVE\_CONNECTION | An Advantage server could not be located for the indicated path. |

Remarks

AdsIsServerLoaded is used to check if an Advantage server is available to access data on the specified machine. AdsIsServerLoaded uses the server types specified in AdsSetServerType to determine which Advantage server types to check. If no server types have been specified by AdsSetServerType, ADS\_REMOTE\_SERVER will be checked. If AdsIsServerLoaded returns a non-zero value in the usServerType parameter, an Advantage server is available, and it results in a connection to the server.

AdsIsServerLoaded returns ADS\_REMOTE\_SERVER in the usServerType parameter if a successful connection is made via an Advantage Database Server.

AdsIsServerLoaded returns ADS\_LOCAL\_SERVER in the usServerType parameter if a successful connection is made via the Advantage Local Server.

AdsIsServerLoaded returns an error code in the return value if unable to connect to the specified location via an Advantage server.

Note This function does not check for the Advantage Internet Server since connection to the Advantage Internet Server requires an Advantage Data Dictionary, username, and password.

Example

[Click Here](ace_examples.htm#adsisserverloadedexample)

See Also

[AdsConnect](ace_adsconnect.htm)

[AdsConnect60](ace_adsconnect60.htm)

[AdsSetServerType](ace_adssetservertype.htm)