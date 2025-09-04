---
title: Error 9032 Resource List Full
slug: error_9032_resource_list_full
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_9032_resource_list_full.htm
source: Advantage CHM
tags:
  - error
checksum: 244b8726e26fd4b07243c5f67cb802873f5859cf
---

# Error 9032 Resource List Full

9032 Resource list full

9032 Resource list full

Advantage Error Guide

| 9032 Resource list full  Advantage Error Guide |  |  |  |  |

Pre-allocated resources are all in use. The internal list (which is an array of structures) that keeps track of memory allocations, internal file creations, semaphore/mutex creations, etc., is full. There are two likely causes for this error:

| 1. | Large transactions are being performed and/or many users are doing one-at-a-time transactions with the "Transaction List Elements" setting too low. |

| 2. | The "Transaction List Elements" setting is set greater than 50,000 while using the Advantage Database Server v4.4 and older. |

In general, 9000 class errors indicate an internal problem within the Advantage server.

On the Windows platform, when Advantage logs a 9000 class error it will also generate a crash dump file. This file will be placed in the error log path (default is c:\), and the filename will be prefixed with "adsdump". Please send this crash dump file, along with all ads\_err error log files to Advantage Technical Support.

For other platforms, please send a small re-creation, along with all ads\_err error log files to Advantage Technical Support.
