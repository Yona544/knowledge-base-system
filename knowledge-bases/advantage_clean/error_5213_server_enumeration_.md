---
title: Error 5213 Server Enumeration
slug: error_5213_server_enumeration_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5213_server_enumeration_.htm
source: Advantage CHM
tags:
  - error
checksum: e62bb64e23616d63f3d41db17ddc0aac7b2a3ba7
---

# Error 5213 Server Enumeration

error\_5213\_server\_enumeration\_error

5213 AE\_SERVER\_ENUMERATION\_ERROR

Advantage Error Guide

| 5213 AE\_SERVER\_ENUMERATION\_ERROR  Advantage Error Guide |  |  |  |  |

Problem:  An error occurred while trying to discover the available instances of Advantage Database Server on the network.

Solution: The text associated with the error may have additional details. This error typically indicates that there was a basic failure at the socket layer that occurred while attempting to send multicast packets to remote servers. If the error does indicate a socket error, it may indicate that there is a networking problem on the local machine.
