---
title: Ace Ads Mgmt Comm Stats
slug: ace_ads_mgmt_comm_stats
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_ads_mgmt_comm_stats.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: d55b784d884d1e1e8c42a26bf864e6103e0b28b5
---

# Ace Ads Mgmt Comm Stats

ADS\_MGMT\_COMM\_STATS

ADS\_MGMT\_COMM\_STATS

Advantage Client Engine

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
