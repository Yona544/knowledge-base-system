---
title: Ade Ads Mgmt Comm Stats
slug: ade_ads_mgmt_comm_stats
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_ads_mgmt_comm_stats.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 31f97b5f0667cb712cfa862fc23c3c64feb22465
---

# Ade Ads Mgmt Comm Stats

ADS\_MGMT\_COMM\_STATS

ADS\_MGMT\_COMM\_STATS

Advantage TDataSet Descendant

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
