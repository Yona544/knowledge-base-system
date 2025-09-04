---
title: Ade Deleteusergroup
slug: ade_deleteusergroup
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_deleteusergroup.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: efc2309e2881169375a5c205f175ec0ec7b222f7
---

# Ade Deleteusergroup

DeleteUserGroup

TAdsDictionary.DeleteUserGroup

Advantage TDataSet Descendant

| TAdsDictionary.DeleteUserGroup  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Syntax

procedure TAdsDictionary.DeleteUserGroup( strGroupName : string );

Parameters

| pucGroupName (I) | Name of the user group object to delete. |

Remarks

DeleteUserGroup removes an existing user group from the database. All references to the user group by the database users are removed from the data dictionary.

DROP permissions on the user group are required to delete a data dictionary user group. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information

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
