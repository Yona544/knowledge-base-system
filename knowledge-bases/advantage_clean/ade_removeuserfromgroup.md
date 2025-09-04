---
title: Ade Removeuserfromgroup
slug: ade_removeuserfromgroup
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_removeuserfromgroup.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: ce4c4ed8a0d7af565210c8c5d709d9fd6fd2ebba
---

# Ade Removeuserfromgroup

RemoveUserFromGroup

TAdsDictionary.RemoveUserFromGroup

Advantage TDataSet Descendant

| TAdsDictionary.RemoveUserFromGroup  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Makes a database user not a member of the specified user group.

Syntax

procedure RemoveUserFromGroup( strGroupName : string;

strUserName : string ); virtual;

Parameters

| pucGroupName (I) | Name of the database user group object to remove the users membership. |
| pucUserName (I) | Name of the database user object to remove from the user groups membership. |

Remarks

RemoveUserFromGroup removes the user from the membership of the specified user group. Once the user is removed from the membership of the user group, the user loses all object access rights that he inherited from the user group.

DROP permissions on the user group are required to remove a user group from a data dictionary. See Advantage Data Dictionary User Permissions for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

procedure RemoveUserFromGroupExample;

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

 

 

oAdsDictionary.RemoveUserFromGroup( 'NewGroup', 'NewUser' );

 

oAdsDictionary.DeleteUserGroup( 'NewGroup' );

 

oAdsDictionary.RemoveUser( 'NewUser' );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

end;
