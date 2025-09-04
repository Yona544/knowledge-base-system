---
title: Ade Removeindex
slug: ade_removeindex
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_removeindex.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 09dd5226093236ad919674092b01f059a3985fdc
---

# Ade Removeindex

RemoveIndex

TAdsDictionary.RemoveIndex

Advantage TDataSet Descendant

| TAdsDictionary.RemoveIndex  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Removes an index from the data dictionary.

Syntax

TAdsDictionary.RemoveIndex( strTableName : string;

strTagName : string );

Parameters

| strTableName | Name of the table that the index tag is part of. |
| strTagName | Name of the tag to delete. |

Remarks

TAdsDictionary.RemoveIndex removes the specified index tag from the Advantage Data Dictionary. If the index tag is designated as the primary key then it cannot be removed. If the index tag is the parent of a referential integrity pair, then it cannot be removed. The function does not delete the index tag from the file. If the last tag in the index file is removed, the index file will be removed from the data dictionary.

ALTER permissions on the associated table are required to remove an index from a data dictionary. See Advantage Data Dictionary User Permissions for more information.

Note This function requires exclusive open of the table. An error will be returned if the table cannot be opened exclusively. If the table is the parent of any referential integrity in the data dictionary, the function will return an error.

 

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

Removing the "Customer" tag from the data dictionary and deleting the files at the same time.

procedure RemoveIndexExample;

var

oAdsDictionary : TAdsDictionary;

oIndexNames : TStringList;

usLength : UNSIGNED16;

pucProperty : array [ 0..ADS\_DD\_MAX\_PROPERTY\_LEN ] of char;

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

 

{\* now we are going to make the call to getviewnames \*}

oIndexNames := TStringList.Create;

oAdsDictionary.GetIndexNames( 'offices', oIndexNames );

oAdsDictionary.GetIndexNames( 'salesreps', oIndexNames );

 

oAdsDictionary.GetIndexProperty( 'offices',

oIndexNames.Strings[ 0 ],

ADS\_DD\_INDEX\_EXPRESSION,

@pucProperty,

usLength );

 

 

oAdsDictionary.RemoveIndex( 'offices',

oIndexNames.Strings[ 0 ] );

 

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

oIndexNames.Free;

 

 

end;

See Also

[AddIndexFile](ade_addindexfile.md)
