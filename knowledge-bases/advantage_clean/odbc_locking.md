---
title: Odbc Locking
slug: odbc_locking
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: odbc_locking.htm
source: Advantage CHM
tags:
  - odbc
checksum: 1ebb4126172c721e1c1faa839ab19730f2b68ca4
---

# Odbc Locking

Locking

Locking

Advantage ODBC Driver

| Locking  Advantage ODBC Driver |  |  |  |  |

With the Advantage ODBC Driver and the Advantage Database Server, you can build and run applications that share database files on the network. Locking is used to enable multiple users to concurrently and safely access the data. When updates are being made to the database tables, a lock must be established on at least the record being updated to prevent other users from locking, updating, or deleting the record. The remaining records in the database file are still accessible to other users.

Using SQL, it is not possible to control locking explicitly from an application (unlike with Xbase languages). The ODBC driver controls all locking of records or files.

Locks are released when a file is closed, which may be done implicitly by a subsequent operation. Also, any command within a transaction does not implicitly unlock any records until the transaction is committed or rolled back.

Lock Limits

The number of locks allowed on your database files is determined by the Advantage Database Server. See [Advantage Locking Modes](master_advantage_locking_modes.md) for more information regarding locking.

Locking Levels

Two locking granularities are provided: Record and File locking. With record locking, each record is locked individually and only records affected by the statement are locked. File locking limits access to a database file, implying that all records are locked.

Choosing the Locking setting is largely a performance issue. In most cases, record locking provides excellent performance while maintaining concurrency control. However, file locking may work better if records are not updated frequently or if a large number of records are being updated at one time.

How Transactions Affect Locking

Two commit modes, Manual Commit and Auto Commit, are available with the Advantage ODBC Driver. In Manual Commit mode, locks are held for updated, inserted, and deleted records until the transaction is committed or rolled back. Locks are then released after the transaction commits or rolls back the changes.

In Auto Commit mode, a formal "transaction" is not actually started on the server. Instead, all changes associated with the updating command are written to the database file as the changes occur. For example, if an UPDATE statement modifies every record in the database file, the record is committed as each record is updated. If a failure occurs during the update, some records in the table are committed while the remainder is not yet modified. If it is critical to verify the changes are committed at one time, use the Manual Commit mode.

Lock Compatibility

The Advantage Database Server, as a default, maintains all locking control through a proprietary locking system. The Advantage locking system allows Advantage to be more efficient and provide the best performance. To take advantage of the proprietary locking scheme, all applications sharing the database files must be Advantage applications. If non-Advantage applications must share the data with Advantage applications, Advantage locking must be set to OFF. If the selected [table type](odbc_table_type.md) is CA-Clipper, CA-Clipper-compatible locking will be used. If the index type is FoxPro, the FoxPro locking scheme will be used.

When using proprietary Advantage files, a proprietary locking scheme is always used.
