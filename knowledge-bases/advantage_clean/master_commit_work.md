---
title: Master Commit Work
slug: master_commit_work
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_commit_work.htm
source: Advantage CHM
tags:
  - master
checksum: fdfe1bd806645125256640815e405760141d5904
---

# Master Commit Work

COMMIT WORK

COMMIT WORK

Advantage SQL Engine

| COMMIT WORK  Advantage SQL Engine |  |  |  |  |

Commits a transaction on the server.

Syntax

COMMIT [WORK]

Remarks

COMMIT WORK commits any work done inside a transaction. The transaction state is shared with the client, so a transaction cannot be committed in SQL if one has not been started either by an Advantage client (i.e., ACE API AdsBeginTransaction) or through the Advantage SQL engine.

When used in [nested transactions](master_nesting_transactions.md), a commit of an inner transaction does not commit the data or release locks. Only committing the outer most transaction will commit the work and end the transaction.

Note SQL transactions behave exactly like client transactions. Therefore, with Advantage Local Server, transactions are not supported, but are expected to be executed in a correct sequence.

Examples

BEGIN TRANSACTION

UPDATE sal SET salary = 35000.00 WHERE emp\_id = 25089

COMMIT WORK

 

BEGIN TRAN

UPDATE sal SET salary = 20000 WHERE hire\_date < '1992-02-14'

COMMIT
