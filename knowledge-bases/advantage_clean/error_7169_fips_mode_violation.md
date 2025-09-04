---
title: Error 7169 Fips Mode Violation
slug: error_7169_fips_mode_violation
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7169_fips_mode_violation.htm
source: Advantage CHM
tags:
  - error
checksum: ad84164668ab4a318827939bad90e109b1c8c3d5
---

# Error 7169 Fips Mode Violation

7169 FIPS Mode Violation

7169 FIPS Mode Violation

Advantage Error Guide

| 7169 FIPS Mode Violation  Advantage Error Guide |  |  |  |  |

Problem: The current request could not be completed because Advantage is running in [FIPS mode](master_fips.md) and the request required use of cryptography that is not approved for FIPS usage.

Solution: If you are trying to open a dictionary or a table that is not using AES encryption while the server is in FIPS mode, the operation cannot be completed. The system procedure [sp\_SetDDEncryptionType](master_sp_setddencryptiontype.md) can be used to change a dictionary to use AES encryption. Tables can be converted to AES encryption with the system procedure [sp\_EncryptTable](master_sp_encrypttable.md). In order to perform the conversion, it is necessary to use clients and servers that are not running in FIPS mode.
