---
title: Master Nesting Transactions
slug: master_nesting_transactions
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_nesting_transactions.htm
source: Advantage CHM
tags:
  - master
checksum: fecac3f7f565f2de1aff08ff916fca2ae89259a3
---

# Master Nesting Transactions

Nesting Transactions

Nesting Transactions

Advantage Concepts

| Nesting Transactions  Advantage Concepts |  |  |  |  |

Transactions can be nested within other transactions. When nesting begin transaction and commit transaction statements, the outermost pair actually begin and commit the transaction. The inner pairs just keep track of the nesting level. Advantage Database Server does not commit the transaction until the commit transaction that matches the outermost begin transaction is issued. Normally, this transaction nesting occurs as stored procedures, user defined function or triggers that contain begin/commit pairs call each other.

The ::conn.TransactionCount global variable keeps track of the current nesting level for transactions. An initial implicit or explicit begin transaction sets ::conn.TransactionCount to 1. Each subsequent begin transaction increments ::conn.TransactionCount, and a commit transaction decrements it. Firing a trigger also increments ::conn.TransactionCount, and the transaction begins with the statement that causes the trigger to fire. Nested transactions are not committed unless ::conn.TransactionCount equals 0.

For example, the following nested groups of statements are not committed by Advantage Database Server until the final commit transaction:

BEGIN TRANSACTION;  
   SELECT ::conn.TransactionCount FROM system.iota;   
   /\* ::conn.TransactionCount = 1 \*/  
   
   BEGIN TRANSACTION;  
       SELECT ::conn.TransactionCount FROM system.iota;  
       /\* ::conn.TransactionCount = 2 \*/  
   
       BEGIN TRANSACTION;  
           SELECT ::conn.TransactionCount FROM system.iota;  
           /\* ::conn.TransactionCount = 3 \*/  
       COMMIT WORK;  
   
   COMMIT WORK;  
   
COMMIT WORK;  
   
SELECT ::conn.TransactionCount FROM system.iota;  
/\* ::conn.TransactionCount = 0 \*/

 

Transaction Boundary

A transaction boundary is established by the server before entering a subroutine such as stored procedure, user defined function or trigger. The subroutine cannot commit or rollback transaction across the transaction boundary. AE\_TRANS\_OUT\_OF\_SEQUENCE (5047) error is returned if the subroutine attempts to commit or rollback the transaction across the boundary. This restriction means that every COMMIT in the subroutine must be matched with a prior BEGIN TRANSACTION. A ROLLBACK without a savepoint name will roll back (cancel) the whole transaction so it is only allowed in a subroutine if the transaction is initiated inside the subroutine.

Upon leaving the subroutine, if there are uncommitted nested transaction (i.e. the transaction count is not the same as before entering the subroutine), the server will log ERR\_UNCOMMITTED\_TRANSACTION (7187) error and bring the transaction count back to its prior state. If there was no error in the subroutine, the server will commit the unbalanced transactions. If there was error in the subroutine, the transaction count will just be reset to its original value. In both cases, no actual change, except the transaction count, is done to the transaction if the transaction was initiated before entering the subroutine. If there was no transaction before entering the subroutine, then the uncommitted transaction will be committed or rolled back depending on whether there was error in the subroutine.

Savepoint Level

A [SAVEPOINT](master_savepoint.md) exists in a savepoint level. There is only one active savepoint level and program can only reference savepoints in the active savepoint level. A new active savepoint level is established by the following actions: invoking a stored procedure, calling a user defined function, entering a trigger, or starting a nested transaction. Savepoints are created in the current active savepoint level. Upon leaving the stored procedure, user defined function, trigger or committing the nested transaction, the current active savepoint level is destroyed and the savepoint level that was active before the current savepoint level become the active savepoint level. When a savepoint level is destroyed, all savepoints created in the savepoint level are destroyed as well.
