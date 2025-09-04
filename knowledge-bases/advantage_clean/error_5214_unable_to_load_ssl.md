---
title: Error 5214 Unable To Load Ssl
slug: error_5214_unable_to_load_ssl
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5214_unable_to_load_ssl.htm
source: Advantage CHM
tags:
  - error
checksum: 1f300b166f22a7c131cef676e63c23ad4ae127fd
---

# Error 5214 Unable To Load Ssl

5214 Unable to Load SSL

5214 Unable to Load SSL

Advantage Error Guide

| 5214 Unable to Load SSL  Advantage Error Guide |  |  |  |  |

Problem:  The Advantage client was not able to load the OpenSSL libraries. In order to use [AES encryption](master_encryption.md) or [TLS communications](master_communications_encryption.md), you must have the FIPS Encryption Security Option available.

Solution: If the libraries are available, verify that they are in a path location that the client application can access.
