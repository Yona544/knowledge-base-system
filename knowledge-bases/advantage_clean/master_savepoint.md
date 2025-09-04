---
title: Master Savepoint
slug: master_savepoint
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_savepoint.htm
source: Advantage CHM
tags:
  - master
checksum: f000a0214cf7712d1c789f11f0bed7c91f4fecc0
---

# Master Savepoint

SAVEPOINT

SAVEPOINT

Advantage SQL Engine

| SAVEPOINT  Advantage SQL Engine |  |  |  |  |

Creates a savepoint inside the existing transaction.

Syntax

SAVEPOINT savepointname

Remarks

savepointname is case insensitive.

 

SAVEPOINT creates a point in the transaction to which all work can be rolled back to without ending the transaction. The transaction state is shared with the client, so a savepoint cannot be created in SQL if a transaction has not been started either by an Advantage client (i.e., ACE API AdsBeginTransaction) or through the Advantage SQL engine.

A savepoint is created in the current savepoint level and is only valid in the current savepoint level. See [Nesting Transactions](master_nesting_transactions.md) for additional information on savepoint level. If a savepoint with identical name exists in the current savepoint level, that savepoint will be destroyed and a new savepoint will be established at the current transaction location. It has no effect on other savepoints.

Note SQL transactions behave exactly like client transactions. Therefore, with Advantage Local Server, transactions are not supported but are expected to be executed in a correct sequence.

Examples

BEGIN TRANSACTION;

UPDATE sal SET salary = 35000.00 WHERE emp\_id = 25089;

SAVEPOINT test;

DELETE FROM sal WHERE salary > 36000.00;

ROLLBACK TO SAVEPOINT test;

COMMIT WORK;
