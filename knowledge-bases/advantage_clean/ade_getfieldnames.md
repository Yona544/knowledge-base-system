---
title: Ade Getfieldnames
slug: ade_getfieldnames
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getfieldnames.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: c82c6bc21629b48273df3729d231d9e062ab62d5
---

# Ade Getfieldnames

GetFieldNames

TAdsDictionary.GetFieldNames

Advantage TDataSet Descendant

| TAdsDictionary.GetFieldNames  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Retrieves a TStringList of the field object names in the data dictionary.

Syntax

TAdsDictionary.GetFieldNames( strTableName, poFieldList : TStringList )

Parameters

| strTableName | The name of the table associated with the field names. |
| poFieldList | A TStringList object that will hold the field names. |

Remarks

TAdsDictionary.GetFieldNames will retrieve all the field object names associated with the data dictionary.

Example

Opens a data dictionary and gets all associated field object names.

procedure GetFieldNamesExample;

var

oAdsDictionary : TAdsDictionary;

oFieldNames : TStringList;

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

oFieldNames := TStringList.Create;

oAdsDictionary.GetFieldNames( 'offices', oFieldNames );

oAdsDictionary.GetFieldNames( 'salesreps', oFieldNames );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

oFieldNames.Free;

 

 

 

end;

See Also

[GetIndexNames](ade_getindexnames.md)

[GetTableNames](ade_gettablenames_ddictionary.md)

[GetIndexFileNames](ade_getindexfilenames.md)

[GetRINames](ade_getrinames.md)
