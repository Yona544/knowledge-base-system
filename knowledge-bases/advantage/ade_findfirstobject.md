FindFirstObject




Advantage Database Server 12  

TAdsDictionary.FindFirstObject

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.FindFirstObject  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.FindFirstObject Advantage TDataSet Descendant ade\_Findfirstobject Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.FindFirstObject  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Retrieves the name of the first object of the specified type from the data dictionary.

Syntax

TAdsDictionary.FindFirstObject( usFindObjectType : UNSIGNED16;

strParentName : string;

pcObjectName : pChar;

pusObjectNameLen : PUNSIGNED16;

phFindHandle : PADSHANDLE );

Parameters

|  |  |
| --- | --- |
| usFindObjectType | Type of objects to search for. See Remarks for allowed values. |
| strParentName (I) | Name of the object that is the parent or owner of the searched object. This parameter is ignored for finding the table or referential integrity definition. For finding index file, index key or field object, this parameter should supply the name of a table object. |
| pcObjectName (O) | Returns the name of first object in the data dictionary matching the search condition. The length of the object name has a maximum length of ADS\_MAX\_OBJECT\_NAME\_LEN. |
| pusObjectNameLen (I/O) | Inputs the size of the buffer pointed to by the pcObjectName. Outputs the length of the object name returned in pcObjectName. |
| phFindHandle (O) | The handle that gets returned so you can use it on a subsequent call to FindNextObject. |

Remarks

TAdsDictionary.FindFirstObject finds an object in the data dictionary matching the specified condition and returns the name of the object. After calling this function, [TAdsDictionary.FindNextObject](ade_findnextobject.htm) can be called to iterate through all objects that match the specified search condition.

Only database objects that the current user has access to will be returned. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

Note You do not need to use this method to get object names out of the data dictionary. TAdsDictionary already has methods to perform these tasks. They are much easier to use.

The following methods can be used:

|  |  |
| --- | --- |
| · | GetFieldNames |

|  |  |
| --- | --- |
| · | GetGroupNames |

|  |  |
| --- | --- |
| · | GetTableNames |

|  |  |
| --- | --- |
| · | GetIndexFileNames |

|  |  |
| --- | --- |
| · | GetIndexNames |

|  |  |
| --- | --- |
| · | GetIndexNamesPerFile |

|  |  |
| --- | --- |
| · | GetRINames |

|  |  |
| --- | --- |
| · | GetStoredProcedureNames |

|  |  |
| --- | --- |
| · | GetUserNames |

|  |  |
| --- | --- |
| · | GetUserNamesFromGroup |

|  |  |
| --- | --- |
| · | GetViewNames |

|  |  |
| --- | --- |
| · | GetDDLinkNames |

|  |  |
| --- | --- |
| usFindObjectType | Description |
| ADS\_DD\_TABLE\_OBJECT | Retrieves the name of a table object. The strParentName is ignored and assumed to be the database. |
| ADS\_DD\_RELATION\_OBJECT | Retrieves the name of a referential integrity definition. The strParentName is ignored and assumed to be the database. |
| ADS\_DD\_INDEX\_FILE\_OBJECT | Retrieves the name of a index file object that is associated with the table object specified by the strParentName. |
| ADS\_DD\_INDEX\_OBJECT | Retrieves the name of an index key that has been defined in any index file associated with the table specified by the strParentName. |
| ADS\_DD\_FIELD\_OBJECT | Retrieves the name of the first field in the table specified by the strParentName. |
| ADS\_DD\_VIEW\_OBJECT | Retrieves the name of a view object. |
| ADS\_DD\_USER\_OBJECT | Retrieves the name of a user object. |
| ADS\_DD\_USER\_GROUP\_OBJECT | Retrieves the name of a group object. |
| ADS\_DD\_PROCEDURE\_OBJECT | Retrieves the name of a stored procedure object. |
| ADS\_DD\_LINK\_OBJECT | Retrieves the name of a link object. |

Example

This example creates a database and adds some tables. It then retrieves the information with FindFirstObject and FindNextObject.

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

 

oTableNames.Free

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

[GetDDLinkNames](ade_getddlinknames_tadsdictionary.htm)

[FindNextObject](ade_findnextobject.htm)

[FindClose](ade_findclose.htm)