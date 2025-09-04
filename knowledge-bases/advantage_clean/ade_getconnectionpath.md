---
title: Ade Getconnectionpath
slug: ade_getconnectionpath
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getconnectionpath.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: b25307292fdd3f6d8968394481b22c7aa7b6d97d
---

# Ade Getconnectionpath

GetConnectionPath

TAdsConnection.GetConnectionPath

Advantage TDataSet Descendant

| TAdsConnection.GetConnectionPath  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Returns the connection path from the TAdsConnection component.

Syntax

function GetConnectionPath : string;

Remarks

This function returns the connection path from the TAdsConnection component. If the connection is using an alias, the connection path associated with the alias will be returned. If the connection is to a data dictionary, this path will NOT contain the name of the data dictionary file (see [GetConnectionWithDDPath](ade_getconnectionwithddpath.md)).

See Also

[GetConnectionWithDDPath](ade_getconnectionwithddpath.md)

[AliasName](ade_aliasname_tadsconnection.md)

[ConnectPath](ade_connectpath_tadsconnection.md)
