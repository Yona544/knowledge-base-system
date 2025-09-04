---
title: Ade Gettablenames Ddictionary
slug: ade_gettablenames_ddictionary
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_gettablenames_ddictionary.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: c08fa59e49235d53cc258d096a007e4e2c8f29b2
---

# Ade Gettablenames Ddictionary

GetTableNames

TAdsDictionary.GetTableNames

Advantage TDataSet Descendant

| TAdsDictionary.GetTableNames  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Returns a TStringList of the Table object names in the data dictionary.

Syntax

TAdsDictionary.GetTableNames( poTableNameList : TStringList )

Parameters

| poTableNameList | A TStringList object that will hold the table names. |

Remarks

TAdsDictionary.GetTableNames will retrieve all the table object names associated with the data dictionary.

Example

Opens a data dictionary and get all associated table Object names.

procedure GetTableNamesExample;

var

oAdsDictionary : TAdsDictionary;

oTableNames : TStringList;

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

oTableNames := TStringList.Create;

oAdsDictionary.GetTableNames( oTableNames );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

oTableNames.Free;

 

 

 

end;

See Also

[GetIndexNames](ade_getindexnames.md)

[GetRINames](ade_getrinames.md)

[GetIndexFileNames](ade_getindexfilenames.md)

[GetFieldNames](ade_getfieldnames.md)
