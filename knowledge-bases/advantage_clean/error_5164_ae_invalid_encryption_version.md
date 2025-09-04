---
title: Error 5164 Ae Invalid Encryption Version
slug: error_5164_ae_invalid_encryption_version
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5164_ae_invalid_encryption_version.htm
source: Advantage CHM
tags:
  - error
checksum: f28e9de9c7a21b9d2ae82c256cca1682000cbd47
---

# Error 5164 Ae Invalid Encryption Version

5164 AE\_INVALID\_ENCRYPTION\_VERSION

5164 AE\_INVALID\_ENCRYPTION\_VERSION

Advantage Error Guide

| 5164 AE\_INVALID\_ENCRYPTION\_VERSION  Advantage Error Guide |  |  |  |  |

Problem: The database table encryption version that is stored in the table header is incorrect.

Solution: The likely cause of this corruption problem is that the database table file has been overwritten by the user. The database should be maintained using the data dictionary management API or the Advantage Data Architect (arc32.exe). Using OS commands or the API to update the file will likely cause corruption.
