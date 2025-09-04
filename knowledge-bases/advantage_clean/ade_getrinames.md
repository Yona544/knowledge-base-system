---
title: Ade Getrinames
slug: ade_getrinames
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getrinames.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: f7d5952c1969f11545c0401d8641f6cce219b151
---

# Ade Getrinames

GetRINames

TAdsDictionary.GetRINames

Advantage TDataSet Descendant

| TAdsDictionary.GetRINames  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Returns a TStringList of the RI object names in the data dictionary.

Syntax

TAdsDictionary.GetRINames( poRINameList : TStringList )

Parameters

| poRINameList | A TStringList object that will hold the RI names. |

Remarks

TAdsDictionary.GetRINames will retrieve all the RI object names associated with the data dictionary.

Example

This example opens a data dictionary and gets all of the associated RI Object names.

procedure GetRINamesExample;

var

oAdsDictionary : TAdsDictionary;

usLength : UNSIGNED16;

oRINames : TStringList;

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

 

{\* now we need to set the primary indexes for offices \*}

 

usLength := 7;

oAdsDictionary.SetTableProperty( 'offices',

ADS\_DD\_TABLE\_PRIMARY\_KEY,

pChar( 'office' ),

usLength,

ADS\_NO\_VALIDATE,

'' );

 

 

{\* now we create the RI \*}

 

oAdsDictionary.CreateRI( 'NewRI',

'',

'offices',

'office',

'salesreps',

'rep\_office',

ADS\_DD\_RI\_CASCADE,

ADS\_DD\_RI\_CASCADE );

 

 

 

 

{\* now we are going to make the call to getRINames \*}

oRINames := TStringList.Create;

oAdsDictionary.GetRINames( oRINames );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

oRINames.Free;

 

 

 

 

end;

See Also

[GetIndexNames](ade_getindexnames.md)

[GetTableNames](ade_gettablenames_ddictionary.md)

[GetIndexFileNames](ade_getindexfilenames.md)
