---
title: Master Set Transaction
slug: master_set_transaction
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_set_transaction.htm
source: Advantage CHM
tags:
  - master
checksum: 59363b3bb0e39b1fa9c6485616baa81681037a09
---

# Master Set Transaction

SET TRANSACTION

SET TRANSACTION

Advantage SQL Engine

| SET TRANSACTION  Advantage SQL Engine |  |  |  |  |

Sets the autocommit state for transactions on the server.

Syntax

SET TRAN[SACTION] AUTOCOMMIT\_ON | AUTOCOMMIT\_OFF | EXPLICIT

Remarks

The AUTOCOMMIT feature allows a transaction to be automatically begun and/or committed around the execution of a DML (Data Manipulation Language) SQL statement. With AUTOCOMMIT\_ON, any INSERT, UPDATE, or DELETE statement would have a transaction begun before it and committed after its completion. With AUTOCOMMIT\_OFF, any INSERT, UPDATE, or DELETE statement would have a transaction begun before it but not committed or rolled back after its completion (it is the users responsibility to commit or rollback the transaction at a later time). The EXPLICIT option simply returns the transaction state to its default state of requiring the user to explicitly begin, commit, and rollback all transactions.

Note Beginning a transaction explicitly sets the AUTOCOMMIT mode to explicit. The AUTOCOMMIT state of a user cannot be altered while inside a transaction.

Examples

SET TRANSACTION AUTOCOMMIT\_ON

UPDATE sal SET salary = 35000.00 WHERE emp\_id = 25089

 

SET TRANSACTION AUTOCOMMIT\_OFF

UPDATE sal SET salary = 20000 WHERE hire\_date < '1992-02-14'

COMMIT WORK

 

SET TRAN EXPLICIT

DELETE FROM customer WHERE purch\_amt < 100.00 AND NOT state = CA

ROLLBACK WORK
