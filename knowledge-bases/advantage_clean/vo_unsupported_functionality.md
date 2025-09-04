---
title: Vo Unsupported Functionality
slug: vo_unsupported_functionality
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_unsupported_functionality.htm
source: Advantage CHM
tags:
  - vo
checksum: ea15cb4a56b4d283069b2b2e15cba1f2e7d8c2ab
---

# Vo Unsupported Functionality

Unsupported Functionality

Unsupported Functionality

Advantage AXSQL RDDs

| Unsupported Functionality  Advantage AXSQL RDDs |  |  |  |  |

Due to the nature of SQL cursors, some RDD functionality isnt supported with the AXSQL RDDs. Listed below are the VO RDD functions that are not supported:

- Pack

- Zap

- FLock

- Reindex

Also, these ACE API functions are not supported when given a table handle from an open AXSQL work area:

- AdsDecryptTable

- AdsEncryptTable

- AdsDecryptRecord

- AdsEncryptRecord

- AdsReindex

- AdsReindexFTS

- AdsLockTable

- AdsUnlockTable

- AdsPackTable

- AdsZapTable
