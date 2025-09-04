---
title: Ade Usergroups Tadsconnection Prop
slug: ade_usergroups_tadsconnection_prop
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_usergroups_tadsconnection_prop.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: fab14bd7a7df3ebd3a3d6da018f5e603f1d60a79
---

# Ade Usergroups Tadsconnection Prop

UserGroups

TAdsConnection.UserGroups

Advantage TDataSet Descendant

| TAdsConnection.UserGroups  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

String list of groups the current user belongs to.

Syntax

property UserGroups: TStringList;

Description

UserGroups is a list of groups the current user belongs to. The UserGroups property is only supported in Delphi/C++Builder versions 5 or greater. If using an older version of Delphi or C++Builder, use the [UserGroupsString](ade_usergroupsstring_tadsconnection_prop.md) property.

The UserGroups is only applicable to database connections), and will be empty if called on a free connection). If called on an inactive connection, UserGroups will be empty.

See Also

[UserGroupsString](ade_usergroupsstring_tadsconnection_prop.md)

[Username](ade_username_tadsconnection.md)
