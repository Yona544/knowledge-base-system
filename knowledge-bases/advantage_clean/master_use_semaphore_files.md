---
title: Master Use Semaphore Files
slug: master_use_semaphore_files
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_use_semaphore_files.htm
source: Advantage CHM
tags:
  - master
checksum: a672c4905b45efceff7a1bc896aba87bf08cf11a
---

# Master Use Semaphore Files

Use Semaphore Files

Use Semaphore Files

Advantage Database Server

| Use Semaphore Files  Advantage Database Server |  |  |  |  |

Default = 0

Zero indicates that the server will use the [Client Timeout](master_client_timeout.md) setting will be used to determine if clients have aborted connections rather than the [Semaphore Connection File Path](master_semaphore_connection_file_path.md) option. Any non-zero value will indicate that the Semaphore Connection File Path configuration parameter should be used. See those sections for more information.

Note For Linux, this parameter is ignored, as semaphore connection files are only used in Advantage for Linux when a 16-bit application connects to the server.
