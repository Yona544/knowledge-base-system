AddUserToGroup




Advantage Database Server 12  

TAdsDictionary.AddUserToGroup

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.AddUserToGroup  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.AddUserToGroup Advantage TDataSet Descendant ade\_Addusertogroup Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.AddUserToGroup  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Syntax

procedure TAdsDictionary.AddUserToGroup( strGroupName : string;

strUserName : string );

Parameters

|  |  |
| --- | --- |
| strGroupName (I) | Name of the database user group object to make the user a member of. |
| strUserName (I) | Name of the database user object that will become a member of the user group. |

Remarks

AddUserToGroup makes the user a member of the specified user group. Once the user is a member of the user group, the user inherits rights to all objects that the user group has. If the user groups object access rights changes, the users inherited rights will change accordingly. A user can be member of multiple user groups. The users effective right to a database object (table, view or stored procedure) is the summation of all inherited rights the user have from all user groups that the user is a member of.

ALTER permissions on the user group are required to add a user to a data dictionary user group. See Advantage Data Dictionary User Permissions for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

procedure AddUserToGroupExample;

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

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

end;