ADS\_MGMT\_COMM\_STATS




Advantage Database Server 12  

ADS\_MGMT\_COMM\_STATS

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADS\_MGMT\_COMM\_STATS  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - ADS\_MGMT\_COMM\_STATS Advantage TDataSet Descendant ade\_Ads\_mgmt\_comm\_stats Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ADS\_MGMT\_COMM\_STATS  Advantage TDataSet Descendant |  |  |  |  |

ADS\_MGMT\_COMM\_STATS = record  
  dPercentCheckSums: double; { % of packets with checksum failures }   
  ulTotalPackets: UNSIGNED32; { Total packets received }   
  ulRcvPktOutOfSeq: UNSIGNED32; { Receive packets out of sequence }   
  ulNotLoggedIn: UNSIGNED32; { Packet owner not logged in }   
  ulRcvReqOutOfSeq: UNSIGNED32; { Receive requests out of sequence }   
  ulCheckSumFailures: UNSIGNED32; { Checksum failures }   
  ulDisconnectedUsers: UNSIGNED32; { Server initiated disconnects }   
  ulPartialConnects: UNSIGNED32; { Removed partial connections }   
  ulInvalidPackets: UNSIGNED32; { Rcvd invalid packets (NT only) }   
  ulRecvFromErrors: UNSIGNED32; { RecvFrom failed (NT only) }   
  ulSendToErrors: UNSIGNED32; { SendTo failed (NT only) }   
end;