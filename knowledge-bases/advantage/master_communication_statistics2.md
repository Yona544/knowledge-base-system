Communication Statistics




Advantage Database Server 12  

Communication Statistics

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Communication Statistics  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Communication Statistics Advantage Database Server master\_Communication\_statistics2 Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Communication Statistics  Advantage Database Server |  |  |  |  |

Communication statistics shows the packet and low-level network status between the Advantage clients and the Advantage Database Server. These items are not configurable in the Advantage Database Server. However, the data is useful in determining the traffic load and other system-related Advantage Database Server information.

Total Packets Received: This value represents all data packets received from Advantage clients since the Advantage Database Server was loaded.

Check-Sum Failures: These represent the number of corrupted packets received over the network. The Advantage Database Server ignores corrupted packets and new packets are resent from the clients. This is not something to be concerned with unless the "% of Total Packets" is high. It is difficult to determine what is "high". Reset the value <F10> and view the results. If large numbers of corruptions occur in a short period of time, another application may be corrupting the packets. Stop the suspected application and try again.

Receive Packets Out of Sequence: Communication packets, which are assigned sequence numbers, are sent between the Advantage client and the Advantage Database Server. If a packet is received out a sequence, this value will be incremented. Packets may be out of sequence due to a packet getting lost on the network, which may cause it to show up after others were received. If a packet is out of sequence, the Advantage Database Server ignores it and waits for the resend.

Receive Requests Out of Sequence: The client is requesting a resend of a packet from the Advantage Database Server but the Advantage Database Server no longer has the packet available. Identify the client that is generating the resends. Exit the application and restart it. Monitor the results.

Packet Owner Not Logged In: The Advantage Database Server was unable to communicate with a client properly and therefore, closed the connection. This occurs when a request for an operation, such as a Seek, is made before the user is properly connected to the Advantage Database Server. Verify that your application is properly connecting to the Advantage Database Server. This value is incremented when the Advantage Database Server initiates a disconnect, and the client is still generating disconnect requests.

Server Initiated Disconnect: A normal client disconnect consists of two steps initiated by the client: 1) the semaphore connection file is closed, (if the [Use Semaphore Files](master_use_semaphore_files.htm) configuration setting equals 1) and 2) a disconnect request is made. If a client PC crashes, is turned off without first logging off the network, or if the network goes down, a normal disconnect will not occur. The Advantage Database Server "watch dog" thread identifies that the client is gone and disconnects the client automatically. This can also occur on a busy network when step 2 above is not immediately serviced after Step 1 occurs.

Removed Partial Connection: When a client connects to the Advantage Database Server, a reply is sent to the client. The Advantage Database Server waits for a response from the client to acknowledge that the reply has been received. If the client does not send a response, the Advantage Database Server terminates the connection. This is a symptom of an extremely busy network.