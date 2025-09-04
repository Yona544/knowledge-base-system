---
title: Error 6325 Unable To Load Ssl Entrypoint
slug: error_6325_unable_to_load_ssl_entrypoint
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6325_unable_to_load_ssl_entrypoint.htm
source: Advantage CHM
tags:
  - error
checksum: 8a2339e99d8079beb45aa11142306a192910bcfc
---

# Error 6325 Unable To Load Ssl Entrypoint

6325 Unable to Load SSL Entrypoint

6325 Unable to Load SSL Entrypoint

Advantage Error Guide

| 6325 Unable to Load SSL Entrypoint  Advantage Error Guide |  |  |  |  |

The client communications layer was not able to load one of the entrypoints from the OpenSSL libraries. This may mean that the wrong version of the library was loaded. In order to use [AES encryption](master_encryption.md) or [TLS communications](master_communications_encryption.md), you must have the FIPS Encryption Security Option available. If the libraries are available, verify that they are in a path location that the application can access.
