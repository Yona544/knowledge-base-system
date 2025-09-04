---
title: Ade Findnextobject
slug: ade_findnextobject
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_findnextobject.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: f86aaf757e926ee4b7fba6d81b5aea6d724b86c4
---

# Ade Findnextobject

FindNextObject

TAdsDictionary.FindNextObject

Advantage TDataSet Descendant

| TAdsDictionary.FindNextObject  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Retrieves the names of the objects matching the search condition from the data dictionary.

Syntax

TAdsDictionary.FindNextObject( hFindHandle : ADSHANDLE

pcObjectName : pChar;

pucObjectNameLen : PUNSIGNED16 );

Parameters

| hFindHandle (I) | The handle that was returned by the call to FindFirstObject. |
| pcObjectName (I/O) | Returns the name of next object in the data dictionary. The length of the object name has a maximum length of ADS\_MAX\_OBJECT\_NAME\_LEN. |
| pucObjectNameLen (I/O) | Inputs the size of the buffer pointed to by the pcObjectName. Outputs the length of the object name returned in pcObjectName. |

Remarks

TAdsDictionary.FindNextObject is used in conjunction with [TAdsDictionary.FindFirstObject](ade_findfirstobject.md) to retrieve the names of the objects matching the search condition from the data dictionary. When names of all objects matching the searching condition have been retrieved, the function returns AE\_NO\_OBJECT\_FOUND.

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

[GetFieldNames](ade_getfieldnames.md)

[GetGroupNames](ade_getgroupnames.md)

[GetTableNames](ade_gettablenames_ddictionary.md)

[GetIndexFileNames](ade_getindexfilenames.md)

[GetIndexNames](ade_getindexnames.md)

[GetIndexNamesPerIndexFile](ade_getindexnamesperindexfile.md)

[GetRINames](ade_getrinames.md)

[GetStoredProcedureNames](ade_getstoredprocedurenames.md)

[GetUserNames](ade_getusernames.md)

[GetUsersFromGroup](ade_getusersfromgroup.md)

[GetViewNames](ade_getviewnames.md)

[FindFirstObject](ade_findfirstobject.md)

[FindClose](ade_findclose.md)
