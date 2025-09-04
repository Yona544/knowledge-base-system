---
title: Error 7162 Unable To Load Ssl
slug: error_7162_unable_to_load_ssl_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7162_unable_to_load_ssl_.htm
source: Advantage CHM
tags:
  - error
checksum: 4b5a862063ee242da7fd364103e5773854354970
---

# Error 7162 Unable To Load Ssl

7162 Unable to Load SSL Entrypoint

7162 Unable to Load SSL Entrypoint

Advantage Error Guide

| 7162 Unable to Load SSL Entrypoint  Advantage Error Guide |  |  |  |  |

Problem: Advantage Database Server was not able to load one of the entrypoints from the OpenSSL libraries. This may mean that the wrong version of the library was loaded.

Solution: In order to use [AES encryption](master_encryption.md) or [TLS communications](master_communications_encryption.md), you must have the FIPS Encryption Security Option available. If the libraries are available, verify that they are in a path location that the server can access.
