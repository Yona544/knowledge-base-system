---
title: Oledb Schema Rowset Support In The Advantage Ole Db Provider
slug: oledb_schema_rowset_support_in_the_advantage_ole_db_provider
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: oledb_schema_rowset_support_in_the_advantage_ole_db_provider.htm
source: Advantage CHM
tags:
  - oledb
checksum: f896d2e2482d4a1e1b1b76afdc8b3bcce0a48d35
---

# Oledb Schema Rowset Support In The Advantage Ole Db Provider

Schema Rowset Support in the Advantage OLE DB Provider

Schema Rowset Support in the Advantage OLE DB Provider

Advantage OLE DB Provider (for ADO)

| Schema Rowset Support in the Advantage OLE DB Provider  Advantage OLE DB Provider (for ADO) |  |  |  |  |

The following tables list schema rowsets and the restriction columns supported by the Advantage OLE DB Provider. When specifying the restriction array either from ADO (ADODB.Connection.OpenSchema) or from OLE DB (IDBSchemaRowset::GetRowset), you must specify VT\_EMPTY ("Empty" in Visual Basic) as the restriction value. For example, the Advantage OLE DB Provider does not support TABLE\_SCHEMA in the TABLES schema rowset, so VT\_EMPTY must be specified as the second restriction array value.

| Schema Rowset | Restriction Columns |
| DBSCHEMA\_TABLES | The following restrictions are supported.  TABLE\_CATALOG  TABLE\_NAME  TABLE\_TYPE |
| DBSCHEMA\_COLUMNS | The following restrictions are supported.  TABLE\_CATALOG  TABLE\_NAME  COLUMN\_NAME |
| DBSCHEMA\_PROVIDER\_TYPES | The following restrictions are supported.  DATA\_TYPE  BEST\_MATCH |
| DBSCHEMA\_INDEXES | The following restrictions are supported.  TABLE\_CATALOG  INDEX\_NAME  TYPE  TABLE\_NAME |
| DBSCHEMA\_CATALOGS | The following restrictions are supported.  CATALOG\_NAME |
| DBSCHEMA\_PRIMARY\_KEYS | The following restrictions are supported.  TABLE\_CATALOG  TABLE\_NAME |
| DBSCHEMA\_PROCEDURES | The following restrictions are supported.  PROCEDURE\_CATALOG  PROCEDURE\_NAME  PROCEDURE\_TYPE |
| DBSCHEMA\_REFERENTIAL\_CONSTRAINTS | The following restrictions are supported.  CONSTRAINT\_CATALOG  CONSTRAINT\_NAME |
| DBSCHEMA\_TABLE\_CONSTRAINTS | The following restrictions are supported.  CONSTRAINT\_CATALOG  CONSTRAINT\_NAME  TABLE\_CATALOG  TABLE\_NAME  CONSTRAINT\_TYPE |
| DBSCHEMA\_TABLE\_PRIVILEGES | The following restrictions are supported.  TABLE\_CATALOG  TABLE\_NAME  GRANTOR  GRANTEE |
| DBSCHEMA\_VIEWS | The following restrictions are supported.  TABLE\_CATALOG  TABLE\_NAME |

The Advantage OLE DB Provider schema rowset support is outlined in the following table.

| OLE DB Schema Name | ADO Schema Name | Description and GUID (if needed) |
| DBSCHEMA\_TABLES | adSchemaTables | The TABLES rowset identifies the tables defined in the database that are accessible to a given user. |
| DBSCHEMA\_COLUMNS | adSchemaColumns | The COLUMNS rowset identifies the columns of tables defined in the database that are accessible to a given user. |
| DBSCHEMA\_PROVIDER\_TYPES | adSchemaProviderTypes | The PROVIDER\_TYPES rowset identifies the (base) data types supported by the data provider. |
| DBSCHEMA\_INDEXES | adSchemaIndexes | The INDEXES rowset identifies the indexes defined in the database that are owned by a given user. |
| DBSCHEMA\_CATALOGS | adSchemaCatalogs | The CATALOGS rowset identifies the physical attributes associated with catalogs accessible from the RDBMS. |
| DBSCHEMA\_PRIMARY\_KEYS | adSchemaPrimaryKeys | The PRIMARY\_KEYS rowset identifies the primary key columns defined in the catalog by a given user. |
| DBSCHEMA\_PROCEDURES | adSchemaProcedures | The PROCEDURES rowset is an OLE DB extension. It identifies the procedures defined in the catalog that are owned by a given user. |
| DBSCHEMA\_REFERENTIAL\_CONSTRAINTS | adSchemaReferentialConstraints | The REFERENTIAL\_CONSTRAINTS rowset identifies the referential constraints defined in the catalog that are owned by a given user. |
| DBSCHEMA\_TABLE\_CONSTRAINTS | adSchemaTableConstraints | The TABLE\_CONSTRAINTS rowset identifies the table constraints defined in the catalog that are owned by a given user. |
| DBSCHEMA\_TABLE\_PRIVILEGES | adSchemaTablePrivileges | The TABLE\_PRIVILEGES rowset identifies the privileges on tables defined in the catalog that are available to or granted by a given user. |
| DBSCHEMA\_VIEWS | adSchemaViews | The VIEWS rowset identifies the views defined in the catalog that are accessible to a given user. |
