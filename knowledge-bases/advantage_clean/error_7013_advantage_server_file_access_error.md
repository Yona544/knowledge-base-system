---
title: Error 7013 Advantage Server File Access Error
slug: error_7013_advantage_server_file_access_error
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7013_advantage_server_file_access_error.htm
source: Advantage CHM
tags:
  - error
checksum: 82b654546fd13ba8a95e25e5e4c760ccfa8410ff
---

# Error 7013 Advantage Server File Access Error

7013 Advantage server file access error

7013 Advantage server file access error

Advantage Error Guide

| 7013 Advantage server file access error  Advantage Error Guide |  |  |  |  |

Problem 1: The user does not have sufficient access rights to open the specified file.

Solution 1: If you are using the Advantage Database Server for Windows, and your data files are located on a drive using NTFS, that PCs "system" group must have full access to the share that contains the data in order for the Advantage Database Server service to have access to that data. Note that it must be that PCs system group that has full access, not the domains system group.

Problem 2: The file(s) is marked read-only.

Solution 2: Remove the read-only attribute on the file(s).
