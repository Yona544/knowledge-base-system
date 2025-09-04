---
title: Error 7007 Maximum Number Of Locks Exceeded
slug: error_7007_maximum_number_of_locks_exceeded
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7007_maximum_number_of_locks_exceeded.htm
source: Advantage CHM
tags:
  - error
checksum: 85e613ab580a4b8b3c2ec09156ded84e380b4b41
---

# Error 7007 Maximum Number Of Locks Exceeded

7007 Maximum number of locks exceeded

7007 Maximum number of locks exceeded

Advantage Error Guide

| 7007 Maximum number of locks exceeded  Advantage Error Guide |  |  |  |  |

Advantage Database Server for Windows

Problem: The maximum number of configured locks are already in use and the Advantage server was unable to allocate more resources for additional locks.

Solution: Increase the setting for the "Number of Data Locks" using the Advantage Configuration Utility. If you don't wish to use the Advantage Configuration Utility, increase the setting for the LOCKS configuration value in the Advantage Database Server configuration registry key using the Registry Editor. The Advantage Database Server Configuration Registry Key is located in the Registry at: HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\Advantage\Configuration. Then re-start the Advantage Database Server for Windows.

Advantage Local Server

Problem: The maximum number of configured locks are already in use and the Advantage server was unable to allocate more resources for additional locks.

Solution: Increase the setting for the LOCKS configuration value in the Advantage Local Server configuration file, ADSLOCAL.CFG. Then re-start the application that uses the Advantage Local Server.
