GetGroupNames




Advantage Database Server 12  

TAdsDictionary.GetGroupNames

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.GetGroupNames  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.GetGroupNames Advantage TDataSet Descendant ade\_Getgroupnames Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.GetGroupNames  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Syntax

TAdsDictionary.GetGroupNames( poGroupNames : TStringList );

Parameters

|  |  |
| --- | --- |
| poGroupNames | A list of group names that are members of the database will be returned in this TStringList object. |

Example

procedure GetGroupNamesExample;

var

oAdsDictionary : TAdsDictionary;

oGroupNameList : TStringList;

begin

{\* call the constructor \*}

oAdsDictionary := TAdsDictionary.Create( self );

 

oAdsDictionary.AdsServerTypes := [stADS\_REMOTE];

 

{\* call the method to create the data dictionary files \*}

oAdsDictionary.CreateDictionary( 'd:\demo\demo.add', FALSE, 'This is a demo database.' );

 

{\* The CreateDictionary call leaves an ADSSYS connection open.\*}

 

oAdsDictionary.CreateUserGroup( 'NewGroup',

'The newest group.' );

 

oAdsDictionary.AddUser( '',

'NewUser',

'mypassword',

'FirstUser' );

 

oAdsDictionary.AddUserToGroup( 'NewGroup',

'NewUser' );

 

oGroupNameList := TStringList.Create;

oAdsDictionary.GetGroupNames( oGroupNameList );

 

 

oAdsDictionary.DeleteUserGroup( 'NewGroup' );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

end;