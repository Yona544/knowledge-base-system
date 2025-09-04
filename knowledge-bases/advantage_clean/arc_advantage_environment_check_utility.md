---
title: Arc Advantage Environment Check Utility
slug: arc_advantage_environment_check_utility
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_advantage_environment_check_utility.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: 264f5a8b3ffeb181b162dd101ccbffce455421b1
---

# Arc Advantage Environment Check Utility

Advantage Environment Check Utility

Advantage Environment Check Utility

Advantage Data Architect

| Advantage Environment Check Utility  Advantage Data Architect |  |  |  |  |

Advantage Environment Check is a diagnostic utility that tests the connection between a client workstation and the Advantage Database Server. Advantage Environment Check reports the user network information that will help troubleshoot problems that may occur when connecting to the Advantage Database Server.

Advantage Environment Check uses a version of AXCWS32.DLL for communication to the Advantage Database Server. This utility will first try to communicate to the Advantage Database Server using IP. If the client or the server does not have IP, this utility will try to use IPX. Advantage Environment Check reports drive mappings, drive types, network settings, Advantage DLLs (32-bit and 16-bit), non-Advantage DLLs (used by Advantage clients), etc. This utility will try to connect to the Advantage Database Server. It will report the server name and name of the semaphore connection file that is used for the connection status to the server.

A log of the session will be recorded in the ENV\_LOG.TXT file that will be created in the directory from which Advantage Data Architect was started. In addition, a file named ADSCOM.TXT will be created that contains information about the discovery process. Make sure you have these files on hand if you need to contact Advantage Technical Support.
