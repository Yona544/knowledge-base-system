---
title: Arc Receive Packets Out Of Sequence Info
slug: arc_receive_packets_out_of_sequence_info
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_receive_packets_out_of_sequence_info.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: e3b7059cca40b7d650999b70f5a845342409dc05
---

# Arc Receive Packets Out Of Sequence Info

Receive Packets Out of Sequence Info

Receive Packets Out of Sequence Info

| Receive Packets Out of Sequence Info |  |  |  |  |

The number of packets that are received out of sequence. Communication packets are assigned sequence numbers. These packets are sent between the client and the Advantage Database Server. If a packet is received out of sequence, this value is incremented. Packets may be out of sequence due to a packet getting lost on the network which may cause it to show up after others were received. If a packet is out of sequence, the Advantage Database Server ignores it and waits for the resend.
