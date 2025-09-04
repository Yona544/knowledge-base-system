---
title: Error 6069 Primary Connection To Advantage Server Failed
slug: error_6069_primary_connection_to_advantage_server_failed
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6069_primary_connection_to_advantage_server_failed.htm
source: Advantage CHM
tags:
  - error
checksum: 8148067b00ff36ae6b204612239a94322f185e23
---

# Error 6069 Primary Connection To Advantage Server Failed

6069 Primary connection to Advantage server failed

6069 Primary connection to Advantage server failed

Advantage Error Guide

| 6069 Primary connection to Advantage server failed  Advantage Error Guide |  |  |  |  |

Problem: The primary connection attempt to the Advantage server failed. If you are running a CA-Clipper application that is using the IP communication library, and you incorrectly linked in the Advantage IP comm layer library using "LIB" instead of "SEARCH" or "MODULE"in your link script, this error will occur.

Solution: If you are running a CA-Clipper application that is using the IP communication library, change your link script to use "SEARCH" or "MODULE" to link in the Advantage IP comm library. Refer to the ADS DOS IP documentation, readme.txt file, or sample link scripts for more information on how to correctly link in the Advantage IP comm library. If you are NOT running a CA-Clipper application that is using the IP communication library, then retry the operation or try reloading your network shell.
