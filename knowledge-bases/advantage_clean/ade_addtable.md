---
title: Ade Addtable
slug: ade_addtable
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_addtable.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: b09626161d9342f6f8f5cf448a2a7001cc58d139
---

# Ade Addtable

AddTable

TAdsDictionary.AddTable

Advantage TDataSet Descendant

| TAdsDictionary.AddTable  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Associates a table with the data dictionary.

Syntax

TAdsDictionary.AddTable( strTableName : string;

strTablePath : string;

strIndexFiles : string;

strComments : string;

usTableType : TAdsTableTypes

usCharType : TAdsCharTypes );

Parameters

| strTableName (I) | Name of the table to be stored in the data dictionary. This name will be used to reference the table in the data dictionary. If this parameter is an empty string, the base name of the table will be used as the default. The name of the table uniquely identifies the table in the data dictionary. |
| strTablePath (I) | Fully qualified path to the table file. If the table has associated memo and structural index files, they are expected to be located in the same directory as the table file. |
| strIndexFiles (I) | Extra index files to associate with the table. Multiple index files can be specified by separating individual index file with semi-colon, ;. Structural index file does not need to be specified. |
| strComments (I) | Optional comments to store in the data dictionary to describe the table. |
| usTableType (I) | The table type (ttAdsADT, ttAdsVFP, ttAdsCDX, ttAdsNTX). |
| usCharType (I) | The table character type. (ANSI, OEM). This can also be one of the dynamically loaded collations such as GENERAL\_VFP\_CI\_AS\_1252. See [dynamic collation support](master_collation_support.md). |

Remarks

TAdsDictionary.AddTable associates a table with the data dictionary. Once the table becomes part of the data dictionary, it can be opened through a data dictionary bound connection and all index files associated with the table will be opened automatically. This is particularly useful if an NTX table is to be used in SQL queries.

When an ADT type table is associated with a data dictionary, additional features, such as default field value, field and record level constraints, referential integrity, and etc., can be defined for the table. Once an ADT type table is associated with a data dictionary, it can only be opened on a connection that is bound with the data dictionary (see AdsConnect60).

When a DBF type (VFP, CDX or NTX) table is associated with a data dictionary, it can still be used through normal non-data dictionary bound connection. Note that if the DBF table is accessed through a non-data dictionary bound connection, the additional non-structural index files will not be opened automatically.

Note TAdsDictionary.AddTable requires exclusive open of the table. An error will be returned if the table cannot be opened exclusively.

 

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

procedure AddTableExample;

var

oAdsDictionary : TAdsDictionary;

begin

{\* call the constructor \*}

oAdsDictionary := TAdsDictionary.Create( self );

 

oAdsDictionary.AdsServerTypes := [stADS\_REMOTE];

 

{\* call the method to create the data dictionary files \*}

oAdsDictionary.CreateDictionary( 'd:\dd\demo.add', FALSE, 'This is a demo database.' );

 

{\* The CreateDictionary call leaves an ADSSYS connection open.\*}

 

{\* now we are going to add a couple tables from our sample tables \*}

oAdsDictionary.AddTable( 'offices',

'd:\demo\offices.adt',

'',

'customers table',

ttAdsADT,

ANSI );

 

oAdsDictionary.AddTable( 'salesreps',

'd:\demo\salesreps.adt',

'',

'customers table',

ttAdsADT,

ANSI );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

end;

See Also

[RemoveTable](ade_removetable.md)

[SetTableProperty](ade_settableproperty.md)

[GetTableProperty](ade_gettableproperty.md)

[SetFieldProperty](ade_setfieldproperty.md)

[GetFieldProperty](ade_getfieldproperty.md)

[AddIndexFile](ade_addindexfile.md)
