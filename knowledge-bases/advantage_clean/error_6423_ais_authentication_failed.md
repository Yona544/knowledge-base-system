---
title: Error 6423 Ais Authentication Failed
slug: error_6423_ais_authentication_failed
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6423_ais_authentication_failed.htm
source: Advantage CHM
tags:
  - error
checksum: 27020820548ed1502bd9e68c8481eb8418386947
---

# Error 6423 Ais Authentication Failed

6423 Authentication failed

6423 Authentication failed

Advantage Error Guide

| 6423 Authentication failed  Advantage Error Guide |  |  |  |  |

This error indicates that the client was not able to establish a valid connection with the Advantage Database Server.

This error can occur if a pre-v10.1 client attempts to connect to a data dictionary [encrypted with AES](master_encryption.md). The old client will use the old style encryption during the authentication (handshaking) process and will not be able to authenticate with the server that is using the newer encryption.
