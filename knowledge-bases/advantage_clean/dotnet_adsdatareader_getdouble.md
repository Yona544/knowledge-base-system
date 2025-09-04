---
title: Dotnet Adsdatareader Getdouble
slug: dotnet_adsdatareader_getdouble
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_getdouble.htm
source: Advantage CHM
tags:
  - dotnet
checksum: fe8ab8ff6dea1196dc6b9ed5d33b9255568d2c53
---

# Dotnet Adsdatareader Getdouble

AdsDataReader.GetDouble

AdsDataReader.GetDouble

Advantage .NET Data Provider

| AdsDataReader.GetDouble  Advantage .NET Data Provider |  |  |  |  |

Gets the value of the specified column as a double-precision floating-point number.

public double GetDouble( int columnNumber );

Remarks

This method retrieves the specified zero-based column value as a double-precision floating-point number. No conversions are performed, therefore the data retrieved must already be a double or an exception is generated. This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.md) to check for null values before calling this method.

See Also

[GetValue](dotnet_adsdatareader_getvalue.md)

[IsDBNull](dotnet_adsdatareader_isdbnull.md)
