---
title: Jdbc Resultsetmetadata Object
slug: jdbc_resultsetmetadata_object
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: jdbc_resultsetmetadata_object.htm
source: Advantage CHM
tags:
  - jdbc
checksum: 4141362fc9e7e5578ee460ec00ff7b598384b422
---

# Jdbc Resultsetmetadata Object

ResultSetMetaData Object

ResultSetMetaData Object

Advantage JDBC Driver

| ResultSetMetaData Object  Advantage JDBC Driver |  |  |  |  |

| Methods | Version Introduced | Supported | Comments |
| String getCatalogName (int) | 1.0 | Yes | Always returns empty string. |
| String getColumnClassName (int) | 2.0 Core | Yes |  |
| int getColumnCount () | 1.0 | Yes |  |
| int getColumnDisplaySize (int) | 1.0 | Yes |  |
| String getColumnLabel (int) | 1.0 | Yes |  |
| String getColumnName (int) | 1.0 | Yes |  |
| int getColumnType (int) | 1.0 | Yes |  |
| String getColumnTypeName (int) | 1.0 | Yes |  |
| int getPrecision (int) | 1.0 | Yes |  |
| int getScale (int) | 1.0 | Yes |  |
| String getSchemaName (int) | 1.0 | Yes |  |
| String getTableName (int) | 1.0 | Yes | Always returns empty string. |
| boolean isAutoIncrement (int) | 1.0 | Yes |  |
| boolean isCaseSensitive (int) | 1.0 | Yes |  |
| boolean isCurrency (int) | 1.0 | Yes |  |
| boolean isDefinitelyWritable (int) | 1.0 | Yes |  |
| int isNullable (int) | 1.0 | Yes |  |
| boolean isReadOnly (int) | 1.0 | Yes |  |
| boolean isSearchable (int) | 1.0 | Yes |  |
| boolean isSigned (int) | 1.0 | Yes |  |
| boolean isWritable (int) | 1.0 | Yes |  |
