AdsConnect




Advantage Database Server 12  

AdsConnect

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConnect  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsConnect Advantage Client Engine ace\_Adsconnect Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsConnect  Advantage Client Engine |  |  |  |  |

Connects to the given server.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsConnect (UNSIGNED8 \*pucServerName,  ADSHANDLE \*phConnect); |

Parameters

|  |  |
| --- | --- |
| pucServerName (I) | Full file path of the data dictionary file, server name, or drive letter to which to connect. If the application uses a server name as the parameter, it must include the share name for Windows or the path from the root for Linux as well. For example, use "\\server\share", "\\server\path\_from\_root", or "\\server\volume". Linux users can also connect to the local machine using a direct path such as "/mydata". All Advantage clients and servers consider either slash type (forward or backslash) to be a path delimiter, this means you could also use a connection path with forward slashes, such as "//server/volume". Linux users should also reference the REPLACE\_UNC\_SERVER section in the [ads.ini](master_ads_ini_file_support.htm) documentation. |
| phConnect (O) | Return the connection handle if successful. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_NO\_DRIVE\_CONNECTION | An Advantage server could not be located for the indicated path. |
| 7085 | Invalid UNC server name. The server name used in the connection path could not be resolved. If using local server verify the name exists in the ads.ini file and that the application is using the correct ads.ini file. If using remote server you should not get this error. Contact your Advantage Technical Services representative. |

Remarks

AdsConnect connects to the Advantage Database Server on the given server. The server name can be a drive letter or any valid path (standard name resolution will be performed). It will return a connection handle if it succeeds. The connection handle can be used in subsequent calls to [AdsOpenTable](ace_adsopentable.htm), [AdsCreateTable](ace_adscreatetable.htm), and transaction processing functions.

Connection paths to the Advantage Database Server can also include a port number if the Advantage Database Server configuration specifies the port number. The form of the connection string can be either of the following (using forward or backward slashes):

//servername:port/path

//ip\_addr:port/path

In the first format (//servername:port), the client will attempt a DNS lookup for the host to find the IP address and then will use the given port to attempt communication with the Advantage Database Server. In the second format, the client simply uses the given IP address and port to attempt to communicate with the Advantage Database Server. The following are syntactically correct connection paths using port numbers:

//theserver:31237/adsdata/testing

//theserver.mydomain.com:31237/adsdata/testing

//1.2.3.4:31237/adsdata/testing

Example

[Click Here](ace_examples.htm#adsconnectexample)

See Also

[AdsDisconnect](ace_adsdisconnect.htm)

[AdsApplicationExit](ace_adsapplicationexit.htm)

[AdsOpenTable](ace_adsopentable.htm)

[AdsSetServerType](ace_adssetservertype.htm)

[AdsIsConnectionAlive](ace_adsisconnectionalive.htm)