---
title: Ace Adsopentable90
slug: ace_adsopentable90
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsopentable90.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 46e9e43ee47e0d8f0c1d96ea85d429b2632065d6
---

# Ace Adsopentable90

AdsOpenTable90

AdsOpenTable90

Advantage Client Engine

| AdsOpenTable90  Advantage Client Engine |  |  |  |  |

Opens an existing table.

Syntax

| UNSIGNED32 | AdsOpenTable90( ADSHANDLE hConnect,  UNSIGNED8 \*pucName,  UNSIGNED8 \*pucAlias,  UNSIGNED16 usTableType,  UNSIGNED16 usCharType,  UNSIGNED16 usLockType,  UNSIGNED16 usCheckRights,  UNSIGNED32 ulOptions,  UNSIGNED8 \*pucCollation,  ADSHANDLE \*phTable); |

Parameters

| hConnect (I) | Optional connection handle used to open the table. If this is 0, then an appropriate available connection will be used, or a new connection will be opened if one is not available. To open a database table), this parameter must be a database connection) handle to the appropriated Advantage Data Dictionary file. |
| pucName (I) | Name of table to open. To open a database table), this parameter must specify the name of the table in the data dictionary. The Advantage Database Server will use the information from the data dictionary to resolve the file path of database table. To open a free table), this parameter may specify the file path of the table. If this parameter does not specify a path, then the default path (see [AdsSetDefault](ace_adssetdefault.md) ) or the search path (see [AdsSetSearchPath](ace_adssetsearchpath.md)) will be used. If no path is given and there is no default or search path, then the current working directory of the application will be used. The Advantage Client Engine resolves all table path names to UNC (Universal Naming Convention). Therefore, it is slightly faster to pass UNC names (e.g., \\server\volume\data\file.dbf) to the Advantage Client Engine rather than relative paths or paths with drive letters. |
| pucAlias (I) | Alias to associate with the table. If NULL, the alias will be the base filename. The alias is limited to 10 characters. |
| usTableType (I) | Type of table. Options are ADS\_DEFAULT, ADS\_ADT, ADS\_VFP, ADS\_NTX and ADS\_CDX. If the specified table type is ADS\_DEFAULT, the function will attempt to open a database table). In such case, the hConnect parameter must be a database connection) handle and the Advantage Server will use the information stored in the data dictionary to resolve the table type. If the specified table type is ADS\_ADT, ADS\_VFP, ADS\_NTX, or ADS\_CDX, the function will attempt to open a free table). |
| usCharType (I) | Type of character data in the table. Valid values include ADS\_ANSI, ADS\_OEM, or one of the [dynamic collations](master_collation_support.md) such as GENERAL\_VFP\_CI\_AS\_1252. This indicates the type of character data to be stored in the table and the collation to use when sorting the data. For compatibility with DOS-based CA-Clipper applications, ADS\_OEM should be specified when opening DBF tables. When opening a database table, (i.e., the usTableType is ADS\_DEFAULT, this parameter is ignored.) The Advantage Server will use the information stored in the data dictionary to resolve the character data type. |
| usLockType (I) | Type of locking to use. Options are ADS\_PROPRIETARY\_LOCKING and ADS\_COMPATIBLE\_LOCKING. If the application is to be used with non-Advantage applications, then ADS\_COMPATIBLE\_LOCKING should be used. If the table will be used only by Advantage applications, then ADS\_PROPRIETARY\_LOCKING should be used. When ADS\_COMPATIBLE\_LOCKING is chosen, Advantage uses the appropriate style based on the table type. When usTableType is ADS\_ADT, this parameter is ignored and ADS\_PROPRIETARY\_LOCKING is always used. See [Advantage Locking Modes](master_advantage_locking_modes.md) for more information. |
| usCheckRights (I) | Indicates if the client is to use rights checking for the file open. Options are ADS\_CHECKRIGHTS and ADS\_IGNORERIGHTS. Note that beginning with version 10.0, the client ignores this setting by default.  To re-enable this setting, use [AdsSetRightsChecking](ace_adssetrightschecking.md). When opening a data dictionary-bound table (usTableType is ADS\_DEFAULT), this parameter is ignored. For data dictionary tables, user access rights are defined in the database (see [AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.md) for more information).    If rights checking has been enabled with AdsSetRightsChecking and ADS\_CHECKRIGHTS is given, then the Advantage Client Engine will perform an existence check on the file and will not send the open request to the server if the table is not visible to the client workstation. If ADS\_IGNORERIGHTS is used, then the client will not perform the file existence check. |
| ulOptions (I) | This is a bit field for defining the options for opening the table. The options can be ORed together. For example, ADS\_EXCLUSIVE | ADS\_READONLY. The options are:  ADS\_DEFAULT: If no options are needed, this value (0) can be used.  ADS\_EXCLUSIVE: Open table for exclusive (non-shared) use. This option is mutually exclusive with the ADS\_SHARED option.  ADS\_SHARED: Open table for shared use. This option is mutually exclusive with the ADS\_EXCLUSIVE option.  ADS\_READONLY: Open table for read-only use. If this option is not set, and the table cannot be opened for read/write access due to an OS file access restriction such as CD-ROM drive or the data dictionary user access restriction, the table will be opened with read-only access when such access is allowed by OS or the data dictionary.  ADS\_CLIPPER\_MEMOS: Strip CA-Clipper style carriage return linefeed character pairs (0x8D 0x0A) from memos. If a memo field contains these characters, they will not be displayable in a Windows application. This option will force the Advantage Client Engine to remove the characters from the memo text.  ADS\_REINDEX\_ON\_COLLATION\_MISMATCH: Automatically rebuild indexes when a collation mismatch is detected when opening indexes for this table. Beginning with version 6.2, Advantage stores a collation sequence identifier in the header of Advantage proprietary index (.ADI) files when it creates a new index file. When opening the index again, it can use that identifier to determine if the current collation sequence matches the one used to create the index. If the ADS\_REINDEX\_ON\_COLLATION\_MISMATCH option is provided, Advantage will attempt to automatically rebuild the index when it detects that the index was originally built with a different collation sequence. Advantage will be unable to rebuild the index if it has any index orders created with the ADS\_CUSTOM option (see [AdsCreateIndex](ace_adscreateindex.md)). It is also not possible to rebuild the index if another user currently has the index open; this can happen when different clients use Advantage Local Server and each client has a different collation sequence. If Advantage is unable to rebuild the index, it will return error code 5175. It is important to note that if the use of this option does trigger an index rebuild, it can slow down the open of the index or table (when using auto-open indexes). For example, if an application is using Advantage Local Server with large tables across a network, an index rebuild may take a considerable amount of time. If any record locks are held by the application on the table that owns this index when this option triggers a reindex, Advantage will release those locks.  ADS\_IGNORE\_COLLATION\_MISMATCH: Ignore collation mismatches when opening index files. A mismatch between the collation sequence used to build an index and the current collation sequence effectively causes the index file to be corrupt. For example, Advantage may not be able to find some keys because they may be sorted differently than they would be according to the current collation sequence. Therefore, an application should only use this option if it plans to immediately rebuild the index file (see [AdsReindex](ace_adsreindex.md), [AdsReindex61](ace_adsreindex61.md)). If neither this option nor ADS\_REINDEX\_ON\_COLLATION\_MISMATCH are specified, then Advantage will return a 5175 error when it detects a collation mismatch and will not open the index file.  ADS\_TEMP\_TABLE: The table to be opened is a [temporary table](master_temporary_tables.md). When this option is specified, the pucName specifies the name of the tables instead of the physical file name. As an alternative, prefix the table name with a # character (e.g., using #Temp1 as the pucName parameter). This is equivalent to specifying the ADS\_TEMP\_TABLE option.  ADS\_CACHE\_READS: Enables read caching on the table. Ignored by dictionary bound tables. See [Table Data Caching](master_table_data_caching.md) for details.  ADS\_CACHE\_WRITES: Enables read and write caching on the table. Ignored by dictionary bound tables. See [Table Data Caching](master_table_data_caching.md) for details. |
| pucCollation (l) | An optional collation language used when opening the table. The collation may be specified for ANSI/OEM characters, Unicode characters or both. Unicode collation name must be pre-pended with a single colon character. If both ANSI/OEM collation and Unicode collation are to be specified, the Unicode collation must be specified after the ANSI/OEM collation. For example: Duden\_DE\_ADS\_CS\_AS\_1252:de\_DE. This parameter is optional. If it is not specified, the collation specified by the usCharType will be used. For ADS\_CDX and ADS\_NTX tables, the ANSI/OEM collation must not be specified.  See [dynamic collation support](master_collation_support.md). |
| phTable (O) | The handle to the table is returned if the table is opened successfully. |

