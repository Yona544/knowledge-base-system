---
title: Dotnet Adsparameter Constructor String Dbtype String Datarowversion
slug: dotnet_adsparameter_constructor_string_dbtype_string_datarowversion_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsparameter_constructor_string_dbtype_string_datarowversion_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 5cee03ffc300ded1c50cc9123fa747e8227b2204
---

# Dotnet Adsparameter Constructor String Dbtype String Datarowversion

AdsParameter Constructor ( string, DbType, string, DataRowVersion )

AdsParameter Constructor ( string, DbType, string, DataRowVersion )

Advantage .NET Data Provider

| AdsParameter Constructor ( string, DbType, string, DataRowVersion )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of the AdsParameter class with the given name, type, source column, and source version.

public AdsParameter

(

string parameterName, // (I) param name

DbType dbType, // (I) param type

string srcColumn, // (I) dataset source column mapping

DataRowVersion srcVersion // (I) current or original

);

Example

AdsParameter param = new AdsParameter( "pk", DbType.String,

"pk", DataRowVersion.Original );
