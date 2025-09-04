AdsGetConnectionPath




Advantage Database Server 12  

AdsGetConnectionPath

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetConnectionPath  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetConnectionPath Advantage Client Engine ace\_Adsgetconnectionpath Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetConnectionPath  Advantage Client Engine |  |  |  |  |

Retrieves the connection path for the given connection.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetConnectionPath (ADSHANDLE hConnect,  UNSIGNED8 \*pucConnectionPath,  UNSIGNED16 \*pusLen); |

Parameters

|  |  |
| --- | --- |
| hConnect (I) | Handle of a connection. |
| pucFldName (O) | Return the connection path. |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

AdsGetConnectionPath is used to retrieve the connection path for the given connection handle. The connection path returned is the connection path given to Advantage when the connection was created.