---
title: Master What Not To Include In A Transaction
slug: master_what_not_to_include_in_a_transaction
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_what_not_to_include_in_a_transaction.htm
source: Advantage CHM
tags:
  - master
checksum: 1efce506437faf0618ee72fa71b5930122910e09
---

# Master What Not To Include In A Transaction

What Not to Include in a Transaction

What Not to Include in a Transaction

Advantage Concepts

| What Not to Include in a Transaction  Advantage Concepts |  |  |  |  |

If transactions are too complex and take too much time, overall system performance can become slow. In most applications, the only operations that should be included within transactions are insert, update, and delete operations. The following activities should be avoided within a transaction.

Creating Files

Your application should not create files during a transaction. All tables and indexes required for a transaction should exist before the transaction begins. Creating tables is a time consuming process. As transactions take longer to complete, multi-user performance will suffer. Long transactions require data locks to be held for a long period of time, which keeps concurrent users from performing transactions on common data.

File create operations within a transaction cannot be rolled back. If a transaction is rolled back, the Advantage TPS does not delete, or "uncreate", any files that are created during a transaction.

Opening Files

Your application should not open files during a transaction. All tables and indexes required for a transaction should be opened before the transaction begins. If an update needs to be made to a table in order to complete the transaction, and that table is unable to be opened, the corresponding update cannot be performed. The application will mostly likely need to roll back the transaction. All previous update and insert operations performed prior to the failed open will be rolled back due to poor transaction programming. If all tables and indexes are opened before the transactions begin, this needless waste of the users time will be avoided.

File open operations within a transaction cannot be rolled back. If a transaction is rolled back, the Advantage TPS does not close any files that are opened during a transaction.

Data Locking

Depending on the application, record and file locking may best be performed before a transaction begins. If an update needs to be made to a record in order to complete the transaction, and the lock operation on that record fails, the corresponding update cannot be performed. The application will mostly likely need to roll back the transaction. All previous update and insert operations performed prior to the failed data lock will be rolled back. If all data locks are acquired before the transaction begins, these unnecessary transaction rollbacks will be avoided. This may be desirable if, for example, an application must obtain a large number of locks for a transaction or high contention for record locks is expected.

If the potential for record lock failure is unlikely, then it may make sense to do record locking within the transaction and simply rollback the transaction if a lock fails. The code to implement this is often simpler; the potential drawback is that the server load may be increased due to the unnecessary rollbacks.

Excessive Insert and Update Operations

The number of insert and update operations in a given transaction should be as low as possible when using transactions with the Read Committed transaction isolation level, and when multiple users are concurrently accessing large table(s) involved with the transaction. The more insert and update operations that are performed in a transaction, the longer a transaction takes to complete. This leads to slower multi-user performance, especially when using transactions with the Read Committed transaction isolation level with large tables. Long transactions require data locks to be held for a long period of time, which keeps concurrent users from performing transactions on common data.

With the Read Committed transaction isolation level, when a record has an update pending, and a concurrent user issues a read operation on that data, the Advantage Database Server scans internal lists to determine if that data is visible to that user. The scan of the internal lists will indicate that the user should see the original (pre-transaction) data that is associated with that record. With many insert and update operations contained in a transaction, the internal lists increase in size and take longer for concurrent users to read the data associated with the transaction.

The Advantage TPS stores insert and update operations that are issued during the Build Phase in transaction log files. The insert and update operations are actually written to the database during the Commit Phase. The more insert and update operations issued during a transaction, the longer it takes to commit a transaction. Transaction performance suffers as Commit Phase times increase.

If the following conditions exist:

- The transaction isolation level is Read Committed

- Many users are concurrently accessing the table(s) involved with the transaction

- The table(s) involved with the transaction contain a rather large number of records

then as a general rules of thumb, no more than 10% of any of the records in the table(s) should be involved in a transaction at any one time or slower overall application performance and throughput may be noticed.

Reading of User Input

Operations that read in user entered data are slow by nature. If these operations are used within a transaction, it takes longer to complete the transaction. Long transactions require data locks to be held for a long period of time, which keeps concurrent users from performing transactions on common data.

Illegal Operations

There are a number of operations that are illegal when issued within a transaction. These operations will generate an error when they are encountered. See your Advantage client-specific documentation for more information on which operations are not supported within transactions.

Application Termination

If an application terminates, whether normally or abnormally while within a transaction, the transaction is automatically rolled back. When the rollback is complete, the database is left as it was before the transaction began. Do not exit from an application while within a transaction.
