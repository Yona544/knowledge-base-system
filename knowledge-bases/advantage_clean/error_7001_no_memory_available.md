---
title: Error 7001 No Memory Available
slug: error_7001_no_memory_available
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7001_no_memory_available.htm
source: Advantage CHM
tags:
  - error
checksum: d776f45adcb1d3e971861070da0f73d7a91efc7e
---

# Error 7001 No Memory Available

7001 No memory available

7001 No memory available

Advantage Error Guide

| 7001 No memory available  Advantage Error Guide |  |  |  |  |

Problem: If connected to the Advantage Database Server, there is not enough available free RAM on the server. If connected to the Advantage Local Server, there is not enough available free RAM on the client.

Solution: If using the Advantage Database Server, lower Advantage Database Server configurable settings (via the Advantage Configuration Utility for the Advantage Database Server for Windows or ADS.CONF for the Advantage Database Server for Linux) so that less memory is required or add RAM to the server. Then re-load/re-start the Advantage Database Server. If using the Advantage Local Server, lower Advantage Local Server configurable settings via ADSLOCAL.CFG so that less memory is required or add RAM to the client. Then re-start the application using the Advantage Local Server.
