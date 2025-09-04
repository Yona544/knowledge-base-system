---
title: Master Sp Addtabletodatabase
slug: master_sp_addtabletodatabase
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_addtabletodatabase.htm
source: Advantage CHM
tags:
  - master
checksum: ef7c153087130ce9ae3cbbde06eabd28fc1a71c9
---

# Master Sp Addtabletodatabase

sp\_AddTableToDatabase

sp\_AddTableToDatabase

Advantage SQL Engine

| sp\_AddTableToDatabase  Advantage SQL Engine |  |  |  |  |

Adds a free table into the data dictionary.

Syntax

sp\_AddTableToDatabase(

TableName,CHARACTER,200,

TablePath,CHARACTER,515,

TableType,SHORTINT,

CharType,SHORTINT,

IndexFiles,MEMO,

Comment,MEMO )

Parameters

| TableName (I) | Name of the table to be stored in the data dictionary. This name will be used to reference the table in the data dictionary. The name of the table uniquely identifies the table in the data dictionary. |
| TablePath (I) | Fully qualified UNC path to the table file, or a relative path to the table from the location of the data dictionary. If the table has associated memo and auto-open index files, they are expected to be located in the same directory as the table file. |
| TableType (I) | Type of table. Valid options include: 1 for NTX DBF tables, 2 for CDX DBF tables, 3 for ADT tables, and 4 for VFP DBF tables. |
| CharType (I) | Type of character data in the table. Options are 1 for ANSI collation and 2 for OEM collation. This indicates the type of character data to be stored in the table. For compatibility with DOS-based CA-Clipper applications, OEM should be specified. When adding Advantage propriety tables, this parameter is ignored and ANSI is always used. If a [dynamic collation](master_collation_support.md) has been specified for the SQL statement, that collation will take precedence over the character type specified in this parameter. |
| IndexFiles (I) | Extra index files to associate with the table. Multiple index files can be specified by separating individual index file with semi-colon, ;. Auto-open index file does not need to be specified. |
| Comments (I) | Optional comments to store in the data dictionary to describe the table. |

Special Return Codes

| AE\_DD\_REQUEST\_NOT\_COMPLETED | Possible cause for this error is that the table may be already part of a data dictionary. Calling the function AdsGetLastError immediately after receiving this error can retrieve a detailed error description. |

Remarks

sp\_AddTableToDatabase associates a table with the database defined in the data dictionary. After the table becomes a database table, other data dictionary functionality, such as default field values and field and record level constraints can be defined for the table. If an NTX table and all of the index files associated with the table are added into the data dictionary, those index files become auto-open indexes. This is particularly useful if an NTX table is to be used in SQL queries.

When an ADT type table is associated with a data dictionary, more advanced features, such as referential integrity, can be defined for the table. Once an ADT type table becomes a database table, it can only be opened on a database connection (see AdsConnect60).

When a DBF type (VFP, CDX or NTX) table is associated with a data dictionary, it can still be opened on free connections. Note that if the DBF table is accessed through a free connection, the additional non-structural index files will not be opened automatically.

Note sp\_AddTableToDatabase requires an exclusive open of ADT tables in order to add them to a data dictionary. An error will be returned if the table cannot be opened exclusively. DBF tables can be added to a data dictionary without an exclusive open.

Example

Add a DBF table with two NTX index files into the data dictionary and name the table in the data dictionary "Customer Information".

EXECUTE PROCEDURE sp\_AddTableToDatabase(

Customer Information,

\\server\share\mydata\customer.dbf,

1,

2,

Lastname.ntx;Cust\_id.ntx,

NULL );

See Also

[sp\_ModifyTableProperty](master_sp_modifytableproperty.md)

[systems.tables](master_system_tables.md)

[sp\_AddIndexFileToDatabase](master_sp_addindexfiletodatabase.md)
