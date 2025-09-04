GetUserProperty




Advantage Database Server 12  

TAdsDictionary.GetUserProperty

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.GetUserProperty  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.GetUserProperty Advantage TDataSet Descendant ade\_Getuserproperty Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.GetUserProperty  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Syntax

procedure GetUserProperty( strUserName : string;

usProperty : UNSIGNED16;

pvProperty : pointer;

var usPropertyLen : UNSIGNED16 ); virtual;

Parameters

|  |  |
| --- | --- |
| strUserName (I) | Name of the database user object to retrieve the associated property. |
| usPropertyID (I) | Index of a database user property to retrieve. See Remarks for allowed values. |
| pvProperty (O) | Pointer to the buffer where the property is to be copied into. |
| usPropertyLen (I/O) | On input, it specifies the size of the buffer pointed to by pvProperty. On output, it returns the length of property stored in the buffer. |

Remarks

GetUserProperty retrieves one user property associated with the specified user. User properties can only be retrieved by the specified user or users with administrative permissions to this user. When the TAdsDictionary is opened as the administrator (ADSSYS user account), properties from any user can be retrieved.

The following are the valid values of usPropertyID and the expected return value in pvProperty and \*pusPropertyLen.

|  |  |
| --- | --- |
| usPropertyID | Description |
| ADS\_DD\_COMMENT | Returns the description of the user in pvProperty. |
| ADS\_DD\_USER\_DEFINED\_PROP | Returns the user defined property for the specified user. |
| ADS\_DD\_USER\_GROUP\_MEMBERSHIP | Returns in the pvProperty the user groups that the specified user is a member of. The group membership is returned as a ; delimited string listing all user groups that the user is a member. For example: if the returned string is Managers;R&D, that means the user belongs to 2 user groups the Managers user group and the R&D user group. |

Example

procedure GetUserProperty;

var

oAdsDictionary : TAdsDictionary;

oGroupNameList : TStringList;

oUserNameList : TStringList;

oUsersInGroupList : TStringList;

usLength : UNSIGNED16;

pucProperty : array[ 0..ADS\_DD\_MAX\_PROPERTY\_LEN ] of char;

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

 

oUserNameList := TStringList.Create;

oAdsDictionary.GetUserNames( oUserNameList );

 

usLength := ADS\_DD\_MAX\_PROPERTY\_LEN;

oAdsDictionary.GetUserProperty( 'NewUser',

ADS\_DD\_COMMENT

@pucProperty,

usLength );

 

oUsersInGroupList := TStringList.Create;

oAdsDictionary.GetUsersFromGroup( 'NewGroup', oUsersInGroupList );

 

 

oAdsDictionary.DeleteUserGroup( 'NewGroup' );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

end;