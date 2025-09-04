---
title: Error 9077 Advantage Server Has Suspended
slug: error_9077_advantage_server_has_suspended
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_9077_advantage_server_has_suspended.htm
source: Advantage CHM
tags:
  - error
checksum: 50ccbbc5c4d65351aebf984b5f718e9ed78da171
---

# Error 9077 Advantage Server Has Suspended

9077 Advantage server has suspended

9077 Advantage server has suspended

Advantage Error Guide

| 9077 Advantage server has suspended  Advantage Error Guide |  |  |  |  |

The Advantage Database Server has suspended, most likely due to an assertion failure. The Advantage Database Server will not accept any requests while in a suspended state. View the Advantage Database Server screen to determine why it has suspended. If the server has suspended due to an assertion failure, read and follow the steps outlined in the Advantage Troubleshooting section for the appropriate Advantage Database Server before proceeding.

The Advantage Database Server may have suspended because it was not properly registered. See the ads\_err.adt or ads\_err.dbf error log (and the ads\_log.txt file in Linux) for further details.

In general, 9000 class errors indicate an internal problem within the Advantage server.

On the Windows platform, when Advantage logs a 9000 class error it will also generate a crash dump file. This file will be placed in the error log path (default is c:\), and the filename will be prefixed with "adsdump". Please send this crash dump file, along with all ads\_err error log files to Advantage Technical Support.

For other platforms, please send a small re-creation, along with all ads\_err error log files to Advantage Technical Support.
