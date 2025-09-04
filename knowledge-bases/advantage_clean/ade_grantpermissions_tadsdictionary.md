---
title: Ade Grantpermissions Tadsdictionary
slug: ade_grantpermissions_tadsdictionary
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_grantpermissions_tadsdictionary.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 8617ac9c8380efda1d58b9175b1a7ed29553ef8a
---

# Ade Grantpermissions Tadsdictionary

GrantPermissions

TAdsDictionary.GrantPermissions

Advantage TDataSet Descendant

| TAdsDictionary.GrantPermissions  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.md)

Grants to a user or a user group one or more permissions to a database object.

Syntax

procedure TAdsDictionary.GrantPermissions( usObjectType : UNSIGNED16;

strObjectName : string;

strParentName : string;

strGrantee : string;

Permissions : TAdsPermissionTypes );

 

TAdsPermissionType = ( ptRead, ptUpdate, ptExecute, ptInherit, ptInsert, ptDelete, ptLinkAccess, ptDrop, tpAlter, ptCreate, ptWithGrant, ptAll, ptAllWithGrant );

TAdsPermissionTypes = set of TAdsPermissionType;

Parameters

| usObjectType (I) | Type of the database object that is specified by the strObjectName parameter. Valid values are ADS\_DD\_TABLE\_OBJECT, ADS\_DD\_COLUMN\_OBJECT, ADS\_DD\_VIEW\_OBJECT, ADS\_DD\_PROCEDURE\_OBJECT or ADS\_DD\_LINK\_OBJECT. |
| strObjectName (I) | Name of the database object to grant the specified permissions on. It may be the name of a database table, the name of a column in a database table, the name of a view, the name of a stored procedure or a link alias. This parameter must be NULL or an empty string when granting CREATE permissions. This parameter must be NULL or an empty string when granting CREATE permissions. |
| strParentName (I) | Name of the database object that is the parent or owner of the object specified by strObjectName. If usObjectType is ADS\_DD\_COLUMN\_OBJECT, this parameter specifies the name of the database table that owns the column specified by the strObjectName parameter. For other object types, the parameter can be empty and it is ignored. |
| strGrantee (I) | Name of a user or a user group that is going to be granted the permissions. |
| Permissions (I) | This is a set of permissions specifying the access permissions to be granted to the user or the user group specified by the strGrantee parameter. Valid permissions are ptRead, ptUpdate, ptExecute, ptInherit, ptInsert, ptDelete, ptLinkAccess, ptDrop, ptAlter, ptCreate, ptWithGrant, ptAll, and ptAllWithGrant. See Remarks for explanation on the effects of permissions. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | The name specified by the strObjectName, strParentName or strGrantee could not be found in the database. |
| AE\_INVALID\_OBJECT\_PERMISSION | The permissions specified by the Permissions parameter contains a permission that is not valid for the specified object type or grantee type. |

Remarks

GrantPermission grants the specified access permissions to a user or a user group on a database object. The newly granted permission will be in addition to any existing permissions the user or the user group has on the specified database object. Permissions granted to views are not effected by the users permissions on the base tables used to construct the view. This behavior allows the use of views to control access to specific columns in the base tables. The following are valid permissions and a description of their affect on a users access to an object.

