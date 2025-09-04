---
title: Dotnet Adsdatareader Getint16
slug: dotnet_adsdatareader_getint16
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_getint16.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 80431454303a5fd093b694e44a662a5712cc4b4c
---

# Dotnet Adsdatareader Getint16

AdsDataReader.GetInt16

AdsDataReader.GetInt16

Advantage .NET Data Provider

| AdsDataReader.GetInt16  Advantage .NET Data Provider |  |  |  |  |

Gets the value of the specified column as a 16-bit signed integer.

public short GetInt16( int columnNumber );

Remarks

This method retrieves the specified zero-based column value as a 16-bit signed integer. No conversions are performed, therefore the data retrieved must already be a 16-bit signed integer or an exception is generated. This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.md) to check for null values before calling this method.

See Also

[GetValue](dotnet_adsdatareader_getvalue.md)

[IsDBNull](dotnet_adsdatareader_isdbnull.md)
