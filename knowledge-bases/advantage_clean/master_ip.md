---
title: Master Ip
slug: master_ip
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_ip.htm
source: Advantage CHM
tags:
  - master
checksum: 09a8fd0e2a71216e671885a66a7a5de3451aa752
---

# Master Ip

IP

IP

Networking Issues

| IP  Networking Issues |  |  |  |  |

The Advantage client can communicate to any Advantage Database Server via the UDP/IP or TCP/IP communication protocol. IP stands for Internet Protocol. UDP/IP allows for datagram communication. In other words, with IP packets the data is sent in one or more packets and there is no guarantee of packet delivery or the sequence of the packets if multiple packets are sent. Advantage has written a transport layer on top of UDP/IP to guarantee packet sequence and delivery. TCP/IP, Transmission Control Protocol, is a communication protocol that adds information to an IP packet that guarantees packet delivery and sequence.

In most situations, the proprietary transport layer using UDP/IP, which is optimized specifically for Advantage, will be faster than TCP/IP. However, when communicating with machines behind a firewall, TCP/IP can prevent a myriad of problems. See [Advantage Communication Transport Layer](master_advantage_communication_transport_layer.md) for more information.
