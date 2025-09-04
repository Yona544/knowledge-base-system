---
title: Ade Getconnectionwithddpath
slug: ade_getconnectionwithddpath
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_getconnectionwithddpath.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 2002ec851ee973768eb21c7a37f44e942955342e
---

# Ade Getconnectionwithddpath

GetConnectionWithDDPath

TAdsConnection.GetConnectionWithDDPath

Advantage TDataSet Descendant

| TAdsConnection.GetConnectionWithDDPath  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Returns the connection path from the TAdsConnection component.

Syntax

function GetConnectionWithDDPath : string;

Remarks

This function returns the connection path from the TAdsConnection component. If the connection is to a data dictionary, this path will contain the name of the data dictionary file. If the connection does not reference a data dictionary, this function behaves the same as [GetConnectionPath](ade_getconnectionpath.md).

See Also

[GetConnectionPath](ade_getconnectionpath.md)

[AliasName](ade_aliasname_tadsconnection.md)

[ConnectPath](ade_connectpath_tadsconnection.md)
