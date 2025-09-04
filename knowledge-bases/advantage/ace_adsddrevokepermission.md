AdsDDRevokePermission




Advantage Database Server 12  

AdsDDRevokePermission

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDRevokePermission  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDRevokePermission Advantage Client Engine ace\_Adsddrevokepermission Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDRevokePermission  Advantage Client Engine |  |  |  |  |

Remove a users or a user groups permissions to a database object.

Syntax

UNSIGNED32 AdsDDRevokePermission( ADSHANDLE hAdminConn,

UNSIGNED16 usObjectType,

UNSIGNED8 \*pucObjectName,

UNSIGNED8 \*pucParentName,

UNSIGNED8 \*pucGrantee,

UNSIGNED32 ulPermissions );

Parameters

|  |  |
| --- | --- |
| hAdminConn (I) | Handle of a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)). |
| usObjectType (I) | Type of the database object that is specified by the pucObjectName parameter. Valid values are ADS\_DD\_TABLE\_OBJECT, ADS\_DD\_COLUMN\_OBJECT, ADS\_DD\_VIEW\_OBJECT, ADS\_DD\_PROCEDURE\_OBJECT, ADS\_DD\_LINK\_OBJECT, ADS\_DD\_PUBLICATION\_OBJECT, and ADS\_DD\_SUBSCRIPTION\_OBJECT. |
| pucObjectName (I) | Name of the database object to revoke the specified permissions from. It may be the name of a database table, the name of a column in a database table, the name of a view, the name of a stored procedure, publication, subscription, or a link alias. |
| pucParentName (I) | Name of the database object that is the parent/owner of the object specified by pucObjectName. This parameter is only used if usObjectType is ADS\_DD\_COLUMN\_OBJECT. In such case, this parameter specifies the name of the database table that owns the column specified by the pucObjectName parameter. For other object types, this parameter can be NULL and it is ignored. |
| pucGrantee (I) | Name of a user or a user group that is going to be granted the permissions. |
| ulPermissions (I) | This is a bit field for defining the access permissions to be revoked from the user or user group specified by the pucGrantee parameter. The permissions can be ORed together. Valid permissions are ADS\_PERMISSION\_READ, ADS\_PERMISSION\_UPDATE, ADS\_PERMISSION\_INSERT, ADS\_PERMISSION\_DELETE, ADS\_PERMISSION\_EXECUTE, ADS\_PERMISSION\_LINK\_ACCESS, ADS\_PERMISSION\_INHERIT, ADS\_PERMISSION\_ALTER, ADS\_PERMISSION\_DROP, ADS\_PERMISSION\_CREATE, ADS\_PERMISSION\_WITH\_GRANT, ADS\_PERMISSION\_ALL, and ADS\_PERMISSION\_ALL\_WITH\_GRANT. Note: The ADS\_PERMISSION\_ALL permission equates to all the permissions for which the current user has ADS\_PERMISSION\_WITH\_GRANT permissions. |

Special Return Codes

|  |  |
| --- | --- |
| usPropertyID | Description |
| AE\_INVALID\_OBJECT\_NAME | The name specified by the pucObjectName, pucParentName or pucGrantee could not be found in the database. |
| AE\_INVALID\_OBJECT\_PERMISSION | The permissions specified by the ulPermissions parameter contains a permission that is not valid for the specified object type or grantee type. |

Remarks

AdsDDRevokePermission removes the specified access permissions on a database object from a user or a user group. The ulPermissions parameter is used to specify a combination of permissions to revoke from the user or the user group. See [AdsDDGrantPermission](ace_adsddgrantpermission.htm) for more information on the types of permission that can be granted or revoked from user and user group.

Note If the user belongs to a user group, revoking a users permission to an object may not remove the users access permission to the object. The user may still inherit permission to the object from the user group that the user is a member of. To prevent the user from inheriting permissions to the object from a user group, revoke the inherit permission (ADS\_PERMISSION\_INHERIT) for the object from the user.

 

Note If the database is not set up to verify the user access permissions, the users access permissions will not be checked by the Advantage servers. See [AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.htm) and ADS\_DD\_VERIFY\_ACCESS\_RIGHTS property for more information. The property defaults to False on newly created data dictionary effectively giving all users full access to all objects in the database.

 

Note The allowed access to database tables is also affected by the table permission level property. See [AdsDDSetTableProperty](ace_adsddsettableproperty.htm) and the ADS\_DD\_TABLE\_PERMISSION\_LEVEL property.

 

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

|  |  |
| --- | --- |
| usFindObjectType | Description |
| ADS\_DD\_PUBLICATION\_OBJECT | Retrieves the name of a publication object. The pucParentName is currently ignored and assumed to be the database. |
| ADS\_DD\_SUBSCRIPTION\_OBJECT | Retrieves the name of a subscription object. The pucParentName is currently ignored and assumed to be the database. |

Example

See [AdsDDGrantPermission](ace_adsddgrantpermission.htm).

See Also

[AdsDDCreateUser](ace_adsddcreateuser.htm)

[AdsDDCreateUserGroup](ace_adsddcreateusergroup.htm)

[AdsDDAddUserToGroup](ace_adsddaddusertogroup.htm)

[AdsDDRemoveUserFromGroup](ace_adsddremoveuserfromgroup.htm)

[AdsDDGrantPermission](ace_adsddgrantpermission.htm)

[AdsDDGetPermissions](ace_adsddgetpermissions.htm)