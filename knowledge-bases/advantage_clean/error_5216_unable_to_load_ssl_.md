---
title: Error 5216 Unable To Load Ssl
slug: error_5216_unable_to_load_ssl_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5216_unable_to_load_ssl_.htm
source: Advantage CHM
tags:
  - error
checksum: 6192b8070668c52111ae9ef9863dc14aa95b1c5b
---

# Error 5216 Unable To Load Ssl

5216 Unable to Load SSL Entrypoint

5216 Unable to Load SSL Entrypoint

Advantage Error Guide

| 5216 Unable to Load SSL Entrypoint  Advantage Error Guide |  |  |  |  |

Problem: Advantage Database Server was not able to load one of the entrypoints from the OpenSSL libraries. This may mean that the wrong version of the library was loaded.

Solution: In order to use [AES encryption](master_encryption.md) or [TLS communications](master_communications_encryption.md), you must have the FIPS Encryption Security Option available. If the libraries are available, verify that they are in a path location that the application can access.
