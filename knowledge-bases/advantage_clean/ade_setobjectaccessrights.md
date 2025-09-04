---
title: Ade Setobjectaccessrights
slug: ade_setobjectaccessrights
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_setobjectaccessrights.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: ebd494701cc335a6dd6fb7b0d315515685b8b330
---

# Ade Setobjectaccessrights

SetObjectAccessRights

TAdsDictionary.SetObjectAccessRights

Advantage TDataSet Descendant

| TAdsDictionary.SetObjectAccessRights  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Sets a database user or a user groups access rights to a table, a view, or a stored procedure.

Syntax

procedure SetObjectAccessRights( strObjectName : string;

strAccessorName : string;

strAllowedRights : string ); virtual;

Parameters

| strObjectName (I) | Name of the database object to grant or remove access. It must specify a database table, view or stored procedure. |
| strAccessorName (I) | Name of the database user or user group to which the access is being granted or removed. |
| strAllowedAccess (I) | NULL terminated string representing the allowed accesses for the user or the user group to the object. The allowed characters in the string are: R: read rights applies to database table or view object only.W: write rights applies to the database table or view object only.X: execution rights applies to stored procedures only.I: inherited rights valid only if the pucAccessorName specifies a database user. |

Remarks

SetObjectAccessRights sets a database user or user groups access rights to the specified database object such as a table, a view or a stored procedure. The new rights overwrite the previous rights specified for the user or the user group to the object. If the database is set up to verify the user access rights, whether a user can access an object in the database depending on the effective rights he has to the object. The following are the rights and how they affect a users access to an object.

| Read Rights | The read rights apply to table or view objects. With the read rights, the user can open a table or view for read purpose. The user can also issue SQL "SELECT " statements against the table or view, but the user is not allowed to issue SQL DML statements, such as "UPDATE " or "DELETE ", against the table or view. If the user has the read rights but not the write rights to a table or view, the user can open the table or view directly with the read only option. |
| Write Rights | The write rights apply to table or view objects. With the write rights, the user can make modification to the content of the table or view. Note that if the user has only the write rights but not the read rights to the table, the effects are (1) the user can issue SQL DML statements, such as "UPDATE" or "DELETE", against the table or view but the user is not allowed to issue SQL "SELECT " statement against the table or view, and (2) the user cannot open the table or view directly because table or view opened directly are always readable. |
| Execution Rights | The execution rights apply to the stored procedure objects. With the execution rights, the user can execute a stored procedure. Without the rights, the user is not allowed to execute the stored procedure. |
| Inherited Rights | The inherited rights can be granted to the database users only. With the inherited rights, a users effective rights to a database object is the sum of all rights to the object that the user and the user groups, for which the user is a member of, have. Note that unless specifically excluded, the user has inherited rights to any database objects by default. For example, if "Group1" has read rights to "table1" and read/write rights to "table2", and "Group2" has write rights to "table1", after making "user1" a member of both "Group1" and "Group2", the effective rights of the user are read/write to both "table1" and "table2". To make "user1" have only read rights to "table1", the administrator can grant the user the read rights without the inherited rights to the table. |

The pucAllowedAccess parameter is used to specify a combination of rights granted to the user or the user group. The following are some sample rights and their implication:

| "RWI" | This combination can be granted to a user for a table or view object. The user is granted the read, write and inherited rights to the object. The "I" is superfluous at this point because the user already has the full read/write access to the object. There is nothing to inherit. However, it is still meaningful because there may be other rights in the future. |
| "RI" | This combination can be granted to a user for a table or view object. The user is granted the read and inherited rights to the object. If any group that the user is a member of has write rights to the table or view, the effective rights of the user to the object is read and write |
| "R" | This combination can be granted to a user or user group for a table or view object. The user is granted the read rights to the object. Since the inherited rights is not granted for the user, the effective rights of the user to the object is read only, even if the user is a member of the groups that have write rights to the object. |
| "I" | This combination can be granted to a user for a table, view or stored procedure object. The user is granted the inherited rights to the object. If the user is not a member of any group, the user does not have any right to the object. Otherwise, the effective rights of the user to the object are the sum of the rights of all user groups that the user is a member of. |
| "" | This combination can be granted to a user or user group for a table, view or stored procedure object. The user or user group is granted no rights to the object. If this is granted to a user, the user can no longer open the table or view or execute the stored procedure. If this is granted to a user group, the users who are member of the group can no longer inherit any rights for this object from the group. However, the users may still inherit rights from other groups that they are members of. |
| "X" | This combination can be granted to a user or user group for a stored procedure object. The user or user group is granted the execution rights to the stored procedure. If this is granted to a user, the user can execute the stored procedure. If this is granted to a user group, all users who are member of the group can now execute the store procedure if they have inherited rights to the stored procedure. |

Note When the database is created, its default is to not check user access rights. Unless the database property ADS\_DD\_VERIFY\_ACCESS\_RIGHTS is set to TRUE, all users will have full rights to all tables, views, or stored procedures in the database. See SetDatabaseProperty for more information.

Example

procedure SetObjectAccessRightsExample;

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

 

oAdsDictionary.AddTable( 'customers',

'd:\demo\customers.adt',

'',

'New Table',

ttAdsADT,

ANSI );

 

oAdsDictionary.AddUser( '',

'NewUser',

'mypassword',

'FirstUser' );

 

oAdsDictionary.SetObjectAccessRights( 'customers',

'NewUser',

'RW' );

 

oAdsDictionary.AddUserToGroup( 'NewGroup',

'NewUser' );

 

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
