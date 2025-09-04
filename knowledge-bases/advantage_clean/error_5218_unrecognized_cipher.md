---
title: Error 5218 Unrecognized Cipher
slug: error_5218_unrecognized_cipher
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5218_unrecognized_cipher.htm
source: Advantage CHM
tags:
  - error
checksum: 29b445bb09fd2852f8271ca37bb2a9842072f89a
---

# Error 5218 Unrecognized Cipher

5218 Unrecognized Cipher

5218 Unrecognized Cipher

Advantage Error Guide

| 5218 Unrecognized Cipher  Advantage Error Guide |  |  |  |  |

Problem: One of the given [TLS ciphers](master_communications_encryption.md) was not supported. The supported values are AES128-SHA, AES256-SHA, and RC4-MD5.

Solution: Verify that the [TLSCiphers connection string](ace_adsconnect101.md) option is correct.
