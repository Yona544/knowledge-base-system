---
title: Error 7160 Unable To Load Ssl
slug: error_7160_unable_to_load_ssl
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7160_unable_to_load_ssl.htm
source: Advantage CHM
tags:
  - error
checksum: ddafd037c455dabde457dc5d3dafeb880ba93465
---

# Error 7160 Unable To Load Ssl

7160 Unable to Load SSL

7160 Unable to Load SSL

Advantage Error Guide

| 7160 Unable to Load SSL  Advantage Error Guide |  |  |  |  |

Problem: Advantage Database Server was not able to load the OpenSSL libraries. In order to use [AES encryption](master_encryption.md) or [TLS communications](master_communications_encryption.md), you must have the FIPS Encryption Security Option available.

Solution: If the libraries are available, verify that they are in a path location that the server can access.
