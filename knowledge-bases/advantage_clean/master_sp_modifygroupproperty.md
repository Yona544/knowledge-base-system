---
title: Master Sp Modifygroupproperty
slug: master_sp_modifygroupproperty
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_modifygroupproperty.htm
source: Advantage CHM
tags:
  - master
checksum: 19e5167bafe9f1b13a8ab2aa5e6fd7eb916e72f6
---

# Master Sp Modifygroupproperty

sp\_ModifyGroupProperty

sp\_ModifyGroupProperty

Advantage SQL Engine

| sp\_ModifyGroupProperty  Advantage SQL Engine |  |  |  |  |

Sets one property associated with a database user group in the data dictionary.

Syntax

sp\_ModifyGroupProperty(

GroupName,CHARACTER,100,

Property,CHARACTER,200,

Value,MEMO )

Parameters

| GroupName (I) | Name of the database user group object to set the associated property. |
| Property (I) | Name of a database user group property to set. See Remarks for allowed values. |
| Property (I) | Value to be stored in the property. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | Possible causes for the error is that the pucUserGroupName does not specify a valid user group in the database. |

Remarks

sp\_ModifyGroupProperty sets one property associated with the specified user group. The new property overwrites the existing property in the data dictionary. The following are the valid values of Property and the expected values.

| usPropertyID | Description |
| COMMENT | Stores a new description for the user group. |

Example

After making a connection to the database, store a new description for the user group "Managers".

EXECUTE PROCEDURE sp\_ModifyGroupProperty(

Managers ,

COMMENT,

Managers of the Data Product Division. );

See Also

[sp\_CreateGroup](master_sp_creategroup.md)

[sp\_DropGroup](master_sp_dropgroup.md)

[sp\_CreateUser](master_sp_createuser.md)

[sp\_DropUser](master_sp_dropuser.md)

[sp\_AddUserToGroup](master_sp_addusertogroup.md)

[sp\_RemoveUserFromGroup](master_sp_removeuserfromgroup.md)
