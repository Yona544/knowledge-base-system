---
title: Ade Getusernames
slug: ade_getusernames
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getusernames.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 87d254104df5187932b9b51049567177ed1dcffc
---

# Ade Getusernames

GetUserNames

TAdsDictionary.GetUserNames

Advantage TDataSet Descendant

| TAdsDictionary.GetUserNames  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Syntax

TAdsDictionary.GetUserNames( poUserNames : TStringList );

Parameters

| poUserNames (O) | The list of user names that belong to the database. |

Remarks

This method will retrieve all of the user names in a database and return them in a TStringList.

Example

procedure GetUserNamesExample;

var

oAdsDictionary : TAdsDictionary;

oGroupNameList : TStringList;

oUserNameList : TStringList;

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

 

 

oAdsDictionary.DeleteUserGroup( 'NewGroup' );

 

oAdsDictionary.IsConnected := FALSE;

 

oGroupNameList.Free;

oUserNameList.Free;

oAdsDictionary.Free;

 

end;
