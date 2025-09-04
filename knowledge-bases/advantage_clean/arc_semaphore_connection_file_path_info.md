---
title: Arc Semaphore Connection File Path Info
slug: arc_semaphore_connection_file_path_info
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_semaphore_connection_file_path_info.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: 1b7afb6b038e2d959e1071ee3086db9128db930d
---

# Arc Semaphore Connection File Path Info

Semaphore Connection File Path Info

Semaphore Connection File Path Info

| Semaphore Connection File Path Info |  |  |  |  |

When an Advantage application connects to the Advantage Database Server, it establishes a connection between the workstation and the Advantage Database Server. A semaphore connection file is opened to aid in determining the connection status between the workstation and the Advantage Database Server service. The default directory in which this semaphore connection file is opened is the server directory where the first database file is to be opened.

Note Semaphore connection files are only used if the configuration parameter Use\_Semaphore\_Files is set to a non-zero value. The default is zero to indicate that semaphore connection files are not used at all. See the configuration option Use\_Semaphore\_Files in the Advantage Database Server Help documentation (ADS.HLP) for more information.
