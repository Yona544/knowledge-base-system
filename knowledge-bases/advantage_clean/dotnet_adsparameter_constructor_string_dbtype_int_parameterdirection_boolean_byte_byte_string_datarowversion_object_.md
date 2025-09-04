---
title: Dotnet Adsparameter Constructor String Dbtype Int Parameterdirection Boolean Byte Byte String Datarowversion Object
slug: dotnet_adsparameter_constructor_string_dbtype_int_parameterdirection_boolean_byte_byte_string_datarowversion_object_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsparameter_constructor_string_dbtype_int_parameterdirection_boolean_byte_byte_string_datarowversion_object_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: bf4fa0eb90ad03354bfad80a1f86c43ff555b189
---

# Dotnet Adsparameter Constructor String Dbtype Int Parameterdirection Boolean Byte Byte String Datarowversion Object

AdsParameter Constructor ( string, DbType, int, ParameterDirection, Boolean, Byte, Byte, string, DataRowVersion, object )

AdsParameter Constructor ( string, DbType, int, ParameterDirection, Boolean, Byte, Byte, string, DataRowVersion, object )

Advantage .NET Data Provider

| AdsParameter Constructor ( string, DbType, int, ParameterDirection, Boolean, Byte, Byte, string, DataRowVersion, object )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new AdsParameter instance with name, type, size, direction, null flag, precision, scale, source column, source version, and a value.

public AdsParameter

(

string parameterName, // (I) parameter name

DbType dbType, // (I) parameter type

int iSize, // (I) parameter width

ParameterDirection direction, // (I) input or output

Boolean isNullable, // (I) can parameter be null?

Byte precision, // (I) precision for numeric

Byte scale, // (I) scale for numeric

string srcColumn, // (I) dataset source column mapping

DataRowVersion srcVersion, // (I) current or original

object value // (I) the parameter value

);

Example

AdsParameter param = new AdsParameter( "name", DbType.String, 15,

ParameterDirection.Input,

false, 0, 0, "Department Name", DataRowVersion.Current,

"Administration" );
