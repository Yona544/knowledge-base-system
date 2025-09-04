---
title: Master Internet Client Timeout
slug: master_internet_client_timeout
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_internet_client_timeout.htm
source: Advantage CHM
tags:
  - master
checksum: 8dcdf07ecd7cd2fa07e56e5f223db56da06c2df9
---

# Master Internet Client Timeout

Internet Client Timeout

Internet Client Timeout

Advantage Database Server

| Internet Client Timeout  Advantage Database Server |  |  |  |  |

Default = 120 (2 minutes)

When an Advantage application calls either an Advantage "connect" API (if available) or opens the first table, it establishes a connection between the application and the Advantage Database Server. The Advantage Database Server needs to ensure that the client application has not aborted its connection to the server. The connection is aborted when the application is abnormally halted. Examples would include a PC being rebooted, a PCs network connection being broken, the application having a GPF, or when an application is halted from within a debugger.

The Advantage server determines if a client had died by keeping track of the last communication the server received from the client. If the server has not received a communication in a given time, then the client is disconnected. The timeout delay is 120 seconds by default. The Advantage Client Engine will start a thread that sends "keep alive" packets to the server at given intervals. These packets are only sent if necessary. If the client has had other communications within the interval, then the "keep alive" packet is not sent.

The Client Timeout algorithm has two drawbacks, however. Both issues affect the developer more so than the end user. The first is that when an application is halted within the debugger, the keep alive packets are not sent to the server by the second thread, which is also halted. If the application is halted for more than the configured time, which is 120 seconds or 2 minutes, by default, the server will abort that applications connection. The second problem is that when the developer aborts an application with a debugger, the connection is left open. The connection will remain open for the configured time.

For Linux:

Add the following line in the Advantage Database Server configuration file (ADS.CONF):

INTERNET\_CLIENT\_TIMEOUT=120

For Windows:

Add the following DWORD using the Registry Editor (REGEDIT.EXE) into the registry:

\\HKEY\_LOCAL\_MACHINE\System\CurrentControlSet\Services\Advantage\Configuration\ INTERNET\_CLIENT\_TIMEOUT=120
