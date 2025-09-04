FindNextObject




Advantage Database Server 12  

TAdsDictionary.FindNextObject

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.FindNextObject  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.FindNextObject Advantage TDataSet Descendant ade\_Findnextobject Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.FindNextObject  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Retrieves the names of the objects matching the search condition from the data dictionary.

Syntax

TAdsDictionary.FindNextObject( hFindHandle : ADSHANDLE

pcObjectName : pChar;

pucObjectNameLen : PUNSIGNED16 );

Parameters

|  |  |
| --- | --- |
| hFindHandle (I) | The handle that was returned by the call to FindFirstObject. |
| pcObjectName (I/O) | Returns the name of next object in the data dictionary. The length of the object name has a maximum length of ADS\_MAX\_OBJECT\_NAME\_LEN. |
| pucObjectNameLen (I/O) | Inputs the size of the buffer pointed to by the pcObjectName. Outputs the length of the object name returned in pcObjectName. |

Remarks

TAdsDictionary.FindNextObject is used in conjunction with [TAdsDictionary.FindFirstObject](ade_findfirstobject.htm) to retrieve the names of the objects matching the search condition from the data dictionary. When names of all objects matching the searching condition have been retrieved, the function returns AE\_NO\_OBJECT\_FOUND.

Only database objects that the current user has access to will be returned. See Advantage Data Dictionary User Permissions for more information.

Example

This example creates a database and adds some tables. It then retrieves the information

with FindFirstObject and FindNextObject.

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

[GetIndexNamesPerIndexFile](ade_getindexnamesperindexfile.htm)

[GetRINames](ade_getrinames.htm)

[GetStoredProcedureNames](ade_getstoredprocedurenames.htm)

[GetUserNames](ade_getusernames.htm)

[GetUsersFromGroup](ade_getusersfromgroup.htm)

[GetViewNames](ade_getviewnames.htm)

[FindFirstObject](ade_findfirstobject.htm)

[FindClose](ade_findclose.htm)