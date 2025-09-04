SetUserGroupProperty




Advantage Database Server 12  

TAdsDictionary.SetUserGroupProperty

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.SetUserGroupProperty  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.SetUserGroupProperty Advantage TDataSet Descendant ade\_Setusergroupproperty Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.SetUserGroupProperty  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Sets one property associated with a database user group in the data dictionary.

Syntax

procedure SetUserGroupProperty( strGroupName : string;

usProperty : UNSIGNED16;

pvProperty : pointer;

usPropertyLen : UNSIGNED16 ); virtual;

Parameters

|  |  |
| --- | --- |
| strGroupName (I) | Name of the database user group object to set the associated property. |
| usPropertyID (I) | Index of a database user group property to set. See Remarks for allowed values. |
| pvProperty (I) | Pointer to the buffer where the property is stored. |
| usPropertyLen (I) | The size of the property stored in the buffer. |

Remarks

SetUserGroupProperty sets one property associated with the specified user group. The new property overwrites the existing property in the data dictionary. The properties can only be set when the TAdsDictionary is open by a user with ALTER permissions for the group. The following are the valid values of usPropertyID and the expected value in pvProperty and usPropertyLen.

ALTER permissions on the user group are required to modify the properties of a data dictionary user group. See Advantage Data Dictionary User Permissions for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

|  |  |
| --- | --- |
| usPropertyID | Description |
| ADS\_DD\_COMMENT | Stores a new description for the user group. The pvProperty is expected to be NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. If pvProperty is NULL or empty string, the user description is removed. |
| ADS\_DD\_USER\_DEFINED\_PROP | Changes the user defined user group property. If pvProperty is NULL, the user defined user group property is removed. User defined property is set, read, and interpreted by the application. It is not used by the Advantage engines. |

Example

procedure SetUserGroupExample

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

 

oAdsDictionary.SetUserGroupProperty( 'NewGroup',

ADS\_DD\_COMMENT,

pChar( 'A better comment.' ),

18 );

 

oAdsDictionary.AddTable( 'customers',

'd:\demo\customers.adt',

'',

'New Table',

ttAdsADT,

ANSI );

 

oAdsDictionary.AddUser( '',

'NewUser',

'mypassword',

'FirstUser' );

 

oAdsDictionary.SetObjectAccessRights( 'customers',

'NewUser',

'RW' );

 

oAdsDictionary.AddUserToGroup( 'NewGroup',

'NewUser' );

 

oUserNameList := TStringList.Create;

oAdsDictionary.GetUserNames( oUserNameList );

 

usLength := ADS\_DD\_MAX\_PROPERTY\_LEN;

oAdsDictionary.GetUserProperty( 'NewUser',

ADS\_DD\_TABLES\_RIGHTS,

@pucProperty,

usLength );

 

oUsersInGroupList := TStringList.Create;

oAdsDictionary.GetUsersFromGroup( 'NewGroup', oUsersInGroupList );

 

 

oAdsDictionary.RemoveUserFromGroup( 'NewGroup', 'NewUser' );

 

oAdsDictionary.DeleteUserGroup( 'NewGroup' );

 

oAdsDictionary.RemoveUser( 'NewUser' );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

end;