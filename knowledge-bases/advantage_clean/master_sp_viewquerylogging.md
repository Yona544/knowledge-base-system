---
title: Master Sp Viewquerylogging
slug: master_sp_viewquerylogging
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_viewquerylogging.htm
source: Advantage CHM
tags:
  - master
checksum: d2b6ddaae27d256de26135027148394d49fb5de5
---

# Master Sp Viewquerylogging

sp\_ViewQueryLogging

sp\_ViewQueryLogging

Advantage SQL Engine

| sp\_ViewQueryLogging  Advantage SQL Engine |  |  |  |  |

Displays which connections are logging queries.

Syntax

sp\_ViewQueryLogging()

Parameters

| Database (O) | Fully qualified path to the data dictionary logging queries. |
| Table (O) | Fully qualified path to the table queries are being logged in. |

Remarks

sp\_ViewQueryLogging returns a result set of all connections currently logging queries.

See Also

[sp\_EnableQueryLogging](master_sp_enablequerylogging.md)

[sp\_DisableQueryLogging](master_sp_disablequerylogging.md)

[sp\_GetQueryLoggingResults](master_sp_getqueryloggingresults.md)
