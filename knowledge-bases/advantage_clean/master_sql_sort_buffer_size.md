---
title: Master Sql Sort Buffer Size
slug: master_sql_sort_buffer_size
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sql_sort_buffer_size.htm
source: Advantage CHM
tags:
  - master
checksum: f09c529c58af1240f887225d6adaa7c58b3b7555
---

# Master Sql Sort Buffer Size

SQL Sort Buffer Size

SQL Sort Buffer Size

Advantage Database Server

| SQL Sort Buffer Size  Advantage Database Server |  |  |  |  |

Default = 8192 Kbytes. Range = 1 - 1048576 Kbytes.

Keyword = SQL\_SORT\_BUFFER

This configuration parameter controls the maximum amount of memory that the query engine will use per connection when sorting data for operations such as GROUP BY, DISTINCT, etc. The buffer size may be adjusted to improve sorting performance at the cost of additional memory usage during query execution.

See Also

[Index Sort Buffer Size](master_index_sort_buffer_size_z_.md)
