---
title: Error 5096 Ae Encryption Not Enabled
slug: error_5096_ae_encryption_not_enabled
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5096_ae_encryption_not_enabled.htm
source: Advantage CHM
tags:
  - error
checksum: 1f91a6942e99723f2491f70798fd1912d4810d4b
---

# Error 5096 Ae Encryption Not Enabled

5096 AE\_ENCRYPTION\_NOT\_ENABLED

5096 AE\_ENCRYPTION\_NOT\_ENABLED

Advantage Error Guide

| 5096 AE\_ENCRYPTION\_NOT\_ENABLED  Advantage Error Guide |  |  |  |  |

Problem: Encryption is not enabled. This error can occur when the requested operation requires a password to be set. Some of the operations that require a password to be set are: encrypting or decrypting records or tables, clearing the password, and appending or modifying records to an encrypted table.

Problem: Encryption is not enabled. Detected on Skip. This error can occur while performing a Skip on the index of a table. The table has encrypted records but no password has been set.

Solution: Set a password before performing the operation.
