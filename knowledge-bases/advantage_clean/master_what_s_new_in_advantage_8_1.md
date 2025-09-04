---
title: Master What S New In Advantage 8 1
slug: master_what_s_new_in_advantage_8_1
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_what_s_new_in_advantage_8_1.htm
source: Advantage CHM
tags:
  - master
checksum: e4779ec3d0a2fc5b99a71adffb49d6d8fb5533fb
---

# Master What S New In Advantage 8 1

What's New in Advantage 8.1

What's New in Advantage 8.1

Advantage Database Server

| What's New in Advantage 8.1  Advantage Database Server |  |  |  |  |

Development & Usability Enhancements

User Defined Functions (UDFs)

User defined functions allow a developer to create reusable functions that can be used in SQL statements or SQL scripts just like existing scalar functions. By encapsulating frequently performed or complex operations into user defined functions, SQL statements or scripts become easier to write, understand, and debug. In a sense, user defined functions make it possible to extend the functionality of the SQL engine.

Numeric Field Type for ADT Tables

A numeric field type, similar to the existing DBF numeric field type, is now available for ADT tables. The numeric type will not lose precision during mathematical operations.

Vertical Filtering for Replication

It is now possible to define vertical filters on replicated tables to control which columns of data are replicated. This provides greater control over the replication process and allows for more flexible scenarios. For example, vertical filters make it possible to replicate to a target table that has fewer columns than the source table.

Trigger Names

Trigger names now only need to be unique on a per-table basis, as opposed to the per-database basis in earlier versions of Advantage.

Advantage Data Architect (ARC) Enhancements

- Schema templates allow you to load pre-existing field and index definitions into the table designer. If many of your tables include similar base schema structures, this is an easy way to quickly create new tables from existing templates.

- Added the ability to assign descriptions to each index in a table.

- Enhanced the table schema printing format.

Support for TOP X in a Subquery

In previous versions of Advantage, the TOP X limiter could not be used in subqueries. With Advantage 8.1, the TOP X limiter can now be used in any SELECT statement.

Server-Side Alias Support

Server-side alias support has been expanded to cover the NetWare and Linux platforms, in addition to the Windows platform, which supported server-side aliases in v8.0.

Crystal Reports

The Advantage Crystal Reports driver now allows applications to pass an existing connection handle to the driver. In addition to increasing performance and reducing overhead, this functionality allows users to report on connection-specific resources, such as temporary tables.

Management Information

Several Advantage management API functions now return the IP address of the Terminal Services client for Advantage connections originating from a Windows Terminal Services session.

GUIDs

The SQL scalar and expression engine function, NEWIDSTRING, can be used to generate a string formatted GUID.

Delphi/C++Builder IDE

The Advantage Data Architect (ARC) table designer has been made available inside the Delphi/C++Builder IDE, allowing tables to be redesigned inside the IDE without opening an ARC session. This functionality is available by right-clicking on a TAdsTable component and selecting ALTER/Restructure Table from the quick menu. This functionality is available in Delphi 5/6/7/2005/2006 and C++Builder 2006.

Performance Enhancements

Increased SQL Performance

Performance has been improved for many types of SQL statements. SQL statements that require temporary storage files will now make use of the cache system. Depending on the amount of cache memory available and the size of the result set, many queries will no longer use temporary disk storage. A simple example is the query "SELECT LASTAUTOINC( STATEMENT ) FROM system.iota". In previous versions of Advantage, the result set (the static cursor) would be realized as a physical file on disk. In v8.1, the result set will be stored in memory and, thus, result in much shorter execution times.

Increased Script Trigger Performance

A statement handle cache has been implemented for script triggers. This cache dramatically increases the performance of triggers written as SQL scripts by reducing query processing overhead and by keeping tables used by the trigger cached on the server. The largest performance increases will be noticed in applications that perform batch insert, update, or delete operations on tables that have script triggers.

Dynamic Cache Size

The cache system now dynamically changes the maximum amount of cache memory it consumes based on the amount of available physical memory available.

Encrypted Indexes

The overhead of using encrypted indexes has been greatly reduced via enhanced integration with the index cache system.

Security Enhancements

TCP/IP Support

The ability to communicate with the Advantage Database Server using TCP/IP is now possible, as opposed to the default proprietary transport implemented using UDP. Many network administrators are reluctant to open UDP ports on their firewalls, and are more comfortable with a TCP port.

.NET Enhancements

Visual Studio 2005 Integration

- Several new properties have been added to the AdsExtendedReader object to retrieve information about the active index. The new properties are AdsActiveHandle, IsIndexCustom, IsIndexCompound, IsIndexDescending, IsIndexPrimaryKey, IsIndexUnique, IndexExpression, and IndexCondition.

- Additional support for functionality in the System.Transactions namespace. AdsConnection will now enlist in ambient transactions (through the TransactionScope object) and commit or rollback as necessary.

- Integration with Visual Studio 2005 and the Server Explorer has been enhanced. It is now possible to add Advantage .NET Data Provider connections in the Server Explorer and create TableAdapters in strongly typed datasets with the TableAdapter Configuration Wizard.
