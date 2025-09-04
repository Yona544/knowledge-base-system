---
title: Master Supported Data Types In The Advantage Sql Engine
slug: master_supported_data_types_in_the_advantage_sql_engine
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_supported_data_types_in_the_advantage_sql_engine.htm
source: Advantage CHM
tags:
  - master
checksum: 58a102f6f0a62d23f8ea74853fd238c9469095d2
---

# Master Supported Data Types In The Advantage Sql Engine

Supported Data Types in the Advantage SQL Engine

Supported Data Types in the Advantage SQL Engine

Advantage SQL Engine

| Supported Data Types in the Advantage SQL Engine  Advantage SQL Engine |  |  |  |  |

The following is a list of data types supported by the Advantage SQL engine. Note that the names in the table are listed as they would appear in a CREATE TABLE statement. For example, to create a table with CHAR and INTEGER field types, you might use a statement like "CREATE TABLE test( c CHAR(25), i INTEGER )". Note that the BLOB data type name will create an Advantage BINARY field.

With ADT and VFP table types, the VARCHAR data type name will create an Advantage VarcharFox field, and the VARBINARY data type name will create an Advantage VarBinaryFox field. With the CDX table type, the VARCHAR data type will created a Varchar field that is not fully supported in the SQL engine and it is not recommended.

It is not possible to create an Advantage IMAGE field through the CREATE TABLE statement. The SQL engine views both IMAGE and BINARY field types as BLOB (Binary Large OBject) fields.

See [ADT Field Types and Specifications](master_adt_field_types_and_specifications.md) or [DBF Field Types and Specifications](master_dbf_field_types_and_specifications.md) for field type specification details.

| Char | Blob | Money |
| Numeric | Short | CIChar |
| Date | Time | RowVersion |
| Logical | TimeStamp | ModTime |
| Memo | AutoInc | VarChar |
| Double | Raw | VarBinary |
| Integer | LongInt | NChar |
| NVarChar | NMemo | GUID |
| CurDouble |  |  |
