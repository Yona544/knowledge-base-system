---
title: Master System Effectivepermissions
slug: master_system_effectivepermissions
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_system_effectivepermissions.htm
source: Advantage CHM
tags:
  - master
checksum: a0d57edb82542aac2df5b9a9652f28585e470f58
---

# Master System Effectivepermissions

system.effectivepermissions

system.effectivepermissions

Advantage SQL Engine

| system.effectivepermissions  Advantage SQL Engine |  |  |  |  |

Contains the effective permissions for each object that a user or user group has in the database. Effective permissions include permissions inherited from user groups. To retrieve only non inherited permissions, use the system.permissions view.

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
| Create | Integer | 4 | Create permission |
| Alter | Integer | 4 | Alter permission. |
| Drop | Integer | 4 | Drop permission. |

Note The integer permission values are interpreted as the following:

NULL Permission does not apply or is unavailable

0 Permission is not granted

1 Permission is granted

2 Permission plus WITH GRANT is granted
