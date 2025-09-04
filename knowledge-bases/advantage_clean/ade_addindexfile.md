---
title: Ade Addindexfile
slug: ade_addindexfile
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_addindexfile.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: d59185f3b6f22bc3a0c5af5f18b3322637e2a23d
---

# Ade Addindexfile

AddIndexFile

TAdsDictionary.AddIndexFile

Advantage TDataSet Descendant

| TAdsDictionary.AddIndexFile  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Syntax

TAdsDictionary.AddIndexFile( strTableName : string;

strIndexFilePath : string;

strComment : string );

Parameters

| strTableName (I) | The name of the table the index file is going to be associated with. |
| strIndexFilePath (I) | Fully qualified path to the index file. |
| strComments (I) | Optional comments to store in the data dictionary to describe the index file. |

Remarks

TAdsDictionary.AddIndexFile associates the index name with table name so the index file will be opened automatically when the table is opened.

Note This function requires exclusive open of the table. An error will be returned if the table cannot be opened exclusively.

 

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

procedure AddIndexFileExample;  
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
  oAdsDictionary.AddTable( 'offices', 'd:\demo\offices.adt', '', 'customers table', ttAdsADT, ANSI );   
   
  oAdsDictionary.AddTable( 'salesreps', 'd:\demo\salesreps.adt', '', 'customers table', ttAdsADT, ANSI );   
   
  {\* now we are going to make the call to getviewnames \*}   
  oIndexNames := TStringList.Create;   
  oAdsDictionary.GetIndexFileNames( 'offices', oIndexNames );   
  oAdsDictionary.GetIndexFileNames( 'salesreps', oIndexNames );   
   
  oAdsDictionary.GetIndexFileProperty( 'offices', oIndexNames.Strings[ 0 ], ADS\_DD\_INDEX\_FILE\_RELATIVE\_PATH,   
                                       @pucProperty, usLength );   
   
  oAdsDictionary.RemoveIndexFile( 'offices', oIndexNames.Strings[ 0 ], FALSE );   
   
  oAdsDictionary.AddIndexFile( 'offices', 'd:\demo\offices.adi', 'The demo index.' );   
   
  oAdsDictionary.IsConnected := FALSE;   
   
  oAdsDictionary.Free;   
  oIndexNames.Free;   
   
end;

See Also

[TAdsDictionary.RemoveTable](ade_removetable.md)

[TAdsDictionary.SetTableProperty](ade_settableproperty.md)

[TAdsDictionary.GetTableProperty](ade_gettableproperty.md)

[TAdsDictionary.SetFieldProperty](ade_setfieldproperty.md)

[TAdsDictionary.GetFieldProperty](ade_getfieldproperty.md)

[TAdsDictionary.AddIndexFile](ade_addindexfile.md)
