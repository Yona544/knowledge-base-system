---
title: Master Sp Createuser
slug: master_sp_createuser
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_createuser.htm
source: Advantage CHM
tags:
  - master
checksum: 851069a4bda1407a3616969bacdb8fce81bebdff
---

# Master Sp Createuser

sp\_CreateUser

sp\_CreateUser

Advantage SQL Engine

| sp\_CreateUser  Advantage SQL Engine |  |  |  |  |

Create a new user in the database.

Syntax

sp\_CreateUser(

UserName,CHARACTER,50,

Password,CHARACTER,20,

Comment,MEMO )

Parameters

| UserName (I) | Name of the user to create. |
| Password (I) | Initial password for the user. This parameter can be NULL or an empty string to specify no password for this user. |
| Comment (I) | Optional description of the user. This parameter can be NULL. |

Remarks

sp\_CreateUser creates a user object in the database. The initial password can be changed by sp\_ModifyUserProperty. Creating users in the database allows the administrator to control who has access to what table in the database. When a database is created, it by default to allow anonymous connections to the database and no access rights checking is performed. Those options can be turned on by [sp\_ModifyDatabase](master_sp_modifydatabase.md).

Example

After making a connection to the database, create a user named "User1" in the database and grant the user read only permission to the "Customer Information" table.

EXECUTE PROCEDURE sp\_CreateUser(

User1,

NULL,

This user has read rights to tables. );

 

GRANT SELECT ON "Customer Information" TO User1;

See Also

[sp\_ModifyDatabase](master_sp_modifydatabase.md)

[sp\_DropUser](master_sp_dropuser.md)

[sp\_ModifyUserProperty](master_sp_modifyuserproperty.md)

[sp\_CreateGroup](master_sp_creategroup.md)

[sp\_DropGroup](master_sp_dropgroup.md)

[sp\_AddUserToGroup](master_sp_addusertogroup.md)

[sp\_RemoveUserFromGroup](master_sp_removeuserfromgroup.md)
