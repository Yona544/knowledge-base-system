---
title: Master Advantage Transaction Processing System Limitations
slug: master_advantage_transaction_processing_system_limitations
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_advantage_transaction_processing_system_limitations.htm
source: Advantage CHM
tags:
  - master
checksum: 6560858a68fa21c94d9791cf80fb5653bad7019f
---

# Master Advantage Transaction Processing System Limitations

Advantage Transaction Processing System Limitations

Advantage Transaction Processing System Limitations

Advantage Concepts

| Advantage Transaction Processing System Limitations  Advantage Concepts |  |  |  |  |

Due to limitations of current client development platforms, network operating systems, and Advantage table formats, there are a few transaction features not supported with the Advantage TPS. The Advantage TPS provides the primary transaction processing features available on the market today. Other DBMS systems may provide additional features that are not supported by the Advantage TPS.

Transaction Spanning Multiple Servers

The Advantage TPS does not support transactions operating on data located on different servers. A transaction can only commit or rollback updates made to tables and index files residing on a single file server.

Operations Aborted during Rollback

If a transaction rollback occurs, all insert, update, and delete operations are aborted. A transaction rollback does not close any files opened during the transaction, does not delete any files created during the transaction, does not undo any "set" operations issued during the transaction, and does not delete any index tags added during a transaction.

Advantage Applications Only

The Advantage TPS should only be used on data files being accessed by Advantage applications. Do not share Xbase tables and index files that are being updated within transactions with non-Advantage applications.

Transaction Journaling

Transaction journaling is the process of logging and archiving all updates made to the database, even after a transaction is completed. Transaction journaling is useful in recovering from server disk crashes. Advantage does not support transaction journaling. The Advantage TPS maintains transaction log files while transactions are active. Once the transactions are completed, the transaction log files are erased.

Appended and Inserted Records after Rollback of a DBF Table

In order for new index keys to be built for records appended or inserted into a DBF table during a transaction, the appended/inserted records are actually inserted into the table before the transaction has been committed. If the transaction is rolled back, the appended records are not removed from a DBF table since another user may have appended additional records. Therefore, if a transaction is rolled back, the Advantage TPS clears out all the fields in the appended/inserted records, marks the appended/inserted records for deletion, and inserts keys into the associated indexes to reference the deleted, appended/inserted records. A record re-use algorithm can be implemented, if desired, to account for and reuse these deleted, appended/inserted records. A periodic Pack of the DBF table would physically removed these deleted, appended/inserted records from the DBF table. Note that this is only an issue with DBF tables, not ADT tables.

Record locks conflict between navigational access and SQL access

When a record is updated within a transaction, a lock is held by the connection that made the modification to the record. This lock is held until the transaction is committed or rolled back. Normally, this lock is shared by all table instances on the connection, meaning that the same table open on the same connection can updated the same record within the transaction without conflict. However, because the SQL engine on the server has no visibility of the locks placed on the client side using navigational access, such Delphi TDataset client application, a lock conflict will result when attempting to update a record using SQL when the same record has been modified by the client application using navigational access, even when on the same connection. The conflict will generally lead to the [5035 (LOCK FAILED)](error_5035_ae_lock_failed.md) error. The same is also true when a record is updated using SQL within a transaction, and then the application attempts to update the same record using navigational access. There is no problem updating the same records multiple time within a transaction using SQL only, or using navigational access only.
