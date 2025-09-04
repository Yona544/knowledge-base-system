---
title: Jdbc Connection String Properties
slug: jdbc_connection_string_properties
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: jdbc_connection_string_properties.htm
source: Advantage CHM
tags:
  - jdbc
checksum: f4ebe7bd7b4da761fdcd9daaf44ac789776ad56e
---

# Jdbc Connection String Properties

Connection String Properties

Connection String Properties

Advantage JDBC Driver

| Connection String Properties  Advantage JDBC Driver |  |  |  |  |

You can use the following connection properties with the JDBC driver manager. The properties have the form:

property=value

Note All connection string property names are case-insensitive. For example, PortNumber is the same as portnumber.

Advantage JDBC Driver Connection String Properties

| Optional Property | Description |
| Catalog | The path of the Advantage Data Dictionary (.ADD) file or the directory of the free tables. This may be an UNC path or a path on the server. If this property is not specified, the path of the Advantage Data Dictionary file or the directory of the free tables must be included in the connection URL. |
| CharType | Type of character data in the table. The valid values for this property are "ansi", "oem" or a known collation name, such as GERMAN\_VFP\_CI\_AS\_1252. See AdsSetCollation for additional information. The default is "ansi". This property indicates the type of character data to be stored in the table and how comparisons of character strings are performed. If the property is set to "ansi" or "oem", the default ansi or oem collation of the server will be used. For compatibility with DOS-based CA-Clipper applications, "oem" should be specified. When TableType property is "adt", oem collation is never used When opening a database table, i.e., table that is part of the Advantage Data Dictionary specified in the Catalog property, this parameter is ignored. The Advantage Server will use the information stored in the data dictionary to resolve the character data type. |
| LockType | Type of locking to use. The valid values for this property are "proprietary" or "compatible". The default is "proprietary". If the application is to be used with non-Advantage applications, then "compatible" locking should be used. If the table will be used only by Advantage applications, then "proprietary" locking should be used. When the TableType property is "adt", this property is ignored and "proprietary" locking is always used. When "compatible" locking is chosen, Advantage uses the appropriate style based on the table type. See [Advantage Locking Modes](master_advantage_locking_modes.md) for more information. |
| Password | The case-sensitive password used to connect to the database defined in the Advantage Data Dictionary. If the catalog property does not specify the path of an Advantage Data Dictionary, this property is ignored. |
| ShowDeleted | This property controls whether the Advantage Database Server filters out records that are marked for deletion in DBF tables. The valid values for this property are "true" or "false". The default is "false". If this property is set to "false", then the server will filter the deleted records, and the client will never "see" those records. When the TableType is "adt", this property is ignored. Records that are deleted in ADT tables can never be retrieved by a client application. |
| TableType | Type of table. The valid values for this property are "adt", "vfp", "cdx" or "ntx". If the catalog property specifies the path of a Advantage Data Dictionary, this property is ignored except for executing the SQL statement "CREATE TABLE ". If the catalog property specifies a directory where free tables are located, this property applies to tables used in all SQL Statements. |
| User | The case-insensitive user name used to connect to the database defined in the Advantage Data Dictionary. If the catalog property does not specify the path of an Advantage Data Dictionary, this property is ignored. |
| QueryTimeout | The SQL Timeout for this connection (in seconds). This timeout will apply to all Statement objects that use this Connection, unless a different timeout has been specified via the Statement.setQueryTimeout method. |
