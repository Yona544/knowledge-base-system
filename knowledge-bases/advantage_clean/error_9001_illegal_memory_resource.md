---
title: Error 9001 Illegal Memory Resource
slug: error_9001_illegal_memory_resource
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_9001_illegal_memory_resource.htm
source: Advantage CHM
tags:
  - error
checksum: 54029f3e7504e5414b1a17f5cd584315e740f548
---

# Error 9001 Illegal Memory Resource

9001 Illegal memory resource

9001 Illegal memory resource

Advantage Error Guide

| 9001 Illegal memory resource  Advantage Error Guide |  |  |  |  |

When verifying client request parameters, the memory (usually the allocated data block) was not in the memory resource list.

In general, 9000 class errors indicate an internal problem within the Advantage server.

On the Windows platform, when Advantage logs a 9000 class error it will also generate a crash dump file. This file will be placed in the error log path (default is c:\), and the filename will be prefixed with "adsdump". Please send this crash dump file, along with all ads\_err error log files to Advantage Technical Support.

For other platforms, please send a small re-creation, along with all ads\_err error log files to Advantage Technical Support.
