---
title: Error 7168 Table Does Not Supp
slug: error_7168_table_does_not_supp
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7168_table_does_not_supp.htm
source: Advantage CHM
tags:
  - error
checksum: 0c7f68772cb9dbaf85c4aec958f398f685dda869
---

# Error 7168 Table Does Not Supp

7168 Table does not Support Strong Encryption

7168 Table does not Support Strong Encryption

Advantage Error Guide

| 7168 Table does not Support Strong Encryption  Advantage Error Guide |  |  |  |  |

Problem: An attempt was made to enable encryption on a table using [AES encryption](master_encryption.md), but the table format does not support it.

Solution: Only ADT and VFP table types support AES encryption; verify that the table type is correct. In addition, the table may need to be updated with additional information to support the encryption type. The system procedure [sp\_EncryptTable](master_sp_encrypttable.md) can be used to convert the table format.
