---
title: Ade Aliasname Tadsconnection
slug: ade_aliasname_tadsconnection
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_aliasname_tadsconnection.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: c3eb9b75ed1aca376058a6b24fac821d82e2fe85
---

# Ade Aliasname Tadsconnection

AliasName

TAdsConnection.AliasName

Advantage TDataSet Descendant

| TAdsConnection.AliasName  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Specifies the alias to be used when connecting to the database server.

Syntax

property AliasName: String;

Description

The file path associated with the specified alias will be used as the database directory. The table type associated with the alias will be set as the default table type for use with this TAdsConnection instance. See [Database Aliases and the ads.ini File](ade_database_aliases_and_the_ads_ini_file.md) for a full description of an Alias.

Note AliasName and [ConnectPath](ade_connectpath_tadsconnection.md) are mutually exclusive. If you enter data into one property, the other will be cleared automatically.
