---
title: Ade Getgroupnames
slug: ade_getgroupnames
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getgroupnames.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: f16def5e9f37f2af3cc5a297cc6b564ed0444eb1
---

# Ade Getgroupnames

GetGroupNames

TAdsDictionary.GetGroupNames

Advantage TDataSet Descendant

| TAdsDictionary.GetGroupNames  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Syntax

TAdsDictionary.GetGroupNames( poGroupNames : TStringList );

Parameters

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
