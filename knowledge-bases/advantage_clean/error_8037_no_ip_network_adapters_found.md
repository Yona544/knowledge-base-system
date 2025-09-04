---
title: Error 8037 No Ip Network Adapters Found
slug: error_8037_no_ip_network_adapters_found
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_8037_no_ip_network_adapters_found.htm
source: Advantage CHM
tags:
  - error
checksum: 6079af5c93059b014c2e71a47595ab354d646fe7
---

# Error 8037 No Ip Network Adapters Found

8037 No IP network adapters found

8037 No IP network adapters found

Advantage Error Guide

| 8037 No IP network adapters found  Advantage Error Guide |  |  |  |  |

Advantage was unable to find any IP adapters. This can occur if the IP stack is not correctly configured. Verify the host name is configured correctly and that the host name has an entry in the "hosts" file as well.

If using the Advantage Database Server for Linux, which does not support IPX, this is a fatal error, and the server will not start. If using any other operating system, this error is for informational purposes, and the server will attempt to continue using IPX.
