---
title: Ace Adsddsetusergroupproperty
slug: ace_adsddsetusergroupproperty
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddsetusergroupproperty.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: ff570d8bbc61ebd7b66d3760a1d21624134b5e0a
---

# Ace Adsddsetusergroupproperty

AdsDDSetUserGroupProperty

AdsDDSetUserGroupProperty

Advantage Client Engine

| AdsDDSetUserGroupProperty  Advantage Client Engine |  |  |  |  |

Sets one property associated with a database user group in the data dictionary.

Syntax

UNSIGNED32 AdsDDSetUserGroupProperty( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucUserGroupName,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 usPropertyLen );

Parameters

| hAdminConn (I) | Handle of a database connection). |
| pucUserGroupName (I) | Name of the database user group object to set the associated property. |
| usPropertyID (I) | Index of a database user group property to set. See Remarks for allowed values. |
| pvProperty (I) | Pointer to the buffer where the property is stored. |
| usPropertyLen (I) | The size of the property stored in the buffer. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | Possible causes for the error is that the pucUserGroupName does not specify a valid user group in the database. |
| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in usPropertyID is not a valid database user group property ID, or the specified property cannot be set. |

Remarks

AdsDDSetUserGroupProperty sets one property associated with the specified user group. The new property overwrites the existing property in the data dictionary. The following are the valid values of usPropertyID and the expected value in pvProperty and usPropertyLen.

ALTER permissions on the user group are required to modify the properties of a data dictionary user group. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

| usPropertyID | Description |
| ADS\_DD\_COMMENT | Stores a new description for the user group. The pvProperty is expected to be NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. If pvProperty is NULL or empty string, the user description is removed. |
| ADS\_DD\_USER\_DEFINED\_PROP | Changes the user defined user group property. If pvProperty is NULL, the user defined user group property is removed. User defined property is set, read, and interpreted by the application. It is not used by the Advantage engines. |

Example

After making a connection to the database, store a new description for the user group "Managers".

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

sprintf( acNewDescription, "%s", "Managers of the Data Product Division. " );

usLen = (UNSIGNED16)( 1 + strlen("Managers of the Data Product Division. " ));

ulReturnCode = AdsDDSetUserGroupProperty( hDD, "Managers", ADS\_DD\_COMMENT,

acNewDescription, usLen );

See Also

[AdsConnect60](ace_adsconnect60.md)

[AdsDDCreateUser](ace_adsddcreateuser.md)

[AdsDDCreateUserGroup](ace_adsddcreateusergroup.md)

[AdsDDDeleteUserGroup](ace_adsdddeleteusergroup.md)

[AdsDDGetUserGroupProperty](ace_adsddgetusergroupproperty.md)

[sp\_ModifyGroupProperty](master_sp_modifygroupproperty.md)
