---
title: Error 7033 Maximum Number Of Connections Exceeded
slug: error_7033_maximum_number_of_connections_exceeded
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7033_maximum_number_of_connections_exceeded.htm
source: Advantage CHM
tags:
  - error
checksum: fd31cbfc8c38562f46446cd7906422500c270413
---

# Error 7033 Maximum Number Of Connections Exceeded

7033 Maximum Number of Connections Exceeded

7033 Maximum Number of Connections Exceeded

Advantage Error Guide

| 7033 Maximum Number of Connections Exceeded  Advantage Error Guide |  |  |  |  |

Advantage Database Server for Linux

Problem: The maximum number of connections are already connected to the Advantage server and the Advantage server was unable to allocate more resources for additional connections.

Solution: Increase the setting for the CONNECTIONS configuration value in the Advantage Database Server for Linux configuration file, ads.conf. Then re-load the Advantage Database Server for Linux.

Advantage Database Server for Windows

Problem: The maximum number of connections are already connected to the Advantage server and the Advantage server was unable to allocate more resources for additional connections.

Solution: Increase the setting for the "Number of Connections" using the Advantage Configuration Utility. If you don't wish to use the Advantage Configuration Utility, increase the setting for the CONNECTIONS configuration value in the Advantage Database Server configuration registry key using the Registry Editor. The Advantage Database Server Configuration Registry Key is located in the Registry at: HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\Advantage\Configuration. Then re-start the Advantage Database Server for Windows.

TCP/IP Connections To Advantage Database Server

Problem: The maximum number of TCP connections are already connected to the Advantage server. .

Solution: The maximum number of concurrent TCP connection to the Advantage Database server is 3000 in 9.x and later release, 1000 in earlier releases. This limit cannot be adjusted. To avoid too many TCP connections to the server, configure the clients to use UDP/IP for communication.

Advantage Local Server

Problem: The maximum number of connections are already connected to the Advantage server and the Advantage server was unable to allocate more resources for additional connections.

Solution: Increase the setting for the CONNECTIONS configuration value in the Advantage Local Server configuration file, ADSLOCAL.CFG. Then re-start the application that uses the Advantage Local Server.
