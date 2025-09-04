---
title: Dotnet Adsparameter Constructor String Dbtype Int String
slug: dotnet_adsparameter_constructor_string_dbtype_int_string_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsparameter_constructor_string_dbtype_int_string_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: c213408dd0d6a123491a4d45a05d4851bdc0400c
---

# Dotnet Adsparameter Constructor String Dbtype Int String

AdsParameter Constructor ( string, DbType, int, string )

AdsParameter Constructor ( string, DbType, int, string )

Advantage .NET Data Provider

| AdsParameter Constructor ( string, DbType, int, string )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of the AdsParameter class with the given name, type, parameter width, and source column mapping.

public AdsParameter

(

string parameterName, // (I) param name

DbType dbType, // (I) param type

int iSize, // (I) parameter width

string sourceColumn // (I) mapping to dataset column

);

Remarks

The Size will be inferred from the value of the DbType parameter and the value if it is not explicity set in the size parameter. This constructor can be used when creating parameters for commands in an [AdsDataAdapter](dotnet_adsdataadapter.md) where it is necessary to map parameters to columns in the DataSet.

Example

AdsParameter param = new AdsParameter( "Description", DbType.String,

100, "Description" );

param.Direction = ParameterDirection.Output;
