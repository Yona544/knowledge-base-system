---
title: Error 9022 Key Not Found
slug: error_9022_key_not_found
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_9022_key_not_found.htm
source: Advantage CHM
tags:
  - error
checksum: de0ec867be21ddc8b4f380f6889124a07d956143
---

# Error 9022 Key Not Found

9022 Key not found

9022 Key not found

Advantage Error Guide

| 9022 Key not found  Advantage Error Guide |  |  |  |  |

This error is not logged. The error means the specified key is not in the index. This is permissible for transient indexes, or if the record in the table is updated by a different user (in which case the client re-reads the data).

In general, 9000 class errors indicate an internal problem within the Advantage server.

On the Windows platform, when Advantage logs a 9000 class error it will also generate a crash dump file. This file will be placed in the error log path (default is c:\), and the filename will be prefixed with "adsdump". Please send this crash dump file, along with all ads\_err error log files to Advantage Technical Support.

For other platforms, please send a small re-creation, along with all ads\_err error log files to Advantage Technical Support.
