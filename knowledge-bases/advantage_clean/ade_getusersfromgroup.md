---
title: Ade Getusersfromgroup
slug: ade_getusersfromgroup
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getusersfromgroup.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 2e7c5580d3e44d7d481e45bc02fab2c7bbf93d3f
---

# Ade Getusersfromgroup

GetUsersFromGroup

TAdsDictionary.GetUsersFromGroup

Advantage TDataSet Descendant

| TAdsDictionary.GetUsersFromGroup  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Syntax

TAdsDictionary.GetUsersFromGroup( strGroupName : string;

oUserNameList : TStringList );

Parameters

| strGroupName ( I ) | The group that contains the users. |
| oUserNameList (O) | The list of users that belong to the given group. |

Remarks

This method will get all of the users for a given group.

Example

procedure GetUsersFromGroupExample;

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

 

oUsersInGroupList := TStringList.Create;

oAdsDictionary.GetUsersFromGroup( 'NewGroup', oUsersInGroupList );

 

 

oAdsDictionary.DeleteUserGroup( 'NewGroup' );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

end;

See Also

[GetIndexNamesPerIndexFile](ade_getindexnamesperindexfile.md)
