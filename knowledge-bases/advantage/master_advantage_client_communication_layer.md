Advantage Client Communication Layer




Advantage Database Server 12  

Advantage Client Communication Layer

Networking Issues

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Client Communication Layer  Networking Issues |  |  | Feedback on: Advantage Database Server 12 - Advantage Client Communication Layer Networking Issues master\_Advantage\_client\_communication\_layer Troubleshooting and Technical Support > Networking Issues > Advantage Client Communication Layer / Dear Support Staff, |  |
| Advantage Client Communication Layer  Networking Issues |  |  |  |  |

The Advantage client communication layer consists of two main parts: the communication layer redirector and the Windows communication layer library or libraries. The diagram below shows the Advantage client communication layer.

The communication layer redirector directs requests to the Advantage Database Server or the Advantage Local Server. When connecting to the Advantage Database Server for Windows or the Advantage Database Server for Linux, the communication layer redirector will further redirect communication between the TCP/IP, UDP/IP, and the IPX protocol.

If a connection has been made to the [Advantage Database Server](master_advantage_database_server.htm), operations are sent to the Advantage Windows communication layer DLL. The Windows communication DLL then packages up the information and sends it to the Advantage Database Server.

If a connection has been made to the [Advantage Local Server](master_advantage_local_server.htm), operations are sent to the Advantage Local Server DLL via a direct API call. No network communication is made between the Advantage application and the Advantage Local Server DLL.