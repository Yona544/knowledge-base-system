sp\_PackTableOnline




Advantage Database Server 12  

sp\_PackTableOnline

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_PackTableOnline  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_PackTableOnline Advantage SQL Engine master\_sp\_PackTableOnline Advantage SQL > System Procedures > Procedures > sp\_PackTableOnline / Dear Support Staff, |  |
| sp\_PackTableOnline  Advantage SQL Engine |  |  |  |  |

Removes all deleted records from a table and re-indexes it while it is in use.  See [Online Table Maintenance](master_online_table_maintenance.htm) for important details.

Syntax

sp\_PackTableOnline( TableName,CHARACTER,515,

                   Options,MEMO )

 

sp\_PackAllTablesOnline( Options,MEMO )

Parameters

|  |  |
| --- | --- |
| TableName (I) | Name and/or path of a table to pack. |
| Options (I) | Optional string list of options.  The supported options are:  |  |  | | --- | --- | | Timeout | Number of seconds to wait during the final stage of the pack before returning an error.  For example: 'Timeout=60' |  |  |  | | --- | --- | | KeepBackupFiles | Keep the original table and index files with a BAK extension after the pack.  For example: 'KeepBackupFiles' |  |  |  | | --- | --- | | Indexes | A comma-delimited list of non-auto-open indexes to open when performing the pack.  For example: 'Indexes=firstname.ntx,lastname.ntx' |  |  |  | | --- | --- | | MemoBlockSize | Memo block size for the packed table. If this is not provided or if the value is 0, the memo block size will not be changed by the pack operation. | |

Remarks

sp\_PackTableOnline performs a pack of a table while the table is opened shared.  This operation is only supported on remote server connections.  If the table is already opened by another user it must be opened using proprietary locking.  If the table is not already open, Advantage will open it with proprietary locking and any requests to open it during the pack must use proprietary locking.

By default only auto-open indexes will be re-indexed.  To include non-auto-open indexes with the pack specify them in the Index options parameter.

The TableName parameter can be a table name or the table path.  If no path is provided, the path of the connection will be used.  If not provided, the table extension (ADT or DBF) will be determined by the table type of the SQL statement.

Encrypted free tables must have the table encryption password set on the SQL statement.  See [AdsStmtSetTablePassword](ace_adsstmtsettablepassword.htm) in ACE or [TAdsQuery.AdsStmtSetTablePassword](ade_adsstmtsettablepassword.htm) in Delphi.

sp\_PackAllTablesOnline simply calls sp\_PackTableOnline for all tables in a dictionary or all the tables in directory of a free connection.  The options parameter is optional and if provided would apply to each call of sp\_PackTableOnline for each table.

Examples

// Simple call with no options

EXECUTE PROCEDURE sp\_PackTableOnline( 'customers.adt' );

// Setting a timeout of 60 seconds

EXECUTE PROCEDURE sp\_PackTableOnline( 'customers', 'Timeout=60' );

// Specifying non-auto-open indexes

EXECUTE PROCEDURE sp\_PackTableOnline( 'customers', 'Indexes=custid.ntx,lastname.ntx' );

// Timeout and keep backup files option

EXECUTE PROCEDURE sp\_PackTableOnline( 'customers', 'Timeout=60;KeepBackupFiles;' );

See Also

[Online Table Maintenance](master_online_table_maintenance.htm)

[sp\_PackTable](master_sp_packtable.htm)

[sp\_ReindexOnline](master_sp_reindexonline.htm)

[sp\_ZapTable](master_sp_zaptable.htm)

[AdsPackTable](ace_adspacktable.htm)