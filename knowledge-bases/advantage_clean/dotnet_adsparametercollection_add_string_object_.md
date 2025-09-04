---
title: Dotnet Adsparametercollection Add String Object
slug: dotnet_adsparametercollection_add_string_object_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsparametercollection_add_string_object_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: fcd652159b0cfb023a31aae1520ea4f185133eac
---

# Dotnet Adsparametercollection Add String Object

AdsParameterCollection.Add( string, object )

AdsParameterCollection.Add( string, object )

Advantage .NET Data Provider

| AdsParameterCollection.Add( string, object )  Advantage .NET Data Provider |  |  |  |  |

Adds a new AdsParameter with the given name and value to the collection.

public AdsParameter Add

(

string parameterName, // (I) parameter name

object value // (I) parameter value

);

Remarks

This returns a reference to the newly created parameter.
