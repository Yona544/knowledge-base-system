---
title: Master Number Of Data Locks L
slug: master_number_of_data_locks_l_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_number_of_data_locks_l_.htm
source: Advantage CHM
tags:
  - master
checksum: 1293309e7d9ce1a1ad36259ddcd648f4c459797f
---

# Master Number Of Data Locks L

Number of Data Locks (-L)

Number of Data Locks (-L)

Advantage Database Server

| Number of Data Locks (-L)  Advantage Database Server |  |  |  |  |

Default = (40 x CONNECTIONS) data locks. Range = 1 - no upper limit.

This is the initial number of record locks, table locks, implicit header locks, and implicit index locks that can be in effect at one time. It may not be necessary to change this parameter. For a frame of reference, check the Advantage Management Utility for the Max Used number. Increase this parameter only if the Max Used Data Locks value is larger than the Configured value or more than zero Data Locks have been rejected.

The "Number of Data Locks" configuration setting on the Advantage Database Server is a "per-client" setting. That is, one data lock must be available per record, table, header, or index lock requested per Advantage client. For example, if 10 Advantage clients each have 15 records or files locked at one time, there must be at least 150 data locks configured on the Advantage Database Server.

If an Advantage application attempts to obtain a record, table, or index lock, and the configured number of data locks have already been used, the Advantage Database Server will attempt to allocate more resources to accommodate more data locks. If that allocation fails, the Advantage application which is attempting to get the lock will receive a 7007 error, Maximum number of locks exceeded, until a lock "element" becomes available. Data locks take very little memory. Setting this value to a very high number should not require much server RAM to be used.
