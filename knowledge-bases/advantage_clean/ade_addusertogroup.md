---
title: Ade Addusertogroup
slug: ade_addusertogroup
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_addusertogroup.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: f5b791302ee672d3b06129c0e68e72b7ecaeade7
---

# Ade Addusertogroup

AddUserToGroup

TAdsDictionary.AddUserToGroup

Advantage TDataSet Descendant

| TAdsDictionary.AddUserToGroup  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Syntax

procedure TAdsDictionary.AddUserToGroup( strGroupName : string;

strUserName : string );

Parameters

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
