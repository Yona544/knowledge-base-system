---
title: Error 9016 Illegal Flags
slug: error_9016_illegal_flags
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_9016_illegal_flags.htm
source: Advantage CHM
tags:
  - error
checksum: 9781b6d2218e3d1fc26964025fd29ef743484730
---

# Error 9016 Illegal Flags

9016 Illegal flags

9016 Illegal flags

Advantage Error Guide

| 9016 Illegal flags  Advantage Error Guide |  |  |  |  |

Shared/Read-only flag from the client driver was not 0 or 1; the header read request was not a correct value; the SOFTSEEK flag from client driver was not 0 or 1.

In general, 9000 class errors indicate an internal problem within the Advantage server.

On the Windows platform, when Advantage logs a 9000 class error it will also generate a crash dump file. This file will be placed in the error log path (default is c:\), and the filename will be prefixed with "adsdump". Please send this crash dump file, along with all ads\_err error log files to Advantage Technical Support.

For other platforms, please send a small re-creation, along with all ads\_err error log files to Advantage Technical Support.
