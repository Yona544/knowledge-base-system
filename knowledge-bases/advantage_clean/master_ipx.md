---
title: Master Ipx
slug: master_ipx
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_ipx.htm
source: Advantage CHM
tags:
  - master
checksum: 72946a2f4bcd7df6a76a2efb93e45f2e2a2bc9d8
---

# Master Ipx

IPX

IPX

Networking Issues

| IPX  Networking Issues |  |  |  |  |

The Advantage client can communicate to any Advantage Database Server (except the Advantage Database Server for Linux) via the IPX communication protocol. IPX stands for Internetwork Packet Exchange and was originally developed by Novell. IPX allows for datagram communication. In other words, with IPX packets the data is sent in one or more packets and there is no guarantee of packet delivery or the sequence of the packets if multiple packets are sent. Either a transport layer on top of IPX or a "different kind of" IPX protocol is necessary to guarantee packet sequence and delivery. SPX, Sequenced Packet Exchange, is a communication protocol that adds information to an IPX packet that guarantees packet delivery and sequence. SPX was found to be too slow, however, so Advantage does not use the SPX protocol. Instead, Advantage uses IPX and a proprietary transport layer that is optimized for Advantage to guarantee IPX packet delivery and sequence. See [Advantage Communication Transport Layer](master_advantage_communication_transport_layer.md) for more information.
