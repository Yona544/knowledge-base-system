GetIndexFileNames




Advantage Database Server 12  

TAdsDictionary.GetIndexFileNames

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.GetIndexFileNames  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.GetIndexFileNames Advantage TDataSet Descendant ade\_Getindexfilenames Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.GetIndexFileNames  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Retrieves a string list of the index file object names in the data dictionary.

Syntax

TAdsDictionary.GetIndexFileNames( strTableName : string,

poIndexFileNameList : TStringList )

Parameters

|  |  |
| --- | --- |
| strTableName | The name of the table that the Index File is associated with. |
| poIndexFileNameList | A TStringList object that will hold the Index File names. |

Remarks

TAdsDictionary.GetIndexFileNames will retrieve all the Index File Name object names associated with the data dictionary.

Example

This example opens a data dictionary and gets all of the associated index file Object names.

procedure GetIndexFileNamesExample;

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

oAdsDictionary.GetIndexFileNames( 'offices', oIndexNames );

oAdsDictionary.GetIndexFileNames( 'salesreps', oIndexNames );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

oIndexNames.Free;

 

 

 

end;

See Also

[GetIndexNames](ade_getindexnames.htm)

[GetTableNames](ade_gettablenames_ddictionary.htm)

[GetRINames](ade_getrinames.htm)

[GetFieldNames](ade_getfieldnames.htm)