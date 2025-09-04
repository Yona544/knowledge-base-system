---
title: Master Effective Permissions Vs Explicit Permissions
slug: master_effective_permissions_vs_explicit_permissions
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_effective_permissions_vs_explicit_permissions.htm
source: Advantage CHM
tags:
  - master
checksum: 1487fefae240d43af962ac106bd095f7c332c829
---

# Master Effective Permissions Vs Explicit Permissions

Effective Permissions vs Explicit Permissions

Effective Permissions vs Explicit Permissions

Advantage Concepts

| Effective Permissions vs Explicit Permissions  Advantage Concepts |  |  |  |  |

A users effective permissions to a specific object in the database consist of the permissions explicitly granted to the user and the permissions derived from the user groups that the user belongs to. The concept is illustrated by the following example:

User1 is a member of GroupA

User2 is a member of GroupA and GroupB

 

GroupA has SELECT (i.e., READ) permission to Table1

GroupB has INSERT permission to Table1

 

If no permission is granted explicitly to User1 and User2, their explicit permissions to the Table1 object is none. However, their effective permissions to the Table1 object are different:

User1 has effective SELECT permission to Table1 inherited from GroupA.

User2 has effective SELECT and INSERT permissions to Table1 inherited from GroupA and GroupB respectively.

The inheritance of the permissions from the user group to specific objects is the default behavior. In rare situation, if it is desirable to prevent the inheritance, it can be achieved by revoking the users inherit permission to the specific object. Using the sample described above, if User2s inherit permission to the Table1 object has been revoked, it will have no permission to the Table1 object even though it belongs to two groups that do have permissions to Table1.
