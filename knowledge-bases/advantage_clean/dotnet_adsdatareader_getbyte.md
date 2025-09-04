---
title: Dotnet Adsdatareader Getbyte
slug: dotnet_adsdatareader_getbyte
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_getbyte.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 0718264e32da08f221d5c265aa4868bbfa5da951
---

# Dotnet Adsdatareader Getbyte

AdsDataReader.GetByte

AdsDataReader.GetByte

Advantage .NET Data Provider

| AdsDataReader.GetByte  Advantage .NET Data Provider |  |  |  |  |

Gets the value of the specified column as a byte.

public byte GetByte( int columnNumber );

Remarks

This method retrieves the specified zero-based column value as a byte. No conversions are performed, therefore the data retrieved must already be a byte or an exception is generated. This method cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.md) to check for null values before calling this method.

See Also

[GetValue](dotnet_adsdatareader_getvalue.md)

[IsDBNull](dotnet_adsdatareader_isdbnull.md)
