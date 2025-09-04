---
title: Effects Of Upgrading To Version12
slug: effects_of_upgrading_to_version12
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: effects_of_upgrading_to_version12.htm
source: Advantage CHM
tags:
  - effects
checksum: 93a43ef1eace994efbb32bb1a276081ab5ec8221
---

# Effects Of Upgrading To Version12

Effects of Upgrading to Version 12

Effects of Upgrading to Version 12

Advantage Database Server

| Effects of Upgrading to Version 12  Advantage Database Server |  |  |  |  |

TDataset Descendant FindKey behavior changed when using dynamic or Unicode collation

In previous releases, when using index built with dynamic (VFP) or Unicode collation, the FindKey method would return records that are partial match of the search text. For example, FindKey( ['abc'] ) would find records with value 'abcde' instead just records with the exact value 'abc'. This behavior is different than using a index built with ANSI collation. This behavior is also not distinguished from the FindNearest method. In Version 12, the behavior of FindKey is now consistent regardless the collation of the index. It is same as using the index built with ANSI collation, i.e.no partial matches would be found when using FindKey. To find partial matches, FindNearest should be used.

SQL Statement Limit Per Connection

In previous versions of Advantage, an application could have any number (limited by system resources) of SQL statements active at the same time. Beginning with this version, each connection is limited to 50 active statements at a time in order to help prevent resource leaks. This limit can be changed for a given connection by calling [sp\_SetStatementLimit](master_sp_setstatementlimit.md), and it can be changed globally at the server by the configuration parameter [SQL\_STATEMENT\_LIMIT](master_sql_statement_limit.md).

Transaction In Subroutines

In previous release, it is possible to commit or to rollback a transaction within a stored procedure or user defined function that the subroutine did not initiate, or to rollback to a savepoint that was not established in the subroutine. These practices are no longer allowed as they could lead to complex programming flow. By requiring nested transactions be committed within the same subroutine, the limitation of not allowing nested transactions in Triggers in previous releases is now removed. It is also now possible to have distinct savepoints with identical name being established in different subroutines. See [Nesting Transactions](master_nesting_transactions.md).

Optimization of LENGTH() Scalar

The scalar [LENGTH()](master_length.md) is now supported for use in [index expressions](master_indexes_with_expressions.md). This changes how the SQL engine maps the use of LENGTH().  If the client is v12.0 or greater, then the SQL engine will map the LENGTH() scalar straight across. With older clients, it mapped it to LEN(RTRIM(fld)).

Default Memo Block Size

The default memo block size for the proprietary ADT file format has been changed from 8 bytes to 256 bytes. This affects the creation of new tables when a memo block size is not specified. This change does not affect existing tables.

Memo Block Size Property in Advantage Data Architect

When modifying table properties in Advantage Data Architect, the memo block size for both data dictionary and free tables can be modified. When the OK button is pressed on the property dialog, a table restructure operation will be triggered if the memo block size property was changed. In previous versions, the memo block size could only be edited for data dictionary bound tables.

Differential Online Backup Will Automatically Re-initialize

The first time you perform a [differential backup](master_differential_backups.md) of an existing database with v12, it will perform a complete backup of all tables. Advantage v12 and later maintains information in the ADT table header about the last valid differential backup. If it detects that it is not valid, it performs a full backup to re-initialize for the next differential backup. Because it uses new header information that is not maintained by versions prior to v12, it will result in the full backup. Thus, the first backup with v12 could take longer to complete.

Online ALTER TABLE Changes

By default Online ALTER TABLE will attempt to perform a no-transition ALTER where users of the table are not required to close the table for the ALTER to finish.  A new option (ONLINE\_WITH\_TRANSITION) is available with ALTER TABLE if the old behavior of always requiring users to close the table is desired.  See [Online Table Maintenance](master_online_table_maintenance.md) for more information.

 

[note - this one can be near the bottom; I doubt it matters to anyone]

CREATE TABLE Syntax

A minor change was made to the table creation syntax to allow the NULL column modifier to be used on ADT tables.  The use of the modifier makes no difference in the actual table with ADTs since ADT fields are nullable by default.  It is an ease-of-use change that allows the same CREATE table statement to be used with both VFP and ADT tables types.  For example, the statement "CREATE TABLE test (field1 integer null, field2 char(20) null)" is valid for both ADT and VFP table types.

MAX\_CACHE\_MEMORY

In previous versions of Advantage, the [MAX\_CACHE\_MEMORY](master_max_cache_memory.md) configuration setting was stored internally as a 32-bit integer. Therefore, the maximum possible cache value was 4095. Values larger than this would result in an artificial limitation of the cache size particularly in 64-bit servers. This limitation has been removed.

Show Memo Data in Grids Advantage Data Architect Setting

The "Show Memo Data in Grids" setting in Advantage Data Architect now defaults to false.  This setting controls whether memo data is displayed automatically in table or result set grids.  Previously the default setting was true.  You can set this option to true or false by choosing "Tools" then "ARC Settings" from the menu in Advantage Data Architect.

Permission Requirement to Create Trigger

The CREATE PROCEDURE permission is now required to create triggers on tables. This permission is in addition to the ALTER permission on the table.

DB:Admin Membership Required to Disable Triggers

In order to disable triggers ([sp\_DisableTriggers](master_sp_disabletriggers.md)), a user must be a member of the [DB:Admin](master_database_base_roles.md) group.

HTTPS enabled by default for Web Configuration Utility

To ensure secure access to ADS Web Administration Utility, HTTPS connections are by default enabled. This can be disabled by editing the adsweb.conf file. Note that disabling SSL connection will make all data visible on the wire.
