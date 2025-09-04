Receive Packets Out of Sequence Info




Advantage Database Server 12  

Receive Packets Out of Sequence Info

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Receive Packets Out of Sequence Info |  |  | Feedback on: Advantage Database Server 12 - Receive Packets Out of Sequence Info arc\_Receive\_packets\_out\_of\_sequence\_info Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Receive Packets Out of Sequence Info |  |  |  |  |

The number of packets that are received out of sequence. Communication packets are assigned sequence numbers. These packets are sent between the client and the Advantage Database Server. If a packet is received out of sequence, this value is incremented. Packets may be out of sequence due to a packet getting lost on the network which may cause it to show up after others were received. If a packet is out of sequence, the Advantage Database Server ignores it and waits for the resend.