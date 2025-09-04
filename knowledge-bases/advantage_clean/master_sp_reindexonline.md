---
title: Master Sp Reindexonline
slug: master_sp_reindexonline
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_reindexonline.htm
source: Advantage CHM
tags:
  - master
checksum: 2f115ed1b23100b86bd367cc3d0a2ffe6eb1576b
---

# Master Sp Reindexonline

sp\_ReindexOnline

sp\_ReindexOnline

Advantage SQL Engine

| sp\_ReindexOnline  Advantage SQL Engine |  |  |  |  |

Rebuilds all auto-open indexes associated with the given table while it is in use.  See [Online Table Maintenance](master_online_table_maintenance.md) for important details.

 

Syntax

sp\_ReindexOnline( TableName,CHARACTER,515,

                Options, MEMO)

Parameters

| TableName (I) | Name of table to rebuild indexes on.  This can include path information for free tables if the table is in a different folder from the connection path. |
| Options (I) | Optional string list of options.  The supported options are:  |  |  | | --- | --- | | Timeout | Number of seconds to wait during the final stage of the reindex before returning an error.  For example: 'Timeout=60' |  |  |  | | --- | --- | | KeepBackupFiles | Keep the original table and index files with a BAK extension after the reindex.  For example: 'KeepBackupFiles' |  |  |  | | --- | --- | | Indexes | A comma-delimited list of non-auto-open indexes to rebuild.  For example: 'Indexes=firstname.ntx,lastname.ntx' | |

Remarks

sp\_ReindexOnline performs a reindex of a table while the table is opened shared.  This operation is only supported on remote server connections.  If the table is already opened by another user it must be opened using proprietary locking.  If the table is not already open, Advantage will open it with proprietary locking and any requests to open it during the reindex must use proprietary locking.

By default only auto-open indexes will be re-indexed.  To include non-auto-open indexes with the pack specify them in the Index options parameter.

The TableName parameter can be a table name or the table path.  If no path is provided, the path of the connection will be used.  If not provided, the table extension (ADT or DBF) will be determined by the table type of the SQL statement.

Encrypted free tables must have the table encryption password set on the SQL statement.  See [AdsConnect101](ace_adsconnect101.md), [AdsStmtSetTablePassword](ace_adsstmtsettablepassword.md) in ACE or [TAdsQuery.AdsStmtSetTablePassword](ade_adsstmtsettablepassword.md) in Delphi.

 

Examples

// Simple call with no options

EXECUTE PROCEDURE sp\_ReindexOnline( 'customers.adt' );

// Setting a timeout of 60 seconds

EXECUTE PROCEDURE sp\_ReindexOnline( 'customers', 'Timeout=60' );

// Specifying non-auto-open indexes

EXECUTE PROCEDURE sp\_ReindexOnline( 'customers', 'Indexes=custid.ntx,lastname.ntx' );

// Timeout and keep backup files option

EXECUTE PROCEDURE sp\_ReindexOnline( 'customers', 'Timeout=60;KeepBackupFiles;' );

See Also

[Online Table Maintenance](master_online_table_maintenance.md)

[sp\_Reindex](master_sp_reindex.md)

[AdsReindex61](ace_adsreindex61.md)

[sp\_CreateIndex](master_sp_createindex.md)
