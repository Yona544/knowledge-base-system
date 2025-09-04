---
title: Ace Adsddaddtable
slug: ace_adsddaddtable
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddaddtable.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 273673ba6dfd3790467644a8748d29ef4e3d9d10
---

# Ace Adsddaddtable

AdsDDAddTable

AdsDDAddTable

Advantage Client Engine

| AdsDDAddTable  Advantage Client Engine |  |  |  |  |

Adds a free table into the data dictionary.

Syntax

UNSIGNED32 AdsDDAddTable( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucTableName,

UNSIGNED8 \*pucTablePath,

UNSIGNED16 usTableType,

UNSIGNED16 usCharType,

UNSIGNED8 \*pucIndexFiles,

UNSIGNED8 \*pucComments );

Parameters

| hAdminConn (I) | Handle of a database connection). |
| pucTableName (I) | Name of the table to be stored in the data dictionary. This name will be used to reference the table in the data dictionary. If this parameter is NULL, the base name of the table without extension will be used by default. The name of the table uniquely identifies the table in the data dictionary. |
| pucTablePath (I) | Fully qualified path to the table file. If the table has associated memo and auto-open index files, they are expected to be located in the same directory as the table file. |
| usTableType (I) | Type of table. Options are ADS\_ADT, ADS\_VFP, ADS\_CDX and ADS\_NTX. |
| usCharType (I) | Type of character data in the table. Valid values include ADS\_ANSI, ADS\_OEM, or one of the [dynamic collations](master_collation_support.md) such as GENERAL\_VFP\_CI\_AS\_1252. This indicates the type of character data to be stored in the table and the collation to use when sorting the data. For compatibility with DOS-based CA-Clipper applications, ADS\_OEM should be specified when opening DBF tables. |
| pucIndexFiles (I) | Extra index files to associate with the table. Multiple index files can be specified by separating individual index file with semi-colon, ;. Auto-open index file does not need to be specified. |
| pucComments (I) | Optional comments to store in the data dictionary to describe the table. |

Special Return Codes

| AE\_DD\_REQUEST\_NOT\_COMPLETED | Possible cause for this error is that the table may be already part of a data dictionary. A detailed error description can be retrieved by calling the function [AdsGetLastError](ace_adsgetlasterror.md) immediately after receiving this error. |

Remarks

AdsDDAddTable associates a table with the database defined in the data dictionary. After the table becomes a database table), other data dictionary functionality, such as default field values and field and record level constraints can be defined for the table. If an NTX table and all index files associated with the table are added into the data dictionary, those index files become auto-open indexes. This is particularly useful if an NTX table is to be used in SQL queries.

CREATE TABLE permissions are required to add a table to a data dictionary. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

When an ADT type table is associated with a data dictionary, more advanced features, such as referential integrity, can be defined for the table. Once an ADT type table becomes a database table), it can only be opened on a database connection) (see [AdsConnect60](ace_adsconnect60.md)).

When a DBF type (CDX, VFP or NTX) table is associated with a data dictionary, it can still be opened on free connections). Note that if the DBF table is accessed through a free connection, the additional non-structural index files will not be opened automatically.

Note AdsDDAddTable requires an exclusive open of ADT tables in order to add them to a data dictionary. An error will be returned if the table cannot be opened exclusively. DBF tables can be added to a data dictionary without an exclusive open.

 

Note AdsDDAddTable can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

Add a DBF table with two NTX index files into the data dictionary and name the table in the data dictionary "Customer Information". Then open the table through an anonymous database connection and perform a go top in the order "Lastname".

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

AdsDDAddTable( hDD, "Customer Information", "n:\\mydata\\customer.dbf", ADS\_NTX,

ADS\_OEM, "Lastname.ntx;Cust\_id.ntx", NULL );

AdsDisconnect( hDD );

 

AdsConnect60("n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, NULL, NULL,

ADS\_DEFAULT, &hConn );

AdsOpenTable( hConn, "Customer Information", NULL, ADS\_DEFAULT, ADS\_DEFAULT,

ADS\_DEFAULT, ADS\_DEFAULT,

ADS\_DEFAULT, &hTable );

AdsGetIndex( hTable, "Lastname", &hOrder );

AdsGotoTop( hOrder );

See Also

[AdsConnect60](ace_adsconnect60.md)

[AdsDDRemoveTable](ace_adsddremovetable.md)

[AdsDDSetTableProperty](ace_adsddsettableproperty.md)

[AdsDDGetTableProperty](ace_adsddgettableproperty.md)

[AdsDDSetFieldProperty](ace_adsddsetfieldproperty.md)

[AdsDDGetFieldProperty](ace_adsddgetfieldproperty.md)

[AdsDDAddIndexFile](ace_adsddaddindexfile.md)

[AdsOpenTable](ace_adsopentable.md)

[sp\_AddTableToDatabase](master_sp_addtabletodatabase.md)
