AdsDDCreateUserGroup




Advantage Database Server 12  

AdsDDCreateUserGroup

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDCreateUserGroup  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDCreateUserGroup Advantage Client Engine ace\_Adsddcreateusergroup Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDCreateUserGroup  Advantage Client Engine |  |  |  |  |

Create a new user group in the database.

Syntax

UNSIGNED32 AdsDDCreateUserGroup( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucGroupName,

UNSIGNED8 \*pucDescription );

Parameters

|  |  |
| --- | --- |
| hAdminConn (I) | Handle of a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)). |
| pucGroupName (I) | Name of the user group to create. |
| pucDescription (I) | Optional description of the user group. This parameter can be NULL. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | Possible cause for the error is that the pucGroupName is already used by another object in database. |

Remarks

AdsDDCreateUserGroup creates a user group object in the database. A user group can be used to logically group users with similar object access rights together. By default, a user inherits rights from the groups that he is a member of. By granting rights to user groups instead of users, it makes it simpler to add and remove access rights to multiple users. A user can become a member of a user group by calling the [AdsDDAddUserToGroup](ace_adsddaddusertogroup.htm) API.

CREATE USER GROUP permissions are required to create a data dictionary user group. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

Note When a database is created, it is by default to not perform access rights checking. In order to enforce the access rights of the users, the ADS\_DD\_VERIFY\_ACCESS\_RIGHTS property of the database must be set to True by calling the [AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.htm) API.

 

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

After making a connection to the database, create a user group named "Managers" in the database and grant the user group read and update permissions to the "Employees" table.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

ulReturnCode = AdsDDCreateUserGroup( hDD, "Managers", "All managers are in this group." );

ulReturnCode = AdsDDGrantPermission( hDD, ADS\_DD\_TABLE\_OBJECT, "Employees", NULL, "Managers",

ADS\_PERMISSION\_READ | ADS\_PERMISSION\_UPDATE );

See Also

[AdsConnect60](ace_adsconnect60.htm)

[AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.htm)

[AdsDDCreateUser](ace_adsddcreateuser.htm)

[AdsDDDeleteUserGroup](ace_adsdddeleteusergroup.htm)

[AdsDDAddUserToGroup](ace_adsddaddusertogroup.htm)

[AdsDDRemoveUserFromGroup](ace_adsddremoveuserfromgroup.htm)

[AdsDDGrantPermission](ace_adsddgrantpermission.htm)

[AdsDDRevokePermission](ace_adsddrevokepermission.htm)

[sp\_CreateGroup](master_sp_creategroup.htm)