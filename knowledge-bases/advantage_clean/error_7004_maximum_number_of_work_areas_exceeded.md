---
title: Error 7004 Maximum Number Of Work Areas Exceeded
slug: error_7004_maximum_number_of_work_areas_exceeded
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7004_maximum_number_of_work_areas_exceeded.htm
source: Advantage CHM
tags:
  - error
checksum: c99fafd19b795a84fed9d3e834b9a8bde7362e76
---

# Error 7004 Maximum Number Of Work Areas Exceeded

7004 Maximum number of work areas exceeded

7004 Maximum number of work areas exceeded

Advantage Error Guide

| 7004 Maximum number of work areas exceeded  Advantage Error Guide |  |  |  |  |

Advantage Database Server for Windows

Problem: The maximum number of configured work areas are already in use and the Advantage server was unable to allocate more resources for additional work areas.

Solution: Increase the setting for the "Number of Work Areas" using the Advantage Configuration Utility. If you don't wish to use the Advantage Configuration Utility, increase the setting for the WORKAREAS configuration value in the Advantage Database Server configuration registry key using the Registry Editor. The Advantage Database Server Configuration Registry Key is located in the Registry at: HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\Advantage\Configuration. Then re-start the Advantage Database Server for Windows.

Advantage Local Server

Problem: The maximum number of configured work areas are already in use and the Advantage server was unable to allocate more resources for additional work areas.

Solution: Increase the setting for the WORKAREAS configuration value in the Advantage Local Server configuration file, ADSLOCAL.CFG. If no WORKAREAS configuration key exists in ADSLOCAL.CFG, add one and set the value to larger than the number of CONNECTIONS multiplied by 25 (which is the default value for the number of work areas if no WORKAREAS configuration key exists). Then re-start the application that uses the Advantage Local Server.
