AdsGetServerName




Advantage Database Server 12  

AdsGetServerName

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetServerName  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetServerName Advantage Client Engine ace\_Adsgetservername Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetServerName  Advantage Client Engine |  |  |  |  |

Retrieves the server name associated with a connection

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetServerName (ADSHANDLE hConnect,  UNSIGNED8 \*pucName,  UNSIGNED16 \*pusLen); |

Parameters

|  |  |
| --- | --- |
| hConnect (I) | Valid connection handle. |
| pucName (O) | Return the server name in this buffer. |
| pusLen (I/O) | Length of buffer on input, length of name on output. |

Remarks

AdsGetServerName returns the name of the server on which the connected Advantage server is loaded. The server name will not include any volume or share information. If accessing data on a local drive and using Advantage Local Server, the drive letter is returned.

Example

[Click Here](ace_examples.htm#adsgetservernameexample)

See Also

None.