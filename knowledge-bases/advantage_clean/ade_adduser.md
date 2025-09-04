---
title: Ade Adduser
slug: ade_adduser
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adduser.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 2d8241c28e950c92153321ff8091db97c5e30e1a
---

# Ade Adduser

AddUser

TAdsDictionary.AddUser

Advantage TDataSet Descendant

| TAdsDictionary.AddUser  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Syntax

procedure TAdsDictionary.AddUser( strGroupName : string;

strUserName : string;

strPassword : string;

strDescription : string );

Parameters

| strGroupName (I) | Name of the user group that the user belongs to initially. This parameter can be NULL to make the user not belong to any user group. |
| strUserName (I) | Name of the user to create. |
| strPassword (I) | Initial password for the user. This parameter can be NULL or pointer to an empty string to specify no password for this user. |
| strDescription (I) | Optional description of the user. This parameter can be NULL. |

Remarks

AddUser creates a user object in the database. If the pucGroupName parameter specifies a user group in the data dictionary, the newly created user becomes a member of the group. The user can become member of multiple groups by calling the AddUserToGroup API. The initial password can be changed by calling the SetUserProperty API. Creating user in the database allows the administrator to control who have access to what table in the database. When a database is created, it is by default to allow anonymous connection to the database and no access rights checking. Those options can be turned on by calling the SetDatabaseProperty API.

CREATE USER permissions are required to add a user to a data dictionary. See Advantage Data Dictionary User Permissions for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

procedure AddUserExample;

var

oAdsDictionary : TAdsDictionary;

begin

{\* call the constructor \*}

oAdsDictionary := TAdsDictionary.Create( self );

 

oAdsDictionary.AdsServerTypes := [stADS\_REMOTE];

 

{\* call the method to create the data dictionary files \*}

oAdsDictionary.CreateDictionary( 'd:\demo\demo.add', FALSE, 'This is a demo database.' );

 

{\* The CreateDictionary call leaves an ADSSYS connection open.\*}

 

oAdsDictionary.AddUser( '',

'NewUser',

'mypassword',

'FirstUser' );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

end;

See Also

[RemoveUser](ade_removeuser.md)

[GetUserProperty](ade_getuserproperty.md)
