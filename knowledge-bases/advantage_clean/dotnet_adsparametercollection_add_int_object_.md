---
title: Dotnet Adsparametercollection Add Int Object
slug: dotnet_adsparametercollection_add_int_object_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsparametercollection_add_int_object_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 5e015fccb5f76c7f82b7c26e59b3c81f870e5b44
---

# Dotnet Adsparametercollection Add Int Object

AdsParameterCollection.Add( int, object )

AdsParameterCollection.Add( int, object )

Advantage .NET Data Provider

| AdsParameterCollection.Add( int, object )  Advantage .NET Data Provider |  |  |  |  |

Adds a new AdsParameter with the given one-based index (for unnamed parameters) and value to the collection.

public AdsParameter Add

(

int iIndex, // (I) index of the parameter (one-based)

object value // (I) parameter value

);

Remarks

This returns a reference to the newly created parameter.
