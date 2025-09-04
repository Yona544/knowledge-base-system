---
title: Dotnet Adsparametercollection Add String Dbtype Int String
slug: dotnet_adsparametercollection_add_string_dbtype_int_string_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsparametercollection_add_string_dbtype_int_string_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 4dec635d809d06e26c843191c08d4346ea631c33
---

# Dotnet Adsparametercollection Add String Dbtype Int String

AdsParameterCollection.Add( string, DbType, int, string )

AdsParameterCollection.Add( string, DbType, int, string )

Advantage .NET Data Provider

| AdsParameterCollection.Add( string, DbType, int, string )  Advantage .NET Data Provider |  |  |  |  |

Adds a new AdsParameter with the given name, type, size, and source column to the collection.

public AdsParameter Add

(

string parameterName, // (I) parameter name

DbType dbType, // (I) param type

int iSize, // (I) width of parameter

string sourceColumn // (I) name to map to source table

);

Remarks

This returns a reference to the newly created parameter.
