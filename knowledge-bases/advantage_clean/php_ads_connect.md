---
title: Php Ads Connect
slug: php_ads_connect
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: php_ads_connect.htm
source: Advantage CHM
tags:
  - php
checksum: c71d567465d3d4f9fcb24f0edea5132374384c05
---

# Php Ads Connect

ads\_connect

ads\_connect

Advantage PHP Extension

| ads\_connect  Advantage PHP Extension |  |  |  |  |

Makes a connection to an Advantage Database Server.

Syntax

resource ads\_connect( string DSN

[, string user ]

[, string password ]

[, int cursor\_option] )

Parameters

| DSN (I) | Connection string specifying the Advantage Database Server in which to connect and the options for that connection. All entries in the connection string are keywords followed by an attribute; a semi-colon separates each keyword attribute pair. All keywords are case insensitive. All attributes are also case insensitive except 'DataDirectory'. The attribute for the DataDirectory keyword may be case sensitive depending on the operating system. |
| user (I) | Optional user name in which to authenticate to the data dictionary. The user name and password are validated against information stored in the data dictionary. If this parameter is specified, the DSN must specify a full path including the Advantage Data Dictionary name. Otherwise, an error will be returned. |
| password (I) | Optional password in which to authenticate to the data dictionary for the specified user. |
| cursor\_option (I) | Optional type of cursor to be returned. Allowed values are: SQL\_CURSOR\_FORWARD\_ONLY, SQL\_CURSOR\_DYNAMIC, or SQL\_CURSOR\_KEYSET\_DRIVEN. |

Remarks

ads\_connect connects to the Advantage Database Server on a given server. The following keywords can be included in the DSN to specify the server in which to connect and the connections properties.

| DataDirectory | The fully qualified path to the computer where the data files exist, and the default location of the data files. This fully qualified path must contain a drive letter or use UNC. The DataDirectory must be specified before a successful connection to an Advantage server can occur. If a Free Connection) is desired, the DataDirectory must specify a directory location. For a Database Connection), the path and data dictionary file must be specified in the DataDirectory entry (e.g., DataDirectory =\\myserver\myvolume\mypath\mydd.add). |
| DefaultType | Specifies the desired table type. Valid values include Advantage for ADT/ADI/ADM files, FoxPro for DBF/CDX/FPT files, Visual FoxPro for DBF/CDX/FPT files compatible with Visual FoxPro, and Clipper for DBF/NTX/DBT files. The default is Advantage. Note: this entry is ignored when obtaining a Database Connection). The table type is stored in the data dictionary for database tables. Note: to get support for NTX index files, create a database (defined in a data dictionary) and add the tables and the associated NTX index files to that database. Then use those tables on that Database Connection). The NTX index files will then get automatically opened when the corresponding DBF table is opened. You can use the Advantage Data Architect to create a database and data dictionary. |
| ServerTypes | The value for ServerTypes is a number N that is the sum of values indicating the types of Advantage servers to which connections are should be attempted. The values for the servers are:  Advantage Database Server = 2  Advantage Internet Server = 4.  For example, to allow a connection to use the Advantage Database Server or the Advantage Internet Server, use: ServerTypes=6 (2+4). When multiple types are specified and multiple server types are available, the order of precedence is Advantage Database Server first and Advantage Internet Server second. The default value is 2, Advantage Database Server. |
| AdvantageLocking | Specifies the locking mode to use with DBF tables. Valid values include On and Off. This setting is applicable to the FoxPro and Clipper DefaultType options. If set to On, Advantages proprietary high-performance internal locking mode is used. If set to Off, DBF tables can be shared in a writable mode with non-Advantage database applications. The default is On. See [Advantage Locking Modes](master_advantage_locking_modes.md) for more information. |
| CharSet | Specifies whether the data in DBF tables is ANSI or OEM. Valid values include ANSI and OEM. This setting is applicable to the FoxPro and Clipper DefaultType options. The default is ANSI. |
| Language | If this setting is provided, it overrides the CharSet setting. It can be used to specify one of the [dynamic collations](master_collation_support.md) such as GENERAL\_VFP\_CI\_AS\_1252 for Visual FoxPro compatibility. These collations can be used with Advantage ADT tables and Visual FoxPro (VFP) tables. |
| Locking | Specifies the granularity of the locking used when updating a record. The two possible values are FILE and RECORD. The default is RECORD, which only locks the specific record to be updated. FILE locks the entire file. |
| MaxTableCloseCache | MaxTableCloseCache is the number of tables to cache open. This feature is provided to improve performance of applications, especially when multiple SQL statements are issued on the same group of tables. The default value is 25. |
| MemoBlockSize | MemoBlockSize controls the size of the memo blocks in the memo file that is created when a table is created that contains a memo, binary, or image field. The default is 64 byte memo blocks in the memo file for FoxPro-compatible tables (DBF/FPT) and 8 byte memo blocks in the memo files for Advantage proprietary tables (ADT/ADM). Clipper-compatible tables (DBF/DBT) always have 512-byte memo blocks in the memo file. |
| Rows | If True, deleted rows in DBF tables are displayed. The default is False. This value is only applicable if the DefaultType is FoxPro or Clipper. |
| RightsChecking | Beginning with version 10.0, the client no longer performs rights checking by default. See [Check Rights](master_check_rights.md) for more information. The default value for this setting is OFF. In order for the setting to have any affect, the application must call the Advantage Client Engine API [AdsSetRightsChecking](ace_adssetrightschecking.md). This setting affects catalog operations such as the ability to retrieve column names from free tables.  It has no affect on data dictionary-bound tables or on SQL statements. If this setting is ON and rights checking is enabled, the client driver will perform a file existence check before requesting the server to open the table. If the client workstation does not have access to the table, the operation will fail. If this setting is OFF, the client will send the open request to the server without performing an existence check. |
| TrimTrailingSpaces | Specifies whether trailing white space is removed from string fields when the data is retrieved. Valid values are True or False. If True is specified, character fields will have trailing white spaced trimmed on retrieval. If False is specified, trailing white space is maintained on the values when they are retrieved. This means that a fixed length field (character) with a width of 10, for example, will always return 10 characters when the value is retrieved; it is padded with as many spaces as necessary. The default is False |
| UseReadAhead | UseReadAhead determines the number of records that should be cached by the client. The default value is 10. A value of 0 or 1 will turn record caching off. See [Read-Ahead Record Caching](master_read_ahead_record_caching.md) for more details. |
| ReadOnly | The value True prevents tables from being updated on this connection. The default value False allows tables to be updated. |
| CommType=UDP\_IP | IPX | TCP\_IP | The default is to try all communication protocols and use the first that successfully connects to the Advantage Database Server. If UDP\_IP is specified, the client will only use UDP/IP to communicate with the Advantage Database Server. If IPX is specified, the client will only use IPX to communicate with the Advantage Database Server. If TCP\_IP is specified, the client will only use TCP/IP to communicate with the Advantage Database Server. |

Example

<?

echo "Basic Connect<br>\n";

$rConn = ads\_connect( "DataDirectory=\\\\server1\\share1\\data\\;ServerTypes=2", "", "" );

echo "Connect<br>\n";

ads\_close( $rConn );

echo "Closed<br>\n";

?>

See Also

[ads\_pconnect](php_ads_pconnect.md)

[ads\_close](php_ads_close.md)

[ads\_close\_all](php_ads_close_all.md)
