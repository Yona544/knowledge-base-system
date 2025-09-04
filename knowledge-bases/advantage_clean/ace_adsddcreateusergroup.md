---
title: Ace Adsddcreateusergroup
slug: ace_adsddcreateusergroup
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddcreateusergroup.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: df8a7854e44cb94eac35707771504e3079c9bdf9
---

# Ace Adsddcreateusergroup

AdsDDCreateUserGroup

AdsDDCreateUserGroup

Advantage Client Engine

| AdsDDCreateUserGroup  Advantage Client Engine |  |  |  |  |

Create a new user group in the database.

Syntax

UNSIGNED32 AdsDDCreateUserGroup( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucGroupName,

UNSIGNED8 \*pucDescription );

Parameters

| hAdminConn (I) | Handle of a database connection). |
| pucGroupName (I) | Name of the user group to create. |
| pucDescription (I) | Optional description of the user group. This parameter can be NULL. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | Possible cause for the error is that the pucGroupName is already used by another object in database. |

Remarks

AdsDDCreateUserGroup creates a user group object in the database. A user group can be used to logically group users with similar object access rights together. By default, a user inherits rights from the groups that he is a member of. By granting rights to user groups instead of users, it makes it simpler to add and remove access rights to multiple users. A user can become a member of a user group by calling the [AdsDDAddUserToGroup](ace_adsddaddusertogroup.md) API.

CREATE USER GROUP permissions are required to create a data dictionary user group. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Note When a database is created, it is by default to not perform access rights checking. In order to enforce the access rights of the users, the ADS\_DD\_VERIFY\_ACCESS\_RIGHTS property of the database must be set to True by calling the [AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.md) API.

 

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

After making a connection to the database, create a user group named "Managers" in the database and grant the user group read and update permissions to the "Employees" table.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

ulReturnCode = AdsDDCreateUserGroup( hDD, "Managers", "All managers are in this group." );

ulReturnCode = AdsDDGrantPermission( hDD, ADS\_DD\_TABLE\_OBJECT, "Employees", NULL, "Managers",

ADS\_PERMISSION\_READ | ADS\_PERMISSION\_UPDATE );

See Also

[AdsConnect60](ace_adsconnect60.md)

[AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.md)

[AdsDDCreateUser](ace_adsddcreateuser.md)

[AdsDDDeleteUserGroup](ace_adsdddeleteusergroup.md)

[AdsDDAddUserToGroup](ace_adsddaddusertogroup.md)

[AdsDDRemoveUserFromGroup](ace_adsddremoveuserfromgroup.md)

[AdsDDGrantPermission](ace_adsddgrantpermission.md)

[AdsDDRevokePermission](ace_adsddrevokepermission.md)

[sp\_CreateGroup](master_sp_creategroup.md)
