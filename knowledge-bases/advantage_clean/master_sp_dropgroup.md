---
title: Master Sp Dropgroup
slug: master_sp_dropgroup
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_dropgroup.htm
source: Advantage CHM
tags:
  - master
checksum: 75dc83c832dd15b9ff017190fab011cde842f86e
---

# Master Sp Dropgroup

sp\_DropGroup

sp\_DropGroup

Advantage SQL Engine

| sp\_DropGroup  Advantage SQL Engine |  |  |  |  |

Delete a user group object from the database.

Syntax

sp\_DropGroup( GroupName,CHARACTER,100 )

Parameters

| GroupName (I) | Name of the user group object to delete. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | Possible cause for the error is that the GroupName is not a valid user group name in the database. |

Remarks

sp\_DropGroup removes an existing user group from the database. All references to the user group by the database users are removed from the data dictionary.

Example

After making a connection to the database, delete the user group named "Managers" from the database.

EXECUTE PROCEDURE sp\_DropGroup( Managers );

See Also

[sp\_CreateGroup](master_sp_creategroup.md)

[sp\_ModifyGroupProperty](master_sp_modifygroupproperty.md)

[sp\_CreateUser](master_sp_createuser.md)

[sp\_DropUser](master_sp_dropuser.md)

[sp\_AddUserToGroup](master_sp_addusertogroup.md)

[sp\_RemoveUserFromGroup](master_sp_removeuserfromgroup.md)
