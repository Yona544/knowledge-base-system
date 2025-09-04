GetIndexNamesPerIndexFile




Advantage Database Server 12  

TAdsDictionary.GetIndexNamesPerIndexFile

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.GetIndexNamesPerIndexFile  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.GetIndexNamesPerIndexFile Advantage TDataSet Descendant ade\_Getindexnamesperindexfile Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.GetIndexNamesPerIndexFile  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Syntax

TAdsDictionary.GetIndexNamesPerIndexFile ( strTableName : string;

strIndexFileName : string;

poIndexNames : TStringList );

Parameters

|  |  |
| --- | --- |
| strTableName (I) | The name of the table the indexes are located. |
| strIndexFileName (I) | The name of the index file where the indexes are located. |
| poIndexNames (O) | The indexes that are located in the given index file. |

Remarks

This function is used to get the indexes within a specific index file.

Example

procedure GetIndexNamesPerIndexFileExample;

var

oAdsDictionary : TAdsDictionary;

oIndexNames : TStringList;

oIndexNameList : TStringList;

usLength : UNSIGNED16;

pucProperty : array [ 0..ADS\_DD\_MAX\_PROPERTY\_LEN ] of char;

 

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

 

oIndexNameList := TStringList.Create;

oAdsDictionary.GetIndexNamesPerIndexFile( 'offices',

oIndexNames.Strings[ 0 ],

oIndexNameList );

 

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

oIndexNames.Free;

 

 

 

end;

See Also

[GetUsersFromGroup](ade_getusersfromgroup.htm)