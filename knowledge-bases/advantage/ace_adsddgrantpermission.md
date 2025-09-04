AdsDDGrantPermission




Advantage Database Server 12  

AdsDDGrantPermission

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDGrantPermission  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDGrantPermission Advantage Client Engine ace\_Adsddgrantpermission Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDGrantPermission  Advantage Client Engine |  |  |  |  |

Grants to a user or a user group one or more permissions to a database object.

Syntax

UNSIGNED32 AdsDDGrantPermission( ADSHANDLE hAdminConn,

UNSIGNED16 usObjectType,

UNSIGNED8 \*pucObjectName,

UNSIGNED8 \*pucParentName,

UNSIGNED8 \*pucGrantee,

UNSIGNED32 ulPermissions );

Parameters

|  |  |
| --- | --- |
| hAdminConn (I) | Handle of a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)). |
| usObjectType (I) | Type of the database object that is specified by the pucObjectName parameter. Valid values are ADS\_DD\_TABLE\_OBJECT, ADS\_DD\_COLUMN\_OBJECT, ADS\_DD\_VIEW\_OBJECT, ADS\_DD\_PROCEDURE\_OBJECT or ADS\_DD\_LINK\_OBJECT. |
| pucObjectName (I) | Name of the database object to grant the specified permissions on. It may be the name of a database table, the name of a column in a database table, the name of a view, the name of a stored procedure, name of a publication, name of a subscription, or a link alias. This parameter must be NULL or an empty string when granting CREATE permissions. |
| pucParentName (I) | Name of the database object that is the parent or owner of the object specified by pucObjectName. If usObjectType is ADS\_DD\_COLUMN\_OBJECT, this parameter specifies the name of the database table that owns the column specified by the pucObjectName parameter. For other object types, the parameter can be NULL and it is ignored. This parameter must be NULL or an empty string when granting CREATE permissions. |
| pucGrantee (I) | Name of a user or a user group that is going to be granted the permissions. |
| ulPermissions (I) | This is a bit field specifying the access permissions to be granted to the user or the user group specified by the pucGrantee parameter. The permissions can be ORed together. Valid permissions are ADS\_PERMISSION\_READ, ADS\_PERMISSION\_UPDATE, ADS\_PERMISSION\_INSERT, ADS\_PERMISSION\_DELETE, ADS\_PERMISSION\_EXECUTE, ADS\_PERMISSION\_LINK\_ACCESS, ADS\_PERMISSION\_INHERIT, ADS\_ PERMISSION\_ALTER, ADS\_PERMISSION\_DROP, ADS\_ PERMISSION\_CREATE, ADS\_PERMISSION\_WITH\_GRANT, ADS\_PERMISSION\_ALL, and ADS\_PERMISSION\_ALL\_WITH\_GRANT. See Remarks for explanation on the effects of permissions. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | The name specified by the pucObjectName, pucParentName or pucGrantee could not be found in the database. |
| AE\_INVALID\_OBJECT\_PERMISSION | The permissions specified by the ulPermissions parameter contains a permission that is not valid for the specified object type or grantee type. |
| AE\_PERMISSION\_DENIED | The current user does not have permission to grant the specified permissions. |

Remarks

AdsDDGrantPermission grants the specified access permissions to a user or a user group on a database object. The newly granted permission will be in addition to any existing permissions the user or the user group has on the specified database object. Permissions granted to views are not effected by the users permissions on the base tables used to construct the view. This behavior allows the use of views to control access to specific columns in the base tables. The following are valid permissions and a description of their effects on a users access to an object.

Note An older version dictionary may be upgraded to the latest version if necessary. This may be required to support new data dictionary functionality. See the Effects of Upgrading section in the current readme.txt file for any changes in behavior this may cause.

 

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

 

Note The ADS\_PERMISSION\_ALL permission equates to all the permissions for which the current user has ADS\_PERMISSION\_WITH\_GRANT permissions.

