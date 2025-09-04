---
title: Error 6097 Bad Ip Address Specified In Connection Path Or In Ads Ini File
slug: error_6097_bad_ip_address_specified_in_connection_path_or_in_ads_ini_file
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6097_bad_ip_address_specified_in_connection_path_or_in_ads_ini_file.htm
source: Advantage CHM
tags:
  - error
checksum: 6a1860083e8b2e62a7287aa3eafcb6ba73777a06
---

# Error 6097 Bad Ip Address Specified In Connection Path Or In Ads Ini File

6097 Bad IP address specified in connection path or in ADS.INI file

6097 Bad IP address and/or bad port specified in connection path or in ADS.INI file

Advantage Error Guide

| 6097 Bad IP address and/or bad port specified in connection path or in ADS.INI file  Advantage Error Guide |  |  |  |  |

Problem: The Advantage Database Server was not found at the IP address and port specified in the connection path or in the ads.ini file.

Solution: Verify the following:

- The IP address and port are correct for the Advantage Database Server you are trying to connect to. If you are specifying the address and port in the connection path (e.g., //server:port/path or //ip:port/path), verify that both are valid values.

- The Advantage Database Server is currently running.

- You can ping the IP address from the client machine to the server machine.

- UDP packets are not filtered between the client and server machine.
