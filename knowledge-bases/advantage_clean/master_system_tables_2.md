---
title: Master System Tables 2
slug: master_system_tables_2
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_system_tables_2.htm
source: Advantage CHM
tags:
  - master
checksum: a0a20e58ca3220d9fc5ca2164e7e2e53b119eaac
---

# Master System Tables 2

system.ansi\_tables

system.ansi\_tables

Advantage SQL Engine

| system.ansi\_tables  Advantage SQL Engine |  |  |  |  |

Contains one row for each table in the database.

| Field Name | Field Type | Field Size | Description |
| Name | Character | 200 | Name of the table object in the data dictionary. |
| Table\_Relative\_Path | Character | 260 | The relative path to the table including the table name. |
| Table\_Type | ShortInt | 2 | Numeric value representing the table type.  1 = ADS\_NTX  2 = ADS\_CDX  3 = ADS\_ADT  4 = ADS\_VFP |
| Table\_Auto\_Create | Logical | 1 | Determines if the table and associated indexes are automatically created if they do not exist. |
| Table\_Primary\_Key | Character | 128 | Name of the tables primary key. |
| Table\_Default\_Index | Character | 128 | Name of the tables default index. |
| Table\_Encryption | Logical | 1 | Determines if the table is encrypted. |
| Table\_Permission\_Level | ShortInt | 2 | Determines how the column level permissions on the table are enforced. |
| Table\_Memo\_Block\_Size | ShortInt | 2 | The size of the memo block used when auto-creating a table. |
| Table\_Validation\_Expr | Memo | variable | Table level validation expression for newly inserted records. |
| Table\_Validation\_Msg | Memo | variable | Custom error message displayed to the user when the table validation method fails. |
| Comment | Memo | variable | Description of the Table. |
| User\_Defined\_Prop | Binary | variable | The user defined property. |
| Triggers\_Disabled | Logical | 1 | Flag indicating if triggers are disabled on this table. |
| Table\_Caching | ShortInt | 2 | Specifies table data caching level.  Please see [Table Data Caching](master_table_data_caching.md) before enabling this feature.  Value is expected to be 1 (ADS\_TABLE\_CACHE\_READS), 2 (ADS\_TABLE\_CACHE\_WRITES), or 0 (ADS\_TABLE\_CACHE\_NONE). |
| Table\_Trans\_Free | Logical | 1 | Specifies whether the table is a [transaction-free table](master_transaction_free_tables.md) that is excluded from all active transactions. |
| Table\_WEB\_Delta | Logical | 1 | Flag indicating if Web Service Delta Support is enabled on this table. |
| Table\_Concurrency\_Enabled | Logical | 1 | Flag indicating if [optimistic concurrency](master_optimistic_concurrency.md) control is enabled on this table. |
