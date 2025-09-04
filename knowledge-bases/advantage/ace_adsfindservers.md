AdsFindServers




Advantage Database Server 12  

AdsFindServers

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsFindServers  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsFindServers Advantage Client Engine Ace\_AdsFindServers Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsFindServers  Advantage Client Engine |  |  |  |  |

Retrieve information about instances of Advantage Database Server on a network.

Syntax

UNSIGNED32 AdsFindServers( UNSIGNED32 ulOptions, ADSHANDLE \*phTable );

Parameters

|  |  |
| --- | --- |
| ulOptions (I) | Options that control the behavior of the API.  Options include:  ADS\_FS\_MULTICAST\_ONLY (0x01): Perform only the initial portion of the enumeration process. The list of servers is gathered via multicast over UDP. The only information returned is the IP address and port number. If the server is v10 or greater, the server name will also be returned.    ADS\_FS\_CONNECT\_ALL (0x02):  Attempt to connect to all server addresses discovered by the multicast operation. This may include addresses that are not reachable through a normal connect call (e.g., an address that is local to the machine and cannot be reached from the network). If there are a large number of addresses returned, this may result in very slow performance from the API due to timeout delays on each connect attempt.    If no options are provided (e.g., ADS\_DEFAULT or 0 is specified), the default behavior is to attempt to connect to addresses that are the same as the multicast response address. One situation in which this might not gather all desired information is if, for example, Advantage Database Server is bound to one address on a multihomed machine and the multicast response is returned from a different address. In this situation, it would be necessary to use the ADS\_FS\_CONNECT\_ALL option. |
| phTable (O) | Returns a table handle that contains one row for each address discovered by the API. |

Output Table Structure

|  |  |
| --- | --- |
| Column Name | Description |
| IP Addr | IP address reported by Advantage Database Server. A single instance of Advantage may report several addresses. |
| Port | Port number to which Advantage Database Server is bound. |
| Multicast Addr | The address from which the multicast response was sent. |
| Server Name | The host name of the server on which Advantage is running. |
| Serial Number | The Advantage serial number. |
| Version | The Advantage version string. |
| Owner | The registered owner of the Advantage Database Server. |
| Install Date | Installation date of the Advantage Database Server. |
| User Count | The maximum number of concurrent users allowed. |
| Server Type | An integer representing the type of server. See [AdsMgGetServerType](ace_adsmggetservertype.htm) for a list of possible values. |
| Up Time | The total time Advantage has been running. The value is a string represented in the form dd:hh:mm:ss. |
| Operations | The total operation count reported by the server. |
| More Info | A memo field that has additional information such as the connection error if the connect attempt to the server failed. |

Remarks

This API retrieves information about instances of Advantage Database Server that can be reached on the local network through the multicast protocol. This API uses the same basic multicast mechanism as the normal discovery process uses when attempting to connect to a specific Advantage Database Server. The requests are sent on multicast address 224.0.1.55 and port number 2989.

The initial multicast operation returns only the IP address and port number and if the server is v10 or greater, then it will also return the server name. The rest of the information is gathered through a normal server connection. Thus, if you only want a list of available servers without any details, the ADS\_FS\_MULTICAST\_ONLY option will provide the fastest performance.

It is possible to prevent this API from obtaining server details. If Advantage Database Server has [free connections disabled](master_disable_free_connections.htm), the connect attempt to gather the additional details will fail, and will only have the address and possibly server name available. If this occurs, the More Info field of the returned table will have the error information for the failed connection attempt.

The table returned by this API is an in-memory table that exists only on the client. If you want to obtain a physical Advantage table, you can use the [AdsCopyTable](ace_adscopytable.htm) API to copy the in-memory table to a physical table. In order for the Advantage Client Engine to create the in-memory table, it needs a connection handle to work with. To do this, it creates a local server connection (ADS\_LOCAL\_SERVER) for the in-memory table. As a result of this, the Advantage Local Server DLL (or shared object) must exist for this API to succeed. When the result table is closed, the associated local server connection is also closed.

A possible use for this API is to ease the deployment of applications. For example, when deploying a client application, you might use this API to retrieve a list of servers to which the application can connect. If your application can automatically connect to the desired server, it may not require any intervention on the part of the user to specify connection information. This functionality in conjunction with [server side aliases](master_server_side_aliases.htm) could simplify a large portion of the initial connection process. If, for example, there is only one server returned, then the application could simply try to connect to that server using a known server side alias. Or it might be possible to use the Owner field of the returned table to distinguish among servers.

Another use might be to automate auditing applications. A small standalone application (or module in a larger application) could use this API to retrieve a list of Advantage Database Servers in conjunction with versions and serial numbers.

Example

The following example calls the AdsFindServers API to retrieve the available instances of Advantage Database Server and copies the result to a physical table named findads.adt.

  ADSHANDLE hConn;

  ADSHANDLE hTable;

  UNSIGNED32 ulRet;

 

  ulRet = AdsFindServers( ADS\_DEFAULT, &hTable );

  if ( ulRet == AE\_SUCCESS )

    {

    // connect to current working directory

    ulRet = AdsConnect60( ".", ADS\_LOCAL\_SERVER, NULL, NULL,

                          ADS\_DEFAULT, &hConn );

 

    if ( ulRet == AE\_SUCCESS )

        {

        ulRet = AdsCopyTable( hTable, ADS\_IGNOREFILTERS,

                              "findads.adt" );

        AdsDisconnect( hConn );

        }

 

    ulRet = AdsCloseTable( hTable );

    }