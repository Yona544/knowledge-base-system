---
title: Ade Usergroupsstring Tadsconnection Prop
slug: ade_usergroupsstring_tadsconnection_prop
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_usergroupsstring_tadsconnection_prop.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 04285a02ee8f39071c5e3206cf13a2cc35b837aa
---

# Ade Usergroupsstring Tadsconnection Prop

UserGroupsString

TAdsConnection.UserGroupsString

Advantage TDataSet Descendant

| TAdsConnection.UserGroupsString  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Semi-colon delimited list of groups the current user belongs to.

Syntax

property UserGroupsString: string;

Description

UserGroupsString contains a semi-colon delimited list of groups the current user belongs to. If you are using Delphi/C++Builder version 5 or greater, use the [UserGroups](ade_usergroups_tadsconnection_prop.md) property.

This string can either be used directly, or modified to contain coma delimiters instead of semi-colon delimiters and placed into a TStringList object. Beware that colons are valid characters in user names.

The UserGroupsString is only applicable to database connections), and will be empty if called on a free connection). If called on an inactive connection, UserGroupsString will return an empty string.

See Also

[UserGroups](ade_usergroups_tadsconnection_prop.md)

[Username](ade_username_tadsconnection.md)
