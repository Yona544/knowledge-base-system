---
title: Master Sp Getsqlstatements
slug: master_sp_getsqlstatements
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_getsqlstatements.htm
source: Advantage CHM
tags:
  - master
checksum: a0a81ece4e5c5fe8673304d371301683e4980ca4
---

# Master Sp Getsqlstatements

sp\_GetSQLStatements

sp\_GetSQLStatements

Advantage SQL Engine

| sp\_GetSQLStatements  Advantage SQL Engine |  |  |  |  |

Returns a result set containing all active queries in the database.

Syntax

sp\_GetSQLStatements ()

Parameters

None.

Output

The sp\_GetSQLStatements procedure will return a result set containing all queries that are open or active in the database. The result set has the following structure.

| Field Name | Field Type | Field Size | Description |
| Query Number | Integer | 4 | A unique identifier for the query. |
| Active | Logical | 1 | True if the server is actively processing the statement. |
| Percent Complete | Double | 8 | The estimated percentage of the query that has been completed. |
| Connection Name | Character | 100 | Name of the computer executing the query. |
| Database User | Character | 100 | Name of the database user executing the query. |
| Database | Character | 255 | Name of the database the user is connected to. |
| Query | Memo | 9 | The current SQL statement that is being executed. |
| Is Script | Logical | 1 | If more than one SQL statement is being processed in the current request. |
| Full Script | Memo | 9 | The complete SQL script sent to the server. This field will be NULL if only a single query is being executed. |
| Start Time | Time | 4 | Time on the server when the query was started. |
| Seconds Until Finished | Integer | 4 | Estimated number of seconds until the query is finished executing. |
| ApplicationID | CiCharacter | 70 | Application ID for the connected user.  See [sp\_SetApplicationID](master_sp_setapplicationid.md). |

Remarks

Prior to v11, sp\_GetSQLStatements would return all open statements on the server.  As of v11, this has been restricted to limit the returned statements to the current database. In addition, the use of this procedure requires DB:Admin membership. Exceptions to this include:

- Free connections can obtain all active SQL statements on other free connections.

- Advantage Local Server connections are not restricted to the same database because the process boundary already limits the statements to those owned by the application.

See Also

[sp\_CancelQuery](master_sp_cancelquery.md)
