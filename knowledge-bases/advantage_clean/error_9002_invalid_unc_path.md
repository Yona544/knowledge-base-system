---
title: Error 9002 Invalid Unc Path
slug: error_9002_invalid_unc_path
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_9002_invalid_unc_path.htm
source: Advantage CHM
tags:
  - error
checksum: d27960f954254bfe0c56a3471341b862e4e78b28
---

# Error 9002 Invalid Unc Path

9002 Invalid UNC path

9002 Invalid UNC path

Advantage Error Guide

| 9002 Invalid UNC path  Advantage Error Guide |  |  |  |  |

The UNC path sent to the Advantage Database Server either did not contain a server name or did not contain a share/volume name.

In general, 9000 class errors indicate an internal problem within the Advantage server.

On the Windows platform, when Advantage logs a 9000 class error it will also generate a crash dump file. This file will be placed in the error log path (default is c:\), and the filename will be prefixed with "adsdump". Please send this crash dump file, along with all ads\_err error log files to Advantage Technical Support.

For other platforms, please send a small re-creation, along with all ads\_err error log files to Advantage Technical Support.
