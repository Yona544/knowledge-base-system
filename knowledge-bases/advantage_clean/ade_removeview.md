---
title: Ade Removeview
slug: ade_removeview
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_removeview.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 1f9368699674ba87cd4aadbd8b5b66f341d68ef6
---

# Ade Removeview

RemoveView

TAdsDictionary.RemoveView

Advantage TDataSet Descendant

| TAdsDictionary.RemoveView  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Removes a View from the data dictionary.

Syntax

TAdsDictionary.RemoveView( strTableName : string }

Parameters

| strViewName | Name of the table identifying the table object in the data dictionary. |

Remarks

TAdsDictionary.RemoveView removes the view object from the data dictionary.

DROP permissions on the view are required to remove a view from a data dictionary. See Advantage Data Dictionary User Permissions for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

procedure RemoveViewExample;

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

oAdsDictionary.Getviewnames( oViewNames );

 

oAdsDictionary.RemoveView( 'View1' );

oAdsDictionary.RemoveView( 'View2' );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

oViewNames.Free;

 

 

 

end;

See Also

[AddView](ade_addview.md)
