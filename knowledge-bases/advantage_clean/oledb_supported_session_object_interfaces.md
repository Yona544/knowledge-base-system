---
title: Oledb Supported Session Object Interfaces
slug: oledb_supported_session_object_interfaces
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_supported_session_object_interfaces.htm
source: Advantage CHM
tags:
  - oledb
checksum: 538dac6ad30d5ec6e81f9b34b02fff178acb8b50
---

# Oledb Supported Session Object Interfaces

Supported Session Object Interfaces

Supported Session Object Interfaces

Advantage OLE DB Provider (for ADO)

| Supported Session Object Interfaces  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The Session object is supported with the Advantage OLE DB Provider. Below is the list of supported interfaces in the Session object. Generally, for each interface listed, all the methods will be supported.

Session Object

| IGetDataSource | IOpenRowset | ISessionProperties | IDBCreateCommand |
| IDBSchemaRowset | ITransaction | ITransactionLocal | ISupportErrorInfo |

Implementation Details by Method

The Advantage OLE DB Provider supports IGetDataSource interface member functions as described in the following table.

| Member Function | Description |
| GetDataSource | Returns an interface pointer on the data source object that created this session. |

The Advantage OLE DB Provider supports IOpenRowset interface member functions as described in the following table.

| Member Function | Description |
| OpenRowset | Opens and returns a rowset that includes all rows from a single base table or index. |

The Advantage OLE DB Provider supports ISessionProperties interface member functions as described in the following table.

| Member Function | Description |
| GetProperties | Returns the list of properties in the Session property group that are currently set on the session. |
| SetProperties | Sets properties in the Session property group. |

The Advantage OLE DB Provider supports IDBCreateCommand interface member functions as described in the following table.

| Member Function | Description |
| CreateCommand | Creates a new command. |

The Advantage OLE DB Provider supports IDBSchemaRowset interface member functions as described in the following table.

| Member Function | Description |
| GetRowset | Returns a schema rowset. |
| GetSchemas | Returns a list of schema rowsets accessible by GetRowset. The current supported schema rowsets are DBSCHEMA\_TABLES, DBSCHEMA\_COLUMNS, DBSCHEMA\_INDEXES, and DBSCHEMA\_PROVIDER\_TYPES. |

The Advantage OLE DB Provider supports ITransaction interface member functions as described in the following table.

| Member Function | Description |
| Abort | Aborts a transaction. If any record inserts/updates/deletes are pending, they will be cancelled before the transaction is aborted. This method is ignored if the Advantage ServerType is ADS\_LOCAL SERVER. |
| Commit | Commits a transaction. If any record inserts/updates/deletes are pending, they will be flushed to the underlying database before the transaction is committed. This method is ignored if the Advantage ServerType is ADS\_LOCAL SERVER. |
| GetTransactionInfo | Returns information about a transaction. |

The Advantage OLE DB Provider supports ITransactionLocal interface member functions as described in the following table.

| Member Function | Description |
| GetOptionsObject | Returns an object that can be used to specify configuration options for a subsequent call to StartTransaction. GetOptionsObject will currently always return E\_FAIL because transaction options objects are not currently supported. |
| StartTransaction | Begins a new transaction. If any record inserts/updates/deletes are pending, they will be flushed to the underlying database before the transaction is started. This method is ignored if the Advantage ServerType is ADS\_LOCAL SERVER. |

The Advantage OLE DB Provider supports ISupportErrorInfo interface member functions as described in the following table.

| Member Function | Description |
| InterfaceSupportsErrorInfo | Indicates whether a specific OLE DB interface can return OLE DB error objects. |
