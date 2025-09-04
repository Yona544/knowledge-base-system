---
title: Odbc Open File Cache
slug: odbc_open_file_cache
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: odbc_open_file_cache.htm
source: Advantage CHM
tags:
  - odbc
checksum: 65168c0c1282343290512c3fabe379c11290336f
---

# Odbc Open File Cache

Open File Cache

Open File Cache

| Open File Cache |  |  |  |  |

This numeric value determines the maximum number of unused file opens to cache. When tables are opened, the Advantage ODBC Driver keeps them open. This provides better performance by preventing the Driver from performing another open if another query uses one of the tables. The advantage of open file caching is increased performance. The disadvantage is that a user may receive a locking conflict even though no one appears to have the file open.

As a default, Open File Cache is set to 5. You can further increase performance by setting Open File Cache to a higher number, such as "10".