Special Return Codes

| 7079, 7080 | The user does not have the proper rights to open the database table. |

Remarks

When opening a free table), if any path information including relative paths such as "..\file.dbf" is included, then the name will be used as given. If no path information is given with pucName, then the following rules are used to find and open the file.

| 1. | If a default path exists ([AdsSetDefault](ace_adssetdefault.md)), attempt to open the file in the specified default path. |

| 2. | If a search path exists ([AdsSetSearchPath](ace_adssetsearchpath.md)), try each path in the search path. |

| 3. | Try to open the file in the current directory that is controlled via the users application. |

AdsOpenTable is used to open an existing table. The connection handle is used to specify a connection, if necessary. This allows flexibility during transactions because transactions are per connection. Using a separate connection will allow a table to remain outside of a transaction if another connection to the same server is in a transaction. See Transaction Processing for more information.

An alias is used as an alternate method of referring to a table in other commands. It can also be used with expressions.

If the table type is ADS\_ADT, then the associated index type is the ADI format, and memos are the ADM format. If the table type is ADS\_NTX, then the associated index type is the NTX format, and memos are DBT format. If the table type is ADS\_CDX or ADS\_VFP, then IDX and CDX index types are used, and memos are the FPT format.

Note usLockType is always set to compatible locking (ADS\_COMPATIBLE\_LOCKING) when used with Advantage Local Server (ADS\_LOCAL\_SERVER) with ADT and DBF tables. usLockType is always set to proprietary locking (ADS\_PROPRIETARY\_LOCKING) when used with the Advantage Database Server (ADS\_REMOTE\_SERVER) with ADT tables. usCheckRights is ignored when used with Advantage Local Server (ADS\_LOCAL\_SERVER) with ADT and DBF tables. It is effectively treated as rights checking on (ADS\_CHECKRIGHTS). If ADS\_OEM is specified for the usCharType when using ADT tables, it will be changed to ADS\_ANSI. ADT tables do not support OEM character sets.

