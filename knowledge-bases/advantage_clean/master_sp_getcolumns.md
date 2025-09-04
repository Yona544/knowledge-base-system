---
title: Master Sp Getcolumns
slug: master_sp_getcolumns
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_getcolumns.htm
source: Advantage CHM
tags:
  - master
checksum: 477cf9078539bf53f335b9f3cc708d933354e468
---

# Master Sp Getcolumns

sp\_GetColumns

sp\_GetColumns

Advantage SQL Engine

| sp\_GetColumns  Advantage SQL Engine |  |  |  |  |

Returns a result containing all columns in tables available on the current connection.

Syntax

EXECUTE PROCEDURE sp\_GetColumns( catalog,CHARACTER,200;

schemaPattern,CHARACTER,200;

tableNamePattern,CHARACTER,255;

columnNamePattern,CHARACTER,200 )

Parameters

| catalog (I) | A string representing a catalog or NULL. In most situations, this value should be NULL. |
| schemaPattern (I) | A string containing a schema pattern. Advantage does not currently support schemas and this value should be NULL. |
| tableNamePattern (I) | A string containing a table name pattern. Only tables that match this pattern will be included in the result set. If this value is NULL, all tables will be returned. |
| columnNamePattern (I) | A string containing a column name pattern. Only columns that match this pattern will be included in the result set. |

Output

The sp\_GetColumns procedure will return a result set containing all columns that pass the input criteria. The result set has the following structure.

| Field Name | Field Type | Field Size | Description |
| TABLE\_CAT | CiCharacter | 200 | The catalog of the table. |
| TABLE\_SCHEM | CiCharacter | 200 | The schema of the table. Advantage does not currently support schemas, so this value will be NULL. |
| TABLE\_NAME | CiCharacter | 255 | The name of the table. |
| COLUMN\_NAME | CiCharacter | 200 | The name of the column. |
| DATA\_TYPE | SHORTINT | 4 | The ODBC data of the column. |
| TYPE\_NAME | CiCharacter | 20 | The SQL type name of the column. |
| COLUMN\_SIZE | INTEGER | 4 | Maximum size of the column. |
| BUFFER\_LENGTH | INTEGER | 4 | The length of data in bytes of data transferred on ODBC calls to SQLGetData, SQLFetch, and SQLFetchScroll. |
| DECIMAL\_DIGITS | SHORTINT | 2 | Total number of significant digits to the right of the decimal place. |
| NUM\_PREC\_RADIX | INTEGER | 4 | The radix of the column. |
| NULLABLE | SHORTINT | 2 | The column is 0 if NULLs are not allowed, 1 if NULLs are allowed, and 2 if the state of the column is unknown. |
| REMARKS | MEMO | 9 | Description of the column. |
| COLUMN\_DEF | MEMO | 9 | Default value of the column. |
| SQL\_DATA\_TYPE | INTEGER | 4 | ODBC datatype with specific information on date and datetime fields. |
| SQL\_DATETIME\_SUB | INTEGER | 4 | Subtype for datatype fields. |
| CHAR\_OCTET\_LENGTH | INTEGER | 4 | The maximum length in bytes of a character or BLOB field. |
| ORDINAL\_POSITION | INTEGER | 4 | The position of the column in the table starting with 1. |
| IS\_NULLABLE | CHAR | 4 | "NO" if the column does not include NULLs, "YES" if the column could include NULLs. The column returns NULL if the state is unknown. |
| NOCPTRANS | SHORTINT | 2 | A value of 1 indicates the field is a VFP field created with the NOCPTRANS option (no code page translations). |

Remarks

This stored procedure returns a result set containing all columns in the tables on this connection that pass the input criteria. With non-data dictionary bound connections, only tables in the same directory as the connection will be returned. With data dictionary bound connections, no free tables will be returned; only data dictionary bound tables will returned.

String Patterns

String patterns allow the result set to be filtered using patterns containing wild card characters. The wild card characters are '%' (percent) and '\_' (underscore). The '%' character matches 0 or more characters, and the '\_' matches exactly one character.

Example

CREATE TABLE #Temp ( i integer );

CREATE TABLE #TempA2 ( i integer );

CREATE TABLE #TempA3 ( i integer );

CREATE TABLE #TempB4 ( i integer );

 

DECLARE GetColumns CURSOR AS EXECUTE PROCEDURE sp\_GetColumns( NULL, NULL, '#%', NULL );

See Also

[sp\_GetTables](master_sp_gettables.md)
