---
title: Master Sp Creategroup
slug: master_sp_creategroup
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_creategroup.htm
source: Advantage CHM
tags:
  - master
checksum: de839691c6cf51113eeda0f82b5d4618841f1fae
---

# Master Sp Creategroup

sp\_CreateGroup

sp\_CreateGroup

Advantage SQL Engine

| sp\_CreateGroup  Advantage SQL Engine |  |  |  |  |

Create a new user group in the database.

Syntax

sp\_CreateGroup(

GroupName,CHARACTER,100,

Comment,MEMO );

Parameters

| GroupName (I) | Name of the user group to create. |
| Comment (I) | Optional description of the user group. This parameter can be NULL. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | Possible cause for the error is that the GroupName is already used by another object in the database. |

Remarks

sp\_CreateGroup creates a user group object in the database. A user group can be used to logically group users with similar object access rights together. By default, a user inherits rights from the groups that he is a member of. By granting rights to user groups instead of users, it makes it simpler to add and remove access rights to multiple users. A user can become a member of a user group by calling the sp\_AddUserToGroup.

Note When a database is created, it does not perform access rights checking by default. In order to enforce the access rights of the users, the VERIFY\_ACCESS\_RIGHTS property of the database must be set to True by calling the [sp\_ModifyDatabase](master_sp_modifydatabase.md).

Example

After making a connection to the database, create a user group named "Managers" in the database and grant the user group read and update permissions to the "Employees" table.

EXECUTE PROCEDURE sp\_CreateGroup(

Managers,

All managers are in this group. );

 

GRANT SELECT,UPDATE ON Employees To Managers;

See Also

[sp\_DropGroup](master_sp_dropgroup.md)

[sp\_ModifyGroupProperty](master_sp_modifygroupproperty.md)

[sp\_CreateUser](master_sp_createuser.md)

[sp\_DropUser](master_sp_dropuser.md)

[sp\_AddUserToGroup](master_sp_addusertogroup.md)

[sp\_RemoveUserFromGroup](master_sp_removeuserfromgroup.md)
