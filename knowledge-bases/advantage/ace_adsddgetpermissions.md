AdsDDGetPermissions




Advantage Database Server 12  

AdsDDGetPermissions

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDGetPermissions  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDGetPermissions Advantage Client Engine ace\_Adsddgetpermissions Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDGetPermissions  Advantage Client Engine |  |  |  |  |

Get a users or a user groups permissions to a database object.

Syntax

UNSIGNED32 ENTRYPOINT AdsDDGetPermissions( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucGrantee,

UNSIGNED16 usObjectType,

UNSIGNED8 \*pucObjectName,

UNSIGNED8 \*pucParentName,

UNSIGNED16 usGetInherited,

UNSIGNED32 \*pulPermissions );

Parameters

|  |  |
| --- | --- |
| hAdminConn (I) | Handle of a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)). |
| pucGrantee (I) | Name of a user or a user group for whom the permissions have been granted. |
| usObjectType (I) | Type of the database object that is specified by the pucObjectName parameter. Valid values are ADS\_DD\_TABLE\_OBJECT, ADS\_DD\_COLUMN\_OBJECT, ADS\_DD\_VIEW\_OBJECT, ADS\_DD\_PROCEDURE\_OBJECT, ADS\_DD\_LINK\_OBJECT, ADS\_DD\_PUBLICATION\_OBJECT, or  ADS\_DD\_SUBSCRIPTION\_OBJECT. |
| pucObjectName (I) | Name of the database object to retrieve the granted permissions for. It may be the name of a database table, the name of a column in a database table, the name of a view, the name of a stored procedure, name of a publication, name of a subscription, or a link alias. |
| pucParentName (I) | Name of the database object that is the parent/owner of the object specified by pucObjectName. This parameter is only used if usObjectType is ADS\_DD\_COLUMN\_OBJECT. In such case, this parameter specifies the name of the database table that owns the column specified by the pucObjectName parameter. For other object types, this parameter can be NULL and it is ignored. |
| usGetInherited (I) | True or False. If True and the pucGrantee specifies a user in the database, the function will return the users effective permission to the object, i.e. the users permission plus any permission the user inherited from the user group that the user belongs to. If False, only the permissions that are specifically granted to the user or the user group are returned. |
| pulPermissions (IO) | Returns the permission granted to the user or user group for this object. This is a bit field and the permissions are ORed together. Valid permissions that can be returned are ADS\_PERMISSION\_READ, ADS\_PERMISSION\_UPDATE, ADS\_PERMISSION\_INSERT, ADS\_PERMISSION\_DELETE, ADS\_PERMISSION\_EXECUTE, ADS\_PERMISSION\_LINK\_ACCESS , ADS\_PERMISSION\_INHERIT, ADS\_PERMISSION\_ALTER, ADS\_PERMISSION\_DROP, ADS\_PERMISSION\_CREATE, ADS\_PERMISSION\_WITH\_GRANT, ADS\_PERMISSION\_ALL, and ADS\_PERMISSION\_ALL\_WITH\_GRANT.  To get the grantees WITH GRANT permissions, \*pulPermissions must be set to ADS\_GET\_PERMISSIONS\_WITH\_GRANT before calling AdsDDGetPermissions. Likewise, to get the grantees CREATE permissions \*pulPermissions must be set to ADS\_GET\_PERMISSIONS\_CREATE and to get the grantees CREATE WITH GRANT permissions, \*pulPermissions must be set to ADS\_GET\_PERMISSIONS\_CREATE\_WITH\_GRANT. See [AdsDDGrantPermission](ace_adsddgrantpermission.htm) for explanation on the effects of various permissions. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | The name specified by the pucObjectName, pucParentName or pucGrantee could not be found in the database. |
| AE\_PERMISSION\_DENIED | The current user does not have permissions to retrieve the grantees permissions. |

Remarks

AdsDDGetPermissions retrieves the users or the user groups permissions on a specified object in the database.

Note The permissions can only be retrieved by the ADSSYS user or a user with administrative permissions for the specified user or user group.

|  |  |
| --- | --- |
| usFindObjectType | Description |
| ADS\_DD\_PUBLICATION\_OBJECT | Retrieves the name of a publication object. The pucParentName is currently ignored and assumed to be the database. |
| ADS\_DD\_SUBSCRIPTION\_OBJECT | Retrieves the name of a subscription object. The pucParentName is currently ignored and assumed to be the database. |

Example

Get the effective permission of user "rsmith" on the "Employees" tables.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

 

/\* Retrieves the permissions for the user rsmith on the "employees" table. \*/

ulReturnCode = AdsDDGetPermissions( hDD, "rsmith", ADS\_DD\_TABLE\_OBJECT, "Employees", NULL, TRUE,

&ulPermissions );

 

AdsDisconnect( hDD );

See Also

[AdsDDCreateUser](ace_adsddcreateuser.htm)

[AdsDDCreateUserGroup](ace_adsddcreateusergroup.htm)

[AdsDDAddUserToGroup](ace_adsddaddusertogroup.htm)

[AdsDDRemoveUserFromGroup](ace_adsddremoveuserfromgroup.htm)

[AdsDDGrantPermission](ace_adsddgrantpermission.htm)

[system.permissions](master_system_permissions.htm)