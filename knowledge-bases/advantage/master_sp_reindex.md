sp\_Reindex




Advantage Database Server 12  

sp\_Reindex

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_Reindex  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_Reindex Advantage SQL Engine master\_sp\_Reindex Advantage SQL > System Procedures > Procedures > sp\_Reindex / Dear Support Staff, |  |
| sp\_Reindex  Advantage SQL Engine |  |  |  |  |

Rebuilds all auto-open indexes associated with the given table.

 

Syntax

sp\_Reindex( TableName,CHARACTER,515,

          PageSize, INTEGER )

Parameters

|  |  |
| --- | --- |
| TableName (I) | Name of table to rebuild indexes on.  This can include path information for free tables if the table is in a different folder from the connection path. |
| PageSize (I) | The page size to use when rebuilding indexes on ADT tables. This is ignored for other table types. If the value 0 is given, the existing page size is used. Valid page sizes can be any value from 512 to 8192. Refer to [Index Page Size](master_index_page_size.htm) and [Index Key Size and Page Size Relationships](master_index_key_size_and_page_size_relationships.htm) for more information. Note that if the table is in an Advantage Data Dictionary, then only the administrator connection can be used to change the page size when reindexing a table. |

Remarks

sp\_Reindex rebuilds all auto-open indexes associated with the given table. Because the reindex operation requires exclusive access to the table, no other connections can have the table open when this is called.

Example

 

-- Rebuild all auto-open indexes on mytable with a page size of 1024

EXECUTE PROCEDURE sp\_Reindex( 'mytable.adt', 1024 );

See Also

[AdsReindex61](ace_adsreindex61.htm)

[sp\_CreateIndex](master_sp_createindex.htm)

[sp\_ReindexOnline](master_sp_reindexonline.htm)