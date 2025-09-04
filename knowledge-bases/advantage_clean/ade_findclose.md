---
title: Ade Findclose
slug: ade_findclose
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_findclose.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: ede29a1f3d90e01ce8b29ccf8706c388f0cb029e
---

# Ade Findclose

FindClose

TAdsDictionary.FindClose

Advantage TDataSet Descendant

| TAdsDictionary.FindClose  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Closes a previously defined search in the data dictionary.

Syntax

TAdsDictionary.FindClose();

Parameters

None.

Remarks

TAdsDictionary.FindClose is used to terminate a search initiated by [TAdsDictionary.FindFirstObject.](ade_findfirstobject.md).

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

[GetFieldNames](ade_getfieldnames.md)

[GetGroupNames](ade_getgroupnames.md)

[GetTableNames](ade_gettablenames_ddictionary.md)

[GetIndexFileNames](ade_getindexfilenames.md)

[GetIndexNames](ade_getindexnames.md)

[GetRINames](ade_getrinames.md)

[GetStoredProcedureNames](ade_getstoredprocedurenames.md)

[GetUserNames](ade_getusernames.md)

[GetUsersFromGroup](ade_getusersfromgroup.md)

[GetViewNames](ade_getviewnames.md)

[FindFirstObject](ade_findfirstobject.md)

[FindNextObject](ade_findnextobject.md)
