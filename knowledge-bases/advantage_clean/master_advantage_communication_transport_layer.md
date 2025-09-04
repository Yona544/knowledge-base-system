---
title: Master Advantage Communication Transport Layer
slug: master_advantage_communication_transport_layer
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_advantage_communication_transport_layer.htm
source: Advantage CHM
tags:
  - master
checksum: d49a63f131ec4622c6e962abb5a879542d944340
---

# Master Advantage Communication Transport Layer

Advantage Communication Transport Layer

Advantage Communication Transport Layer

Networking Issues

| Advantage Communication Transport Layer  Networking Issues |  |  |  |  |

The Advantage client can communicate with the Advantage Database Server using either datagram or streaming paradigms. UDP/IP or IPX are the protocols used for datagram communication and do not guarantee reliable data delivery. TCP/IP is the protocol used for streaming communication and does guarantee reliable data delivery.

Because the datagram paradigm does not guarantee delivery of data, Advantage has written sophisticated communication algorithms, which are optimized for use with Advantage. This proprietary datagram transport layer guarantees delivery of packet data and the sequencing of that packet data between the Advantage client and the Advantage Database Server.

The Advantage datagram transport layer supports sending bursts of data packets, rather than sending packets one at a time. A single IPX packet is limited to 512 bytes of data. A single IP packet is limited to approximately 1450 bytes of data. Advantage will send up to 16 packets at once in a single burst. Therefore, a burst of IPX packets can contain up to 8K bytes of data, and a burst of UDP/IP packets can contain up to approximately 23K bytes of data.

The most common chunk of data that is sent between an Advantage client and the Advantage Database Server is 10 table records (because of read-head record caching). Depending on the record size, a single burst of datagram packets is usually sufficient to transfer the data. However, using streaming communication, the record transfer will take multiple round trips because every 2900 bytes of data must be acknowledged. Advantage datagram communication will exhibit better performance than streaming communication protocol in most situations, because it significantly decreases the number of acknowledgement packets required.

To provide reliable communication, the Advantage datagram communication layer will sequence and merge the packet data within the burst(s) back into a single chunk of data. If packets within the burst are never received due to a network failure or the like, the missing packets are simply resent. The TCP/IP protocol provides this functionality for Advantage when using streaming communication.
