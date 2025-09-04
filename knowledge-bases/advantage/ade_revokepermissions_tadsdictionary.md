RevokePermissions




Advantage Database Server 12  

TAdsDictionary.RevokePermissions

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary.RevokePermissions  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary.RevokePermissions Advantage TDataSet Descendant ade\_Revokepermissions\_tadsdictionary Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDictionary.RevokePermissions  Advantage TDataSet Descendant |  |  |  |  |

[TAdsDictionary](ade_tadsdictionary.htm)

Remove a users or a user groups permissions to a database object.

Syntax

procedure TAdsDictionary.RevokePermissions( usObjectType : UNSIGNED16;

strObjectName : string;

strParentName : string;

strGrantee : string;

Permissions : TAdsPermissionTypes );

Parameters

|  |  |
| --- | --- |
| usObjectType (I) | Type of the database object that is specified by the strObjectName parameter. Valid values are ADS\_DD\_TABLE\_OBJECT, ADS\_DD\_COLUMN\_OBJECT, ADS\_DD\_VIEW\_OBJECT, ADS\_DD\_PROCEDURE\_OBJECT or ADS\_DD\_LINK\_OBJECT. |
| strObjectName (I) | Name of the database object to revoke the specified permissions on. It may be the name of a database table, the name of a column in a database table, the name of a view, the name of a stored procedure or a link alias. |
| strParentName (I) | Name of the database object that is the parent or owner of the object specified by strObjectName. If usObjectType is ADS\_DD\_COLUMN\_OBJECT, this parameter specifies the name of the database table that owns the column specified by the strObjectName parameter. For other object types, the parameter can be empty and it is ignored. |
| strGrantee (I) | Name of a user or a user group to revoke the permissions for. |
| Permissions (I) | This is a set of permissions specifying the access permissions to be revoked from the user or the user group specified by the strGrantee parameter. Valid permissions are ptRead, ptUpdate, ptExecute, ptInherit, ptInsert, ptDelete, ptLinkAccess, ptDrop, ptAlter, ptCreate, ptWithGrant, ptAll, and ptAllWithGrant. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | The name specified by the pucObjectName, pucParentName or pucGrantee could not be found in the database. |
| AE\_INVALID\_OBJECT\_PERMISSION | The permissions specified by the ulPermissions parameter contains a permission that is not valid for the specified object type or grantee type. |

Remarks

RevokePermission removes the specified access permissions on a database object from a user or a user group. The ulPermissions parameter is used to specify a combination of permissions to revoke from the user or the user group. See [GrantPermissions](ade_grantpermissions_tadsdictionary.htm) for more information on the types of permissions that can be granted or revoked from users and user groups.

Note If the user belongs to a user group, revoking a users permission to an object may not remove the users access permission to the object. The user may still inherit permission to the object from the user group that the user is a member of. To prevent the user from inheriting permissions to the object from a user group, revoke the inherit permission (ptInherit) for the object from the user.

 

Note The users access permissions are not checked by the Advantage servers, if the database is not set up to verify the user access permissions. See [SetDatabaseProperty](ade_setdatabaseproperty.htm) and ADS\_DD\_VERIFY\_ACCESS\_RIGHTS property for more information. The property defaults to False on newly created data dictionary effectively giving all users full access to all objects in the database.

 

Note The allowed access to database tables is also affected by the table permission level property. See [SetTableProperty](ade_settableproperty.htm) and the ADS\_DD\_TABLE\_PERMISSION\_LEVEL property.

 

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

See [GrantPermissions](ade_grantpermissions_tadsdictionary.htm) example.

See Also

[AddUser](ade_adduser.htm)

[CreateUserGroup](ade_createusergroup.htm)

[AddUserToGroup](ade_addusertogroup.htm)

[RemoveUserFromGroup](ade_removeuserfromgroup.htm)

[GrantPermissions](ade_grantpermissions_tadsdictionary.htm)

[GetPermissions](ade_getpermissions_tadsdictionary.htm)