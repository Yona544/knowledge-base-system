---
title: Ade Removeuser
slug: ade_removeuser
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_removeuser.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 803b2719d9e50b4e2f838f3a65750176b991d49a
---

# Ade Removeuser

RemoveUser

TAdsDictionary.RemoveUser

Advantage TDataSet Descendant

| TAdsDictionary.RemoveUser  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Deletes a user object from the database.

Syntax

procedure RemoveUser( strUserName : string );

Parameters

| pucUserName (I) | Name of the user object to delete. |

Remarks

RemoveUser removes an existing user from the database. Once the user is removed from the database, any future connection attempts to the database using the specified user name will fail with authentication error. Any existing connections by the user will still be valid. However, those connection may not be able to open table or execute SQL statement if the database is set up to verify the users access rights. If the database is not set up to verify the users access rights, those connection can still open table and execute SQL statement. See SetDatabaseProperty for information on setting up user access rights verification.

DROP permissions on the user are required to remove a user from a data dictionary. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

procedure RemoveUserExample;

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

 

 

usLength := ADS\_DD\_MAX\_PROPERTY\_LEN;

oAdsDictionary.GetUserGroupProperty( 'NewGroup',

ADS\_DD\_TABLES\_RIGHTS,

@pucProperty,

usLength );

 

 

oGroupNameList := TStringList.Create;

oAdsDictionary.GetGroupNames( oGroupNameList );

 

oUserNameList := TStringList.Create;

oAdsDictionary.GetUserNames( oUserNameList );

 

usLength := ADS\_DD\_MAX\_PROPERTY\_LEN;

oAdsDictionary.GetUserProperty( 'NewUser',

ADS\_DD\_TABLES\_RIGHTS,

@pucProperty,

usLength );

 

oUsersInGroupList := TStringList.Create;

oAdsDictionary.GetUsersFromGroup( 'NewGroup', oUsersInGroupList );

 

 

oAdsDictionary.DeleteUserGroup( 'NewGroup' );

 

oAdsDictionary.RemoveUser( 'NewUser' );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

end;
