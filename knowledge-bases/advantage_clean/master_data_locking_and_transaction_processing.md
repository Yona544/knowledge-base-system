---
title: Master Data Locking And Transaction Processing
slug: master_data_locking_and_transaction_processing
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_data_locking_and_transaction_processing.htm
source: Advantage CHM
tags:
  - master
checksum: 14ae8ceccd46d1699d3c648f55127902d9e9eeda
---

# Master Data Locking And Transaction Processing

Data Locking and Transaction Processing

Data Locking and Transaction Processing

Advantage Concepts

| Data Locking and Transaction Processing  Advantage Concepts |  |  |  |  |

Record locking allows a record to be updated in a table that is opened for Shared use in a multi-user environment. Before a record can be updated, it must first be locked. This will prevent any other user from updating that specific record, but that record can still be read by other users. Other users, at the same time, can obtain record locks on other records and update them concurrently with that first user's update of his record.

A table lock locks an entire table, which allows the user who holds the table lock to update any record in the table while preventing all other users from being able to update or insert records in the table. Other users can still read the record/table while a record/table lock is in place. Keep in mind that use of table locks may cause multi-user performance degradation as other users wanting to perform updates and inserts will have to wait for the table lock to be released.

With Advantage, record locking can be explicitly specified before updating a record or it can be implicitly done for you. If a record is explicitly locked, it must be explicitly unlocked. The converse is also true. If a record is implicitly locked, it will be implicitly unlocked for you. When the actual data unlocking occurs depends upon whether you are in a transaction or not. When in a transaction, once locks are acquired, they are maintained throughout the entire transaction to ensure that the updates can be made to the tables during the commit or rollback of the transaction. Once the transaction completes, all implicit locks will be unlocked for you. Explicit locks must still be explicitly unlocked, however. Calling the Advantage function to explicitly unlock a record will return success during a transaction, but Advantage will continue to hold the lock until the end of the transaction at which time it will release the lock. If it is undesirable for all records in a table to remain locked until the conclusion of the transaction, utilizing a transaction-free table may be appropriate.  See the topic [Transaction-Free Tables](master_transaction_free_tables.md) for details.

Depending on the application, it may be best to explicitly lock all applicable records before starting a transaction. If an application needs to update a record in order to complete the transaction and it attempts unsuccessfully to lock the record during the transaction, the corresponding update cannot be performed. The application will most likely need to roll back the transaction. If an application acquires explicit data locks before a transaction begins, it will prevent unnecessary rollbacks. This may be desirable if, for example, an application must obtain a large number of locks for a transaction or high contention for record locks is expected.

If the potential for record lock failure is unlikely, it may make sense to use implicit record locking within the transaction and simply rollback the transaction if a lock fails. The code to implement this is often simpler; the potential drawback is that the server load may be increased due to the unnecessary rollbacks.

See Also

[Explicit and Implicit Record Locking with the Advantage Client Engine API](master_explicit_and_implicit_record_locking_with_the_advantage_client_engine.md)

[Transaction-Free Tables](master_transaction_free_tables.md)
