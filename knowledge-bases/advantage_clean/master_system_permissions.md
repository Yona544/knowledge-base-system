---
title: Master System Permissions
slug: master_system_permissions
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_system_permissions.htm
source: Advantage CHM
tags:
  - master
checksum: 5f1a6cc5250f5bda864d8615fb30c4664b4e33f9
---

# Master System Permissions

system.permissions

system.permissions

Advantage SQL Engine

| system.permissions  Advantage SQL Engine |  |  |  |  |

Contains the complete permissions for each object that a user or user group has in the database. Note this table does not include inherited permissions. To retrieve the inherited permissions, use the system.effectivepermissions view.

| Field Name | Field Type | Field Size | Description |
| Name | Character | 200 | Object name. |
| Object\_Type | Integer | 4 | The object type. |
| Parent | Character | 200 | The object parent. |
| Grantee | Character | 200 | The user or user group that the permission is for. |
| Select | Integer | 4 | Read permission. |
| Update | Integer | 4 | Update permission. |
| Insert | Integer | 4 | Insert permission. |
| Delete | Integer | 4 | Delete permission. |
| Execute | Integer | 4 | Execute permission. |
| Access | Integer | 4 | Link access permission. |
| Inherit | Integer | 4 | Inherit permission. |
| Create | Integer | 4 | Create permission. |
| Alter | Integer | 4 | Alter permission. |
| Drop | Integer | 4 | Drop permission. |

Note The integer permission values are interpreted as the following:

NULL Permission does not apply or is unavailable

0 Permission is not granted

1 Permission is granted

2 Permission plus WITH GRANT is granted
