---
title: Error 7031 Could Not Get Advantage Configuration Information
slug: error_7031_could_not_get_advantage_configuration_information
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7031_could_not_get_advantage_configuration_information.htm
source: Advantage CHM
tags:
  - error
checksum: b4e7a41dd1dfd4051185a9e73c47d04b3567ccac
---

# Error 7031 Could Not Get Advantage Configuration Information

7031 Could not get Advantage configuration information

7031 Could not get Advantage configuration information

Advantage Error Guide

| 7031 Could not get Advantage configuration information  Advantage Error Guide |  |  |  |  |

Advantage Database Server for Windows

Problem: The Advantage Configuration Registry Key could not be opened when the Advantage Database Server Service was started.

Solution: Make sure the Advantage Configuration Registry Key exists. The Advantage Configuration Registry Key is located in the Registry at: HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\Advantage\Configuration. The Registry can be viewed via the Registry Editor.

Advantage Database Server for Linux

Problem: The Advantage Database Server for Linux configuration file, ads.conf, could not be opened when the Advantage Database Server was loaded.

Solution: Make sure no one is viewing or editing the Advantage Database Server configuration file, ads.conf, when the Advantage Database Server is being loaded.

Advantage Local Server

Problem: The Advantage Local Server configuration file, ADSLOCAL.CFG, could not be opened when the Advantage Local Server DLL was loaded. If the ADSLOCAL.CFG could not be opened when the Advantage Local Server DLL is loaded, the configuration defaults will get used and no error will be generated other than this 7031 warning in the error log file.

Solution: Make sure no one is viewing or editing the Advantage Local Server configuration file, ADSLOCAL.CFG, when the Advantage Local Server DLL is being loaded.
