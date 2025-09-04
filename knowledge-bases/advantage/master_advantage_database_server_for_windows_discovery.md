Advantage Database Server for Windows Discovery




Advantage Database Server 12  

Advantage Database Server for Windows Discovery

Networking Issues

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Database Server for Windows Discovery  Networking Issues |  |  | Feedback on: Advantage Database Server 12 - Advantage Database Server for Windows Discovery Networking Issues master\_Advantage\_database\_server\_for\_windows\_discovery Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Advantage Database Server for Windows Discovery  Networking Issues |  |  |  |  |

A mailslot is an abstract mailbox. Microsoft networking provides APIs used to send data packets (or mail) to a mailslot (or mailbox). The NetBIOS protocol is used to route mailslot communication. The Advantage Database Server for Windows creates a mailslot with a unique name that includes the name of the Windows computer. This mailslot it used for discovery of the Advantage Database Server for Windows.

Advantage clients send "mail" to the Advantage Database Server mailslot on the specified server. If the Advantage Database Server has been started on that Windows server, the Advantage Database Server will receive that mailslot message and will respond to the Advantage client with all of its IP and IPX addresses. The Advantage client can then use this information to connect to the Advantage Database Server for Windows.

During the mailslot search, Advantage clients also send out an UDP/IP multicast packet that contains the name of the file server specified for the connection. All Advantage Database Servers running on an UDP/IP-enabled machine will receive this multicast packet. Each Advantage Database Server that receives this packet will inspect the packet, comparing its file server name to the name in the packet. If the names match the Advantage Database Server will respond to the client with all of its IP and IPX addresses, which the client can then use to connect to the Advantage Database Server. The multicast requests are sent on multicast address 224.0.1.55 and port number 2989.

If the Advantage client from its mailslot communication receives no response, and no servers reply to the multicast request, the Advantage Database Server is not available on the specified server. If the Advantage application has been written to attempt a connection to the Advantage Internet Server as well as the Advantage Database Server, a connection via the Advantage Internet Server will then be attempted. If the connection to the Advantage Internet Server is either not attempted or is not successful, and if the Advantage application has been written to attempt a connection to the Advantage Local Server as well as the Advantage Database Server, a connection via the Advantage Local Server will then be attempted. If all Advantage server connection attempts are unsuccessful, a 6060 "Advantage Server Not Available" error will be generated.

Even when using TCP/IP to communicate with the Advantage Database Server, UDP/IP is used for discovery. TCP/IP does not support discovery, so an IP address must be specified for TCP/IP connections if UDP/IP packets cannot reach the Advantage Database Server.