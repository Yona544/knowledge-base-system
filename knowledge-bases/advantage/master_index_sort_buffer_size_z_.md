Index Sort Buffer Size (-Z)




Advantage Database Server 12  

Index Sort Buffer Size (-Z)

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Index Sort Buffer Size (-Z)  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Index Sort Buffer Size (-Z) Advantage Database Server master\_Index\_sort\_buffer\_size\_z\_ Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Index Sort Buffer Size (-Z)  Advantage Database Server |  |  |  |  |

Default = 32768 Kbytes. Range = 1 - 1048576 Kbytes.

Keyword = SORT\_BUFFER

The default Index Sort Buffer Size is large enough to build most indexes. The buffer size may be adjusted to improve sorting performance at the cost of additional memory usage during index builds. For the best performance, the sort buffer size can be calculated by: (index key size + 4) x Number of Records. For example, an index build on a character field of width 20 will require 24 bytes per record. To perform the entire sort in memory for a 1,000,000 record table would require a buffer of 24,000,000 bytes. The SORT\_BUFFER value would need to be at least 23438 to avoid using a temporary sort file (23,438 \* 1024 > 24,000,000).

The Index Sort Buffer Size is the MAXIMUM amount of memory per connection that the Advantage Database Server will use when building an index on the server. The Advantage Database Server may not use the entire Index Sort Buffer Size. It will only use as much memory as it needs. If there is not enough memory available on the server for the size of the calculated sort buffer, Advantage will adjust its sort buffer calculation downwards and will use only what memory is available.

If you are building full text search indexes (see [Full Text Search](master_full_text_search.htm)), it may be desirable to increase the sort buffer size because full text search indexes can have large numbers of keys. The initial sorting operation stores all keys including duplicates, which cannot be removed until the data is sorted. Normal (non-FTS) index builds generally have one key per record. FTS index builds have 0 or more keys (perhaps thousands) for each record.

See Also

[SQL Sort Buffer Size](master_sql_sort_buffer_size.htm)