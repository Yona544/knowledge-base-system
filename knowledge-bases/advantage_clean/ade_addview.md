---
title: Ade Addview
slug: ade_addview
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_addview.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 16d1978971aa2e4ea23df34aaac41b4ba7816ccc
---

# Ade Addview

AddView

TAdsDictionary.AddView

Advantage TDataSet Descendant

| TAdsDictionary.AddView  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Creates a new view in the data dictionary.

Syntax

TAdsDictionary.AddView(strViewName : string;

strComments : string;

strSQL : string );

Parameters

| strViewName | Name of the view to create. |
| strComments | The comments for the new view. |
| strSQL | The SQL to create the view. |

Remarks

TAdsDictionary.AddView creates a new view in the data dictionary.

CREATE VIEW permissions are required to add a view to a data dictionary. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

procedure AddViewExample;

var

oAdsDictionary : TAdsDictionary;

oViewNames : TStringList;

begin

{\* call the constructor \*}

oAdsDictionary := TAdsDictionary.Create( self );

 

oAdsDictionary.AdsServerTypes := [stADS\_REMOTE];

 

{\* call the method to create the data dictionary files \*}

oAdsDictionary.CreateDictionary( 'd:\dd\demo.add', FALSE, 'This is a demo database.' );

 

{\* The CreateDictionary call leaves an ADSSYS open.\*}

 

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

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

oViewNames.Free;

 

 

 

end;

See Also

[RemoveView](ade_removeview.md)
