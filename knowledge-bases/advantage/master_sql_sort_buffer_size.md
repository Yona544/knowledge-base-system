SQL Sort Buffer Size




Advantage Database Server 12  

SQL Sort Buffer Size

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| SQL Sort Buffer Size  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - SQL Sort Buffer Size Advantage Database Server master\_Sql\_sort\_buffer\_size Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| SQL Sort Buffer Size  Advantage Database Server |  |  |  |  |

Default = 8192 Kbytes. Range = 1 - 1048576 Kbytes.

Keyword = SQL\_SORT\_BUFFER

This configuration parameter controls the maximum amount of memory that the query engine will use per connection when sorting data for operations such as GROUP BY, DISTINCT, etc. The buffer size may be adjusted to improve sorting performance at the cost of additional memory usage during query execution.

See Also

[Index Sort Buffer Size](master_index_sort_buffer_size_z_.htm)