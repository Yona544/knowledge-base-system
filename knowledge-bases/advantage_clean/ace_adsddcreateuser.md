---
title: Ace Adsddcreateuser
slug: ace_adsddcreateuser
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddcreateuser.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 86c762fd72b2b7d4b51db25810c5369817e77265
---

# Ace Adsddcreateuser

AdsDDCreateUser

AdsDDCreateUser

Advantage Client Engine

| AdsDDCreateUser  Advantage Client Engine |  |  |  |  |

Create a new user in the database.

Syntax

UNSIGNED32 AdsDDCreateUser( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucGroupName,

UNSIGNED8 \*pucUserName,

UNSIGNED8 \*pucPassword,

UNSIGNED8 \*pucDescription );

Parameters

| hAdminConn (I) | Handle of a database connection). |
| pucGroupName (I) | Name of the user group that the user belongs to initially. This parameter can be NULL to make the user not belong to any user group. |
| pucUserName (I) | Name of the user to create. |
| pucPassword (I) | Initial password for the user. This parameter can be NULL or pointer to an empty string to specify no password for this user. |
| pucDescription (I) | Optional description of the user. This parameter can be NULL. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | Two of the possible causes for the error are that the pucUserName is already used by another object in database or the pucGroupName (if specified) does not identify a user group in the database. |

Remarks

AdsDDCreateUser creates a user object in the database. If the pucGroupName parameter specifies a user group in the data dictionary, the newly created user becomes a member of the group. The user can become member of multiple groups by calling the [AdsDDAddUserToGroup](ace_adsddaddusertogroup.md) API. The initial password can be changed by calling the [AdsDDSetUserProperty](ace_adsddsetuserproperty.md) API. Creating user in the database allows the administrator to control who have access to what table in the database. When a database is created, it is by default to allow anonymous connection to the database and no access rights checking. Those options can be turned on by calling the [AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.md) API.

CREATE USER permissions are required to create a data dictionary user. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

After making a connection to the database, create a user named "User1" in the database and grant the user read only permission to the "Customer Information" table.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

ulReturnCode = AdsDDCreateUser( hDD, NULL, "User1", NULL, "This user has read rights to tables. " );

ulReturnCode = AdsDDGrantPermission( hDD, ADS\_DD\_TABLE\_OBJECT, "Customer Information", NULL, "User1",

ADS\_PERMISSION\_READ );

See Also

[AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.md)

[AdsDDDeleteUser](ace_adsdddeleteuser.md)

[AdsDDGetUserProperty](ace_adsddgetuserproperty.md)

[AdsDDSetUserProperty](ace_adsddsetuserproperty.md)

[AdsDDCreateUserGroup](ace_adsddcreateusergroup.md)

[AdsDDDeleteUserGroup](ace_adsdddeleteusergroup.md)

[AdsDDAddUserToGroup](ace_adsddaddusertogroup.md)

[AdsDDRemoveUserFromGroup](ace_adsddremoveuserfromgroup.md)

[AdsDDGrantPermission](ace_adsddgrantpermission.md)

[AdsDDRevokePermission](ace_adsddrevokepermission.md)

[sp\_CreateUser](master_sp_createuser.md)
