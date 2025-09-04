---
title: Ace Adsddremoveuserfromgroup
slug: ace_adsddremoveuserfromgroup
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddremoveuserfromgroup.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: c6cae7ae7829dbf0a46c49449a81c26ca89e3c9e
---

# Ace Adsddremoveuserfromgroup

AdsDDRemoveUserFromGroup

AdsDDRemoveUserFromGroup

Advantage Client Engine

| AdsDDRemoveUserFromGroup  Advantage Client Engine |  |  |  |  |

Makes a database user not a member of the specified user group.

Syntax

UNSIGNED32 AdsDDRemoveUserFromGroup( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucGroupName,

UNSIGNED8 \*pucUserName );

Parameters

| hAdminConn (I) | Handle of a database connection). |
| pucGroupName (I) | Name of the database user group object to remove the users membership. |
| pucUserName (I) | Name of the database user object to remove from the user groups membership. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | Either the pucGroupName does not specify a valid user group in the database or the pucUserName does not specify a valid database user. |
| AE\_NOT\_MEMBER\_OF\_GROUP | The user is not a member of the specified user group. |

Remarks

AdsDDRemoveUserFromGroup removes the user from the membership of the specified user group. Once the user is removed from the membership of the user group, the user loses all object access rights that he inherited from the user group.

ALTER permissions on the user group are required to remove a user from a data dictionary user group. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

After making a connection to the database, remove user "rsmith" from the user group "Managers". If the only rights the user has to the table "employees" are inherited from the "Managers" user group, the user "rsmith" will now have no rights to the "employees" table after being removed from the user group.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

ulReturnCode = AdsDDRemoveUserFromGroup( hDD, "Managers", "rsmith" );

AdsDisconnect( hDD );

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "rsmith", NULL, ADS\_DEFAULT, &hConn );

/\* The following call should fail with an error of either a 7079 or 7080 \*/

ulReturnCode = AdsOpenTable( hConn, "employees", NULL, ADS\_DEFAULT, ADS\_DEFAULT, ADS\_DEFAULT,

ADS\_DEFAULT, ADS\_DEFAULT, &hTable );

See Also

[AdsDDCreateUser](ace_adsddcreateuser.md)

[AdsDDCreateUserGroup](ace_adsddcreateusergroup.md)

[AdsDDDeleteUserGroup](ace_adsdddeleteusergroup.md)

[AdsDDAddUserToGroup](ace_adsddaddusertogroup.md)

[AdsDDGrantPermission](ace_adsddgrantpermission.md)

[AdsDDRevokePermission](ace_adsddrevokepermission.md)

[sp\_RemoveUserFromGroup](master_sp_removeuserfromgroup.md)
