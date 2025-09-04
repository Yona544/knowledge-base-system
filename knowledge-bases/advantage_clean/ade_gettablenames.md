---
title: Ade Gettablenames
slug: ade_gettablenames
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_gettablenames.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: ef17264cc41ead8cf986ee592f267be855997339
---

# Ade Gettablenames

GetTableNames

TAdsConnection.GetTableNames

Advantage TDataSet Descendant

| TAdsConnection.GetTableNames  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Populates a string list with the tables associated with the connection.

Syntax

procedure TAdsConnection.GetTableNames( poList : TStrings; strFileMask : String );

Description

Use GetTableNames to get a list of tables associated with the TAdsConnection component. The [TAdsConnection.IsConnected](ade_isconnected_tadsconnection.md) property must be set to True before calling GetTableNames. If GetTableNames is called on a connection that uses the [TAdsConnection.ConnectPath](ade_connectpath_tadsconnection.md) property, all files matching the strFileMask parameter will be returned. If GetTableNames is called on a connection that uses the [TAdsConnection.AliasName](ade_aliasname_tadsconnection.md) property, tables matching the alias tabletype will be returned, and the strMask parameter will be ignored. If GetTableNames is called using an alias that points to an Advantage Data Dictionary, or a connection path that points to an Advantage Data Dictionary, the strFileMask parameter will be ignored, and all tables registered in the data dictionary will be returned.

See Also

[AliasName](ade_aliasname_tadsconnection.md)

[ConnectPath](ade_connectpath_tadsconnection.md)
