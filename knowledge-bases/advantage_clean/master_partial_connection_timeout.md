---
title: Master Partial Connection Timeout
slug: master_partial_connection_timeout
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_partial_connection_timeout.htm
source: Advantage CHM
tags:
  - master
checksum: eb3c2e78997f10b8fb69013c397adc8fcdb1ad19
---

# Master Partial Connection Timeout

Partial Connection Timeout

Partial Connection Timeout

Advantage Database Server

| Partial Connection Timeout  Advantage Database Server |  |  |  |  |

Default is 120000 (2 minutes).

Minimum value is 10000 (10 seconds).

This setting tells the server how long (in milliseconds) to wait for a client to fully connect. If the client does not fully connected within this time, the server will disconnect the partial connection. This setting should only need to be increased in very rare conditions where a slow network is causing connection failures. In this case, this setting should be used in conjunction with the Advantage client setting of Max Timeouts. The Max Timeouts setting is the amount of time the client waits for a response from the Advantage Database Server.

For Windows:

Add the following DWORD using the Registry Editor (REGEDIT.EXE) into the registry:

\\HKEY\_LOCAL\_MACHINE\System\CurrentControlSet\Services\Advantage\Configuration\PARTIAL\_CONNECTION\_TIMEOUT=120000

For Linux:

Add the following line in the Advantage Database Server configuration file (ads.conf):

PARTIAL\_CONNECTION\_TIMEOUT=120000

For Advantage Clients:

Add the following entry in the ADS.INI file:

[SETTINGS]

// A Default value of 30 is used if this is 0 or not specified

// The following example setting specifies that the client will retry communicating with the

// server 40 times before returning a timeout error.

MAX\_TIMEOUTS=40
