---
title: Dotnet Adsconnection Getddobjects
slug: dotnet_adsconnection_getddobjects
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_getddobjects.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 27ceec4ae90e77fd533c36e94743d5e2c68b4cd3
---

# Dotnet Adsconnection Getddobjects

AdsConnection.GetDDObjects

AdsConnection.GetDDObjects

Advantage .NET Data Provider

| AdsConnection.GetDDObjects  Advantage .NET Data Provider |  |  |  |  |

Retrieves the names of objects of the specified type from an open data dictionary.

public object[] GetDDObjects( AdsObjectType type, string strParent );

Remarks

GetDDObjects finds objects in the data dictionary matching the specified AdsObjectType and returns the object names in an array. The strParent parameter is the name of the object that is the parent or owner of the objects searched for. This parameter is ignored when searching for table, view, user group or referential integrity objects. When searching for an index file or a field object, strParent should supply the name of the associated table object. When searching for a user, strParent can optionally supply the name of the user group to limit the search result to users who are members of the user group.

Note The AdsConnection must be open on a data dictionary connection when GetDDObjects is called.

See Also

[AdsObjectType](dotnet_adsconnection_adsobjecttype.md)
