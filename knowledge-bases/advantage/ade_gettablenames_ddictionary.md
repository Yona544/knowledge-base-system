GetTableNames




Advantage Database Server 12  

TAdsDictionary.GetTableNames

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.GetTableNames  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.GetTableNames Advantage TDataSet Descendant ade\_Gettablenames\_ddictionary Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.GetTableNames  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Returns a TStringList of the Table object names in the data dictionary.

Syntax

TAdsDictionary.GetTableNames( poTableNameList : TStringList )

Parameters

|  |  |
| --- | --- |
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

[GetIndexNames](ade_getindexnames.htm)

[GetRINames](ade_getrinames.htm)

[GetIndexFileNames](ade_getindexfilenames.htm)

[GetFieldNames](ade_getfieldnames.htm)