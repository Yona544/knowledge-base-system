AdsConnect60




Advantage Database Server 12  

AdsConnect60

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConnect60  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsConnect60 Advantage Client Engine ace\_Adsconnect60 Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsConnect60  Advantage Client Engine |  |  |  |  |

Connects to the given server or to a database in an Advantage Data Dictionary.

Syntax

UNSIGNED32 AdsConnect60( UNSIGNED8 \*pucConnectPath,

UNSIGNED16 usServerTypes,

UNSIGNED8 \*pucUserName,

UNSIGNED8 \*pucPassword,

UNSIGNED32 ulOptions,

ADSHANDLE \*phConnect );

Parameters

|  |  |
| --- | --- |
| pucConnectPath (I) | Full file path of the data dictionary file, server name, or drive letter to which to connect. If the application uses a server name as the parameter, it must include the share name for Windows or the path from the root for Linux as well. For example, use "\\server\share", "\\server\path\_from\_root", or "\\server\volume". Linux users can also connect to the local machine using a direct path such as "/mydata". All Advantage clients and servers consider either slash type (forward or backslash) to be a path delimiter, this means you could also use a connection path with forward slashes, such as "//server/volume". Linux users should also reference the REPLACE\_UNC\_SERVER section in the [ads.ini](master_ads_ini_file_support.htm) documentation. |
| usServerTypes (I) | Enumeration of server types to allow client connections. Options are ADS\_REMOTE\_SERVER, ADS\_AIS\_SERVER, and ADS\_LOCAL\_SERVER. The default is ADS\_REMOTE\_SERVER logically ORed with ADS\_AIS\_SERVER. |
| pucUserName (I) | Optional user name to verify in the data dictionary. The user name and password is validated against information stored in the data dictionary. If this parameter is not NULL, the pucConnectPath must specify an Advantage Data Dictionary. Otherwise, an error will be returned. |
| pucPassword (I) | Optional password for the user. |
| ulOptions (I) | Options for connecting to Advantage servers. Allowed values are ADS\_DEFAULT, ADS\_INC\_USERCOUNT, ADS\_STORED\_PROC\_CONN, ADS\_COMPRESS\_ALWAYS, ADS\_COMPRESS\_NEVER, and ADS\_COMPRESS\_INTERNET. The values can be ORed together. See Remarks for more information on the options. |
| phConnect (O) | The handle of the connection is returned if it the connection is made successfully. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_NO\_DRIVE\_CONNECTION | An Advantage server could not be located for the indicated path. |
| AE\_INVALID\_PASSWORD | Either the user is unknown in the database or an incorrect password is entered for the user. |
| 7077 | The Advantage Database Server cannot open the specified data dictionary. |
| 7078 | Authentication error. |
| 7085 | Invalid UNC server name. The server name used in the connection path could not be resolved. If using local server verify the name exists in the ads.ini file and that the application is using the correct ads.ini file. If using remote server you should not get this error. Contact your Advantage Technical Services representative. |

Remarks

AdsConnect60 connects to the Advantage Database Server on the given server. The pucConnectPath parameter can be a full file path to an Advantage Data Dictionary file, a drive letter, or any valid path (standard name resolution will be performed). Only those server types that are specified in usServerType parameter will be considered when attempting to connect. If the usServerType is 0, this call obeys the default server types that may have been set by calling [AdsSetServerType](ace_adssetservertype.htm). The function returns a connection handle if it succeeds. The connection handle can be used in subsequent calls to [AdsOpenTable](ace_adsopentable.htm), [AdsCreateTable](ace_adscreatetable.htm), and transaction processing functions.

If the pucConnectPath parameter specifies a path to an Advantage Data Dictionary file, the returned connection handle is a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)) handle. A database connection handle can be used in all functions where a connection handle is required. In addition, a database connection provides access to additional functionality provided by the Advantage Data Dictionary. Specifically, a database connection handle is required to open ADT tables that are part of the database defined in the data dictionary. See [Advantage Data Dictionary](master_advantage_data_dictionary.htm) for more information.

If the pucConnectPath parameter does not specify a path to an Advantage Data Dictionary file, the returned connection handle is a [free connection](javascript:hhpopuplink.TextPopup(popid_7577555X,FontFace,-1,-1,-1,-1)) handle.

