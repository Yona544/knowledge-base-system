---
title: Ace Adsddgetusergroupproperty
slug: ace_adsddgetusergroupproperty
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddgetusergroupproperty.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 23387cea89ef313cbc3140fd29af5382cb97a3f3
---

# Ace Adsddgetusergroupproperty

AdsDDGetUserGroupProperty

AdsDDGetUserGroupProperty

Advantage Client Engine

| AdsDDGetUserGroupProperty  Advantage Client Engine |  |  |  |  |

Retrieves one property associated with a database user group from the data dictionary into the supplied buffer.

Syntax

UNSIGNED32 AdsDDGetUserGroupProperty( ADSHANDLE hDBConn,

UNSIGNED8 \*pucUserGroupName,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 \*pusPropertyLen );

Parameters

| hDBConn (I) | Handle of a database connection). |
| pucUserGroupName (I) | Name of the database user group object to retrieve the associated property. |
| usPropertyID (I) | Index of a database user group property to retrieve. See Remarks for allowed values. |
| pvProperty (O) | Pointer to the buffer where the property is to be copied into. |
| \*pusPropertyLen (I/O) | On input, it specifies the size of the buffer pointed to by pvProperty. On output, it returns the length of property stored in the buffer. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | Possible cause for the error is that the pucUserGroupName does not specify a valid user group in the database. |
| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in usPropertyID is not a valid database user group property ID, or the specified property is not retrievable. |
| AE\_INSUFFICIENT\_BUFFER | The size of the property to be copied into pvProperty is larger than the buffer size specified by \*pusPropertyLen. The required buffer length is returned in \*pusPropertyLen when this error occurs. |
| AE\_PROPERTY\_NOT\_SET | The requested property is not set in the data dictionary. No data is returned in pvProperty and \*pusPropertylen. |

Remarks

AdsDDGetUserGroupProperty retrieves one property associated with the specified user group. User group properties are only available to users that belong to the specified group or to users with ALTER permissions for the group. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. When connected as the administrator (ADSSYS user account), properties from any user group can be retrieved. The following are the valid values of usPropertyID and the expected return value in pvProperty and \*pusPropertyLen.

| usPropertyID | Description |
| ADS\_DD\_COMMENT | Returns the description of the user group in pvProperty. |
| ADS\_DD\_USER\_DEFINED\_PROP | Returns the user defined property for the specified user group. |

Example

After making a connection to the database, retrieve a list of tables that the user group "Managers" has any access rights to.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

usLen = sizeof( aucTableRights );

ulReturnCode = AdsDDGetUserGroupProperty( hDD, "Managers", ADS\_DD\_TABLE\_RIGHTS,

aucTableRights, &usLen );

See Also

[AdsDDCreateUserGroup](ace_adsddcreateusergroup.md)

[AdsDDSetUserGroupProperty](ace_adsddsetusergroupproperty.md)

[AdsDDAddUserToGroup](ace_adsddaddusertogroup.md)

[AdsDDRemoveUserFromGroup](ace_adsddremoveuserfromgroup.md)

[AdsDDGetUserProperty](ace_adsddgetuserproperty.md)

[AdsDDGrantPermission](ace_adsddgrantpermission.md)

[AdsDDRevokePermission](ace_adsddrevokepermission.md)

[system.usergroups](master_system_usergroups.md)
