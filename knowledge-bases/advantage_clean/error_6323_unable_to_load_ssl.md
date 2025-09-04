---
title: Error 6323 Unable To Load Ssl
slug: error_6323_unable_to_load_ssl
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6323_unable_to_load_ssl.htm
source: Advantage CHM
tags:
  - error
checksum: 51781c1a18294261c3d5d15a97308adf188cf8fa
---

# Error 6323 Unable To Load Ssl

6323 Unable to Load SSL

6323 Unable to Load SSL

Advantage Error Guide

| 6323 Unable to Load SSL  Advantage Error Guide |  |  |  |  |

The client communications layer was not able to load the OpenSSL libraries. In order to use [AES encryption](master_encryption.md) or [TLS communications](master_communications_encryption.md), you must have the FIPS Encryption Security Option available. If the libraries are available, verify that they are in a path location that the application can access.
