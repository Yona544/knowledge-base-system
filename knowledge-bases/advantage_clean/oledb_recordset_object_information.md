---
title: Oledb Recordset Object Information
slug: oledb_recordset_object_information
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_recordset_object_information.htm
source: Advantage CHM
tags:
  - oledb
checksum: 10cacd36d97f3e04db14168692e9cc799b67098c
---

# Oledb Recordset Object Information

Recordset Object Information

Recordset Object Information

Advantage OLE DB Provider (for ADO)

| Recordset Object Information  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The following tables list the features available with a Recordset object opened with this provider. For more detailed information about Recordset behavior for your provider configuration, run the Supports method.

Availability of standard ADO 2.1 Recordset methods:

| Method | Supported? | Comments |
| AddNew | Yes | Batch adds are supported for current record only when using server-side cursors. |
| Cancel | No | Asynchronous Recordset opens are not supported. |
| CancelBatch | Yes | Batch update mode is supported for current record only when using server-side cursors. |
| CancelUpdate | Yes |  |
| Clone | Yes |  |
| Close | Yes |  |
| CompareBookmarks | Yes |  |
| Delete | Yes | Batch deletes are supported for current record only when using server-side cursors. |
| Find | Yes | Does a sequential search for the specified data in the current Recordset. Since the search is sequential, this method can take a long time to complete if the Recordset is large and the search condition results in few matches. Use the Seek method to perform a very fast search. |
| GetRows | Yes |  |
| GetString | Yes |  |
| Move | Yes | When using server-side cursors, a Move method will move the current Recordset pointer via an Advantage [Skip](master_skip_movement.md) operation. If the number of records to Move is a large value (e.g., several hundreds or thousands of records) in a large table, this operation may be slow. To move to a specific record in a Recordset, use the Recordset.Bookmark property. |
| MoveFirst | Yes | When using server-side cursors, a MoveFirst method will move the current Recordset pointer to the first record in the recordset via an Advantage [Go Top](master_go_top_movement.md) operation. This operation should be very fast and efficient. |
| MoveLast | Yes | When using server-side cursors, a MoveLast method will move the current Recordset pointer to the last record in the recordset via an Advantage [Go Bottom](master_go_bottom_movement.md) operation. Unless this method causes an SQL static cursor to be dynamically populated, this operation should be very fast and efficient. |
| MoveNext | Yes | When using server-side cursors, a MoveNext method will move the current Recordset pointer to the next record in the recordset via an Advantage [Skip](master_skip_movement.md) operation. This operation should be very fast and efficient. |
| MovePrevious | Yes | When using server-side cursors, a MovePrevious method will move the current Recordset pointer to the previous record in the recordset via an Advantage [Skip](master_skip_movement.md) operation. This operation should be very fast and efficient. |
| NextRecordset | No | Multiple Recordsets are not supported with server-side cursors. |
| Open | Yes | Asynchronous opens are not supported. |
| Requery | Yes |  |
| Resync | Yes |  |
| Save | No | Save functionality is not supported with server-side cursors. |
| Seek | Yes | When using server-side cursors, a Seek method will search the index of the current Recordset to quickly locate the row that matches the specified value, and changes the current record position to that record. This method is only supported when the Recordset has been opened directly on a table (with a command type of adCmdTableDirect) or has been opened with an SQL query that results in a live cursor. This operation is performed via an Advantage [Seek](master_seek_movement.md) operation. This operation should be very fast and efficient. |
| Supports | Yes |  |
| Update | Yes |  |
| UpdateBatch | Yes | Batch update mode supported for current record only when using server-side cursors. |

Availability of standard ADO 2.1 Recordset properties:

