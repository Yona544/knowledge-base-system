---
title: Error 7164 Unrecognized Cipher
slug: error_7164_unrecognized_cipher
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7164_unrecognized_cipher.htm
source: Advantage CHM
tags:
  - error
checksum: 0aaacaa6990ec6d62055eba26ab2b0ac13a7ea84
---

# Error 7164 Unrecognized Cipher

7164 Unrecognized Cipher

7164 Unrecognized Cipher

Advantage Error Guide

| 7164 Unrecognized Cipher  Advantage Error Guide |  |  |  |  |

Problem: One of the given [TLS ciphers](master_communications_encryption.md) is not supported. The supported values are AES128-SHA, AES256-SHA, and RC4-MD5.

Solution: Verify that the [TLS\_CIPHERS](master_tls_ciphers.md) configuration parameter is correct.
