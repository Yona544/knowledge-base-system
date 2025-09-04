sp\_mgGetCommStats




Advantage Database Server 12  

sp\_mgGetCommStats

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_mgGetCommStats  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_mgGetCommStats Advantage SQL Engine master\_Sp\_mggetcommstats Advantage SQL > System Procedures > Procedures > sp\_mgGetCommStats / Dear Support Staff, |  |
| sp\_mgGetCommStats  Advantage SQL Engine |  |  |  |  |

Returns the current Advantage Database Server communication statistics.

Syntax

EXECUTE PROCEDURE sp\_mgGetCommStats()

Parameters

|  |  |
| --- | --- |
| PercentCheckSums (O) | Percentage of total packets received that have check sum failures. |
| TotalPackets (O) | Total number of packets received from Advantage clients since the Advantage Database Server was started/loaded. |
| RcvPktOutOfSeq (O) | Communications packets, which are assigned sequence numbers, are sent between the Advantage client and the Advantage Database Server. If a packet is received out of sequence, this data member will be incremented. Packets may be out of sequence due to a packet getting lost on the network that may cause it to show up after others were received. If a packet is out of sequence, the Advantage Database Server ignores it and waits for the resend. |
| NotLoggedIn (O) | The Advantage Database Server was unable to communicate with a client properly and closed the connection. This occurs when a request for a command, such as a SEEK, is a made before the user is properly connected to the Advantage Database Server. Verify your application is properly connecting to the Advantage Database Server. Also, this data member is incremented when the Advantage Database Server initiates a disconnect (see ulDisconnectedUsers), and the client is still generating disconnect requests. |
| RcvReqOutOfSeq (O) | The client is requesting a resend of a packet from the Advantage Database Server, but the packet is no longer available. Identify the client that is generating the resends. Stop the application and restart it. Monitor the results. |
| CheckSumFailures (O) | These represent the number of corrupted packets received over the network. Corrupted packets are ignored by the Advantage Database Server and new packets are resent from the Advantage client. This is not something to be concerned with unless the percentage of total packets that have check sum failures (in dPercentCheckSums) is high. It is difficult to determine what is "high". Reset the communication statistics via AdsMgResetCommStats and get the communication statistics again via this API. If large numbers of corruptions occur in a short period of time, another application or a bad network card may be corrupting the packets. |
| DisconnectedUsers (O) | A normal client disconnect consists of two steps initiated by the client: 1) the semaphore connection file is closed and 2) a disconnect request is made. If a client PC crashes, is turned off without logging off the network first, or if the network goes down, a normal disconnect will not occur. The Advantage Database Server "watch dog" thread identifies the client is gone and disconnects the client automatically. This can also occur on a busy network when step 2 above is not immediately serviced after step 1 occurs. |
| PartialConnects (O) | When a client connects to the Advantage Database Server, a reply is sent to the client. The Advantage Database Server waits for a response from the client to acknowledge the reply has been received. If the client does not send a response, the Advantage Database Server terminates the connection. This is a symptom of an extremely busy network. |
| InvalidPackets (O) | Number of invalid packets received by the Advantage Database Server. |
| RcvFromErrors (O) | Number of errors that occurred when the Advantage Database Server was receiving packets. |
| SendToErrors (O) | Number of errors that occurred when the Advantage Database Server was sending packets. |

Remarks

The communication statistics show the packet and low level network status between clients and the Advantage Database Server. This procedure returns zeros for all values when it is called on an Advantage Local Server connection.

Example

EXECUTE PROCEDURE sp\_mgGetCommStats();

See Also

[sp\_mgResetCommStats](master_sp_mgresetcommstats.htm)