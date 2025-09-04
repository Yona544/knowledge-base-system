---
title: Ace Adsddgetuserproperty
slug: ace_adsddgetuserproperty
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddgetuserproperty.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 06fe79a2bc28d8e6dc99c88e98c03696fb2852ba
---

# Ace Adsddgetuserproperty

AdsDDGetUserProperty

AdsDDGetUserProperty

Advantage Client Engine

| AdsDDGetUserProperty  Advantage Client Engine |  |  |  |  |

Retrieves one property associated with a database user from the data dictionary into the supplied buffer.

Syntax

UNSIGNED32 AdsDDGetUserProperty( ADSHANDLE hDBConn,

UNSIGNED8 \*pucUserName,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 \*pusPropertyLen );

Parameters

| hDBConn (I) | Handle of a database connection). |
| pucUserName (I) | Name of the database user object to retrieve the associated property. |
| usPropertyID (I) | Index of a database user property to retrieve. See Remarks for allowed values. |
| pvProperty (O) | Pointer to the buffer where the property is to be copied into. |
| pusPropertyLen (I/O) | On input, it specifies the size of the buffer pointed to by pvProperty. On output, it returns the length of property stored in the buffer. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | Possible cause for the error is that the pucUserName does not specify a valid user name in the database. |
| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in usPropertyID is not a valid database user property ID, or the specified property is not retrievable. |
| AE\_INSUFFICIENT\_BUFFER | The size of the property to be copied into pvProperty is larger than the buffer size specified by \*pusPropertyLen. The required buffer length is returned in \*pusPropertyLen when this error occurs. |
| AE\_PROPERTY\_NOT\_SET | The requested property is not set in the data dictionary. No data is returned in pvProperty and \*pusPropertylen. |

Remarks

AdsDDGetUserProperty retrieves one user property associated with the specified user. User properties can only be retrieved by the specified user or users with administrative permissions to this user. When connected as the administrator (ADSSYS user account), properties from any user can be retrieved. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. The following are the valid values of usPropertyID and the expected return value in pvProperty and \*pusPropertyLen.

| usPropertyID | Description |
| ADS\_DD\_COMMENT | Returns the description of the user in pvProperty. |
| ADS\_DD\_USER\_DEFINED\_PROP | Returns the user defined property for the specified user. |
| ADS\_DD\_USER\_GROUP\_MEMBERSHIP | Returns in the pvProperty the user groups that the specified user is a member of. The group membership is returned as a ; delimited string listing all user groups that the user is a member. For example: if the returned string is Managers;R&D, that means the user belongs to 2 user groups the Managers user group and the R&D user group. |

Example

After making a connection to the database, retrieve a list of the user groups that the user User1 is a member of.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

usLen = sizeof( aucGroups );

ulReturnCode = AdsDDGetUserProperty( hDD, "User1", ADS\_DD\_USER\_GROUP\_MEMBERSHIP, aucGroups, &usLen );

See Also

[AdsDDCreateUser](ace_adsddcreateuser.md)

[AdsDDSetUserProperty](ace_adsddsetuserproperty.md)

[AdsDDCreateUserGroup](ace_adsddcreateusergroup.md)

[AdsDDDeleteUserGroup](ace_adsdddeleteusergroup.md)

[AdsDDAddUserToGroup](ace_adsddaddusertogroup.md)

[AdsDDRemoveUserFromGroup](ace_adsddremoveuserfromgroup.md)

[AdsDDGrantPermission](ace_adsddgrantpermission.md)

[AdsDDRevokePermission](ace_adsddrevokepermission.md)

[system.views](master_system_views.md)
