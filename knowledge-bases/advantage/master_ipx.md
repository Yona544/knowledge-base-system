IPX




Advantage Database Server 12  

IPX

Networking Issues

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IPX  Networking Issues |  |  | Feedback on: Advantage Database Server 12 - IPX Networking Issues master\_Ipx Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| IPX  Networking Issues |  |  |  |  |

The Advantage client can communicate to any Advantage Database Server (except the Advantage Database Server for Linux) via the IPX communication protocol. IPX stands for Internetwork Packet Exchange and was originally developed by Novell. IPX allows for datagram communication. In other words, with IPX packets the data is sent in one or more packets and there is no guarantee of packet delivery or the sequence of the packets if multiple packets are sent. Either a transport layer on top of IPX or a "different kind of" IPX protocol is necessary to guarantee packet sequence and delivery. SPX, Sequenced Packet Exchange, is a communication protocol that adds information to an IPX packet that guarantees packet delivery and sequence. SPX was found to be too slow, however, so Advantage does not use the SPX protocol. Instead, Advantage uses IPX and a proprietary transport layer that is optimized for Advantage to guarantee IPX packet delivery and sequence. See [Advantage Communication Transport Layer](master_advantage_communication_transport_layer.htm) for more information.