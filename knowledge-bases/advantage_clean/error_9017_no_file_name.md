---
title: Error 9017 No File Name
slug: error_9017_no_file_name
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_9017_no_file_name.htm
source: Advantage CHM
tags:
  - error
checksum: 70997cfb094617f5bf9d12853edd06ba4a10eb4c
---

# Error 9017 No File Name

9017 No file name

9017 No file name

Advantage Error Guide

| 9017 No file name  Advantage Error Guide |  |  |  |  |

One of three things occurred: 1) The length of the file name to open or create was 0 or greater than the maximum allowed; 2) The file name did not have a '.' for the extension; or 3) Adding a new extension to a file name made the length of the file name greater than the maximum allowed.

In general, 9000 class errors indicate an internal problem within the Advantage server.

On the Windows platform, when Advantage logs a 9000 class error it will also generate a crash dump file. This file will be placed in the error log path (default is c:\), and the filename will be prefixed with "adsdump". Please send this crash dump file, along with all ads\_err error log files to Advantage Technical Support.

For other platforms, please send a small re-creation, along with all ads\_err error log files to Advantage Technical Support.
