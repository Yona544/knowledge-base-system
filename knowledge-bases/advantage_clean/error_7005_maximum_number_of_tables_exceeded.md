---
title: Error 7005 Maximum Number Of Tables Exceeded
slug: error_7005_maximum_number_of_tables_exceeded
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7005_maximum_number_of_tables_exceeded.htm
source: Advantage CHM
tags:
  - error
checksum: d3aaf58bd99e0ae4daba3696cc732c747d20ce8d
---

# Error 7005 Maximum Number Of Tables Exceeded

7005 Maximum number of tables exceeded

7005 Maximum number of tables exceeded

Advantage Error Guide

| 7005 Maximum number of tables exceeded  Advantage Error Guide |  |  |  |  |

Advantage Database Server for Windows

Problem: The maximum number of configured tables are already in use and the Advantage server was unable to allocate more resources for additional tables.

Solution: Increase the setting for the "Number of Tables" using the Advantage Configuration Utility. If you don't wish to use the Advantage Configuration Utility, increase the setting for the TABLES configuration value in the Advantage Database Server configuration registry key using the Registry Editor. The Advantage Database Server Configuration Registry Key is located in the Registry at: HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\Advantage\Configuration. Then re-start the Advantage Database Server for Windows.

Advantage Local Server

Problem: The maximum number of configured tables are already in use and the Advantage server was unable to allocate more resources for additional tables.

Solution: Increase the setting for the TABLES configuration value in the Advantage Local Server configuration file, ADSLOCAL.CFG. Then re-start the application that uses the Advantage Local Server.
