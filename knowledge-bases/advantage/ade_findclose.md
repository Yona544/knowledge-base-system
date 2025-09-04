FindClose




Advantage Database Server 12  

TAdsDictionary.FindClose

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.FindClose  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.FindClose Advantage TDataSet Descendant ade\_Findclose Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.FindClose  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Closes a previously defined search in the data dictionary.

Syntax

TAdsDictionary.FindClose();

Parameters

None.

Remarks

TAdsDictionary.FindClose is used to terminate a search initiated by [TAdsDictionary.FindFirstObject.](ade_findfirstobject.htm).

Example

procedure FindTablesExample;

var

oAdsDictionary : TAdsDictionary;

usObjectNameLen : UNSIGNED16;

hFindHandle : ADSHANDLE;

oTableNames : TStringList;

aucObjectName : array [ 0..ADS\_DD\_MAX\_OBJECT\_NAME\_LEN ] of char;

 

begin

{\* call the constructor \*}

oAdsDictionary := TAdsDictionary.Create( self );

 

{\* set the server type \*}

 

oAdsDictionary.AdsServerTypes := [ stADS\_LOCAL ];

 

{\* call the method to create the data dictionary files \*}

oAdsDictionary.CreateDictionary( 'd:\dd\demo.add', FALSE, 'This is a demo database.' );

 

{\*

\* The CreateDictionary call leaves an ADSSYS connection open. We can now

\* use that connection to call other administrative methods.

\* }

 

 

oAdsDictionary.AddTable( 'NewTable',

'd:\demo\demotable.adt',

'',

'This is my first table.',

ttAdsADT,

ANSI );

 

oAdsDictionary.AddTable( 'NewTable2',

'd:\demo\demotableb.adt',

'',

'This is my second table.',

ttAdsADT,

ANSI );

 

 

{\*

\* now we have added tables to the dictionary, lets call FindFirstObject

\* and FindNextObject to get the table names.

\*}

 

usObjectNameLen := ADS\_DD\_MAX\_OBJECT\_NAME\_LEN;

oAdsDictionary.FindFirstObject( ADS\_DD\_TABLE\_OBJECT,

'',

@aucObjectName,

@usObjectNameLen,

@hFindHandle );

 

{\* now create our TStringList to hold the TableNames \*}

 

oTableNames := TStringList.Create;

aucObjectName[ usObjectNameLen ] := #0;

oTableNames.Add( aucObjectName );

 

 

{\*

\* now we are going to keep looping until FindNextObject returns

\* no more names.

\*}

 

while( TRUE ) do

begin

try

oAdsDictionary.FindNextObject( hFindHandle,

@aucObjectName,

@usObjectNameLen );

aucObjectName[ usObjectNameLen ] := #0;

oTableNames.Add( aucObjectName );

except

aucObjectName[ usObjectNameLen ] := #0;

oTableNames.Add( aucObjectName );

break;

end;

 

end; {\* while \*}

 

oAdsDictionary.FindClose( hFindHandle );

 

oAdsDictionary.IsConnected := FALSE;

 

oTableNames.Free;

oAdsDictionary.Free;

 

 

end;

See Also

[GetFieldNames](ade_getfieldnames.htm)

[GetGroupNames](ade_getgroupnames.htm)

[GetTableNames](ade_gettablenames_ddictionary.htm)

[GetIndexFileNames](ade_getindexfilenames.htm)

[GetIndexNames](ade_getindexnames.htm)

[GetRINames](ade_getrinames.htm)

[GetStoredProcedureNames](ade_getstoredprocedurenames.htm)

[GetUserNames](ade_getusernames.htm)

[GetUsersFromGroup](ade_getusersfromgroup.htm)

[GetViewNames](ade_getviewnames.htm)

[FindFirstObject](ade_findfirstobject.htm)

[FindNextObject](ade_findnextobject.htm)