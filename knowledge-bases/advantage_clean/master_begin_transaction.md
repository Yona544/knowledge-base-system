---
title: Master Begin Transaction
slug: master_begin_transaction
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_begin_transaction.htm
source: Advantage CHM
tags:
  - master
checksum: 306980541c5816c412a1eff324a569441c302bd9
---

# Master Begin Transaction

BEGIN TRANSACTION

BEGIN TRANSACTION

Advantage SQL Engine

| BEGIN TRANSACTION  Advantage SQL Engine |  |  |  |  |

Begins a transaction on the server.

Syntax

BEGIN TRAN[SACTION]

Remarks

BEGIN TRANSACTION begins a transaction for the calling user. Transactions can be [nested](master_nesting_transactions.md) by executing BEGIN TRANSACTION inside of an existing transaction.

Note SQL transactions behave exactly like client transactions. Therefore, with Advantage Local Server, transactions are not supported, but are expected to be executed in a correct sequence.

Examples

BEGIN TRANSACTION

UPDATE sal SET salary = 35000.00 WHERE emp\_id = 25089

COMMIT WORK

 

BEGIN TRAN

UPDATE sal SET salary = 20000 WHERE hire\_date < '1992-02-14'

ROLLBACK WORK
