---
title: Error 9027 Receive Request Out Of Sequence
slug: error_9027_receive_request_out_of_sequence
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_9027_receive_request_out_of_sequence.htm
source: Advantage CHM
tags:
  - error
checksum: 997a7acdc7e29f3a11f7bdf144721c17cc7ebee4
---

# Error 9027 Receive Request Out Of Sequence

9027 Receive request out of sequence

9027 Receive request out of sequence

Advantage Error Guide

| 9027 Receive request out of sequence  Advantage Error Guide |  |  |  |  |

The server received a resend request or acknowledge that didn't have the current sequence number. It is not logged in the error log but is visible by the Advantage Management Utility.

In general, 9000 class errors indicate an internal problem within the Advantage server.

On the Windows platform, when Advantage logs a 9000 class error it will also generate a crash dump file. This file will be placed in the error log path (default is c:\), and the filename will be prefixed with "adsdump". Please send this crash dump file, along with all ads\_err error log files to Advantage Technical Support.

For other platforms, please send a small re-creation, along with all ads\_err error log files to Advantage Technical Support.
