ADS\_MGMT\_COMM\_STATS




Advantage Database Server 12  

ADS\_MGMT\_COMM\_STATS

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADS\_MGMT\_COMM\_STATS  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - ADS\_MGMT\_COMM\_STATS Advantage Client Engine ace\_Ads\_mgmt\_comm\_stats Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ADS\_MGMT\_COMM\_STATS  Advantage Client Engine |  |  |  |  |

typedef struct

{

double dPercentCheckSums; /\* % of pkts with checksum failures \*/

UNSIGNED32 ulTotalPackets; /\* Total packets received \*/

UNSIGNED32 ulRcvPktOutOfSeq; /\* Receive packets out of sequence \*/

UNSIGNED32 ulNotLoggedIn; /\* Packet owner not logged in \*/

UNSIGNED32 ulRcvReqOutOfSeq; /\* Receive requests out of sequence \*/

UNSIGNED32 ulCheckSumFailures; /\* Checksum failures \*/

UNSIGNED32 ulDisconnectedUsers; /\* Server initiated disconnects \*/

UNSIGNED32 ulPartialConnects; /\* Removed partial connections \*/

UNSIGNED32 ulInvalidPackets; /\* Received invalid packets \*/

UNSIGNED32 ulRecvFromErrors; /\* RecvFrom failed \*/

UNSIGNED32 ulSendToErrors; /\* SendTo failed \*/

} ADS\_MGMT\_COMM\_STATS;