| ptRead | This permission can be granted to a user or a user group on a table, a view or a column object. A user must have read permission to a table or view to open the table directly or issue an SQL SELECT statement against the table. When the read permission is granted on a table, the read permission is implicitly granted to all columns in the table. When the read permission is granted to a column in a table, a partial read permission is granted for the table. If the user does not have full read permission to a table, the allowed access to the table is controlled by the tables permission level property. See [SetTableProperty](ade_settableproperty.md) and ADS\_DD\_TABLE\_PERMISSION\_LEVEL for more information. |
| ptUpdate | This permission can be granted to a user or a user group on a table, a view or a column object. To modify existing data a user must be granted this permission. When this permission is granted on a table object, the permission is implicitly granted to all columns in the table. This permission affects SQL UPDATE statements and tables opened directly. |
| ptInsert | This permission can be granted to a user or a user group on a table, a view or a column object. A user must have insert permission to a table to insert new rows or provide data for a new row. Insert permission on a table or view allows the user to insert new rows into the table. Insert permission on column allows the user to provide data for a newly inserted row. Columns without the insert permission can only post the default value for a column in a newly inserted row. When granted to a table, this permission is implicitly granted to all columns in the table. This permission affects SQL INSERT statements and tables opened directly. |
| ptDelete | This permission can be granted to a user or a user group on a table or view object. This permission specifies whether the user can delete rows from a table or view. This permission affects SQL DELETE statements and tables opened directly. |
| ptExecute | This permission can be granted to a user or a user group on a stored procedure object. This permission affects SQL EXECUTE PROCEDURE statements. |
| ptLinkAccess | This permission can be granted to a user or a user group on a link object. If this permission is not granted, the user cannot access tables on the link. A link is a reference to another database managed by the Advantage Database Server or Advantage Local Server. See [CreateDDLink](ade_createddlink_tadsdictionary.md) for addition information on links. |
| ptInherit | This permission can be granted to a user on a table, a view, a stored procedure or a link object. With this permission, the users effective access permission to a database object is the sum of all permissions granted to the user and all user groups to which the user belongs. For columns in a table, the user inherits permissions from its user groups only when the user is granted inherit permission on the table. By default all users are granted the inherit permission to database objects. For example, if "Group1" has read permission to "table1" and read and update permission to "table2"; and "Group2" has update permission to "table1", after making "user1" a member of both "Group1" and "Group2", the effective permissions of the user are read and update for both "table1" and "table2". To restrict "user1" to read permission to "table1", the administrator can grant the user the read permission to "table1" and revoke the users inherit permission to "table1". See [RevokePermissions](ade_revokepermissions_tadsdictionary.md) for additional information. |
| ptAlter | This permission can be granted to a user or a user group on a table, view, user, user group, relation, procedure, link, or the database itself. With this permission, the grantee can modify the privileged properties of the specified object. To grant ALTER permissions for the database object, simply set pucObjectName to "Database" and pucParent to NULL or an empy string. |
| ptDrop | This permission can be granted to a user or a user group on a table, view, user, user group, relation, procedure, or link. With this permission the grantee can remove (drop) the specified object from the database. |
| ptCreate | This permission can be granted to a user or a user group on a table, user, user group, view, procedure, or link. With this permission the grantee can create new objects of the specified type as well as add existing objects to the database such as tables and indexes. To grant this permission simply set usObjectType to the desired database object type and set pucObjectName and pucParentName to NULL or empty strings. ptCreate cannot be ORed together with any other permission except ptWithGrant. |
| ptWithGrant | This permission allows the grantee to grant the specified permission to another user or user group. This permission cannot be used alone, it must be ORed together with the permission or permissions to be granted. If the grantee does not already have the specified permissions ORed with WITH GRANT, they will be granted the specified permissions. |
| ptAll | This permission grants all available permissions to the user or user group that are aplicable for the specified object. |
| ptAllWithGrant | This permission is the same as ADS\_PERMISSION\_ALL except that it also gives the grantee WITH GRANT permissions for the specified object. |

The Permissions parameter is used to specify a combination of permissions to grant to the user or the user group. Assuming that the user currently has no permission (the inherit permission has been revoked) to an object, the following are some sample permissions combination and their effect on the object:

[ptRead, ptUpdate, ptInsert, ptDelete, ptInherit]

After granting this combination of permissions on a database table or view to a user, the user has full access to the table. The inherit permission is superfluous at this point because there is no addition permissions for the user to inherit. However, it is still meaningful because there may be other permissions in the future or the user may have certain permissions revoked on the table. This combination is not valid for column objects because inherit and delete permissions. This combination cannot be granted to a user group because of the inherit permission.

[ptRead, ptInherit]

This combination can be granted to a user on a table or a view. Besides having read permission to the table or view, the user will inherit other permissions from the user groups that the user belongs to. Other possible permissions that the user could inherit are insert, update, and delete.

[ptRead]