|  |  |
| --- | --- |
| usPropertyID | Description |
| ADS\_PERMISSION\_READ | This permission can be granted to a user or a user group on a table, a view or a column object. A user must have read permission to a table or view to open the table directly or issue an SQL SELECT statement against the table. When the read permission is granted on a table, the read permission is implicitly granted to all columns in the table. When the read permission is granted to a column in a table, a partial read permission is granted for the table. If the user does not have full read permission to a table, the allowed access to the table is controlled by the tables permission level property. See [AdsDDSetTableProperty](ace_adsddsetdatabaseproperty.htm) and ADS\_DD\_TABLE\_PERMISSION\_LEVEL for more information. |
| ADS\_PERMISSION\_UPDATE | This permission can be granted to a user or a user group on a table, a view or a column object. To modify existing data a user must be granted this permission. When this permission is granted on a table object, the permission is implicitly granted to all columns in the table. This permission affects SQL UPDATE statements and tables opened directly. |
| ADS\_PERMISSION\_INSERT | This permission can be granted to a user or a user group on a table, a view or a column object. A user must have insert permission to a table to insert new rows or provide data for a new row. Insert permission on a table or view allows the user to insert new rows into the table. Insert permission on column allows the user to provide data for a newly inserted row. If a new row is inserted into a table and the user does not have insert permission to some of the columns in the table, only default value can be posted to those columns. When granted to a table, this permission is implicitly granted to all columns in the table. This permission affects SQL INSERT statements and tables opened directly. |
| ADS\_PERMISSION\_DELETE | This permission can be granted to a user or a user group on a table or view object. This permission specifies whether the user can delete rows from a table or view. This permission affects SQL DELETE statements and tables opened directly. |
| ADS\_PERMISSION\_EXECUTE | This permission can be granted to a user or a user group on a stored procedure object. This permission affects SQL EXECUTE PROCEDURE statements. |
| ADS\_PERMISSION\_LINK\_ACCESS | This permission can be granted to a user or a user group on a link object. If this permission is not granted, the user cannot access tables on the link. A link is a reference to another database managed by the Advantage Database Server or Advantage Local Server. See [AdsDDCreateLink](ace_adsddcreatelink.htm) for addition information on links. |
| ADS\_PERMISSION\_INHERIT | This permission can be granted to a user on a table, a view, a stored procedure, subscription, publication, or a link object. With this permission, the users effective access permission to a database object is the sum of all permissions granted to the user and all user groups to which the user belongs. This permission can only be granted or revoked by the ADSSYS or members of the DB:Admin group and it cannot be granted with the ADS\_PERMISSION\_WITH\_GRANT option. For columns in a table, the user inherits permissions from its user groups only when the user is granted inherit permission on the table. By default all users are granted the inherit permission to database objects. For example, if "Group1" has read permission to "table1" and read and update permission to "table2"; and "Group2" has update permission to "table1", after making "user1" a member of both "Group1" and "Group2", the effective permissions of the user are read and update for both "table1" and "table2". To restrict "user1" to read permission to "table1", the administrator can grant the user the read permission to "table1" and revoke the users inherit permission to "table1". See [AdsDDRevokePermission](ace_adsddrevokepermission.htm) for additional information. |
| ADS\_PERMISSION\_ALTER | This permission can be granted to a user or a user group on a table, view, user, user group, relation, procedure, link, subscription, publication, or the database itself. With this permission, the grantee can modify the privileged properties of the specified object. To grant ALTER permissions for the database object, simply set pucObjectName to "Database" and pucParent to NULL or an empy string. |
| ADS\_PERMISSION\_DROP | This permission can be granted to a user or a user group on a table, view, user, user group, relation, procedure, subscription, publication, or link. With this permission the grantee can remove (drop) the specified object from the database. |
| ADS\_PERMISSION\_CREATE | This permission can be granted to a user or a user group on a table, user, user group, view, procedure, subscription, publication, or link. With this permission the grantee can create new objects of the specified type as well as add existing objects to the database such as tables and indexes. To grant this permission simply set usObjectType to the desired database object type and set pucObjectName and pucParentName to NULL or empty strings. ADS\_PERMISSION\_CREATE cannot be ORed together with any other permission except ADS\_PERMISSION\_WITH\_GRANT. |
| ADS\_PERMISSION\_WITH\_GRANT | This permission allows the grantee to grant the specified permission to another user or user group. This permission cannot be used alone. It must be ORed together with the permission or permissions to be granted. If the grantee does not already have the specified permissions ORed with WITH GRANT, they will be granted the specified permissions. |
| ADS\_PERMISSION\_ALL | This permission grants all available permissions to the user or user group that are aplicable for the specified object. Note: The ADS\_PERMISSION\_ALL permission equates to all the permissions for which the current user has ADS\_PERMISSION\_WITH\_GRANT permissions. |
| ADS\_PERMISSION\_ALL\_WITH\_GRANT | This permission is the same as ADS\_PERMISSION\_ALL except that it also gives the grantee WITH GRANT permissions for the specified object. |
| ADS\_DD\_PUBLICATION\_OBJECT | Retrieves the name of a publication object. The pucParentName is currently ignored and assumed to be the database. |
| ADS\_DD\_SUBSCRIPTION\_OBJECT | Retrieves the name of a subscription object. The pucParentName is currently ignored and assumed to be the database. |

The ulPermissions parameter is used to specify a combination of permissions to grant to the user or the user group. Assuming that the user currently has no permission (the inherit permission has been revoked) to an object, the following are some sample permissions combination and their effect on the users access to the object:

ADS\_PERMISSION\_READ | ADS\_PERMISSION\_UPDATE | ADS\_PERMISSION\_INSERT | ADS\_PERMISSION\_DELETE | ADS\_PERMISSION\_INHERIT

