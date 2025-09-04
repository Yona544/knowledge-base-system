---
title: Master Sp Setstatementlimit
slug: master_sp_setstatementlimit
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_setstatementlimit.htm
source: Advantage CHM
tags:
  - master
checksum: 2b3dd4329b8ed6da1334914878151772ac45520c
---

# Master Sp Setstatementlimit

sp\_SetStatementLimit

sp\_SetStatementLimit

Advantage SQL Engine

| sp\_SetStatementLimit  Advantage SQL Engine |  |  |  |  |

Set the current connection's SQL statement limit.

Syntax

sp\_SetStatementLimit( Limit, INTEGER )

Parameters

| Limit (I) | The maximum number of statements allowed on the current connection. If Limit is specified as zero, then the limit is disabled. |

Output

None

Remarks

Beginning with v12 of Advantage, each connection is, by default, limited to 50 active SQL statements. If a single connection reaches that limit, subsequent attempts to create new SQL statements will result in a [7216](error_7216_query_limit_exceede.md) error being returned.  The purpose for the limit is to help with resource management. Many development environments (e.g., those without automatic garbage collection) require that resources such as statement handles be closed when the application is finished with them. If they are not closed, then it results in a resource leak. The SQL statement handles are reclaimed when the connection is released. But if the connection stays active for some time and multiple statement handles are leaked, it can result in using a large number of server-side resources unnecessarily.

The system procedure sp\_SetStatementLimit allows this limit to be modified if the current connection needs to be able to have a larger number of SQL statements active at the same time. The limit for the current connection can be completely removed by calling the function with zero (0) as the parameter.

The default setting for the server is controlled by the configuration parameter [SQL\_STATEMENT\_LIMIT](master_sp_setstatementlimit.md).

See Also

[sp\_mgGetConfigInfo](master_sp_mggetconfiginfo.md)

[SQL\_STATEMENT\_LIMIT](master_sql_statement_limit.md)

[sp\_mgSetConfigValue](master_sp_mgsetconfigvalue.md)
