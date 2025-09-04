---
title: Dotnet Adsdatareader Getfloat
slug: dotnet_adsdatareader_getfloat
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_getfloat.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 089bb393bf899f9616572fb47d66fe652bf60085
---

# Dotnet Adsdatareader Getfloat

AdsDataReader.GetFloat

AdsDataReader.GetFloat

Advantage .NET Data Provider

| AdsDataReader.GetFloat  Advantage .NET Data Provider |  |  |  |  |

Gets the value of the specified column as a single-precision floating-point number.

public float GetFloat( int columnNumber );

Remarks

This method retrieves the specified zero-based column value as a single-precision floating-point number. No conversions are performed, therefore the data retrieved must already be a float or an exception is generated. This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.md) to check for null values before calling this method.

See Also

[GetValue](dotnet_adsdatareader_getvalue.md)

[GetDouble](dotnet_adsdatareader_getdouble.md)

[IsDBNull](dotnet_adsdatareader_isdbnull.md)
