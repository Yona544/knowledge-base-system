DeleteUserGroup




Advantage Database Server 12  

TAdsDictionary.DeleteUserGroup

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.DeleteUserGroup  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.DeleteUserGroup Advantage TDataSet Descendant ade\_Deleteusergroup Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.DeleteUserGroup  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Syntax

procedure TAdsDictionary.DeleteUserGroup( strGroupName : string );

Parameters

|  |  |
| --- | --- |
| pucGroupName (I) | Name of the user group object to delete. |

Remarks

DeleteUserGroup removes an existing user group from the database. All references to the user group by the database users are removed from the data dictionary.

DROP permissions on the user group are required to delete a data dictionary user group. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

procedure DeleteUserGroupExample;

var

oAdsDictionary : TAdsDictionary;

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

 

 

oAdsDictionary.DeleteUserGroup( 'NewGroup' );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

end;