If the table to be opened is a database table), (i.e., usTableType parameter is ADS\_DEFAULT) there may be additional features and limitations on the use of the returned table handle. Properties defined for the table in the data dictionary are automatically available for the database table. See [AdsDDSetTableProperty](ace_adsddsetdatabaseproperty.md) and [AdsDDSetFieldProperty](ace_adsddsetfieldproperty.md) for more information. Adding or removing an index with the table will modify the definitions stored in the database.

Example

ulRetCode = AdsOpenTable90( 0, "D:\\data\\customers.dbf", "customers", ADS\_VFP,

   ADS\_OEM, ADS\_COMPATIBLE, ADS\_IGNORERIGHTS,

   ADS\_DEFAULT, "GERMAN\_VFP\_CI\_AS\_1252", &hTable );

See Also

[sp\_GetCollations](master_sp_getcollations.md)

[AdsCreateTable](ace_adscreatetable.md)

[AdsCreateIndex](ace_adscreateindex.md)

[AdsConnect](ace_adsconnect.md)

[AdsConnect60](ace_adsconnect60.md)

[AdsCloseTable](ace_adsclosetable.md)

[AdsGetTableHandle](ace_adsgettablehandle.md)

[AdsSetDefault](ace_adssetdefault.md)

[AdsSetSearchPath](ace_adssetsearchpath.md)

[AdsCacheOpenTables](ace_adscacheopentables.md)

[AdsGetTableFilename](ace_adsgettablefilename.md)

[AdsGetTableType](ace_adsgettabletype.md)

[AdsGetTableCharType](ace_adsgettablechartype.md)

[AdsGetTableLockType](ace_adsgettablelocktype.md)

[AdsGetTableOpenOptions](ace_adsgettableopenoptions.md)

[AdsGetTableRights](ace_adsgettablerights.md)

[AdsGetTableAlias](ace_adsgettablealias.md)

[AdsSetServerType](ace_adssetservertype.md)

[AdsDDCreate](ace_adsddcreate.md)

[AdsDDAddTable](ace_adsddaddtable.md)

[AdsDDSetTableProperty](ace_adsddsettableproperty.md)

[AdsDDGetTableProperty](ace_adsddgettableproperty.md)

[AdsDDSetFieldProperty](ace_adsddsetfieldproperty.md)

[AdsDDGetFieldProperty](ace_adsddgetfieldproperty.md)

[AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.md)
