---
title: Error 6102 Xxxxxx Is Illegal During A Transaction
slug: error_6102_xxxxxx_is_illegal_during_a_transaction
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6102_xxxxxx_is_illegal_during_a_transaction.htm
source: Advantage CHM
tags:
  - error
checksum: a46927e4c768e6cf22cbbc08cec929d75c2248cf
---

# Error 6102 Xxxxxx Is Illegal During A Transaction

6102 XXXXXX is illegal during a transaction

6102 XXXXXX is illegal during a transaction

Advantage Error Guide

| 6102 XXXXXX is illegal during a transaction  Advantage Error Guide |  |  |  |  |

Problem: The application issued an illegal command (where XXXXXX is the illegal command) during a transaction.

Solution: The following commands and their associated functions are illegal and will not be performed when used within a transaction:

- UNLOCK, AX\_Unlock(), dbUnlock(), dbUnlockAll(), dbRUnlock(), AX\_IsLocked()

- PACK, ZAP

- REINDEX, dbReindex()

- DELETE TAG, AX\_KillTag(), ordDestroy()

- AX\_DBFEncrypt(), AX\_DBFDecrypt()

- AX\_File2BLOB()

- CLOSE, CLOSE INDEXES, AX\_ClearOrder(), dbCloseArea(), dbClearIndex()

Note A CLOSE command will not only cause an error, it will actually close the table and any open indexes in the work area and then rollback the current transaction.
