AddView




Advantage Database Server 12  

TAdsDictionary.AddView

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.AddView  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.AddView Advantage TDataSet Descendant ade\_Addview Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.AddView  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Creates a new view in the data dictionary.

Syntax

TAdsDictionary.AddView(strViewName : string;

strComments : string;

strSQL : string );

Parameters

|  |  |
| --- | --- |
| strViewName | Name of the view to create. |
| strComments | The comments for the new view. |
| strSQL | The SQL to create the view. |

Remarks

TAdsDictionary.AddView creates a new view in the data dictionary.

CREATE VIEW permissions are required to add a view to a data dictionary. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

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

[RemoveView](ade_removeview.htm)