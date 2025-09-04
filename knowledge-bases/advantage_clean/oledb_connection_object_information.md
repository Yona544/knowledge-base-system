---
title: Oledb Connection Object Information
slug: oledb_connection_object_information
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_connection_object_information.htm
source: Advantage CHM
tags:
  - oledb
checksum: d35b944e68928335c8db20f123304ba8119efb75
---

# Oledb Connection Object Information

Connection Object Information

Connection Object Information

Advantage OLE DB Provider (for ADO)

| Connection Object Information  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The following tables list the features available with a Connection object opened with this provider.

Availability of standard ADO 2.1 Connection methods:

| Method | Supported? | Comments |
| BeginTrans | Yes | Distributed transactions not supported. If any record inserts/updates/deletes are pending, they will be flushed to the underlying database before the transaction is started. This method ignored if the Advantage ServerType is ADS\_LOCAL SERVER. |
| Cancel | No | Asynchronous connections not supported. |
| Close | Yes |  |
| CommitTrans | Yes | If any record inserts/updates/deletes are pending, they will be flushed to the underlying database before the transaction is committed. This method ignored if the Advantage ServerType is ADS\_LOCAL SERVER. |
| Execute | Yes | Executing asynchronous commands is not supported. The parameters RecordsAffected and Parameters are both fully supported. |
| Open | Yes | Opening tables asynchronously is not supported. |
| OpenSchema | Yes | adSchemaProviderTypes, adSchemaTables, adSchemaIndexes, adSchemaColumns, adSchemaCatalogs, adSchemaPrimaryKeys, adSchemaProcedures, adSchemaReferentialConstraints, adSchemaTableConstraints, adSchemaTablePrivileges, and adSchemaViews Schema Recordsets available. |
| RollbackTrans | Yes | If any record inserts/updates/deletes are pending, they will be cancelled before the transaction is aborted. This method ignored if the Advantage ServerType is ADS\_LOCAL SERVER. |

Availability of standard ADO 2.1 Connection properties:

| Property | Availability | Comments |
| Attributes | read/write |  |
| CommandTimeout | read/write | Due to limitations within ADO, this property is completely ignored. Command objects that are associated with this Connection object do not inherit the CommandTimeout property from the Connection object. Specifying a command timeout value is supported by the Advantage OLE DB Provider, but is must be specified via each individual Command.CommandTimeout property. |
| ConnectionString | read/write |  |
| ConnectionTimeout | read/write | The connection timeout is ignored. |
| CursorLocation | read/write | Client cursors will use the ADO Client Cursor Engine. Use of Client cursors can allow for functionality such as disconnected Recordsets, but be aware that Client cursors can be very slow initially because every single record in the rowset/cursor is read over to the client when the rowset/cursor is first opened. |
| DefaultDatabase | not available |  |
| IsolationLevel | always adXactReadCommitted |  |
| Mode | read/write | See Mode property value table below for details. |
| Provider | read/write |  |
| State | always adStateClosed  or adStateOpen | Asynchronous operations are not supported. |
| Version | read-only |  |

The Advantage OLE DB Provider interprets the Mode property values as follows:

| Value | Description |
| adModeRead | Open files in the database with read-only permissions. |
| adModeReadWrite | Open files in the database with read/write permissions. Same result as adModeWrite. This Mode is the default if no Mode is specified. |
| adModeWrite | Open files in the database with read/write permissions. Same result as adModeReadWrite. |
| adModeShareDenyNone | Open files in the database for "shared" used. Neither read nor write access to those files in the database is denied to others. |
| adModeShareDenyRead | Open files in the database for "exclusive" use. Prevents others from opening those files in the database. Same result as adModeShareExclusive. This mode is only available when the command type (as specified in the Command object's CommandType property, as an option in the Command object's Execute method, as an option in the Connection object's Execute method, or as an option in the Recordset object's Open method) is adCmdTableDirect. This Mode is ignored if the command type is specified as adCmdUnspecified, adCmdText, adCmdTable, or adCmdStoredProc. |
| adModeShareDenyWrite | This value is ignored. The default Mode, adModeReadWrite, will be used if this Mode is the only one specified. |
| adModeShareExclusive | Open files in the database for "exclusive" use. Prevents others from opening those files in the database. Same result as adModeShareDenyRead. This mode is only available when the command type (as specified in the Command object's CommandType property, as an option in the Command object's Execute method, as an option in the Connection object's Execute method, or as an option in the Recordset object's Open method) is adCmdTableDirect. This Mode is ignored if the command type is specified as adCmdUnspecified, adCmdText, adCmdTable, or adCmdStoredProc. |

The Advantage OLE DB Provider cannot use server side cursors to support the multiple-rowsets result generated by many commands. If a consumer requests a Recordset requiring server cursor support, an error occurs if the command text used generates more than a single recordset as its result.
