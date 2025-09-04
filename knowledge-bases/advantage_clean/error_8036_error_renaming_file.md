---
title: Error 8036 Error Renaming File
slug: error_8036_error_renaming_file
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_8036_error_renaming_file.htm
source: Advantage CHM
tags:
  - error
checksum: d856a5ddfc072bdb09812bd208d80dd3d93c150e
---

# Error 8036 Error Renaming File

8036 Error renaming file

8036 Error renaming file

Advantage Error Guide

| 8036 Error renaming file  Advantage Error Guide |  |  |  |  |

Problem: An error occurred when attempting to rename a file. In addition to the system error code associated with the failure, the Advantage error log will contain both the old name and the new name of the file.

Solution: Make copies of the file(s) and attempt to rename the file manually.

Errors in the 8000 range are returned when the Advantage server makes a direct call to an OS API, and that function returns a failure. If you receive an error in the 8000 range, retry the database operation. If the error condition persists, please send a small re-creation to Advantage [Technical Support](master_technical_support_u_s__and_canada.md) demonstrating the problem so that Advantage R&D can investigate the issue.
