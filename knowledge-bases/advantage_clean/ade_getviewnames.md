---
title: Ade Getviewnames
slug: ade_getviewnames
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getviewnames.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 3e838802c056c7db6b0ca6c61a4d1bc9520e50f1
---

# Ade Getviewnames

GetViewNames

TAdsDictionary.GetViewNames

Advantage TDataSet Descendant

| TAdsDictionary.GetViewNames  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Returns a TStringList of the view object names in the data dictionary.

Syntax

TAdsDictionary.GetViewNames( poViewNameList : TStringList )

Parameters

| poViewNameList | A TStringList object that will hold the RI names. |

Remarks

TAdsDictionary.GetViewNames will retrieve all the view object names associated with the data dictionary.

Example

This example opens a data dictionary and gets all of the associated view Object names.

procedure GetViewNames;

var

oAdsDictionary : TAdsDictionary;

oViewNames : TStringList;

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

 

oAdsDictionary.AddView( 'View1',

'',

'select \* from offices' );

 

oAdsDictionary.AddView( 'View2',

'',

'select \* from salesreps' );

 

 

 

{\* now we are going to make the call to getviewnames \*}

oViewNames := TStringList.Create;

oAdsDictionary.GetViewNames( oViewNames );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

oViewNames.Free;

 

 

 

end;

See Also

[GetIndexNames](ade_getindexnames.md)

[GetTableNames](ade_gettablenames_ddictionary.md)

[GetIndexFileNames](ade_getindexfilenames.md)
