---
title: Ade Removeindexfile
slug: ade_removeindexfile
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_removeindexfile.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 5bfedab9a98da5461b0c62774764d166e3a92a0d
---

# Ade Removeindexfile

RemoveIndexFile

TAdsDictionary.RemoveIndexFile

Advantage TDataSet Descendant

| TAdsDictionary.RemoveIndexFile  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Removes an index file from the data dictionary.

Syntax

TAdsDictionary.RemoveIndexFile( strTableName : string;

strIndexFileName : string;

bDelete : boolean );

Parameters

| strTableName | Name of the table identifying the table object in the data dictionary. |
| strIndexFileName | Name of the index file to remove. |
| bDelete | If this parameter is TRUE, the index file will be removed from storage permanently. |

Remarks

TAdsDictionary.RemoveIndexFile removes an index file from the data dictionary. All index tags in the index file will be removed. If a tag is a primary key, the index file will not be removed. If bDelete is TRUE the index file will be removed from the drive.

ALTER permissions on the associated table are required to remove an index from a data dictionary. See Advantage Data Dictionary User Permissions for more information.

Note This function requires exclusive open of the table. An error will be returned if the table cannot be opened exclusively. If the table is the parent of any referential integrity in the data dictionary, the function will return an error.

 

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

procedure RemoveIndexFileExample;

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

oAdsDictionary.GetIndexFileNames( 'offices', oIndexNames );

oAdsDictionary.GetIndexFileNames( 'salesreps', oIndexNames );

 

oAdsDictionary.GetIndexFileProperty( 'offices',

oIndexNames.Strings[ 0 ],

ADS\_DD\_INDEX\_FILE\_RELATIVE\_PATH,

@pucProperty,

usLength );

 

oAdsDictionary.RemoveIndexFile( 'offices',

oIndexNames.Strings[ 0 ],

FALSE );

 

oAdsDictionary.AddIndexFile( 'offices',

'd:\demo\offices.adi',

'The demo index.' );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

oIndexNames.Free;

 

 

 

end;

See Also

[AddTable](ade_addtable.md)
