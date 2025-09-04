---
title: Oledb Supporting Local Transactions
slug: oledb_supporting_local_transactions
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_supporting_local_transactions.htm
source: Advantage CHM
tags:
  - oledb
checksum: fec6e5e0f2e061ae42f4a930744c2103f51e1823
---

# Oledb Supporting Local Transactions

Supporting Local Transactions

Supporting Local Transactions

Advantage OLE DB Provider (for ADO)

| Supporting Local Transactions  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The Advantage OLE DB Provider implements local transaction support.

By default, the Advantage OLE DB Provider uses an auto-commit transaction mode, where each discrete action on a consumer session comprises a complete transaction against an Advantage Database Server installation. The Advantage OLE DB Provider auto-commit mode is local, and auto-commit transactions never span more than a single session.

The Advantage OLE DB Provider exposes the ITransactionLocal interface, allowing the consumer to use explicitly and implicitly started transactions on a single Advantage Database Server connection.

A session delimits transaction scope for an Advantage OLE DB Provider local transaction. When, at a consumer's direction, the Advantage OLE DB Provider submits a request to a connected the Advantage Database Server installation, the request constitutes a unit of work for the Advantage OLE DB Provider. Local transactions always wrap one or more units of work on a single Advantage OLE DB Provider session.

Using the default the Advantage OLE DB Provider auto-commit mode, a single unit of work is treated as the scope of a local transaction. Only one unit participates in the local transaction. When a session is created, the Advantage OLE DB Provider begins a transaction for the session. Upon successful completion of a work unit, the work is committed. On failure, any work begun is rolled back and the error is reported to the consumer. In either case, the Advantage OLE DB Provider begins a new local transaction for the session so that all work is conducted within a transaction.

The Advantage OLE DB Provider consumer can direct more precise control over local transaction scope by using the ITransactionLocal interface. When a consumer session initiates a transaction, all session work units between the transaction start point and the eventual ITransaction::Commit or ITransaction::Abort method calls are treated as an atomic unit. The Advantage OLE DB Provider implicitly begins a transaction when directed to do so by the consumer. If the consumer does not request retention, the session reverts to parent transaction-level behavior, most commonly auto-commit mode.

The Advantage OLE DB Provider supports ITransactionLocal::StartTransaction parameters as described in the following table.

| Parameter | Description |
| isoLevel | In local transactions, the Advantage OLE DB Provider supports ISOLATIONLEVEL\_READCOMMITTED and ISOLATIONLEVEL\_CURSORSTABILITY. |
| isoFlags | The Advantage OLE DB Provider returns an error for any value other than zero. |
| pOtherOptions | The Advantage OLE DB Provider ignores pOtherOptions |
| pulTransactionLevel | If not NULL, the Advantage OLE DB Provider returns the nested level of the transaction. |

For local transactions, the Advantage OLE DB Provider implements ITransaction::Abort parameters as follows.

| Parameter | Description |
| pboidReason | Ignored if set. Can safely be NULL. |
| fRetaining | When TRUE, a new transaction is implicitly begun for the session. The transaction must be committed or terminated by the consumer. When FALSE, the Advantage OLE DB Provider reverts to auto-commit mode for the session. |
| FAsync | The Advantage OLE DB Provider does not support asynchronous abort. The Advantage OLE DB Provider returns XACT\_E\_NOTSUPPORTED if the value is not FALSE. |

For local transactions, the Advantage OLE DB Provider implements ITransaction::Commit parameters as described in the following table.

| Parameter | Description |
| FRetaining | When TRUE, a new transaction is implicitly begun for the session. The transaction must be committed or terminated by the consumer. When FALSE, the Advantage OLE DB Provider reverts to auto-commit mode for the session. |
| GrfTC | The Advantage OLE DB Provider does not support asynchronous returns. The Advantage OLE DB Provider returns XACT\_E\_NOTSUPPORTED for any asynchronous values. |
| GrfRM | The Advantage OLE DB Provider returns an error for any value other than zero. |

The Advantage OLE DB Provider rowsets on the session are preserved after a local commit or abort operation.

When a transaction start operation is issued, if any record inserts/updates/deletes are pending, they will be flushed to the underlying database before the transaction is started . When a transaction abort operation is issued, if any record inserts/updates/deletes are pending, they will be cancelled before the transaction is aborted. When a transaction commit operation is issued, if any record inserts/updates/deletes are pending, they will be flushed to the underlying database before the transaction is committed. Transaction start, commit, and abort operations are ignored if the Advantage ServerType is ADS\_LOCAL SERVER.

