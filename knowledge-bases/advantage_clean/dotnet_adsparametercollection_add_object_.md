---
title: Dotnet Adsparametercollection Add Object
slug: dotnet_adsparametercollection_add_object_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsparametercollection_add_object_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 69f35648f42b4e3a7e0fb85ad411b2909f69629e
---

# Dotnet Adsparametercollection Add Object

AdsParameterCollection.Add( object )

AdsParameterCollection.Add( object )

Advantage .NET Data Provider

| AdsParameterCollection.Add( object )  Advantage .NET Data Provider |  |  |  |  |

Adds the given [AdsParameter](dotnet_adsparameter.md) to the collection.

public int Add( object value );

Remarks

The method returns the collection index of the newly added parameter. If the value is not of type AdsParameter, an InvalidCastException will be thrown.
