---
title: Error 5004 Ae File Not Found
slug: error_5004_ae_file_not_found
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5004_ae_file_not_found.htm
source: Advantage CHM
tags:
  - error
checksum: bc033063f98a93844481ad76b2e3916b8f0b83bf
---

# Error 5004 Ae File Not Found

5004 AE\_FILE\_NOT\_FOUND

5004 AE\_FILE\_NOT\_FOUND

Advantage Error Guide

| 5004 AE\_FILE\_NOT\_FOUND  Advantage Error Guide |  |  |  |  |

Either the Advantage Client Engine could not find the specified file, or you do not have sufficient rights to access the file. An incorrect path may cause this error. To identify an incorrect path, change the Advantage Database Server security method to "Ignore Rights" in your application. For example, for the TDataSet Descendant, set the AdsTableOptions' AdsRightsCheck property to False. When restarted, the application will generate a 7008 error, which will be logged in the Advantage error log file. Verify that the path in error log's "filename" column is correct.

Note If connecting to a Linux server using a UNC path, you may get this error if you have Advantage Rights Checking enabled. The Linux client cannot resolve the UNC path to check for file existence, so rights checking should be disabled. Also, if you are connecting to any server with a connection path that contains an IP address and/or port number, you will get this error. See [Database Security](master_database_security.md) for client-specific directions on enabling/disabling Advantage Rights Checking.
