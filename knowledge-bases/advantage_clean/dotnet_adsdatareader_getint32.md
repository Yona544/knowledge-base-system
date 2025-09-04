---
title: Dotnet Adsdatareader Getint32
slug: dotnet_adsdatareader_getint32
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_getint32.htm
source: Advantage CHM
tags:
  - dotnet
checksum: d47aad2f5f84d6db563cab29dc0b39c5cc4b64ad
---

# Dotnet Adsdatareader Getint32

AdsDataReader.GetInt32

AdsDataReader.GetInt32

Advantage .NET Data Provider

| AdsDataReader.GetInt32  Advantage .NET Data Provider |  |  |  |  |

Gets the value of the specified column as a 32-bit signed integer.

public int GetInt32( int columnNumber );

Remarks

This method retrieves the specified zero-based column value as a 32-bit signed integer. No conversions are performed, therefore the data retrieved must already be a 32-bit signed integer or an exception is generated. This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.md) to check for null values before calling this method.

See Also

[GetValue](dotnet_adsdatareader_getvalue.md)

[IsDBNull](dotnet_adsdatareader_isdbnull.md)