The pucUserName and pucPassword parameters are optional. They are used by the Advantage Server to authenticate the user when attempting to obtain a database connection. If the pucUserName parameter is provided, the pucConnectPath must specify a path to an Advantage Data Dictionary file. However, the user name and password are not required when making a database connection. The database specified by the pucConnectPath can be set up to allow anonymous user connections (see [AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.htm) for information). In such a case, using no user name and no password is a valid combination to obtain a database connection. If the database specified by the pucConnectPath is set up to require users to log in, a valid combination of user name and password must be supplied to obtain a database connection.

The ulOptions parameter specifies options used when making the connection. The following values can be ORed together in the ulOptions parameter.

|  |  |
| --- | --- |
| ADS\_DEFAULT | If no options are needed, this constant (0) can be used. |
| ADS\_INC\_USERCOUNT | If this option is passed, the user count on the Advantage Database Server will be incremented, even if the current PC is already connected to the Advantage server. Without this option, if the same PC connects to Advantage more than one time they are counted as a single user and only the connection count is incremented.  In general, this property was added to allow an Advantage middleware type of application to increment the Advantage Database Server user count for each remote client workstation indirectly accessing the Advantage Database Server. This provides an easy way for Advantage middleware applications to abide by the Advantage Database Server license agreement as related to remote client workstations taking up a "user" toward the maximum number of licensed users. |
| ADS\_STORED\_PROC\_CONN | Used to NOT increase the user count on the server. All stored procedure developers should use this option when making connections from stored procedures. If the application is not a stored procedure, then this has no effect. |
| ADS\_COMPRESS\_ALWAYS | If this option is specified, then all data communications between the client and server will be compressed unless compression is specifically turned off at the server. See [Communications Compression](master_communications_compression.htm). This option is ignored for ADS\_LOCAL\_SERVER connections. |
| ADS\_COMPRESS\_NEVER | If this option is specified, then compression will not be used for communications between the client and server. This option is ignored for ADS\_LOCAL\_SERVER connections. |
| ADS\_COMPRESS\_INTERNET | If this option is specified, then all data communications for ADS\_AIS\_SERVER connections will be compressed unless compression is specifically turned off at the server. See [Communications Compression](master_communications_compression.htm). This option is ignored for ADS\_LOCAL\_SERVER connections. |
| ADS\_UDP\_IP\_CONNECTION | If this option is specified, then the client will communicate with the server using UPD/IP. |
| ADS\_IPX\_CONNECTION | If this option is specified, then the client will communicate with the server using IPX. |
| ADS\_TCP\_IP\_CONNECTION | If this option is specified, then the client will communicate with the server using TCP/IP. |
| ADS\_TLS\_CONNECTION | In order to use Transport Layer Security (TLS) communications, it is necessary to use the [AdsConnect101](ace_adsconnect101.htm) API. It is not possible to use this option directly because other information (TLS certificate and common name) must also be provided. |

Note that if none of the ADS\_COMPRESS options are specified, the COMPRESSION setting in the ADS.INI file will be used if available.

Connection paths to the Advantage Database Server can also include a port number if the Advantage Database Server configuration specifies the port number. The form of the connection string can be either of the following (using forward or backward slashes):

//servername:port/path

//ip\_addr:port/path

In the first format (//servername:port), the client will attempt a DNS lookup for the host to find the IP address and then will use the given port to attempt communication with the Advantage Database Server. In the second format, the client simply uses the given IP address and port to attempt to communicate with the Advantage Database Server. The following are syntactically correct connection paths using port numbers:

//theserver:31237/adsdata/testing

//theserver.mydomain.com:31237/adsdata/testing

//1.2.3.4:31237/adsdata/testing

Example

Making a data dictionary bound connection and opening the "Customer Information" table in the database.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, NULL, NULL, ADS\_DEFAULT, &hConn );

AdsOpenTable( hConn, "Customer Information", NULL, ADS\_DEFAULT, ADS\_ANSI, ADS\_DEFAULT,

ADS\_DEFAULT, ADS\_DEFAULT, &hTable );

See Also

[AdsOpenTable](ace_adsopentable.htm)

[AdsDisconnect](ace_adsdisconnect.htm)

[AdsSetServerType](ace_adssetservertype.htm)

[AdsDDCreate](ace_adsddcreate.htm)

[AdsDDAddTable](ace_adsddaddtable.htm)

[AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.htm)

[AdsDDGetTableProperty](ace_adsddgettableproperty.htm)

[AdsDDGetFieldProperty](ace_adsddgetfieldproperty.htm)

[AdsIsConnectionAlive](ace_adsisconnectionalive.htm)