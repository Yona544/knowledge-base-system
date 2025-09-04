---
title: Error 5035 Ae Lock Failed
slug: error_5035_ae_lock_failed
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5035_ae_lock_failed.htm
source: Advantage CHM
tags:
  - error
checksum: 716a93d88e55b52e146fd9304dce12205f9962e1
---

# Error 5035 Ae Lock Failed

5035 AE\_LOCK\_FAILED

5035 AE\_LOCK\_FAILED

Advantage Error Guide

| 5035 AE\_LOCK\_FAILED  Advantage Error Guide |  |  |  |  |

The requested lock could not be granted.

- The file or record may be locked by another user.

- When using the Advantage proprietary table type (ADTs) and the current record has been deleted.

- The record may have been modified within a transaction and the transaction has no been committed or rolled back. See [Advantage Transaction Processing System Limitations](master_advantage_transaction_processing_system_limitations.md).

 

Linux Note If using a pre-2.4 kernel, it is possible to get this error because of an incorrect lock offset range. See [USE\_LOW\_LOCK\_OFFSETS](master_advantage_local_server_configuration.md) for more details.
