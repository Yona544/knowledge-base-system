---
title: Error 7006 Maximum Number Of Index Files Exceeded
slug: error_7006_maximum_number_of_index_files_exceeded
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7006_maximum_number_of_index_files_exceeded.htm
source: Advantage CHM
tags:
  - error
checksum: 02823453dd0b133a23059dc83c9404eb99f95a31
---

# Error 7006 Maximum Number Of Index Files Exceeded

7006 Maximum number of index files exceeded

7006 Maximum number of index files exceeded

Advantage Error Guide

| 7006 Maximum number of index files exceeded  Advantage Error Guide |  |  |  |  |

Advantage Database Server for Windows

Problem: The maximum number of configured index files are already in use and the Advantage server was unable to allocate more resources for additional index files.

Solution: Increase the setting for the "Number of Index Files" using the Advantage Configuration Utility. If you don't wish to use the Advantage Configuration Utility, increase the setting for the INDEXES configuration value in the Advantage Database Server configuration registry key using the Registry Editor. The Advantage Database Server Configuration Registry Key is located in the Registry at: HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\Advantage\Configuration. Then re-start the Advantage Database Server for Windows.

Advantage Local Server

Problem: The maximum number of configured index files are already in use and the Advantage server was unable to allocate more resources for additional index files.

Solution: Increase the setting for the INDEXES configuration value in the Advantage Local Server configuration file, ADSLOCAL.CFG. Then re-start the application that uses the Advantage Local Server.
