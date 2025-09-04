AdsCheckExistence




Advantage Database Server 12  

AdsCheckExistence

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCheckExistence  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsCheckExistence Advantage Client Engine ace\_Adscheckexistence Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsCheckExistence  Advantage Client Engine |  |  |  |  |

Checks for existence of a file.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsCheckExistence (ADSHANDLE hConnect,  UNSIGNED8 \*pucFilename,  UNSIGNED16 \*pusOnDisk); |

Parameters

|  |  |
| --- | --- |
| hConnect (I) | Handle of an Advantage Client Engine connection, or zero to let the Advantage Client Engine handle the connection. |
| pucFilename (I) | Filename to check for existence. |
| pusOnDisk (O) | True if the file exists, else False. |

Remarks

AdsCheckExistence checks for existence of a file (any file, not just a table) named pucFilename. How the existence check is done by Advantage depends on many factors. These factors include whether or not you are using a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)) or [free connection](javascript:hhpopuplink.TextPopup(popid_7577555X,FontFace,-1,-1,-1,-1)), whether you are checking for a table that is already open, or checking for a table or some other file. It also depends upon the Advantage server type to which you are connected. Those server type variations are discussed below:

Advantage Internet Server connections:

If a table name is specified, and that table exists in the data dictionary (when using a database connection), or if that table is already open on the current connection, this function will return True in the pusOnDisk parameter. Otherwise, it is assumed the specified file does not exist, and False is returned in the pusOnDisk parameter.

Advantage Database Server and Advantage Local Server connections:

If a table name is specified, and that table exists in the data dictionary (when using a database connection), or if that table is already open on the current connection, this function will return True in the pusOnDisk parameter. Otherwise, a non-Advantage, low-level file access function is called from the client to check for existence of the specified file. If checking for file existence of a file on a server, this function cannot override normal access rights imposed by that server. If the client has access rights to the specified file, and it exists, True will be returned in the pusOnDisk parameter. If the specified file does not exist, or if the client does not have access rights to the specified file that does exist, this function will return False in the pusOnDisk parameter.

Example

None.

See Also

[AdsOpenTable](ace_adsopentable.htm)

[AdsConnect](ace_adsconnect.htm)