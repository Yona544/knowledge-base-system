---
title: Master Sql Statement Limit
slug: master_sql_statement_limit
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sql_statement_limit.htm
source: Advantage CHM
tags:
  - master
checksum: 944d39ad9815e1b1d8513783cc94c3b698fb3b69
---

# Master Sql Statement Limit

SQL Statement Limit

SQL Statement Limit

Advantage Database Server

| SQL Statement Limit  Advantage Database Server |  |  |  |  |

Default = 50

Keyword = SQL\_STATEMENT\_LIMIT

This configuration parameter controls the maximum number of SQL statements that a single connection can keep open at one time. To completely remove the limitation for all connections on the server, this value can be set to zero (0). To modify the limit for a specific connection, an application call [sp\_SetStatementLimit](master_sp_setstatementlimit.md).

See Also

[sp\_SetStatementLimit](master_sp_setstatementlimit.md)

[7216 Error](error_7216_query_limit_exceede.md)
