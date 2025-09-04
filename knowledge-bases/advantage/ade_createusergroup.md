CreateUserGroup




Advantage Database Server 12  

TAdsDictionary.CreateUserGroup

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.CreateUserGroup  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.CreateUserGroup Advantage TDataSet Descendant ade\_Createusergroup Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.CreateUserGroup  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Syntax

procedure CreateUserGroup( strGroupName : string;

strDescription : string );

Parameters

|  |  |
| --- | --- |
| strGroupName (I) | Name of the user group to create. |
| strDescription (I) | Optional description of the user group. This parameter can be NULL. |

Remarks

CreateUserGroup creates a user group object in the database. A user group can be used to logically group users with similar object access rights together. By default, a user inherits rights from the groups that he is a member of. By granting rights to user groups instead of users, it makes it simpler to add and remove access rights to multiple users. A user can become a member of a user group by calling the AddUserToGroup API.

CREATE USER GROUP permissions are required to create a data dictionary user group. See Advantage Data Dictionary User Permissions for more information.

Note When a database is created, it is by default to not perform access rights checking. In order to enforce the access rights of the users, the ADS\_DD\_VERIFY\_ACCESS\_RIGHTS property of the database must be set to TRUE by calling the [SetDatabaseProperty](ade_setdatabaseproperty.htm).

 

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

procedure CreateUserGroupExample;

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