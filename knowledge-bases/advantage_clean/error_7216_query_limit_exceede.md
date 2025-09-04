---
title: Error 7216 Query Limit Exceede
slug: error_7216_query_limit_exceede
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7216_query_limit_exceede.htm
source: Advantage CHM
tags:
  - error
checksum: d56c027724b03d081e2962812877e583866e6d07
---

# Error 7216 Query Limit Exceede

7216 SQL Statement Limit Exceeded

7216 SQL Statement Limit Exceeded

 

Advantage Error Guide

| 7216 SQL Statement Limit Exceeded     Advantage Error Guide |  |  |  |  |

Problem:  The configured SQL statement limit was exceeded.  Beginning with v12 of Advantage, the default number of SQL statements that a connection can obtain at a given time is 50. This limitation is intended to help application developers manage resources. In some development environments, it is possible to "leak" statement handles due to programming errors.

Solution:  It is possible to increase or disable the limit for a given connection by executing the SQL statement [sp\_SetStatementLimit](master_sp_setstatementlimit.md). Note that this must be executed on an existing statement handle if the error has already been encountered (the irony is not lost). The limit for the server itself can be changed by setting the [SQL\_STATEMENT\_LIMIT](master_sql_statement_limit.md) configuration parameter.