| Property | Availability | Comments |
| AbsolutePage | read/write |  |
| AbsolutePosition | read/write |  |
| ActiveCommand | read-only |  |
| ActiveConnection | read/write |  |
| BOF | read-only |  |
| Bookmark | read/write | When using server-side cursors, setting the Bookmark property will reposition the current Recordset pointer via an Advantage [Go To](master_go_to_movement.md) operation. This operation is very fast and is the recommended means to move to a specific record in a Recordset, as opposed to using the Recordset.Move method, which can be slow. Setting the bookmark will position to the physical record number in the underlying Advantage table; it will not set the bookmark to a logical or virtual record position. With Advantage, it is not necessary to position to a record and get a bookmark before you can set the bookmark at some later time. In other words, you can perform a "go to" operation by setting the Bookmark property at any time. For example, Recordset.Bookmark = CDbl(5) will position the pointer to the 5th record in the underlying table. When using Visual Basic and performing a Go To operation by setting the Bookmark to a literal value, it is often best to use a literal value that is a double. When getting the Bookmark property and later setting the Bookmark property to that stored value, using a variant seems to work well. |
| CacheSize | read/write | Corresponds to Advantages Read Ahead Record Caching. |
| CursorLocation | read/write | Client cursors will use the ADO Client Cursor Engine. Use of Client cursors can allow for functionality such as disconnected Recordsets, but be aware that Client cursors can be very slow initially because every single record in the rowset/cursor is read over to the client when the rowset/cursor is first opened. |
| CursorType | read/write | Server-side cursor types will be forward-only, dynamic, or static. If adOpenForwardOnly is specified as the cursor type, the Advantage OLE DB provider will use an aggressive read-ahead cache value that can improve performance when reading through the table. Forward-only cursors may be useful when reading through a table in a single pass for batch processing operations. Note that forward-only cursors may be edited, but this negates the benefits; your application should probably use a dynamic cursor if you plan to edit it. See [Read-Ahead Record Caching](master_read_ahead_record_caching.md) for more information. If another cursor type is specified, the Advantage OLE DB provider will default to the type that matches the underlying rowset (either dynamic or static based on the SQL query used to specify the cursor). Please note that the default server type (if not specified) is forward-only. Some data grids such as the Microsoft ADO DataGrid require scrollable cursors and will not display a forward-only cursor. |
| DataMember | read/write |  |
| DataSource | read/write |  |
| EditMode | read-only |  |
| EOF | read-only |  |
| Filter | read/write | The filter property can be used to apply filter conditions to an open recordset. It results in setting a server-side Advantage Optimized Filter. ADO processes the filter condition before sending it to the Advantage OLE DB Provider, therefore, the filter condition must adhere to the ADO specification. The following lists some of the rules for ADO filter strings.  |  |  | | --- | --- | | · | Field names that have spaces in them must be enclosed in square brackets. |  |  |  | | --- | --- | | · | Operators must be one of the following: <, >, <=, >=, <>, =, or LIKE. |  |  |  | | --- | --- | | · | String values must be enclosed in single quotes. |  |  |  | | --- | --- | | · | If a string contains single quotes, use two of them in succession to represent a single quote in the filter value. |  |  |  | | --- | --- | | · | ADO does not define any precedence between AND and Or operators, therefore you must use parentheses to specify the grouping of conditions. |  |  |  | | --- | --- | | · | The LIKE operator can be used to perform inexact string matching (in conjunction with an asterisk in the value). For example, to find values that begin with some string, you can specify a filter condition such as: |  lastname LIKE Wi\*  This will find all records where the lastname field begins with the characters Wi. If the asterisks are at the beginning and end of the value, the search will be for values that contain the characters.  lastname LIKE \*mit\*  This will find all records where the lastname field contains the character sequence mit.  |  |  | | --- | --- | | · | Date, time, and timestamp values must be enclosed in # characters. For example: |  entrytime = #January 21, 1985 2:36pm#  entrytime = #1/21/1985 14:36:00#  ADO provides for a wide range and flexibility in specifying dates and times. Refer to the ADO specification for details.  The following lists some filter limitations specific to the Advantage OLE DB Provider.  |  |  | | --- | --- | | · | Memo, raw, and BLOB fields cannot be filtered. |  |  |  | | --- | --- | | · | A single filter condition cannot contain both exact and inexact string matching. For example, this filter is not valid: |  lastname = Smith or lastname LIKE Sch\*  Advantage does not allow these two types of matching to be used at the same time in the same filter expression. They both result in the same Advantage operator (=) but use a different table-wide setting to control the type of string matching. The following expression is valid:  lastname = Smith or lastname LIKE \*ch\*  The Advantage operator that results from the LIKE operator in this case (containment) is different and does not require the table-wide setting. |
| Index | read/write | When using server-side cursors, the Index property allows you to specify the currently active index order in which the Recordset is sorted. This property is only supported when the Recordset has been opened directly on a table (with a command type of adCmdTableDirect) or has been opened with an SQL query that results in a live cursor. This property will automatically be set to the default index specified in the [Advantage Data Dictionary](master_advantage_data_dictionary.md) if a default index is specified. |
| LockType | read/write | adLockBatchOptimistic indicates optimistic batch updates -- use this value to enter batch update mode with client-side cursors. adLockOptimistic indicates optimistic locking, record by record -- the provider uses optimistic locking, locking records only when you call the Update method. adLockPessimistic indicates pessimistic locking, record by record -- the provider does what is necessary to ensure successful editing of the records, usually by locking records at the data source immediately after editing. adLockReadOnly indicates read-only records -- you cannot alter the data.  If the CursorLocation property is adUseClient (i.e., when using a client-side cursor), the ADO Client Cursor Engine handles all locking. Use adLockBatchOptimistic for batch mode updates, adLockOptimistic for immediate mode updates, and adLockReadOnly for read-only Recordsets. The adLockPessimistic setting is not supported if the CursorLocation property is set to adUseClient.  If the CursorLocation property is adUseServer (i.e., when using a server-side cursor), Advantage itself handles all locking. Advantage supports read-only Recordsets and immediate mode updateable Recordsets with server-side cursors. If the LockType is specified as adLockReadOnly, a read-only Recordset will result. If the LockType is specified as adLockBatchOptimistic, adLockOptimistic, or adLockPessimistic, an immediate-mode updateable Recordset will result. After a Recordset has been opened using a server-side cursor, Advantage will return adLockReadOnly for read-only Recordsets, and adLockPessimistic for immediate-mode updateable Recordsets. |
| MarshalOptions | not available |  |
| MaxRecords | read-only | Setting the MaxRecords is not supported. |
| PageCount | read-only |  |
| PageSize | read/write |  |
| RecordCount | read-only |  |
| Sort | read/write | Supported with client cursors with ADO Client Cursor Engine. |
| Source | read/write |  |
| State | adStateClosed or adStateOpen only | Asynchronous operations are not supported. |
| Status | read-only |  |
| StayInSync | read/write |  |

The Advantage OLE DB Provider supports both Batch and Immediate Update Modes with server-side cursors. Batch Update Mode is supported for the current record only when using server-side cursors. Thus, you can update multiple fields in a single record without each field update being flushed to the underlying database. But, a "batch" of record updates can consist of no more than 1 record. If a row has an update, insert, or deletion pending, and the current row position is changed, that updated/inserted/deleted row will be automatically flushed to the underlying database when the record position changes. Since a "batch" of record updates can consist of no more than one record, the CancelUpdate and a CancelBatch methods behave identically when in Batch Update Mode with server-side cursors. Batch update mode behaves as expected when using client-side cursors.
