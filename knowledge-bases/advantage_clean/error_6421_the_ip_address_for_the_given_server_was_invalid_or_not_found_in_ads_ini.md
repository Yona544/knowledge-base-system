---
title: Error 6421 The Ip Address For The Given Server Was Invalid Or Not Found In Ads Ini
slug: error_6421_the_ip_address_for_the_given_server_was_invalid_or_not_found_in_ads_ini
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6421_the_ip_address_for_the_given_server_was_invalid_or_not_found_in_ads_ini.htm
source: Advantage CHM
tags:
  - error
checksum: 41f22ad438f645a3fb55464bb5a429e0ddc8eeee
---

# Error 6421 The Ip Address For The Given Server Was Invalid Or Not Found In Ads Ini

6421 The IP address for the given server was invalid or not found in ADS.INI

6421 The IP address for the given server was invalid or not found in ADS.INI

Advantage Error Guide

| 6421 The IP address for the given server was invalid or not found in ADS.INI  Advantage Error Guide |  |  |  |  |

Problem: A 6421 error occurs when connecting to the Advantage Internet Server.

Solution: Verify that the Internet address in the ads.ini file is correct. The Internet section in the ads.ini file should have the following format.

[pbr]

INTERNET\_IP=144.233.44.91

INTERNET\_PORT=2001

For more information, see [ads.ini file support](master_ads_ini_file_support.md)
