---
title: Arc Server Initiated Disconnect Info
slug: arc_server_initiated_disconnect_info
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_server_initiated_disconnect_info.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: 88b930dd704f3e2e37ce8f86f62240cfd3dfb4ab
---

# Arc Server Initiated Disconnect Info

Server Initiated Disconnect Info

Server Initiated Disconnect Info

| Server Initiated Disconnect Info |  |  |  |  |

A normal client disconnect consists of two steps initiated by the client: 1) the semaphore connection file is closed, and 2) a disconnect request is made. If a client PC crashes, is turned off without first logging off the network, or if the network goes down, a normal disconnect will not occur. The Advantage Database Server "watch dog" thread identifies the client is gone and disconnects the client automatically. This can also occur on a busy network when step 2 above is not immediately serviced after step 1 occurs.
