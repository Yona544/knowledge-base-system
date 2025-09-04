---
title: Dotnet Adsdatareader Getint64
slug: dotnet_adsdatareader_getint64
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_getint64.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 9f4a434f5eaae8fa797d9298da3307c6cb6517c7
---

# Dotnet Adsdatareader Getint64

AdsDataReader.GetInt64

AdsDataReader.GetInt64

Advantage .NET Data Provider

| AdsDataReader.GetInt64  Advantage .NET Data Provider |  |  |  |  |

Gets the value of the specified column as a 64-bit signed integer.

public long GetInt64( int columnNumber );

Remarks

This method retrieves the specified zero-based column value as a 64-bit signed integer. No conversions are performed, therefore the data retrieved must already be a 64-bit signed integer or an exception is generated. This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.md) to check for null values before calling this method.

See Also

[GetValue](dotnet_adsdatareader_getvalue.md)

[IsDBNull](dotnet_adsdatareader_isdbnull.md)
