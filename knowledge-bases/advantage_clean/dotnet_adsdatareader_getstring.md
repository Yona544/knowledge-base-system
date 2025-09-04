---
title: Dotnet Adsdatareader Getstring
slug: dotnet_adsdatareader_getstring
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_getstring.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 1c3d6efb82c691fd37c8cc12783973488c596979
---

# Dotnet Adsdatareader Getstring

AdsDataReader.GetString

AdsDataReader.GetString

Advantage .NET Data Provider

| AdsDataReader.GetString  Advantage .NET Data Provider |  |  |  |  |

Gets the value of the specified column as a string.

public string GetString( int columnNumber );

Remarks

This method retrieves the specified zero-based column value as a string. No conversions are performed, therefore the data retrieved must already be a string or an exception is generated. This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.md) to check for null values before calling this method.

See Also

AdsDataReader.GetValue

[IsDBNull](dotnet_adsdatareader_isdbnull.md)
