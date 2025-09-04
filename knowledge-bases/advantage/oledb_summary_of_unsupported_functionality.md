Summary of Unsupported Functionality




Advantage Database Server 12  

Summary of Unsupported Functionality

Advantage OLE DB Provider (for ADO)

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Summary of Unsupported Functionality  Advantage OLE DB Provider (for ADO) |  |  | Feedback on: Advantage Database Server 12 - Summary of Unsupported Functionality Advantage OLE DB Provider (for ADO) oledb\_Summary\_of\_unsupported\_functionality Advantage OLE DB Provider (for ADO) > Low Level OLE DB Information > Unsupported Functionality > Summary of Unsupported Functionality / Dear Support Staff, |  |
| Summary of Unsupported Functionality  Advantage OLE DB Provider (for ADO) |  |  |  |  |

Asynchronous operations

The Advantage OLE DB Provider does not support obtaining connections, opening rowsets, executing commands, aborting transactions, or committing transactions asynchronously. If an asynchronous operation is requested, it will be ignored.

Multiple Rowset Results

The Advantage OLE DB Provider does not support returning multiple rowset results with commands when using server-side cursors.

Transactions

The Advantage Database Server supports local transactions. That is, transactions that exist on a single server upon which the Advantage Database Server is running. Advantage does not currently support distributed transactions.

The only transaction isolation levels supported by Advantage are Read Committed and Cursor Stability. If a different transaction isolation level is specified when starting a transaction, an error will be returned.

The Advantage OLE DB Provider only supports transactions when accessing data via the Advantage Database Server. If the Advantage Local Server is being used (because the Advantage ServerType property was set to ADS\_LOCAL\_SERVER), all transaction operations will be ignored. The application will not receive an error when starting, committing, or aborting transactions, but those operations will simply be ignored.

Cursor Types

Advantage does not completely obey the CursorType setting. If a forward-only cursor is specified (adOpenForwardOnly), Advantage will create a forward-only cursor. But if any other cursor type is specified, then Advantage will create either a dynamic or static cursor and set the CursorType property appropriately. When opening a table directly (adCmdTableDirect), the cursor type will be dynamic if adOpenForwardOnly is not specified. When using a command object and an SQL statement and a cursor type other than adOpenForwardOnly is specified, then the Advantage SQL engine will create a static or dynamic cursor based on the SQL statement type.

SQL Parameters

Advantage does support input parameters in SQL statements. Advantage does not support output parameters in SQL statements, however.

OLE DB/ADO Conformance Level

The Advantage OLE DB Provider is an OLE DB version 2.1-compliant provider. Thus, it is also ADO version 2.1-compliant. Any new interfaces, objects, methods, properties, etc. available in OLE DB or ADO v2.5 or greater are not supported in the Advantage OLE DB Provider.

Delayed/Batch Updates

The Advantage OLE DB Provider supports both Delayed and Immediate Update Modes with server-side cursors. The Advantage OLE DB Provider supports only one pending row update/insert/deletion when in Delayed (or Batch) Update Mode with server-side cursors, however. Thus, multiple columns in a single row can be updated before that entire row is flushed to the data source. But if a row has an update, insert, or deletion pending, and the current row position is changed, that updated/inserted/deleted row will be automatically flushed to the data source when the record position changes.

Table and Index Creation and Deletion

The Advantage OLE DB Provider supports creating tables and indexes via the SQL statements CREATE TABLE and CREATE INDEX, respectively. The Advantage OLE DB Provider supports also supports deleting tables and indexes via the SQL statements DROP TABLE and DROP INDEX, respectively. Tables and indexes can also be easily created or restructured by using the Advantage Data Architect utility. But, the Advantage OLE DB Provider does not currently support the Session objects ITableDefinition or IIndexDefinition interfaces to create, modify, or delete tables or indexes.

SQL Syntax

Advantage SQL support consists of most of the SQL-92 standard with ODBC extensions. See [Supported SQL Statements](master_supported_sql_statements.htm) for detailed information on the SQL syntax supported (and not supported) by Advantage.

Client Cursor Support

The Advantage OLE DB Provider provides native support for Server-side cursors. Client-side cursors can be used with ADO and the Advantage OLE DB Provider, but the ADO Client Cursor Engine will manage those client cursors. Use of Client cursors can allow for functionality such as disconnected Recordsets, but be aware that Client cursors can be slow initially with very large Recordsets because every single record in the rowset/cursor is read over to the client when the rowset/cursor is first opened.

Timeouts

The Advantage OLE DB Provider does not recognize timeout values associated with obtaining a connection. If a timeout value is specified, it will be ignored.

Accessors

Optimized and ByRef accessors are not supported by the Advantage OLE DB Provider. Thus IAccessor::CreateAccessor will be unable to create an optimized or ByRef accessor.