---
title: Dotnet Adsdatareader Getdatetime
slug: dotnet_adsdatareader_getdatetime
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_getdatetime.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 5d6c8576e332ec8c8e2544499100e4be44ddeee6
---

# Dotnet Adsdatareader Getdatetime

AdsDataReader.GetDateTime

AdsDataReader.GetDateTime

Advantage .NET Data Provider

| AdsDataReader.GetDateTime  Advantage .NET Data Provider |  |  |  |  |

Gets the value of the specified column as a DateTime object.

public DateTime GetDateTime( int columnNumber );

Remarks

This method retrieves the specified zero-based column value as a DateTime object. No conversions are performed, therefore, the data retrieved must already be a DateTime-compatible value, or an exception is generated. This method can be used to retrieve timestamp, ModTime, and date field values, but cannot be used to retrieve null values. Call [AdsDataReader.IsDBNull](dotnet_adsdatareader_isdbnull.md) to check for null values before calling this method.

See Also

[GetValue](dotnet_adsdatareader_getvalue.md)

[IsDBNull](dotnet_adsdatareader_isdbnull.md)
