---
title: Master Advantage Client Communication Layer
slug: master_advantage_client_communication_layer
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_advantage_client_communication_layer.htm
source: Advantage CHM
tags:
  - master
checksum: 5cc9f24322cc0e7bd27d67fade2454d45ddd045c
---

# Master Advantage Client Communication Layer

Advantage Client Communication Layer

Advantage Client Communication Layer

Networking Issues

| Advantage Client Communication Layer  Networking Issues |  |  |  |  |

The Advantage client communication layer consists of two main parts: the communication layer redirector and the Windows communication layer library or libraries. The diagram below shows the Advantage client communication layer.

The communication layer redirector directs requests to the Advantage Database Server or the Advantage Local Server. When connecting to the Advantage Database Server for Windows or the Advantage Database Server for Linux, the communication layer redirector will further redirect communication between the TCP/IP, UDP/IP, and the IPX protocol.

If a connection has been made to the [Advantage Database Server](master_advantage_database_server.md), operations are sent to the Advantage Windows communication layer DLL. The Windows communication DLL then packages up the information and sends it to the Advantage Database Server.

If a connection has been made to the [Advantage Local Server](master_advantage_local_server.md), operations are sent to the Advantage Local Server DLL via a direct API call. No network communication is made between the Advantage application and the Advantage Local Server DLL.
