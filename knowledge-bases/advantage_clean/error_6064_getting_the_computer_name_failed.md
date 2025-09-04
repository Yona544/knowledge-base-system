---
title: Error 6064 Getting The Computer Name Failed
slug: error_6064_getting_the_computer_name_failed
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6064_getting_the_computer_name_failed.htm
source: Advantage CHM
tags:
  - error
checksum: 88615e78e0fd4c07629aaf229828ecba82f43b3b
---

# Error 6064 Getting The Computer Name Failed

6064 Getting the computer name failed

6064 Getting the computer name failed

Advantage Error Guide

| 6064 Getting the computer name failed  Advantage Error Guide |  |  |  |  |

Problem: When using 16-bit Windows applications with local drive letters, the name of the local machine is needed. An error occurred while getting the name of the current machine.

Solution: Make sure that the IP and/or IPX protocol is installed. Verify that NETAPI.DLL is in your search path. If possible, specify a UNC path instead of a drive letter.
