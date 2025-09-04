---
title: Error 7030 Missing Advantage Configuration File Ads Cfg Or Adslocal Cfg
slug: error_7030_missing_advantage_configuration_file_ads_cfg_or_adslocal_cfg
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7030_missing_advantage_configuration_file_ads_cfg_or_adslocal_cfg.htm
source: Advantage CHM
tags:
  - error
checksum: 4a0ce85eed932f864d9220622357c3667b6959b8
---

# Error 7030 Missing Advantage Configuration File Ads Cfg Or Adslocal Cfg

7030 Missing Advantage configuration file, ADS.CFG or ADSLOCAL.CFG

7030 Missing Advantage configuration file ADSLOCAL.CFG

Advantage Error Guide

| 7030 Missing Advantage configuration file ADSLOCAL.CFG  Advantage Error Guide |  |  |  |  |

Problem: This error is applicable to the Advantage Local Server only. The Advantage configuration file, ADSLOCAL.CFG, was not found when the Advantage Local Server DLL was loaded. The ADSLOCAL.CFG configuration file must be located in the current working directory, the Windows system directory, or the client's search path. If the ADSLOCAL.CFG file is not found when the Advantage Local Server DLL is loaded, the configuration defaults will get used and no error will be generated other than this 7030 warning in the error log file.

Solution: Put ADSLOCAL.CFG in the current working directory, the Windows system directory, or the client's search path.
