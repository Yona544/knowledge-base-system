---
title: Ace Adsdddeleteusergroup
slug: ace_adsdddeleteusergroup
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsdddeleteusergroup.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: d2bc8e1c8cefbecc84cf8cd4ce56fd6dc7be4077
---

# Ace Adsdddeleteusergroup

AdsDDDeleteUserGroup

AdsDDDeleteUserGroup

Advantage Client Engine

| AdsDDDeleteUserGroup  Advantage Client Engine |  |  |  |  |

Delete a user group object from the database.

Syntax

UNSIGNED32 AdsDDDeleteUserGroup( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucGroupName );

Parameters

| hAdminConn (I) | Handle of a database connection). |
| pucGroupName (I) | Name of the user group object to delete. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | Possible cause for the error is that the pucGroupName is not a valid user group name in the database. |

Remarks

AdsDDDeleteUserGroup removes an existing user group from the database. All references to the user group by the database users are removed from the DD.

DROP permissions on the user group are required to delete a data dictionary user group. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

After making a connection to the database, delete the user group named "Managers" from the database.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

ulReturnCode = AdsDDDeleteUserGroup( hDD, "Managers" );

See Also

[AdsDDCreateUser](ace_adsddcreateuser.md)

[AdsDDCreateUserGroup](ace_adsddcreateusergroup.md)

[AdsDDAddUserToGroup](ace_adsddaddusertogroup.md)

[AdsDDRemoveUserFromGroup](ace_adsddremoveuserfromgroup.md)

[AdsDDGrantPermission](ace_adsddgrantpermission.md)

[AdsDDRevokePermission](ace_adsddrevokepermission.md)

[sp\_DropGroup](master_sp_dropgroup.md)