After granting this combination of permissions on a database table or view to a user, the user has full access to the table. The inherit permission is superfluous at this point because there is no addition permissions for the user to inherit. However, it is still meaningful because there may be other permissions in the future or the user may have certain permissions revoked on the table. This combination is not valid for column objects because of the inherit and delete permissions. This combination cannot be granted to a user group because of the inherit permission.

ADS\_PERMISSION\_READ | ADS\_PERMISSION\_INHERIT

This combination can be granted to a user on a table or a view. Besides having read permission to the table or view, the user will inherit other permissions from the user groups that the user belongs to. Other possible permissions that the user could inherit are insert, update, and delete.

ADS\_PERMISSION\_READ

This permission can be granted to a user or user group on a table, a view, or a column object. If granted this permission, the user has read-only access to the object. If the object is a table, the effective rights for the user to the table are read only access to all columns because the inherit permission was not granted. The users permission to the table is independent of the permissions granted to the user groups that the user may be a member of. If this permission is granted to a user group, all users in the user group will have effective read permission to the table or the view, provided that the users have been granted the inherit permission.

ADS\_PERMISSION\_INHERIT

This permission can be granted to a user on a table, a view or a stored procedure object. If granted this permission, the user can inherit permissions from the user groups they belong to. If the user is not a member of any user groups, the user will have no access to the object. If the user belongs to any user groups, the effective permissions for the user on the object is the sum of the permissions of all user groups that the user belongs to.

ADS\_PERMISSION\_EXECUTE

This combination can be granted to a user or user group on a stored procedure object. The user must be granted this permission to execute a stored procedure. If this permission is granted to a user group, all members of the user group who have been granted the inherited permission for the stored procedure can execute the stored procedure.

Note If the database is not set up to verify the user access permissions, the users access permissions will not be checked by the Advantage servers. See [AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.htm) and ADS\_DD\_VERIFY\_ACCESS\_RIGHTS property for more information. The property defaults to False on newly created data dictionary, effectively giving all users full access to all objects in the database.

 

Note Access to database tables is also affected by the table permission level property. See [AdsDDSetTableProperty](ace_adsddsettableproperty.htm) and the ADS\_DD\_TABLE\_PERMISSION\_LEVEL property.

 

Note The current user must be ADSSYS or have WITH GRANT permissions to grant permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

Example

After making a connection to the database, set up the access rights for the "Managers" user group to various tables and stored procedures. The user "rsmith" is then added to the "Managers" user group. Finally, access to the table "Salaries" is revoked from the user "rsmith" although he still has access to other managerial tables and views.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

 

/\* Grant managers full access to the "employees" table. \*/

ulReturnCode = AdsDDGrantPermission( hDD, ADS\_DD\_TABLE\_OBJECT, "Employees", NULL, "Managers",

ADS\_PERMISSION\_READ | ADS\_PERMISSION\_UPDATE | ADS\_PERMISSION\_INSERT |

ADS\_PERMISSION\_DELETE );

 

/\* Grant managers full access to the "salaries" table \*/

ulReturnCode = AdsDDGrantPermission( hDD, ADS\_DD\_TABLE\_OBJECT, "Salaries", NULL, "Managers",

ADS\_PERMISSION\_READ | ADS\_PERMISSION\_UPDATE | ADS\_PERMISSION\_INSERT |

ADS\_PERMISSION\_DELETE );

 

/\* Grant managers the execution right to the "New Hire" store procedure \*/

ulReturnCode = AdsDDGrantPermission( hDD, ADS\_DD\_PROCEDURE\_OBJECT, "New Hire", NULL, "Managers",

ADS\_PERMISSION\_INHERIT );

 

/\* Add rsmith to the managers group. \*/

ulReturnCode = AdsDDAddUserToGroup( hDD, "Managers", "rsmith" );

 

/\*

\* rsmith inherits all rights from the managers group. However, rsmith is only an

\* administrative assistant, so he is not allowed access to salary information.

\* Therefore, revoke his inherited rights to the "salaries" table.

\*/

ulReturnCode = AdsDDRevokePermission( hDD, ADS\_DD\_TABLE\_OBJECT, "Salaries", NULL, "rsmith",

ADS\_PERMISSION\_INHERIT );

 

AdsDisconnect( hDD );

See Also

[AdsDDCreateUser](ace_adsddcreateuser.htm)

[AdsDDCreateUserGroup](ace_adsddcreateusergroup.htm)

[AdsDDAddUserToGroup](ace_adsddaddusertogroup.htm)

[AdsDDRemoveUserFromGroup](ace_adsddremoveuserfromgroup.htm)

[AdsDDRevokePermission](ace_adsddrevokepermission.htm)

[AdsDDGetPermissions](ace_adsddgetpermissions.htm)