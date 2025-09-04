---
title: Dotnet Adsparametercollection Add String Dbtype
slug: dotnet_adsparametercollection_add_string_dbtype_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsparametercollection_add_string_dbtype_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 5ff4babe402766e50c2c16189ad797bc7018e326
---

# Dotnet Adsparametercollection Add String Dbtype

AdsParameterCollection.Add( string, DbType )

AdsParameterCollection.Add( string, DbType )

Advantage .NET Data Provider

| AdsParameterCollection.Add( string, DbType )  Advantage .NET Data Provider |  |  |  |  |

Add a new AdsParameter of the given name and type to the collection.

public AdsParameter Add

(

string parameterName, // (I) parameter name

DbType type // (I) parameter type

);

Remarks

This returns a reference to the newly created parameter.