The Advantage Database Server supports local transactions. That is, transactions that exist on a single server upon which the Advantage Database Server is running. Advantage does not currently support distributed transactions.

The only transaction isolation levels supported by Advantage are Read Committed and Cursor Stability. If a different transaction isolation level is specified when starting a transaction, an error will be returned.

The following Advantage field types cannot be updated within a transaction: Binary and Image. An AutoIncrement field can never be updated whether in a transaction or not.

The value for the Data Source Initialization property DBPROP\_SUPPORTEDTXNDDL with the Advantage OLE DB Provider is set to DBPROPVAL\_TC\_DDL\_IGNORE because most DDL statements will be allowed to occur, but will be ignored by the transaction in that those DDL statements occur immediately and cannot be rolled back. Some DDL statements will cause an error when performed within a transaction, however. The following table discusses how DDL operations are treated by Advantage when performed within a transaction:

| DDL Operation | Behavior |
| Table/Index Open | Opening a table or an index within a transaction is ignored. If the transaction is rolled back, the table and/or index will remain open. |
| Table/Index Creation | Creating a table or an index within a transaction is ignored. If the transaction is rolled back, the table and/or index will remain in existence. |
| Index rebuild (reindex) | Reindexing an index file during a transaction is illegal. If the tables are reindexed during a transaction, an error will be generated. A reindex is illegal during a transaction because Advantage TPS may have multiple index keys referencing a single record during a transaction for data visibility purposes. A reindex of the index would cripple this functionality. |
| Table/Index Close | If a table, memo, and indexes associated with the table are closed within a transaction, but they were never modified during the transaction, the files will be closed. If they were modified in any way, the files will be cached closed. The file will not actually be closed until the transaction is committed or rolled back. |
| Table deletion | Deleting a table is illegal during a transaction. If it is attempted an error will be generated. Deleting a table is illegal during a transaction because Advantage TPS cannot "undelete" a table in the event of a transaction rollback. |
| Index deletion | Deleting an index (tag) from a compound index file or deleting an index file entirely is illegal during a transaction. If it is attempted an error will be generated. Deleting an index is illegal during a transaction because Advantage TPS cannot "undelete" a index in the event of a transaction rollback. |
| Pack or Zap | Packing or zapping a file during a transaction is illegal. If a pack or zap operation is attempted during a transaction, an error will be generated. Packing or zapping a file is illegal during a transaction because Advantage TPS cannot "unpack" or "unzap" a file in the event of a transaction rollback. |

 

The Advantage OLE DB Provider does not implement the ITransactionObject interface. A consumer attempt to retrieve a reference on the interface returns E\_NOINTERFACE.

The following example uses ITransactionLocal.

 

// Interfaces used in the example.

IDBCreateSession \*pIDBCreateSession = NULL;

ITransaction \*pITransaction = NULL;

IDBCreateCommand \*pIDBCreateCommand = NULL;

IRowset \*pIRowset = NULL;

HRESULT hr;

 

// Get the command creation and local transaction interfaces for the

// session.

if ( FAILED( hr = pIDBCreateSession->CreateSession( NULL,

IID\_IDBCreateCommand,

(IUnknown\*\*) &pIDBCreateCommand ) ) )

{

// Process error from session creation. Release any references and

// return.

}

 

if ( FAILED( hr = pIDBCreateCommand->QueryInterface(

IID\_ITransactionLocal,

(void\*\*) &pITransaction ) ) )

{

// Process error. Release any references and return.

}

 

// Start the local transaction.

if ( FAILED( ( (ITransactionLocal\*) pITransaction)->StartTransaction(

ISOLATIONLEVEL\_READCOMMITTED,

0, NULL, NULL ) ) )

{

// Process error from StartTransaction. Release any references and

// return.

}

 

// Get data into a rowset, and then update the data. Functions are not

// illustrated in this example.

if ( FAILED( hr = ExecuteCommand( pIDBCreateCommand, &pIRowset ) ) )

{

// Release any references and return.

}

 

// If rowset data update fails, terminate the transaction--else

// commit. The example doesn't retain the rowset.

if ( FAILED( hr = UpdateDataInRowset( pIRowset, bDelayedUpdate ) ) )

{

// Get error from update, then terminate.

pITransaction->Abort( NULL, FALSE, FALSE );

}

else

{

if ( FAILED( hr = pITransaction->Commit( FALSE, XACTTC\_SYNC, 0 ) ) )

{

// Get error from failed commit.

}

}

 

if ( FAILED( hr ) )

{

// Update of data or commit failed. Release any references and

// return.

}

 

// Release any references and continue.
