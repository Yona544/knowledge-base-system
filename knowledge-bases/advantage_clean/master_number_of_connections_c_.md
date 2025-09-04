---
title: Master Number Of Connections C
slug: master_number_of_connections_c_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_number_of_connections_c_.htm
source: Advantage CHM
tags:
  - master
checksum: 68ec8253c906183a1d380800e635e889f74d83a8
---

# Master Number Of Connections C

Number of Connections (-C)

Number of Connections (-C)

Advantage Database Server

| Number of Connections (-C)  Advantage Database Server |  |  |  |  |

Default = User Option purchased. Range = 1 - no upper limit.

This is the initial number of connections that can be active on the Advantage Database Server at one time. Connections are defined as follows:

- For Advantage DOS-based applications, a "connection" is defined as a single application connected to the Advantage Database Server.

- For Advantage 16-bit Windows applications, a "connection" is defined as a single application connected to the Advantage Database Server. Additional "connections" to the Advantage Database Server via calls to the Advantage "connect" API can be obtained.

- For Advantage 32-bit Windows applications, a "connection" is defined as a single application connected to the Advantage Database Server. Additional "connections" to the Advantage Database Server can be obtained via calls to the Advantage "connect" API, using an Advantage connection component, or using an Advantage connection object

For example, to minimize memory usage, if you are licensed for 100 users, but have only 75 connections, you can save a small amount of memory by configuring the number of connections to 75. Or, if you are licensed for 20 users but have 3 Advantage applications running on each workstation, the number of connections should be set to at least 60.

If more Advantage applications attempt to connect to the Advantage Database Server than there are number of connections configured, the Advantage Database Server will attempt to allocate more resources to accommodate more connections. If that allocation fails, the Advantage application that is attempting to connect will receive a 7033 error, Connection Table Full, until a connection becomes available.
