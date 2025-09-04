---
title: Ade Getindexnames
slug: ade_getindexnames
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getindexnames.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: c4942067c24d756f34f3549584102d8c5037f02a
---

# Ade Getindexnames

GetIndexNames

TAdsDictionary.GetIndexNames

Advantage TDataSet Descendant

| TAdsDictionary.GetIndexNames  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Retrieves a string list of the index tag object names in the data dictionary.

Syntax

TAdsDictionary.GetIndexNames( strTableName : string;

poIndexNameList : TStringList )

Parameters

| strTableName | The name of the table that the tags are associated with. |
| poIndexNameList | A TStringList object that will hold the index names. |

Remarks

TAdsDictionary.GetIndexNames will retrieve all the index tag object names associated with the data dictionary.

Example

This example opens a data dictionary and retrieves all of the associated index tag object names.

procedure GetIndexNamesExample;

var

oAdsDictionary : TAdsDictionary;

oIndexNames : TStringList;

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

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

oIndexNames.Free;

 

 

end;

See Also

[GetRINames](ade_getrinames.md)

[GetTableNames](ade_gettablenames_ddictionary.md)

[GetIndexFileNames](ade_getindexfilenames.md)

[GetFieldNames](ade_getfieldnames.md)
