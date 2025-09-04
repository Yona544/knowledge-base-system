---
title: Ade Getindexnamesperindexfile
slug: ade_getindexnamesperindexfile
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getindexnamesperindexfile.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: f79f32f71259005ef6c0e3e85be1d7a49f7518dd
---

# Ade Getindexnamesperindexfile

GetIndexNamesPerIndexFile

TAdsDictionary.GetIndexNamesPerIndexFile

Advantage TDataSet Descendant

| TAdsDictionary.GetIndexNamesPerIndexFile  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Syntax

TAdsDictionary.GetIndexNamesPerIndexFile ( strTableName : string;

strIndexFileName : string;

poIndexNames : TStringList );

Parameters

| strTableName (I) | The name of the table the indexes are located. |
| strIndexFileName (I) | The name of the index file where the indexes are located. |
| poIndexNames (O) | The indexes that are located in the given index file. |

Remarks

This function is used to get the indexes within a specific index file.

Example

procedure GetIndexNamesPerIndexFileExample;

var

oAdsDictionary : TAdsDictionary;

oIndexNames : TStringList;

oIndexNameList : TStringList;

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

 

oIndexNameList := TStringList.Create;

oAdsDictionary.GetIndexNamesPerIndexFile( 'offices',

oIndexNames.Strings[ 0 ],

oIndexNameList );

 

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

oIndexNames.Free;

 

 

 

end;

See Also

[GetUsersFromGroup](ade_getusersfromgroup.md)
