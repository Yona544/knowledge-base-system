---
title: Devguide Transaction Savepoints
slug: devguide_transaction_savepoints
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_transaction_savepoints.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: c8f6eea306d530e02f26c589adc4ba66dfdcfc4d
---

# Devguide Transaction Savepoints

Transaction Savepoints

     Transaction Savepoints

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Transaction Savepoints  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Transactions in Advantage now support savepoints. A savepoint identifies a state during a transaction to which you may want to roll back to, without having to roll back the entire transaction.

You can have multiple savepoints for a single transaction. You specify which savepoint you want to roll back to when you want to perform a partial rollback. When you roll back to a given savepoint, those operations within the transaction that were executed prior to the savepoint remain intact.

Transaction savepoints are discussed in detail in Chapter 12.
