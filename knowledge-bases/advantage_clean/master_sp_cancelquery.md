---
title: Master Sp Cancelquery
slug: master_sp_cancelquery
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_cancelquery.htm
source: Advantage CHM
tags:
  - master
checksum: 61e576a05b05214084c367e825f869e4e6231ebe
---

# Master Sp Cancelquery

sp\_CancelQuery

sp\_CancelQuery

Advantage SQL Engine

| sp\_CancelQuery  Advantage SQL Engine |  |  |  |  |

Cancels a query being processed by the Advantage Query Engine.

Syntax

sp\_CancelQuery( Query Number, Integer );

Parameters

| Query Number (I) | Number of the query to cancel. The query number is returned by sp\_GetSQLStatements. |

Output

None.

Remarks

sp\_CancelQuery terminates the execution of a query by another user. To terminate a query, the query must be being actively processed on a data dictionary connection. Query termination requires an administrative connection to the same data dictionary as the other user is connected to. Queries on non-data dictionary connections cannot be cancelled.

See Also

[sp\_GetSQLStatements](master_sp_getsqlstatements.md)
