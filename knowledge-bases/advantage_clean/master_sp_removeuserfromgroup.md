---
title: Master Sp Removeuserfromgroup
slug: master_sp_removeuserfromgroup
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_removeuserfromgroup.htm
source: Advantage CHM
tags:
  - master
checksum: e049487a78d6cd540b7312fbbaf32ee2c789b405
---

# Master Sp Removeuserfromgroup

sp\_RemoveUserFromGroup

sp\_RemoveUserFromGroup

Advantage SQL Engine

| sp\_RemoveUserFromGroup  Advantage SQL Engine |  |  |  |  |

Removes a database user from the specified user group.

Syntax

sp\_RemoveUserFromGroup(

UserName,CHARACTER,50,

GroupName,CHARACTER,100 )

Parameters

| UserName (I) | Name of the database user object to remove from the user groups membership. |
| GroupName (I) | Name of the database user group object to remove the users membership. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | Either the GroupName does not specify a valid user group in the database or the UserName does not specify a valid database user. |
| AE\_NOT\_MEMBER\_OF\_GROUP | The user is not a member of the specified user group. |

Remarks

sp\_RemoveUserFromGroup removes the user from the membership of the specified user group. Once the user is removed from the membership of the user group, the user loses all object access rights that he inherited from the user group.

Example

After making a connection to the database, remove user "rsmith" from the user group "Managers". If the only rights the user has to the table "employees" are inherited from the "Managers" user group, the user "rsmith" will now have no rights to the "employees" table after being removed from the user group.

EXECUTE PROCEDUE sp\_RemoveUserFromGroup(

rsmith,

Managers )

See Also

[sp\_CreateGroup](master_sp_creategroup.md)

[sp\_DropGroup](master_sp_dropgroup.md)

[sp\_CreateUser](master_sp_createuser.md)

[sp\_DropUser](master_sp_dropuser.md)

[sp\_AddUserToGroup](master_sp_addusertogroup.md)
