---
title: Error 6422 The Port For The Given Server Was Invalid Or Not Found In Ads Ini
slug: error_6422_the_port_for_the_given_server_was_invalid_or_not_found_in_ads_ini
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6422_the_port_for_the_given_server_was_invalid_or_not_found_in_ads_ini.htm
source: Advantage CHM
tags:
  - error
checksum: b823dcf23e8993f1c62d62e24ab996690c2169d0
---

# Error 6422 The Port For The Given Server Was Invalid Or Not Found In Ads Ini

6422 The port for the given server was invalid or not found in ADS.INI

6422 The port for the given server was invalid or not found in ADS.INI

Advantage Error Guide

| 6422 The port for the given server was invalid or not found in ADS.INI  Advantage Error Guide |  |  |  |  |

Problem: A 6422 error occurs when connecting to the Advantage Internet Server.

Solution: Verify that the Internet port in the ads.ini file is correct. The Internet section in the ads.ini file should have the following format.

[pbr]

INTERNET\_IP=144.233.44.91

INTERNET\_PORT=2001

For more information, see [ADS.INI File Support](master_ads_ini_file_support.md)
