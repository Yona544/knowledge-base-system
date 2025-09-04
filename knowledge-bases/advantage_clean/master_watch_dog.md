---
title: Master Watch Dog
slug: master_watch_dog
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_watch_dog.htm
source: Advantage CHM
tags:
  - master
checksum: 7c1e376cf7d1dbbb5f2eb69b5fda6bdde29f8efc
---

# Master Watch Dog

Watch Dog

Watch Dog

Advantage Database Server

| Watch Dog  Advantage Database Server |  |  |  |  |

The Advantage Database Server Watch Dog is a process that enhances data integrity. If the Advantage Database Server does not receive a response from a connected client for a configurable amount of time, the connection is automatically closed. All database files that the connection had open will also be closed. (See [Internet Client Timeout](master_internet_client_timeout.md).)

The client workstations send watchdog packets during periods of inactivity to prevent the Advantage Database Server from closing the connection.
