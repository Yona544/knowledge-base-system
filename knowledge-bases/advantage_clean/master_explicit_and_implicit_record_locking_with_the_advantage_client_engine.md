---
title: Master Explicit And Implicit Record Locking With The Advantage Client Engine
slug: master_explicit_and_implicit_record_locking_with_the_advantage_client_engine
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_explicit_and_implicit_record_locking_with_the_advantage_client_engine.htm
source: Advantage CHM
tags:
  - master
checksum: 7325185a91b2595932ebc8ce10e7d91730bd1559
---

# Master Explicit And Implicit Record Locking With The Advantage Client Engine

Explicit and Implicit Record Locking with the Advantage Client Engine

Explicit and Implicit Record Locking with the Advantage Client Engine

Advantage Concepts

| Explicit and Implicit Record Locking with the Advantage Client Engine  Advantage Concepts |  |  |  |  |

The Advantage Client Engine supports two Advantage record locking methods: explicit and implicit. Explicit record locking follows the familiar CA-Clipper method of calling a function to lock a record before allowing updates to that record using the AdsLockRecord function. The Advantage Client Engine also supports implicit record locking, where the Advantage Client Engine locks the record when the first attempt to update a record is made.

Explicit record locking provides the most locking control to the developer of the two locking methods, but requires more work to use. Explicit record locking also has benefits when using Advantage Transaction Processing. All records to be updated can be locked before beginning a transaction, which maximizes the probability of success for the transaction.

Implicit record locking is a pessimistic locking scheme that the Advantage Client Engine uses to lock records to be updated. When the first update occurs for a record that is not locked, the Advantage Client Engine makes an attempt to lock the record. If the Advantage server fails to lock the record, usually because another user has a lock, the function returns AE\_LOCK\_FAILED. If the lock is successful, it will be maintained on subsequent updates to the record. The implicit lock is not released until the record pointer is repositioned, the table is closed, or the record update is flushed. If the implicit lock is acquired in a transaction, the Advantage Client Engine will wait until the transaction is committed or rolled back to release all implicit locks on the table.

The drawback of relying on implicit record locking is lack of control. If an implicit lock fails on a transaction, extra logic may be required to recover. Also, if an application begins an update using an implicit lock, the status of the lock is not obvious.

The benefits of implicit record locking are that it is easier from a coding standpoint, and slightly, but not significantly, faster than using explicit locking.

There will no doubt be situations in an application where the Advantage Client Engines implicit locking scheme will be quite sufficient, and other times when explicit locking will be required. The Advantage Client Engine provides both to leave the choice up to the programmer.
