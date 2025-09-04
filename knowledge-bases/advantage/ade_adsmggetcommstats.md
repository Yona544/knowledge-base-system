AdsMgGetCommStats




Advantage Database Server 12  

AdsMgGetCommStats

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsMgGetCommStats  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsMgGetCommStats Advantage TDataSet Descendant ade\_Adsmggetcommstats Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsMgGetCommStats  Advantage TDataSet Descendant |  |  |  |  |

Returns current Advantage Database Server communication statistics

Syntax

function AdsMgGetCommStats( hMgmtHandle : ADSHANDLE;

pstCommStats : pADS\_MGMT\_COMM\_STATS;

pusStructSize : pWord ):UNSIGNED32;

Parameters

|  |  |
| --- | --- |
| hMgmtHandle (I) | Management API connection handle of server to get communication statistics. |
| pstCommStats (O) | Returned communication statistics structure. |
| pusStructSize (I/O) | Size (in bytes) of pstCommStats structure on input. On output, size (in bytes) of data returned. |

Remarks

AdsMgGetCommStats returns a structure containing the current Advantage Database Server communication statistics. The communication statistics show the packet and low level network status between Advantage clients and the Advantage Database Server. The data is useful in determining the traffic load and other system related server information.

It is possible that the size of the ADS\_MGMT\_COMM\_STATS structure will increase in future releases of the Advantage Database Server. Since it is possible to use a newer version of the Advantage Database Server with an older version of the Advantage Client Engine, any new and additional communication statistics data that may exist if using a newer version of the Advantage Database Server will not be returned in pstCommStats. The pstCommStats structure will only be filled with the amount of data specified in pusStructSize. The value returned in the pusStructSize parameter is the size of the ADS\_MGMT\_COMM\_STATS structure in the current version of the Advantage Database Server. If the size of the pstCommStats structure input in pusStructSize is the same as the size returned in pusStructSize, then the Advantage client has received all possible communication statistics information.

Since it is possible that the size of the ADS\_MGMT\_COMM\_STATS structure will increase in future releases of Advantage, it is highly recommended that on input the pusStructSize parameter is literally initialized with sizeof( ADS\_MGMT\_COMM\_STATS ) rather than being initialized with a literal value.

The following is a description of the communication statistics information available in the ADS\_MGMT\_COMM\_STATS structure:

|  |  |
| --- | --- |
| dPercentCheckSums | Percentage of total packets received that have checksum failures. |
| ulTotalPackets | Total number of packets received from Advantage clients since the Advantage Database Server was started/loaded. |
| ulRcvPktOutOfSeq | Communications packets, which are assigned sequence numbers, are sent between the Advantage client and the Advantage Database Server. If a packet is received out of sequence, this data member will be incremented. Packets may be out of sequence due to a packet getting lost on the network that may cause it to show up after others were received. If a packet is out of sequence, the Advantage Database Server ignores it and waits for the resend. |
| ulNotLoggedIn | The Advantage Database Server was unable to communicate with a client properly and closed the connection. This occurs when a request for a command, such as a SEEK, is a made before the user is properly connected to the Advantage Database Server. Verify your application is properly connecting to the Advantage Database Server. Also, this data member is incremented when the Advantage Database Server initiates a disconnect (see ulDisconnectedUsers), and the client is still generating disconnect requests. |
| ulRcvReqOutOfSeq | The client is requesting a resend of a packet from the Advantage Database Server, but the packet is no longer available. Identify the client that is generating the resends. Stop the application and restart it. Monitor the results. |
| ulCheckSumFailures | These represent the number of corrupted packets received over the network. The Advantage Database Server ignores corrupted packets and new packets are resent from the Advantage client. This is not something to be concerned with unless the percentage of total packets that have checksum failures (in dPercentCheckSums) is high. It is difficult to determine what is "high". Reset the communication statistics via AdsMgResetCommStats and get the communication statistics again via this API. If large numbers of corruptions occur in a short period of time, another application or a bad network card may be corrupting the packets. |
| ulDisconnectedUsers | A normal client disconnect consists of two steps initiated by the client: 1) the semaphore connection file is closed and 2) a disconnect request is made. If a client PC crashes, is turned off without logging off the network first, or if the network goes down, a normal disconnect will not occur. The Advantage Database Server "watch dog" thread identifies the client is gone and disconnects the client automatically. This can also occur on a busy network when Step 2 above is not immediately serviced after Step 1 occurs. |
| ulPartialConnects | When a client connects to the Advantage Database Server, a reply is sent to the client. The Advantage Database Server waits for a response from the client to acknowledge the reply has been received. If the client does not send a response, the Advantage Database Server terminates the connection. This is a symptom of an extremely busy network. |
| ulInvalidPackets | Number of invalid packets received specifically by the Advantage Database Server for Windows. |
| ulRecvFromErrors | Number of errors that occurred when the Advantage Database Server for Windows was receiving packets. |
| ulSendToErrors | Number of errors that occurred when the Advantage Database Server for Windows was sending packets. |

Example

var

hMgmtHandle : ADSHANDLE;

ulRetVal : UNSIGNED32;

stCommStats : ADS\_MGMT\_COMM\_STATS;

usSize : UNSIGNED16;

begin

ulRetVal := ACE.AdsMgConnect( '\\MyExample\Server', nil, nil, @hMgmtHandle );

 

// If there was an error then show it and exit

if ( ulRetVal <> AE\_SUCCESS ) then

begin

Application.MessageBox( 'Could not connect to server.', 'Connection Error', ID\_OK );

exit;

end;

 

usSize := sizeof( ADS\_MGMT\_COMM\_STATS );

ulRetVal := ACE.AdsMgGetCommStats( hMgmtHandle, @stCommStats, @usSize );

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

Application.MessageBox( 'Could not get Communication stats.',

'Communication Error', ID\_OK );

exit;

end

else

begin

Application.MessageBox( pchar('The number of invalid packets recieved is: '

+ IntToStr( stCommStats.ulInvalidPackets )),

'Up Time',

ID\_OK );

end;

See Also

[AdsMgConnect](ade_adsmgconnect.htm)

[AdsMgResetCommStats](ade_adsmgresetcommstats.htm)

[ADS\_MGMT\_COMM\_STATS](ade_ads_mgmt_comm_stats.htm)