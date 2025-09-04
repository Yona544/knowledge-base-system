---
title: Master Sp Gettables
slug: master_sp_gettables
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_gettables.htm
source: Advantage CHM
tags:
  - master
checksum: 3d6f4fbd29aa202b2a4af0e913b6cce03d761f10
---

# Master Sp Gettables

sp\_GetTables

sp\_GetTables

Advantage SQL Engine

| sp\_GetTables  Advantage SQL Engine |  |  |  |  |

Returns a result containing tables available on the current connection.

Syntax

EXECUTE PROCEDURE sp\_GetTables( catalog,Character,200;

schemaPattern, Character,200;

tableNamePattern, Character,255;

Types,memo; )

Parameters

| catalog (I) | A string representing a catalog or NULL. In most situations, this value should be NULL. |
| schemaPattern (I) | A string containing a schema pattern. Advantage does not currently support schemas and this value should be NULL. |
| tableNamePattern (I) | A string containing a table name pattern. Only tables that match this pattern will be included in the result set. If this value is NULL, all tables will be returned. |
| Types (I) | A semicolon-delimited list of table types to return. The current values supported by Advantage are "TABLE", "VIEW", "SYSTEM TABLE", and "LOCAL TEMPORARY". |

Output

The sp\_GetTables procedure will return a result set containing all tables that pass the input criteria. The result set has the following structure:

| Field Name | Field Type | Field Size | Description |
| TABLE\_CAT | CiCharacter | 200 | The catalog of the table. |
| TABLE\_SCHEM | CiCharacter | 200 | The schema of the table. Advantage does not currently support schemas, so this value will be NULL. |
| TABLE\_NAME | CiCharacter | 255 | The name of the table. |
| TABLE\_TYPE | CiCharacter | 17 | The type of the table, the current values supported by Advantage are "TABLE", "VIEW", "SYSTEM TABLE", and "LOCAL TEMPORARY". |
| REMARKS | MEMO | 9 | NULL or a comment on the table. |

Remarks

This stored procedure returns a list of available tables on the connection. With non-data dictionary bound connections, only tables in the same directory as the connection will be returned. With data dictionary bound connections, no free tables will be returned; only data dictionary bound tables will be returned.

String Patterns

String patterns allow the result set to be filtered using patterns containing wild card characters. The wild card characters are '%' (percent) and '\_' (underscore). The '%' character matches 0 or more characters, and the '\_' matches exactly one character.

Example

CREATE TABLE #Temp ( i integer );

CREATE TABLE #TempA2 ( i integer );

CREATE TABLE #TempA3 ( i integer );

CREATE TABLE #TempB4 ( i integer );

 

EXECUTE PROCEDURE sp\_GetTables( NULL, NULL, NULL, 'Local Temporary' );

See Also

[sp\_GetColumns](master_sp_getcolumns.md)
