AdsFlushFileBuffers




Advantage Database Server 12  

AdsFlushFileBuffers

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsFlushFileBuffers  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsFlushFileBuffers Advantage Client Engine ace\_Adsflushfilebuffers Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsFlushFileBuffers  Advantage Client Engine |  |  |  |  |

Flushes all cached record changes to disk.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsFlushFileBuffers (ADSHANDLE hTable); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or dynamic cursor. |

Remarks

AdsFlushFileBuffers forces all file buffers associated with the specified table to be written to disk. This operation flushes changes to the current record as well, similar to calling AdsWriteRecord or a record movement.

This API was designed to address the operating system behaviors of Windows when using the Advantage Local Server with files on a local hard drive. Windows will often cache file changes in buffers and not write them to disk for lengthy periods of time. When using Advantage Local Server to access tables on local hard drives, this means table inserts/updates are not always flushed to disk in a timely manner. This can lead to table corruption should the database connection be abnormally terminated.

Note This API has no effect when using a table handle on an Advantage Database Server connection.

 

Note This API will only work on read/write enabled tables and cursors. An error will be returned with any read-only handles.

Example

// Get a local server connection, open a table, append a new record,

// and then guarantee the file updates are flushed to disk.

 

AdsConnect60( "c:\\mydata", ADS\_LOCAL\_SERVER, NULL, NULL, ADS\_DEFAULT, &hConnect );

AdsOpenTable( hConnect, "c:\\mydata\\mytable.adt", NULL, ADS\_ADT, ADS\_ANSI, ADS\_DEFAULT,

ADS\_DEFAULT, ADS\_DEFAULT, &hTable );

AdsAppendRecord( hTable );

AdsSetField( hTable, "UID", "3456", 5 );

AdsSetField( hTable, "Misc", aucMemoBuff, aucMemoLen );

 

// This will flush the update of the inserted record as well as guarantee the write

// is flushed to disk.

AdsFlushFileBuffers( hTable );

 

AdsCloseTable( hTable );

AdsDisconnect( hConnect );