This permission can be granted to a user or user group on a table, a view, or a column object. If granted this permission, the user has read-only access to the object. If the object is a table, the effective rights for the user to the table are read only access to all columns because the inherit permission was not granted. The users permission to the table is independent of the permissions granted to the user groups that the user may be a member of. If this permission is granted to a user group, all users in the user group will have effective read permission to the table or the view, provided that the users have been granted the inherit permission.

[ptInherit]

This permission can be granted to a user on a table, a view or a stored procedure object. If granted this permission, the user can inherit permissions from the user groups they belong to. If the user is not a member of any user groups, the user will have no access to the object. If the user belongs to any user groups, the effective permissions for the user on the object is the sum of the permissions of all user groups that the user belongs to.

[ptExecute]

This combination can be granted to a user or user group on a stored procedure object. The user must be granted this permission to execute a stored procedure. If this permission is granted to a user group, all members of the user group who have been granted the inherit permission for the stored procedure can execute the stored procedure.

Note The users access permissions are not checked by the Advantage servers, if the database is not set up to verify the user access permissions. See [SetDatabaseProperty](ade_setdatabaseproperty.md) and ADS\_DD\_VERIFY\_ACCESS\_RIGHTS property for more information. The property defaults to False on newly created data dictionary, effectively giving all users full access to all objects in the database.

 

Note Access to database tables is also affected by the table permission level property. See [SetTableProperty](ade_settableproperty.md) and the ADS\_DD\_TABLE\_PERMISSION\_LEVEL property.

 

Note The current user must be ADSSYS or have WITH GRANT permissions to grant permissions. See Advantage Data Dictionary User Permissions for more information.

 

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

After connecting to the database, set up the access rights for the "Managers" user group to various tables, views and stored procedures. The user "rsmith" is added to the "Managers" user group. Finally, the access to the table "Salaries" is excluded from user "rsmith" although he still have access to other managerial tables and views.

procedure GrantAndRevokePermissions;

var

oAdsDictionary : TAdsDictionary;

begin

{\* Create the dictionary component and connect to a dictionary. \*}

oAdsDictionary := TAdsDictionary.Create( self );

 

oAdsDictionary.AdsServerTypes := [stADS\_REMOTE];

 

oAdsDictionary.ConnectPath :='n:\MyData\myData.ADD';

oAdsDictionary.UserName := 'ADSSYS';

oAdsDictionary.LoginPrompt := False;

 

oAdsDictionary.IsConnected := True;

 

{\* Grant managers full access to the 'employees' table. \*}

oAdsDictionary.GrantPermissions( ADS\_DD\_TABLE\_OBJECT,

'Employees',

'',

'Managers',

[ptRead, ptUpdate, ptInsert, ptDelete] );

 

{\* Grant managers full access to the 'salaries' table. \*}

oAdsDictionary.GrantPermissions( ADS\_DD\_TABLE\_OBJECT,

'Salaries',

'',

'Managers',

[ptRead, ptUpdate, ptInsert, ptDelete] );

 

{\* Grant managers the execute priviledge to the "New Hire" stored procedure. \*}

oAdsDictionary.GrantPermissions( ADS\_DD\_PROCEDURE\_OBJECT,

'New Hire',

'',

'Managers',

[ptExecute] );

 

{\* Add rsmith to the managers group. \*}

oAdsDictionary.AddUserToGroup( 'Managers', 'rsmith' );

 

 

{\*

\* rsmith inherits all rights from the managers group. However, rsmith is only an

\* administrative assistant, so he is not allowed access the salary information.

\* Therefore, revoke his inherited rights to the 'salaries' table.

\*}

oAdsDictionary.RevokePermissions( ADS\_DD\_TABLE\_OBJECT,

'Salaries',

'',

'rsmith',

[ptInherit] );

 

oAdsDictionary.IsConnected := FALSE;

 

oAdsDictionary.Free;

 

end;

See Also

[AddUser](ade_adduser.md)

[CreateUserGroup](ade_createusergroup.md)

[AddUserToGroup](ade_addusertogroup.md)

[RemoveUserFromGroup](ade_removeuserfromgroup.md)

[RevokePermissions](ade_revokepermissions_tadsdictionary.md)

[GetPermissions](ade_getpermissions_tadsdictionary.md)
