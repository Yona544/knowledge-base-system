---
title: Jdbc Transaction Processing In Jdbc
slug: jdbc_transaction_processing_in_jdbc
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: jdbc_transaction_processing_in_jdbc.htm
source: Advantage CHM
tags:
  - jdbc
checksum: ab47582c7f08ca123516a71030ff0576b9ac70d5
---

# Jdbc Transaction Processing In Jdbc

Transaction Processing in JDBC

Transaction Processing in JDBC

Advantage JDBC Driver

| Transaction Processing in JDBC  Advantage JDBC Driver |  |  |  |  |

The following documentation discusses the use of transaction processing in the Advantage JDBC Driver. For general information about the Advantage Transaction Processing System, see [Transaction Processing System (TPS)](master_transaction_processing_system.md).

Transaction isolation levels and the auto commit setting

Advantage Database Server supports the read committed transaction isolation level as well as not using transaction processing at all. In the Advantage JDBC Driver, the specified transaction can be requested using the Connection.setTransactionIolation method. For performance reasons, when the Advantage JDBC Connection object is first obtained from the JDBC Driver manager, the transaction isolation level is initialized to TRANSACTION\_NONE and the AutoCommit flag is ignored at this level. Calling the Connection.setAutoCommit method will automatically set the transaction isolation level to read committed and hence enable transaction processing. To disable transaction processing, the Connection.setTransactionIsolation method should be called with the TRANSACTION\_NONE option. Calling the Connection.setTransactionIsolation has no effect on the connection's current auto commit setting. In summary, there are two ways to enable transaction processing on the connection:

| 1. | Calling the Connection.setAutoCommit method. |

| 2. | Calling the Connection.setTransactionIsolation with the TRANSACTION\_READ\_COMMITTED as the parameter. |

There is only one way to disable transaction processing on the connection: calling the Connection.setTransactionIoslation with the TRANSACTION\_NONE as the parameter.

The following table outlines the effect of the various combinations of the AutoCommit and TransactionIsolation flag.

Note The Data Modification Language (DML) statements include "UPDATE ", "INSERT INTO ", "DELETE FROM " SQL statements, as well as the UpdateRow, InsertRow, DeleteRow methods of the ResultSet object.

| AutoCommit | TransactionIsolation  (Read Uncommitted is automatically upgraded to Readed Committed) | Effect on Data Modification Language (DML) statements | Comments |
| True | Read Committed | A Transaction is started on the execution of the DML statement and committed or rolled back at the end of the execution. If a batch execution of DML statements is performed, the transaction is started and committed for each statement in the batch. |  |
| False | Read Committed | A Transaction is started on the execution of the first DML statement and is active until the Connection.commit or Connection.rollback is called. All updates performed between the execution of the first DML statement and the call to the commit or rollback methods are in the same transaction and may be committed or rolled back as an atomic operation. | If there is a transaction active, and either the AutoCommit or the TransactionIsolation property is changed, the transaction will be committed implicitly. |
| True | None | No transaction will be started. |  |
| False | None | No transaction will be started. |  |
