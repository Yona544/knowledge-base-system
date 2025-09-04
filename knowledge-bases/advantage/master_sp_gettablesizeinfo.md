sp\_GetTableSizeInfo




Advantage Database Server 12  

sp\_GetTableSizeInfo

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_GetTableSizeInfo  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_GetTableSizeInfo Advantage SQL Engine master\_Sp\_GetTableSizeInfo Advantage SQL > System Procedures > Procedures > sp\_GetTableSizeInfo / Dear Support Staff, |  |
| sp\_GetTableSizeInfo  Advantage SQL Engine |  |  |  |  |

Retrieve information about the table and memo file size.

Syntax

sp\_GetTableSizeInfo( TableName,CHARACTER,515 );

Parameters

TableName (I)        Name (and optional path) of table

Output

The sp\_GetTableSizeInfo procedure returns a result set containing the following information for the specified table.

|  |  |  |  |
| --- | --- | --- | --- |
| Field Name | Field Type | Field Size | Description |
| TableHeaderSize | Integer | 4 | Length in bytes of the table header, which includes field information. |
| RecordLength | Integer | 4 | Length in bytes of a single record. |
| RawRecordCount | Integer | 4 | Number of all records in the table (including deleted records). |
| DeletedRecordCount | Integer | 4 | The number of deleted records in the table. Note that with DBF tables (non-ADT), computing the number of deleted records requires setting a filter on the table of the form "DELETED()=.F.". You can optimize that with a [binary index](master_binary_indexes.htm). If [DBF deleted records](master_xbase_deleted_records.htm) are being displayed, then the returned deleted count will be zero. |
| MemoHeaderSize | Integer | 4 | Length in bytes of the memo file header. Note that this does not necessarily represent the exact number of bytes before the first usable memo block depending on the block size that is in use. |
| MemoBlockSize | Integer | 4 | Length in bytes of a single memo block. |
| MemoBlockCount | Integer | 4 | The total number of memo blocks in the file (including orphaned and free memo blocks). |

Remarks

This procedure allows you to find out specific information that can help with maintenance decisions. For example, if the number of deleted records (DeletedRecordCount) is sufficiently large based on your application usage, you may choose to pack the table.

Or, for example, you could determine the physical file size of a table (TableHeaderSize + RecordLength \* RawRecordCount). The memo file size can be computed by multiplying the memo block size by the block count. Note that the actual memo file size may differ by a few bytes from the calculation when the data in the last block is less than the block size (common).

See Also

[Supported File Formats](ace_supported_file_formats.htm)